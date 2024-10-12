**Research and Documentation of Algorithm Categories for Rocket League Bot**

* **Q-Learning \- Anna Ivanytska**

**Materials:**   
[Q-Learning Algorithm: From Explanation to Implementation | by Amrani Amine | Towards Data Science](https://towardsdatascience.com/q-learning-algorithm-from-explanation-to-implementation-cdbeda2ea187)  
[An Introduction to Q-Learning: A Tutorial For Beginners | DataCamp](https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial)  
[Reinforcement Learning Explained Visually (Part 4): Q Learning, step-by-step | by Ketan Doshi | Towards Data Science](https://towardsdatascience.com/reinforcement-learning-explained-visually-part-4-q-learning-step-by-step-b65efb731d3e)

**What is Q-learning?**

Q-learning is a model-free, value-based, off-policy algorithm that will find the best series of actions based on the agent's current state. The “Q” stands for quality. Quality represents how valuable the action is in maximizing future rewards.  

**Examples of uses:**

Not founded.

**Why does it has limited popularity in developing bots for Rocket League?**

1. High Dimensionality and Complexity: Rocket League is a fast-paced game with a complex environment. The state space is vast, including variables such as player positions, ball trajectory, and physics interactions. This complexity makes it difficult for Q-learning algorithms to converge to optimal policies, as they require substantial amounts of data to effectively learn from such a high-dimensional space.  
2. Inconsistent Human Behavior: Human players exhibit a wide range of strategies and behaviors, which complicates the learning process. Since there is no single optimal action in many situations, Q-learning struggles to generalize from the diverse actions taken by players, leading to inconsistent learning outcomes.  
3. Compounding Errors: In Q-learning, a single incorrect action can lead to a state that the model has not encountered before, complicating the learning process. This issue is exacerbated in a dynamic game like Rocket League, where quick decision-making is critical.  
4. Resource Intensity: Developing a competent Q-learning bot requires significant computational resources and time. The training process involves running numerous simulations, which can be resource-intensive. This might deter developers from pursuing Q-learning in favor of simpler or more established methods.

**Conclusion:**

Given these challenges, developers of Rocket League bots tend to prefer more advanced machine learning techniques that can handle the game's complexity more effectively, such as deep reinforcement learning or imitation learning.

***Police Optimization***

* **Police Optimization \- Igor Malkovskiy**

**Materials:**   
[**Policy Gradient Algorithms Explained by Arthur Juliani | Towards Data Science**](https://towardsdatascience.com/an-intuitive-explanation-of-policy-gradient-part-1-reinforce-aa4392cbfd3c)  
[**Parts 2:Kinds of RL Algorithms**](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html)  
[**Part 3:Intro to Police optimization**](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)  
[**Proximal Police Optimization**](https://huggingface.co/blog/deep-rl-ppo)

**What is Police Optimization?**

Policy Optimization is a method in reinforcement learning that focuses on improving the policy directly by optimizing its parameters. Unlike value-based methods like Q-Learning, which optimize the value function, Policy Optimization aims to improve the agent’s behavior policy continuously. You can find exactly how Police Optimization works in the links above.

**Examples of uses:**  
[**Building-a-reinforcement-learning-agent-that-can-play-rocket-league**](https://sohum-padhye.medium.com/building-a-reinforcement-learning-agent-that-can-play-rocket-league-5df59c69b1f5)

### **Why Policy Optimization is/Isn't Popular for Developing Bots in Rocket League:**

#### **Why Policy Optimization Isn't Popular for Developing Bots in Rocket League:**

1. **High Computational Complexity**: Policy optimization algorithms like Proximal Policy Optimization (PPO) and Trust Region Policy Optimization (TRPO) require significant computational resources. Rocket League is a fast-paced game with highly complex physical interactions, making the process of training and optimizing policies extremely resource-intensive. To train bots effectively, a vast number of simulations are required, which becomes a barrier for many developers.  
2. **Sensitivity to Hyperparameters**: Policy optimization algorithms are very sensitive to hyperparameter tuning (e.g., learning rate, regularization coefficients, etc.). Incorrectly chosen parameters can lead to unstable or non-functional learning, making their application in complex game scenarios like Rocket League more difficult, as these algorithms require precise tuning for each specific state.  
3. **Generalization Problems**: Rocket League is a game with a wide range of scenarios where strategies can change rapidly. Policy optimization algorithms often struggle to generalize in fast-changing game states, especially in complex situations requiring continuous control. This makes them less suitable for games with high variability, where rapid adaptation is necessary.  
4. **Complexity of Reward Shaping**: Policy optimization requires careful design of the reward function to help the agent learn the correct actions in the long term. In Rocket League, rewards can be difficult to formulate because the game combines many short-term goals (e.g., hitting the ball, blocking an opponent) with long-term strategies (e.g., overall ball possession, positioning), making the reward function design a challenging task.

#### **Why Policy Optimization Could Be Useful for Developing Bots in Rocket League:**

1. **Effectiveness in Continuous Action Spaces**: Unlike Q-Learning, which is better suited for discrete actions, Policy Optimization works well with continuous action spaces, making it potentially suitable for complex game environments like Rocket League, where fine-tuned control over the car and the ball is required.  
2. **Resilience to Noise and Stochastic Scenarios**: Policy optimization algorithms handle noise and stochastic scenarios better than value-based approaches. In Rocket League, many factors can change rapidly (e.g., unexpected ball hits, sudden opponent strategies), and Policy Optimization could help bots respond more flexibly to such changes.

### **Conclusion:**

While Policy Optimization may theoretically offer advantages in games with continuous action spaces like Rocket League, in practice, its use is limited due to computational complexity, generalization challenges, and the difficulty of hyperparameter tuning. As a result, developers often prefer simpler and less resource-intensive approaches, such as Deep Q-Learning or hybrid algorithms.

