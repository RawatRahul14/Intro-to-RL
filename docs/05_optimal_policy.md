## Optimal Policy and Value Functions

**Iterative Policy Evaluation**, **Policy Improvement**, **Policy Iteration**, and **Value Iteration**. These methods are fundamental for solving MDPs and are used to find the **optimal policy** and **value functions**.

1. **Iterative Policy Evaluation**

This method computes the **state-value function** ($V^\pi(s)$) for a given policy $\pi$.

**Iterative Policy Evaluation** is a way to estimate how "good" a policy (a way of making decision) is, based on the reward it will earn over time.

**Algorithm:**
- Start wuth an initial value function $V(s) = 0$ for all states.
- Update $V(s)$ iteratively using the Bellman Equation for policy evaluation:
$$
V^\pi := \sum_a \pi(a|s) \sum_{s'} P(s'|s, a)[R(s, a) + \gamma V^\pi(s')]
$$
- Repeat until convergence ($\Delta < \theta$, where $\Delta$ is the maximum change in $V(s)$).

2. **Policy Improvement**

This method improves the policy by acting greedily with respect to the current value function.

**Algorithm:**
- For each state s, update the policy to:

$$
\pi'(s) = arg \max_a \sum_{s'} P(s'|s, a)[R(s, a) + \gamma V(s')]
$$

3. **Policy Iteration**

Policy Iteration alternates between **Policy Evaluation** and **Policy Iteration** until the policy converges to the optimal policy $\pi ^\star$.

**Algorithm:**
- Starts with an arbitrary policy $\pi$.
- Performs policy evaluation to compute $V ^ \pi(s)$.
- Perform policy improvement to compute a new policy $\pi '$.
- Repeat steps 2-3 times until the policy stops changing.

4. **Value Iteration**

Value Iteration directly finds the optimal value function $V ^\star(s)$ by iteratively applying the **Bellman Optimality Equation:**

$$
V ^\star(s) = \max_a \sum_{s'} P(s'|s, a)[R(s, a) + \gamma V ^\star(s')]
$$

**Algorithm**
- Starts with $V(s) = 0$ for all states.
- Update $V(s)$ for all states using:
$$
V(s) := \max_a \sum_{s'} P(s'|s, a)[R(s, a) + \gamma V(s')]
$$
- Repeat until convergence.

Below is the Maze tha have been used in the coding part:

![Diagram Description](path.drawio.svg)
