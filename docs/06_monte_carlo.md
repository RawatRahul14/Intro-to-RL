## Monte Carlo Prediction

Monte Carlo prediction estimates the value function $V(s)$ for a given policy $\pi$, based on returns observed from sample episodes.

**Steps:**

- Generate episodes by following the policy $\pi$.
- For each state in episodes, coompute the term $G_t$ from that state onward:

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma ^ 2 R_{t+3} + \dots
$$

- Update $V(s)$ as the average of all observed returns for that state.


## MOnte Carlo Control (Exploring Starts)

Monte Carlo control learns the **optimal policy** $\pi ^\star$ by iteratively improving both the policy and action-value funtion $Q(s, a)$.

**Steps:**

- Use an exploring-starts approach:
    - Randomly initialize each episode with a state-action pair to ensure all state-action pairs are explored.

- Generate an episode and compute returns $G_t$ for each state-action pair.
- Update $Q(s, a)$ as the average of returns for each s, a.
- Update the policy $\pi(s)$ to select the action a with the highest $Q(s, a)$:

$$
\pi (s) = arg \max_a Q(s, a)
$$