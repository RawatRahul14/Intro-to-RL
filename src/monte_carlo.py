import numpy as np
from collections import defaultdict
from tqdm import tqdm

class GridWorld:
    def __init__(self):
        self.height = 4
        self.width = 4
        self.start_pos = (0, 0)  # Top-left corner
        self.goal_pos = (3, 3)   # Bottom-right corner
        self.current_pos = self.start_pos
        
        # Define actions as a dictionary
        self.actions = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1)
        }
        self.action_list = list(self.actions.keys())
        
    def reset(self):
        # Setting the current position to the start position on reseting
        self.current_pos = self.start_pos
        return self.current_pos
    
    def is_terminal(self, state):
        return state == self.goal_pos
    
    def step(self, action):
        # Get movement direction
        move = self.actions[action]
        
        # Calculate new position
        new_pos = (self.current_pos[0] + move[0], 
                  self.current_pos[1] + move[1])
        
        # Check if new position is valid
        if (0 <= new_pos[0] < self.height and 
            0 <= new_pos[1] < self.width):
            self.current_pos = new_pos
        
        # Reward: -1 for each step, +10 for reaching goal
        reward = 10 if self.current_pos == self.goal_pos else -1
        done = self.is_terminal(self.current_pos)
        
        return self.current_pos, reward, done

class MonteCarloAgent:
    def __init__(self, env, gamma = 0.99, epsilon = 0.1):
        self.env = env
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.actions = env.action_list
        
        """
        Initialize Q-values, returns, and policy using action strings:

        self.Q: Stores Q-values (expected returns) for each state-action pair
            Format: state -> {"up": value, "right": value, "down": value, "left": value}
            Default: All values initialized to 0

        self.returns: Stores historical returns for each state-action pair
                Format: state -> {"up": [return1, return2, ...], "right": [...], ...}
                Default: Empty lists for each action

        self.policy: Stores probability distribution over actions for each state
                Format: state -> {"up": prob, "right": prob, "down": prob, "left": prob}
                Default: Uniform distribution (0.25 for each action)
        """

        self.Q = defaultdict(lambda: {action: 0 for action in self.actions})
        self.returns = defaultdict(lambda: {action: [] for action in self.actions})
        self.policy = defaultdict(lambda: {action: 1 / len(self.actions) for action in self.actions})
        
    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.actions)  # Random action
        
        return max(self.Q[state].items(), key = lambda x: x[1])[0]  # Greedy action
    
    def generate_episode(self):
        episode = []
        state = self.env.reset()
        done = False
        
        while not done:
            action = self.choose_action(state)
            next_state, reward, done = self.env.step(action)
            episode.append((state, action, reward))
            state = next_state
            
        return episode
    
    def update(self, episodes = 1000):
        # Add tqdm progress bar
        pbar = tqdm(range(episodes), desc = "Training Episodes")
        
        # Track average returns for progress
        episode_returns = []
        
        for _ in pbar:
            # Generate episode using current policy
            episode = self.generate_episode()
            episode_return = sum(r for _, _, r in episode)
            episode_returns.append(episode_return)
            
            # Calculate returns for each step
            G = 0
            for t in range(len(episode)-1, -1, -1):
                state, action, reward = episode[t]
                G = reward + self.gamma * G
                
                # Check if state-action pair appears for first time in episode
                if (state, action) not in [(s, a) for (s, a, r) in episode[:t]]:
                    self.returns[state][action].append(G)

                    # Update Q-value with average return
                    self.Q[state][action] = np.mean(self.returns[state][action])
                    
                    # Update policy (epsilon-greedy)
                    best_action = max(self.Q[state].items(), key = lambda x: x[1])[0]
                    for a in self.actions:
                        self.policy[state][a] = (
                            1 - self.epsilon + self.epsilon / len(self.actions) 
                            if a == best_action 
                            else self.epsilon / len(self.actions)
                        )
            
            # Update progress bar with average return over last 100 episodes
            if len(episode_returns) >= 100:
                avg_return = np.mean(episode_returns[-100:])
                pbar.set_postfix({"Avg Return (last 100)": f"{avg_return:.2f}"})

def visualize_policy(agent):
    # Action symbols
    symbols = {"up": "↑", "right": "→", "down": "↓", "left": "←"}
    
    print("\nLearned Policy:")
    for i in range(4):
        for j in range(4):
            state = (i, j)
            if state == agent.env.goal_pos:
                print("G", end = " ")
            elif state == agent.env.start_pos:
                print("S", end = " ")
            else:
                best_action = max(agent.Q[state].items(), key = lambda x: x[1])[0]
                print(symbols[best_action], end = " ")
        print()

def run_example():
    env = GridWorld()
    agent = MonteCarloAgent(env)
    
    # Train the agent
    print("\nStarting training...")
    agent.update(episodes = 1000)
    
    # Visualize the learned policy
    visualize_policy(agent)
    
    # Test the learned policy
    print("\nTesting learned policy...")
    state = env.reset()
    total_reward = 0
    path = [state]
    done = False
    
    while not done:
        action = max(agent.Q[state].items(), key = lambda x: x[1])[0]
        state, reward, done = env.step(action)
        path.append(state)
        total_reward += reward
        
    print(f"\nTotal reward: {total_reward}")
    print(f"Path taken: {path}")
    
    # Print Q-values for start state
    print("\nQ-values at start state:")
    for action, value in agent.Q[env.start_pos].items():
        print(f"{action}: {value:.2f}")

if __name__ == "__main__":
    run_example()