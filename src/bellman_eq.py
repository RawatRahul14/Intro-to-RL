import numpy as np

class GridWorld:
    def __init__(self, grid_size = (4, 4), goal = (3, 3), step_reward = -1, goal_reward = 10):
        self.grid_size = grid_size
        self.goal = goal
        self.step_reward = step_reward
        self.goal_reward = goal_reward
        self.state = (0, 0)

    def reset(self):
        """Reset the environment to the initial state."""
        self.state = (0, 0)
        return self.state

    def step(self, action):
        """Take an action and return the next state, reward, and done."""
        x, y = self.state
        if action == "up":
            x = max(0, x - 1)
        elif action == "down":
            x = min(self.grid_size[0] - 1, x + 1)
        elif action == "left":
            y = max(0, y - 1)
        elif action == "right":
            y = min(self.grid_size[1] - 1, y + 1)

        self.state = (x, y)

        if self.state == self.goal:
            return self.state, self.goal_reward, True  # Goal state reached
        else:
            return self.state, self.step_reward, False  # Regular step

    def get_all_states(self):
        """Return all possible states in the environment."""
        return [(x, y) for x in range(self.grid_size[0]) for y in range(self.grid_size[1])]

    def get_possible_actions(self):
        """Return all possible actions."""
        return ["up", "down", "left", "right"]

def random_policy(state, actions):
    """Returns a random action"""
    return np.random.choice(actions)

def policy_evaluation(env, policy, gamma = 0.9, theta = 1e-6):
    """Evaluate the state-value function V(s) for a given policy."""
    # Initialise V(s) for all states
    states = env.get_all_states()
    V = {state: 0 for state in states}

    # Possible actions
    actions = env.get_possible_actions()

    while True:
        # Track the maximum change in V(s)
        delta = 0

        for state in states:
            env.state = state
            v = V[state]
            new_v = 0

            for action in actions:
                next_state, reward, _ = env.step(action)

                action_prob = 1/len(actions)
                new_v += action_prob * (reward + gamma * V[next_state])

            # Update V(S)
            V[state] = new_v
            delta = max(delta, abs(v - new_v))
        
        if delta < theta:
            break

    return V

def compute_action_value(env, V, gamma = 0.9):
    """Compute Action-Value function Q(s, a) given V(s)"""
    Q = {}
    actions = env.get_possible_actions()
    states = env.get_all_states()

    for state in states:
        Q[state] = {}
        env.state = state

        for action in actions:
            next_state, reward, _ = env.step(action)
            Q[state][action] = reward + gamma * V[next_state]

    return Q

# Initialise the Environment
env = GridWorld()

# Policy evaluation
V = policy_evaluation(env, random_policy)
print("State-Value Function (V): ")
for state, value in V.items():
    print(f"State: {state}: {value:.2f}")

# Compute Q(s, a)
Q = compute_action_value(env, V)
print("\nAction-Value Function (Q): ")
for state, actions in Q.items():
    print(f"State {state}: ")
    for action, value in actions.items():
        print(f"\tAction {action}: {value:.2f}")