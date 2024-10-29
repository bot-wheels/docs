# Research on Data Rendering Options During Training Rocket League Bot

## Introduction

When training a Rocket League bot, visualizing the data in real-time can be challenging. The `rlgym-ppo` library does not provide a straightforward way to display data in real-time using external game visualizers. The best method for real-time visualization is to run the trained bot using `rl-bot`.

## Real-Time Visualization with rl-bot

`rl-bot` allows for real-time visualization by running the trained bot directly in the Rocket League game. This method provides an immediate and interactive way to observe the bot's performance and behavior during training. Methodes are described in `interface-overlay-research.md`.

## Integration with Weights & Biases (wandb)

`rlgym-ppo` offers excellent integration with Weights & Biases (wandb). Wandb is a tool that helps track machine learning experiments, visualize metrics, and collaborate with team members. It provides a comprehensive dashboard to monitor various aspects of the training process, such as loss, accuracy, and other performance metrics.

## Data Displayed During PPO Training

During Proximal Policy Optimization (PPO) training, the following types of data are typically displayed:

- **Training Loss**: Indicates how well the model is learning.
- **Reward**: Measures the performance of the bot.
- **Episode Length**: Shows the duration of each training episode.
- **Policy and Value Function Metrics**: Provide insights into the policy and value function updates.

These metrics can be effectively displayed using wandb, which offers real-time tracking and visualization capabilities. However, for real-time game visualization, `rl-bot` is the preferred tool.

## Summary

In conclusion, for real-time visualizations of the Rocket League bot's performance, `rl-bot` should be used. For monitoring and visualizing machine learning-related data during and after training, `wandb` provides a robust solution. Combining both tools allows for comprehensive analysis and visualization of the training process.
