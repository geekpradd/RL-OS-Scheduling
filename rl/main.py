from env import SchedulingEnv
import gym
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import A2C, DDPG, DQN, TD3
import argparse

def parse_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-q", "--quantumList", default="8, 8, 16",
                    help="q1,q2,q3, ...", type=str)
    ap.add_argument("-l", "--jobList", default="32:0, 16:16, 26:42",
                    help="burst1:arrivalTime1,burst2:arrivalTime2, ...")
    ap.add_argument("-b", "--boost", default=0,
                    help="", type=int)
    ap.add_argument("-a", "--agent", default="DQN", help="Agent", type=str)
    return ap

arg_parser = parse_arguments()
args = vars(arg_parser.parse_args())
env = SchedulingEnv(args)

agent_dict = {"A2C": A2C, "DQN":DQN, "DDPG":DDPG, "TD3":TD3}

model = agent_dict[args.get("agent", "DQN")]('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)
# bound on iterations = 100000
check_env(env, warn=True)

obs = env.reset()
r = 0
for i in range(100000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    r += reward
    if done:
      obs = env.reset()
      break 

print ("reward = ", r)
# st = env.reset()
# while True:
#     st, r, done, _ = env.step(st)
#     if done:
#         break

# env.render()

