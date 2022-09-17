# import gym library & PPO model
import gym
from stable_baselines3 import PPO

# define directories to load trained models and to write tensorboard logs
models_dir = "models/PPO"
logdir = "logs"

# define the specific saved model to load
model_path = f"{models_dir}/600000.zip"

# create & initialize environment 
env = gym.make("LunarLander-v2")
env.reset()

# load PPO model from defined path, in this case the 600k model
model = PPO.load(model_path, env=env)

# define number of timesteps for the model to run
TIMESTEPS = 10000

# model will train for 100 loops for a total of 1 million *additional* timesteps (now an aggregate of 2 million)
# model is saved every 10k timesteps
for i in range(1,100):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*i}")

#close the environment
env.close()