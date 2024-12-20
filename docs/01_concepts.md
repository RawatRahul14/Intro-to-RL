## What is Reinforcement Learning?

Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. The agent aims to maximize cumulative rewards over time. Unlike supervised learning, RL does not rely on labeled input-output pairs; instead, it learns through trial and error, guided by rewards or punishments.

### Core Concepts of Reinforcement Learning

1. **Agent and Environment**
    - ***Agent***: The learner or decision-maker. It is the entity that takes actions in the environment based on its policy.
    - ***Environment***: Everything the agent interacts with. It provides feedback in the form of rewards and transitions the agent to new states based on the actions taken.

2. **State (S)**
    - A state represents the current situation of the environment, providing all necessary information for the agent to decide what action to take.
    - Example:
        - In chess, the state could be the current arrangement of the board.
        - In a robot navigation task, the state could be the robot's position and orientation.

3. **Action (A)**
    - Actions are the choices available to the agent at any given state. The agent chooses an action to affect the environment.
    - Example:
        - In chess, an action could be moving a piece to a specific position.
        - In a robotic arm, an action could be rotating a joint by a specific angle.

4. **Reward (R)**
    - A scalar feedback signal received after an action is taken. It indicates how good or bad the action was in a particular state.
    - Example:
        - In a game, a reward might be +1 for a win, -1 for a loss, and 0 otherwise.
        - In a self-driving car, a reward might be a small negative value for every second spent on the road to encourage faster completion.

5. **Policy (𝜋)**
    - The policy defines the agent's behavior: a mapping from states to actions. It can be deterministic (a = π(s)) or stochastic (P(a ∣ s)).
    - Example:
        - In a board game, the policy might decide the next move based on the game's current state.

6. **Value Function**
    - The value function estimates the long-term return (future rewards) for being in a certain state or taking a certain action.
        - ***State-Value Function (V(s))***: Expected return starting from state s and following the policy thereafter.
        - ***Action-Value Function (Q(s,a))***: Expected return starting from state s, taking action a, and following the policy thereafter.

### Markov Decision Process (MDP)
Reinforcement Learning problems are modeled as a Markov Decision Process (MDP). An MDP provides a mathematical framework to describe decision-making problems where outcomes are partly random and partly under the control of the agent.

An MDP is defined by the following components:

1. States (S):
    - The set of all possible states in the environment.
    - Example: In a grid world, the states could be the coordinates of the grid.

2. Actions (A):
    - The set of all possible actions the agent can take.
    - Example: In a grid world, actions might be {up,down,left,right}.

3. Transition Function (P(s′ ∣ s, a)):
    - Defines the probability of moving to state s′ after taking action a in state s.
    - Example: If a robot moves with some uncertainty, the transition might be probabilistic rather than deterministic.

4. Reward Function (R(s,a)):
    - Specifies the immediate reward received after taking action a in state s.

5. Discount Factor (γ):
    - A value between 0 and 1 that determines the importance of future rewards. 
    - γ = 0: The agent focuses only on immediate rewards.
    - γ close to 1: The agent values future rewards more heavily.

## The Goal of Reinforcement Learning
The objective of an RL agent is to find an optimal policy (π*) that maximizes the expected cumulative reward (or return). The return Gt at time step t is given by:

![alt text](images/image.png)

**Where**: 
- R(t+k+1) is the reward received k steps into the future.
- γ is the discount factor, which ensures the return is finite.

## Key Intuitions
- **Exploration vs. Exploitation**:
     - The agent must balance exploring new actions to discover their rewards and exploiting known actions that yield high rewards.
- **Delayed Gratification**:
    - Actions that might not provide immediate rewards could lead to higher cumulative rewards in the future.
- **Markov Property**:
    - The future state depends only on the current state and action, not on the sequence of states that preceded it.

For the code file:

Click on the [link](../src/main.py).