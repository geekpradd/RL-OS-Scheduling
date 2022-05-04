from env import SchedulingEnv
import gym
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import A2C, DDPG, DQN, TD3
import argparse

def parse_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--numQueues", default=3,
                    help="number of queues", type=int)
    ap.add_argument("-b", "--boost", default=0,
                    help="", type=int)
    return ap

arg_parser = parse_arguments()
args = vars(arg_parser.parse_args())
env = SchedulingEnv(args["boost"], args["numQueues"], True)

# bound on iterations = 100000
obs = env.reset()
init_quantum = env.quantum_list
print(init_quantum)

r = 0
for i in range(100000):
    obs, reward, done, info = env.step(init_quantum)
    r += reward
    if done:
    #   obs = env.reset()
      break 
print ("reward = ", r)
env.render()

