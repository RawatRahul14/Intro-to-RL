import numpy as np

class GridWorld:
    def __init__(self, grid_size = (4, 4), goal = (3, 3), step_reward = -1, goal_reward = 10, obstacle = None):
        if obstacle is None:
            obstacle = [(0, 1), (0, 2), (0, 3), (1, 1), (2, 1), (3, 0), (3, 1), (3, 2)]
        self.grid_size = grid_size
        self.goal = goal
        self.step_reward = step_reward
        self.goal_reward = goal_reward
        self.obstacle = obstacle
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
        elif self.state in self.obstacle:
            return self.state, -3, True
        elif self.state == (0, 0):
            return self.state, -5, True
        else:
            return self.state, self.step_reward, False  # Regular step

    def get_all_states(self):
        """Return all possible states in the environment."""
        return [(x, y) for x in range(self.grid_size[0]) for y in range(self.grid_size[1])]

    def get_all_actions(self):
        """Return all possible actions."""
        return ["up", "down", "left", "right"]


def iterative_policy_evaluation(env, policy, gamma=0.9, theta=1e-6):
    """Evaluate the value function V(s) for a given policy."""
    states = env.get_all_states()
    actions = env.get_all_actions()
    action_prob = 1 / len(actions)

    V = {state: 0 for state in states}

    for _ in range(5):
        delta = 0

        for state in states:
            env.state = state
            v = V[state]
            new_v = 0

            for action in actions:
                next_state, reward, _ = env.step(action)
                new_v += action_prob * (reward + gamma * V[next_state])

            V[state] = new_v
            delta = max(delta, abs(v - new_v))
        if delta < theta:
            break
    return V


def policy_improvement(env, V, gamma=0.9):
    """Improve the policy based on the current value function V(s)."""
    states = env.get_all_states()
    actions = env.get_all_actions()
    policy = {}

    for state in states:
        env.state = state
        action_values = {}
        for action in actions:
            next_state, reward, _ = env.step(action)
            action_values[action] = reward + gamma * V[next_state]
        print(f"State {state}, Action Values: {action_values}")  # Debug action values
        best_action = max(action_values, key=action_values.get)
        policy[state] = {a: 1 if a == best_action else 0 for a in actions}

    return policy


def policy_iteration(env, gamma=0.9, theta=1e-6):
    """Perform policy iteration to find the optimal policy and value function."""
    states = env.get_all_states()
    actions = env.get_all_actions()

    # Initialize a random policy with equal probabilities for all actions
    policy = {state: {action: 1 / len(actions) for action in actions} for state in states}
    V = {state: 0 for state in states}

    for _ in range(5):
        # Policy Evaluation
        V = iterative_policy_evaluation(env, policy, gamma, theta)

        # Policy Improvement
        new_policy = policy_improvement(env, V, gamma)

        # Stop if the policy has converged
        if new_policy == policy:
            break

        policy = new_policy

    return policy, V

def value_iteration(env, gamma=0.9, theta=1e-6):
    """Perform value iteration to find the optimal value function and policy."""
    states = env.get_all_states()
    actions = env.get_all_actions()
    V = {state: 0 for state in states}

    for _ in range(5):
        delta = 0

        for state in states:
            env.state = state
            v = V[state]
            action_values = []
            for action in actions:
                next_state, reward, _ = env.step(action)
                action_values.append(reward + gamma * V[next_state])
            V[state] = max(action_values)
            delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break

    policy = {}
    for state in states:
        env.state = state
        action_values = {}
        for action in actions:
            next_state, reward, _ = env.step(action)
            action_values[action] = reward + gamma * V[next_state]
        best_action = max(action_values, key=action_values.get)
        policy[state] = best_action

    return policy, V


# Initialize the environment
env = GridWorld()

# Policy Iteration
optimal_policy, optimal_value = policy_iteration(env)
print("Optimal Policy from Policy Iteration:")
for state, action in optimal_policy.items():
    print(f"State {state}: {action}")

# Value Iteration
optimal_policy_vi, optimal_value_vi = value_iteration(env)
print("\nOptimal Policy from Value Iteration:")
for state, action in optimal_policy_vi.items():
    print(f"State {state}: {action}")