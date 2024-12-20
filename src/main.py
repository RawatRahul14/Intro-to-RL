import gym
import numpy as np

# Function to run a random agent in the CartPole-v1 environment
def run_random_agent(episodes = 10):
    # Create the environment for CartPole-v1 with a human render mode (it displays the environment visually)
    env = gym.make("CartPole-v1", render_mode = "human")

    for episode in range(episodes):
        # Reset the environment for a new episode, and get the initial state
        state = env.reset()[0]
        total_reward = 0
        done = False
        truncated = False # Time limit

        # Run the simulation until the episode is finished or truncated
        while not (done or truncated):
            # (CartPole has two possible actions)
            action = env.action_space.sample()

            # Take the action and get the next state, reward, done, truncated status, and additional info
            state, reward, done, truncated, info = env.step(action)
            
            total_reward += reward

        print(f"Episode: {episode + 1} finished with reward: {total_reward}")
    
    # Close the environment to free up resources after all episodes are done
    env.close()

if __name__ == "__main__":
    run_random_agent()