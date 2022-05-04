from scheduling_queue import RRQueue
from scheduling_queue import FCFSQueue


class Mlfq:
    def __init__(self, number_of_queues, quantum_list, job_list, boost, gui, mode):
        self.number_of_queues = number_of_queues
        self.current_time = 0
        self.job_list = job_list
        self.boost = boost
        self.gui = gui
        self.queues = list()
        self.mode = mode
        self.init_queues(number_of_queues, quantum_list)
        

    def init_queues(self, number_of_queues, quantum_list):
        if self.mode != "fcfs":
            for i in range(number_of_queues - 1):
                self.queues.append(RRQueue(i, quantum_list[i], self.mode))
                self.gui.draw_rr_queue_header(i, quantum_list[i])

        self.queues.append(FCFSQueue(number_of_queues - 1))
        self.gui.draw_fcfs_queue_header(number_of_queues - 1)

        if self.mode != "fcfs":
            for i in range(number_of_queues - 1):
                self.queues[i].set_next_queue(self.queues[i + 1])

    def add_arrival_to_first_queue(self, process, priority):
        if process.arrival == self.current_time:
            self.queues[priority].add_process(process)

    def loop(self):
        while True:
            pending_jobs = [job for job in self.job_list if not job.is_finished()]
            if len(pending_jobs) == 0:
                break

            for process in pending_jobs:
                self.add_arrival_to_first_queue(process, priority=0)

            if self.is_boost_available():
                self.boost_jobs()

            highest_queue = self.get_highest_non_empty_queue()
            if highest_queue is not None:
                process_id = highest_queue.run_process(self.current_time)
                self.gui.draw_process_rect(highest_queue.queue_id, self.current_time, process_id)

            self.current_time += 1

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

    def print_statistics(self):
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


