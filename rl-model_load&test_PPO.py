# import gym library & PPO model
import gym
from stable_baselines3 import PPO

# define directories to load trained models
models_dir = "models/PPO"

# define the specific saved model to load
model_path = f"{models_dir}/600000.zip"

# create & initialize environment 
env = gym.make("LunarLander-v2")
env.reset()

# load PPO model from defined path, in this case the 600k model
model = PPO.load(model_path, env=env)

# the agent will use the trained model for 10 episodes and render to screen
episodes = 10
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:    
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)

# close the environment
env.close()