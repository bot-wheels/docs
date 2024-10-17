# Research and Documentation of Algorithm Categories for Rocket League Bot

## Q-Learning - Anna Ivanytska

### Materials

- [Q-Learning Algorithm: From Explanation to Implementation | by Amrani Amine | Towards Data Science](https://towardsdatascience.com/q-learning-algorithm-from-explanation-to-implementation-cdbeda2ea187)  
- [An Introduction to Q-Learning: A Tutorial For Beginners | DataCamp](https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial)  
- [Reinforcement Learning Explained Visually (Part 4): Q Learning, step-by-step | by Ketan Doshi | Towards Data Science](https://towardsdatascience.com/reinforcement-learning-explained-visually-part-4-q-learning-step-by-step-b65efb731d3e)

### What is Q-learning?

Q-learning is a model-free, value-based, off-policy algorithm that finds the best series of actions based on the agent's current state. The “Q” stands for quality, representing how valuable an action is in maximizing future rewards.

### Examples of uses

None found.

### Why does it have limited popularity in developing bots for Rocket League?

1. **High Dimensionality and Complexity**: Rocket League is a fast-paced game with a complex environment, involving variables such as player positions, ball trajectory, and physics interactions. This vast state space makes it difficult for Q-learning algorithms to converge to optimal policies, as they require substantial data to learn effectively.
2. **Inconsistent Human Behavior**: Human players display a wide range of strategies and behaviors, which complicates learning. Since no single optimal action exists in many scenarios, Q-learning struggles to generalize from diverse actions, leading to inconsistent learning outcomes.
3. **Compounding Errors**: A single incorrect action can lead to unfamiliar states, making learning more difficult. This issue is magnified in Rocket League, where quick decision-making is crucial.
4. **Resource Intensity**: Developing a competent Q-learning bot requires significant computational resources and time due to the need for numerous simulations.

### Conclusion

Due to these challenges, Rocket League bot developers prefer more advanced machine learning techniques, such as deep reinforcement learning or imitation learning, which can handle the game's complexity more effectively.

---

## Policy Optimization - Igor Malkovskiy

### Materialss

- [Policy Gradient Algorithms Explained by Arthur Juliani | Towards Data Science](https://towardsdatascience.com/an-intuitive-explanation-of-policy-gradient-part-1-reinforce-aa4392cbfd3c)  
- [Parts 2: Kinds of RL Algorithms](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html)  
- [Part 3: Intro to Policy Optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)  
- [Proximal Policy Optimization](https://huggingface.co/blog/deep-rl-ppo)

### What is Policy Optimization?

Policy Optimization is a reinforcement learning method that improves the agent’s behavior policy by directly optimizing its parameters. Unlike value-based methods like Q-learning, which optimize the value function, Policy Optimization focuses on continuous improvement of the policy itself.

### Examples of usess

- [Building a reinforcement learning agent that can play Rocket League](https://sohum-padhye.medium.com/building-a-reinforcement-learning-agent-that-can-play-rocket-league-5df59c69b1f5)

### Why Policy Optimization Isn't Popular for Developing Bots in Rocket League

1. **High Computational Complexity**: Policy optimization algorithms, such as Proximal Policy Optimization (PPO) and Trust Region Policy Optimization (TRPO), require significant computational resources. Rocket League’s complex physical interactions make training and optimizing policies resource-intensive, as numerous simulations are necessary.
2. **Sensitivity to Hyperparameters**: Policy optimization algorithms are highly sensitive to hyperparameters like learning rate and regularization coefficients. Incorrect tuning can lead to unstable or non-functional learning, complicating the application in complex environments like Rocket League.
3. **Generalization Problems**: Rocket League presents a wide range of fast-changing scenarios. Policy optimization algorithms often struggle to generalize in such situations, particularly when continuous control is required.
4. **Complexity of Reward Shaping**: Effective reward design is crucial in policy optimization, and in Rocket League, rewards are challenging to formulate due to the combination of short-term goals (e.g., hitting the ball) and long-term strategies (e.g., ball possession and positioning).

### Why Policy Optimization Could Be Useful for Developing Bots in Rocket League

1. **Effectiveness in Continuous Action Spaces**: Policy optimization excels in environments with continuous action spaces, making it potentially suitable for games like Rocket League that require precise control over the car and the ball.
2. **Resilience to Noise and Stochastic Scenarios**: Policy optimization handles noise and stochastic scenarios better than value-based methods. This is particularly advantageous in Rocket League, where the game's dynamics can change rapidly due to unexpected ball movements or opponent strategies.

### Conclusionn

Although Policy Optimization offers theoretical advantages in environments with continuous action spaces like Rocket League, its use is limited in practice due to high computational demands, generalization challenges, and sensitivity to hyperparameters. Developers often prefer simpler and less resource-intensive approaches, such as Deep Q-Learning or hybrid algorithms.
