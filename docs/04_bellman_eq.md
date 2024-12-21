## Bellman Equations

The **Bellman equations** describe the relationship between a value function and its components (rewards and transitions).

**Bellman Equation for $V^\pi(s)$**:
The value of a state under the policy $\pi$ is equal to the immediate reward plus thediscounted value of the next value:

$$
V^\pi(s) = \sum_a \pi(a | s) \sum_{s'} P (s' | s, a)[R(s, a) + \gamma V^\pi(s')]
$$

where,

- $\sum_a \pi(a | s)$: This is the probability of selecting action a in state s under policy $\pi$.

- $P(s'|s, a)$: Probability of going to state s' from s.
- $\gamma$: Discount Factor.
- $R(s,a)$: This is the reward the agent recieves after taking the action a in the state s.
- $V^\pi(s')$: This is the future value after for new state after the action a is taken.

**Bellman equation for $Q^\pi(s, a)$**:
The value of state-action pair policy $\pi$ is equal to the immediate reward plus the discounted value of the next state:

$$
Q^\pi(s, a) = \sum_{s'}P(s'|s, a)[R(s, a) + \gamma \sum_{a'} \pi(a'|s') Q^\pi(s'|a')]
$$

where, 
- $P(s'|s, a)$: Probability of going to state $s'$ after taking action a in state s.
- $R(s, a)$: Immidiate reward of taking action a at state s.
- $\gamma$: Discount factor.
- $\pi(a'|s')$: It represents how the agent behaves (takes action) when in the state s' (next state).
- $Q^\pi(s'|a')$: Cumulative value for the next state s' after taking action a'.
- $\sum_{a'}$: Considering all the actions the agent can take in the next state s'.

**Bellman Optimality Equations:**

For the optimal value functions, the **Bellman** equations become:

**For $V^*(s)$:**

$$
V^*(s) = \max_a \sum_{s'} P (s' | s, a)[R(s, a) + \gamma V^*(s')]
$$

**For $Q^*(s, a)$:**

$$
Q^*(s, a) = \sum_{s'}P(s'|s, a)[R(s, a) + \gamma \max_{a'} Q^*(s'|a')]
$$

These equations are central to algorithms like **Value Iteration** and **Q-Learning**.

For the code file:

Click on the [link](../src/bellman_eq.py).