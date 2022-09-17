# import gym library
import gym

# create environment 
env = gym.make("LunarLander-v2")

# initialize environment
env.reset()

# print("sample action: ", env.action_space.sample())
# print("observation space shape: ", env.observation_space.shape)
# print("sample observation: ", env.observation_space.sample())

# have agent take random actions for 200 steps and render to screen
for step in range(200):
    env.render()
    obs, reward, done, info = env.step(env.action_space.sample())
    # print(reward)

# close environment
env.close()