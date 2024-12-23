## Understanding Markov Decision Processes (MDPs)

Markov Decision Processes (MDPs) are a mathematical framework used to model decision-making problems. They are widely used in Reinforcement Learning (RL) to describe the interaction between an agent and its environment.

The Markov Decision Process (MDP) is primarily a framework or model that provides a formal way to describe a decision-making problem where outcomes are influenced by both the current state and the agent's actions. It does not inherently include any learning mechanism. Instead, learning algorithms are applied to solve the MDP.

1. Why Do We Need MDPs?

Many real-world problems involve sequential decision-making:

- A robot navigating a maze.
- A taxi picking up and dropping off passengers.
- A stock trader deciding when to buy or sell stocks.

In these problems, the agent needs to make a series of decisions, considering the future outcomes of its actions. MDPs provide a formal framework for such problems, helping us define:

- The current situation (state).
- The available choices (actions).
- The rules of the environment (transitions).
- The objective (maximize rewards).

2. Key Components of an MDP
An MDP is defined by five components:
(S,A,P,R,γ).

- States (S)
    - What is it?

        The set of all possible situations the agent can be in. A state captures everything the agent needs to know about the environment at a particular time.
    - Examples:
        - In a grid world: The state could be the agent's current position (e.g., S = (x, y)).
       - In a game of chess: The state could be the arrangement of pieces on the board.

- Actions (A)
    - What is it?

        The set of all possible decisions the agent can make in a given state.
    - Examples:
        - In a grid world: Actions could be up, down, left, or right.
        - In a robot arm: Actions could be moving a joint by a specific angle.

- Transition Function (P(s′ ∣ s, a))
    - What is it?

        Describes the dynamics of the environment: If the agent takes action a in state s, what is the probability of moving to state s′?
    - Examples:
        - In a simple environment: P(s′ ∣ s, a) might be deterministic (e.g., moving right always moves to the next cell).
        - In a stochastic environment: P(s′ ∣ s, a) might include randomness (e.g., the agent may slip and move to a different state than intended).

- Rewards (R(s, a))
    - What is it?

        A numerical feedback signal that tells the agent how good or bad it is to take action a in state s.
    - Examples:
        - In a delivery problem: +10 for successful delivery, −1 for every step taken.
        - In a game: +100 for winning, −100 for losing, 0 otherwise.

- Discount Factor (γ)
    - What is it?

        A value between 0 and 1 that determines the importance of future rewards compared to immediate rewards.
    - Examples:
        - γ = 0: The agent only cares about immediate rewards.
        - γ = 0.9: The agent values future rewards but discounts them as they get further into the future.

3. The Goal of an MDP
The objective of the agent in an MDP is to maximize the total reward (called the return) over time.
The return is defined as:

$$
G_{t} = R_{t+1} + \gamma R_{t+2} + \gamma ^ 2 R_{t+3} + \dots = \sum_{k=0}^\infty \gamma^k R_{t+k+1}
$$

Where:
- R(t+1) : Reward received after the first action.
- γ: Discount factor that reduces the weight of future rewards.

The agent must learn a policy (π), which is a mapping from states to actions, to maximize this return.

4. Example: Grid world

Let's take a simple grid world of environment to understand how to define an MDP.

**Environmental Description**
- A 5 X 5 grid where an agent starts at the top-left corner and needs to reach the bottom-right corner.
- The agent can move up, down, right and left.
- Each move gives a reward of -1 (penalty for taking a step).
- Reaching the goal gives a reward of +10.

**MDP Defination**
- States (S):
    - Each cell in a grid is state
    - S = {(0, 0), (0, 1), ..., (4, 4)}

- Actions (A):
    - A = {up, down, left, right}

- Transition Function (P(s' | s, a)): 
    - If the agent tries to move outside the grid, it stays in the same state.
    - For example, if the agent is at (0, 0) and chooses `up`, it remains at (0, 0).

- Rewards (R(s, a)):
    - R(s, a) = -1 for every step.
    - R((4, 4), any action) = +10

- Discount Factor (γ):
    - Choose γ = 0.9 to encourage faster completion.

5. Solving an MDP
To solve an MDP, an agent must learn:
- **Value Function (V(s))**:

    The expected return starting from state s.

$$
V(s) = E_\pi [G_t|s_t = s]
$$

- **Action-Value Function (Q(s, a)):**
    
    The expected return starting from state s, taking action a, and following the policy thereafter.

$$
Q(s, a) = E_\pi [G_t|s_t = s, a_t = a]
$$

The agent can then use algorithms like **Dynamic Programming, Monte Carlo,** or **Temporial Difference Learnging** to compute these functions.

For the code file:

Click on the [link](../src/mdp.py).