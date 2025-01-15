import numpy as np
import gymnasium as gym

# create Taxi3 environment
env = gym.make("Taxi-v3")

# number of states
state_size = env.observation_space.n
# number of action
action_size = env.action_space.n
# initialize Q-table with zeros
q_table = np.zeros((state_size, action_size))

# hyperparameters

# total of episodes
episodes = 25000
# learning rate
alpha = 0.05
# discount factor
gamma = 0.9
# start exploration rate
epsilon = 1.0
# min epsilon value
epsilon_min = 0.01
# How much epsilon lowers each time. New epsilon is epsilon*epsilon_decay.
epsilon_decay = 0.995
# max moves per episode
max_steps = 100
# q-learning algorithm
for episode in range(episodes):
    # episode reset while learning, done in start of episode
    state = env.reset()[0]
    done = False
    total_rewards = 0
    for step in range(max_steps):
        # epsilon-greedy action selectio
        if np.random.uniform(0, 1) < epsilon:
            # use random action
            action = env.action_space.sample()
        else:
            # use best action
            action = np.argmax(q_table[state, :])
        # make the action and observe result
        new_state, reward, done, truncated, info = env.step(action)

        # update q-table
        q_table[state, action] += alpha * (
            reward + gamma * np.max(q_table[new_state, :]) - q_table[state, action]
        )
        state=new_state
        total_rewards+=reward
        if done:
            break

    #Decay epsilon value
    epsilon=max(epsilon_min,epsilon*epsilon_decay)

#evaluation for trained policy
evaluation_episodes=10
total_rewards=[]
total_steps=0
for i in range(evaluation_episodes):
    state = env.reset()[0]
    done = False
    episode_rewards = 0
    steps = 0

    while not done and steps < max_steps:
        action = np.argmax(q_table[state, :])  # Exploit learned policy
        new_state, reward, done, truncated, info = env.step(action)
        episode_rewards += reward
        state = new_state
        steps += 1

    total_rewards.append(episode_rewards)
    total_steps+=steps

# Compute average reward
average_reward = np.mean(total_rewards)
# Compute average actions
average_actions=total_steps/evaluation_episodes
print(f"Average number of actions is {average_actions} and average reward is {average_reward}")