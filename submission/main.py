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
    ap.add_argument("-a", "--agent", default="A2C", help="Agent", type=str)
    ap.add_argument("-f", "--file", default="rl_model", help="File to store model", type=str)
    return ap

arg_parser = parse_arguments()
args = vars(arg_parser.parse_args())
env = SchedulingEnv(args["boost"], args["numQueues"], False)
# ac = env.quantum_list
# while True:
#     st, r, done, _ = env.step(ac)
#     if done:
#         obs = env.reset()
#         break 

# check_env(env, warn=True)

agent_dict = {"A2C": A2C}
print("Agent: ", args["agent"])
model = agent_dict[args["agent"]]('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)
# bound on iterations = 100000

obs = env.reset()
r = 0
for i in range(100000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    r += reward
    if done:
      obs = env.reset()
      break 
# env.render()
print ("reward = ", r)

model.save(args["file"])
# st = env.reset()
# while True:
#     st, r, done, _ = env.step(st)
#     if done:
#         break

# env.render()

