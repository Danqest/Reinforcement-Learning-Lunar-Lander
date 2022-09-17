# import gym library and PPO model
import gym
from stable_baselines3 import PPO

# create & initialize environment 
env = gym.make("LunarLander-v2")
env.reset()

# load PPO model and train for 100k time steps
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)

# after training, the agent will use the trained model for 10 episodes and render to screen
episodes = 10
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:    
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample())

#close the environment
env.close()