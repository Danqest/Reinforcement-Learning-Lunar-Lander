# import gym library, PPO model, and os library
import gym
from stable_baselines3 import PPO
import os

# define directories to save trained models and tensorboard logs
models_dir = "models/PPO"
logdir = "logs"

# if the directories do not exist, create them
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
if not os.path.exists(logdir):
    os.makedirs(logdir)

# create & initialize environment 
env = gym.make("LunarLander-v2")
env.reset()

# load PPO model and path for tensorboard logs
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logdir)

# define number of timesteps for the model to run
TIMESTEPS = 10000

# model will run for 100 loops for a total of 1 million timesteps
# model is saved every 10k timesteps
for i in range(1,100):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*i}")

#close the environment
env.close()