# RL based OS process Scheduling

## Introduction
This project aims to implement a scheduling algorithm for a real-time operating system. We use the MLFQ algorithm as the baseline. In the MLFQ algorithm, there are multiple queues but the quantum of each queue is pre-decided. We aim to address this problem by using an RL agent to control the quantum of each queue.


## Code
The Code is divided into multiple files:
- `process.py`: The process class. 
- `scheduling_queue.py`: The queue class which simulates 1 single queue of the MLFQ algorithm.
- `gui.py`: The GUI class. To display the schedule generated
- `env.py`: The OpenAI Gym environment class which simulates the MLFQ algorithm on a randomly sampled instance. It takes the quantum list as the action
- `main.py`: Takes as input the number of Queues, Agent to train and file for agent and trains that particular algorithm. Currently, only A2C is supported.
- `check.py`: Used to run the agent given on a test instance.
- `check_baseline.py`: Used to run the baseline agent on a test instance.
  
## Dependencies
- OpenAI Gym
- Numpy
- PySimpleGUI
- Stable Baselines 3

## Output
The output is present in the output directory.
The folder name is numberOfQueues_agentType_BoostingValue. rl file contains result for the A2C agent. base file contains the result for the baseline agent. rl_model.zip contains the model weights.