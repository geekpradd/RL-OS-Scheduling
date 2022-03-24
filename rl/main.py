from env import SchedulingEnv
import gym
# from stable_baselines3.common.env_checker import check_env
import argparse

def parse_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-q", "--quantumList", default="8, 16",
                    help="q1,q2,q3, ...", type=str)
    ap.add_argument("-l", "--jobList", default="32:0, 16:16, 26:42",
                    help="burst1:arrivalTime1,burst2:arrivalTime2, ...")
    ap.add_argument("-b", "--boost", default=0,
                    help="", type=int)
    return ap

arg_parser = parse_arguments()
args = vars(arg_parser.parse_args())
env = SchedulingEnv(args)


while True:
    _, _, done, _ = env.step({})
    if done:
        break

env.render()

# check_env(env, warn=True)