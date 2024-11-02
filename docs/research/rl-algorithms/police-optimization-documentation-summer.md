# Research and Documentation of Algorithm Categories for Rocket League Bot

* **Police Optimization \- Igor Malkovskiy**

**Materials:**

[Policy Gradient Algorithms Explained by Arthur Juliani | Towards Data Science](https://towardsdatascience.com/an-intuitive-explanation-of-policy-gradient-part-1-reinforce-aa4392cbfd3c)

[Parts 2:Kinds of RL Algorithms](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html)

[Part 3:Intro to Police optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)

[Proximal Police Optimization](https://huggingface.co/blog/deep-rl-ppo)

**What is Police Optimization?**

Policy Optimization is a method in reinforcement learning that focuses on improving the policy directly by optimizing its parameters. Unlike value-based methods like Q-Learning, which optimize the value function, Policy Optimization aims to improve the agent’s behavior policy continuously. You can find exactly how Police Optimization works in the links above.

**Examples of uses:**

[Building-a-reinforcement-learning-agent-that-can-play-rocket-leagu](https://sohum-padhye.medium.com/building-a-reinforcement-learning-agent-that-can-play-rocket-league-5df59c69b1f5)

[RL_Final_Report.pdf](http://bryantmcarthur.com/Papers/RL_Final_Report.pdf)

[MA_Neville_Walo_Seer_RLRL.pdf](https://nevillewalo.ch/assets/docs/MA_Neville_Walo_Seer_RLRL.pdf) - there is a github with this work attached to the second page from below

***Why Policy Optimization is/Isn't Popular for Developing Bots in Rocket League:***

Policy optimization is popular for developing bots in Rocket League due to its adaptability in dynamic environments. It allows for direct optimization of the agent’s behavior, crucial in a fast-paced game where decision-making needs to be continuous and efficient. Methods like PPO (Proximal Policy Optimization) can adjust actions in real-time, enhancing performance in complex scenarios like ball control or aerial maneuvers.

However, policy optimization isn't always favored because it often requires significant computational resources and data. Training can be slow, and models may struggle with long-term strategy, which is key in Rocket League. Thus, alternative methods like imitation learning or hybrid approaches might be preferred in certain contexts for efficiency and strategic depth.

**Conclusion:**

In conclusion, while policy optimization provides a powerful framework for developing adaptable and responsive bots in Rocket League, its computational intensity and challenges with long-term strategy can limit its widespread use. Depending on the specific goals—whether it's real-time performance or strategic planning—developers may choose alternative or hybrid approaches to better balance efficiency and effectiveness in bot behavior.
