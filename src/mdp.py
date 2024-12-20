import numpy as np

class GridWorld:
    def __init__(self, grid_size = (5, 5)):
        self.grid_size = grid_size
        self.state = (0, 0)
        self.goal = (4, 4)

    def reset(self):
        self.state = (0, 0)
        return self.state
    
    def step(self, action):
        x, y = self.state

        if action == "up":
            x = max(0, x - 1)
        
        elif action == "down":
            x = min(self.grid_size[0] - 1, x + 1)

        elif action == "left":
            y = max(0, y - 1)

        else:
            y = min(self.grid_size[1] - 1, y + 1)

        self.state = (x, y)

        if self.state == self.goal:
            return self.state, 10, True
        
        else:
            return self.state, -1, False
        
env = GridWorld()
state = env.reset()
done = False

while not done:
    action = np.random.choice(["up", "down", "left", "right"])
    next_state, reward, done = env.step(action)
    print(f"State: {state}, Action: {action}, Reward: {reward}, Next State: {next_state}")
    state = next_state