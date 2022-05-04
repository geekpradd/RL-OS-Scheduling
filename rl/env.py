# TODO: add what all observations are needed

import gym
import numpy as np
from gui import Gui
from process import Process
import PySimpleGUI as sg
from scheduling_queue import RRQueue
from scheduling_queue import FCFSQueue

STATE_SPACE_SIZE = 10

def parse_jobs(jobs):
    returned_jobs = list()
    for job in jobs:
        burst, arrival = job.split(":")

        returned_jobs.append(Process(int(burst), int(arrival)))
    return returned_jobs

def to_stateSpace(jobs):
    return np.convolve(jobs, np.ones(STATE_SPACE_SIZE+ len(jobs) -1)/STATE_SPACE_SIZE, 'valid')

class SchedulingEnv(gym.Env):
    def __init__(self, args):
        # print(args)
        self.boost = args.get("boost",0)
        jobs = str(args.get("jobList","")).split(",")
        self.quantum_list = str(args.get("quantumList","8,16")).split(",")
        self.quantum_list = np.array([int(quantum) for quantum in self.quantum_list])
        self.number_of_queues = len(self.quantum_list) + 1
        self.gui = Gui(1000, 500)
        self.job_list = parse_jobs(jobs)
        self.current_time = 0
        self.queues = list()
        self.init_queues(self.number_of_queues, self.quantum_list)
        self.observation_space = gym.spaces.Box(np.array([0]*STATE_SPACE_SIZE*2), np.array([np.inf]*STATE_SPACE_SIZE*2), shape = (STATE_SPACE_SIZE*2,),dtype= np.float32) 
        self.action_space = gym.spaces.Box(low=1, high=100, shape=(self.number_of_queues-1,), dtype=np.float32)

    def init_queues(self, number_of_queues, quantum_list):
        for i in range(number_of_queues - 1):
            self.queues.append(RRQueue(i, quantum_list[i]))
            self.gui.draw_rr_queue_header(i, quantum_list[i])

        self.queues.append(FCFSQueue(number_of_queues - 1))
        self.gui.draw_fcfs_queue_header(number_of_queues - 1)

        for i in range(number_of_queues - 1):
            self.queues[i].set_next_queue(self.queues[i + 1])
    
    def add_arrival_to_first_queue(self, process, priority):
        if process.arrival == self.current_time:
            self.queues[priority].add_process(process)
            
    def is_boost_available(self):
        if self.boost <= 0 or self.current_time == 0:
            return False
        return True
    
    def boost_jobs(self):
        if self.current_time % self.boost == 0:
            for queue in self.queues:
                queue.empty()
            for job in self.job_list:
                if not job.is_finished():
                    self.queues[0].add_process(job)
                    
    def get_highest_non_empty_queue(self):
        for queue in self.queues:
            if queue.is_empty():
                continue
            return queue
        
    
    def reset(self):
        for job in self.job_list:
            job.reset()
        self.current_time = 0
        observation = np.append(to_stateSpace([0]),to_stateSpace([0]))
        return observation  # reward, done, info can't be included
    
        
    def step(self, action):
        self.quantum_list = action
        for i in range(self.number_of_queues - 1):
            q = self.queues[i]
            q.quantum = self.quantum_list[q.priority]
            
        pending_jobs = [job for job in self.job_list if not job.is_finished()]
        if len(pending_jobs) == 0:
            return self.quantum_list, 0, True, {}
        
        for process in pending_jobs:
            self.add_arrival_to_first_queue(process, priority=0)

        if self.is_boost_available():
            self.boost_jobs()

        highest_queue = self.get_highest_non_empty_queue()
        reward = 0
        if highest_queue is not None:
            process_id, reward = highest_queue.run_process(self.current_time)
            self.gui.draw_process_rect(highest_queue.queue_id, self.current_time, process_id)

        total_time = []
        remaining_time = []
        for job in self.job_list:
                if job.arrival > self.current_time:
                    continue
                total_time.append(job.burst_time)
                remaining_time.append(job.time_left)
        self.current_time += 1 
        observation = np.append(to_stateSpace(remaining_time),to_stateSpace(total_time))
        return observation, reward, False, {}
    
    
    def render(self, mode='human'):
        total_turnaround_time = total_wait = total_response = 0
        for i, job in enumerate(self.job_list):
            self.gui.print_process_statistics(i, job, self.number_of_queues)
            total_response += job.statistics.response_time
            total_turnaround_time += job.statistics.turnaround
            total_wait += job.statistics.wait
        total_jobs = len(self.job_list)
        self.gui.print_global_statistics(total_turnaround_time,
                                         total_wait,
                                         total_response,
                                         total_jobs,
                                         self.number_of_queues,
                                         self.current_time,
                                         self.boost)
        while True:
            event, values = self.gui.window.read()
            if event in (None, 'Exit'):  # if user closes window or clicks cancel
                break
        self.gui.window.close()
    
    def close (self):
        pass