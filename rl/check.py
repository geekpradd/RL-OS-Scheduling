from env import SchedulingEnv
import gym
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import A2C, DDPG, DQN, TD3
import argparse
import numpy as np

np.random.seed(2)

def parse_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--numQueues", default=3,
                    help="number of queues", type=int)
    ap.add_argument("-b", "--boost", default=0,
                    help="", type=int)
    ap.add_argument("-a", "--agent", default="A2C", help="Agent", type=str)
    ap.add_argument("-f", "--file", default="rl_model", help="File to store model", type=str)
    return ap

arg_parser = parse_arguments()
args = vars(arg_parser.parse_args())
env = SchedulingEnv(args["boost"], args["numQueues"], False)

agent_dict = {"A2C": A2C, "DDPG":DDPG, "TD3":TD3}
print("Agent: ", args["agent"])
model = agent_dict[args["agent"]].load(args["file"])

# bound on iterations = 100000
for i in range(100):
    obs = env.reset()
    init_quantum = env.quantum_list
    r= 0
    while True:
        action, _state = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        r += reward
        if done:
            break 
    print (f"Iteration {i}: reward = ", r)
    print("---------------------------------------------------------------------------------------")

