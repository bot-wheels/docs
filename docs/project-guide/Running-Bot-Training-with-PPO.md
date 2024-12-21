# Documentation for Running Bot Training with PPO

## Introduction

This documentation provides clear instructions on how to run bot training using the PPO algorithm. It outlines all necessary steps, configurations, and dependencies required for successful execution. Below, you will find prerequisites to set up the environment, detailed configuration steps, and guidance on initiating the training process.

## Prerequisites

- You need the following libraries to run the bot:
  - configparser
  - os
  - rlgym
  - stable_baselines3 (PPO)
  - pynput (keyboard)
  - gym.spaces
  - numpy
  - pathlib
- The bot relies on a custom GoogleDriveManager (from utils.drive_manager import GoogleDriveManager).  
  - A credentials.json file is required, containing secrets to connect to Google Drive.  
  - Users who want to run the script must share their email to gain access.  
  - For inquiries related to Google Drive, contact @Assassin-PL.

## Configuration Steps

1. **Install Dependencies**  
   Make sure you have all required libraries installed. A virtual environment (e.g., venv or conda) is highly recommended to keep dependencies organized.

2. **Create the Agent Instance**  
   Instantiate the `SimpleAgent` class. This agent automatically loads any previously trained model if one is found:

   ```python
   from agent import SimpleAgent

   agent = SimpleAgent()

   ```

3. **Configure Bot Settings**  
   In the `setting.cfg` file, adjust the bot's parameters to define how the training loop behaves. For example, you can modify episode lengths, reward function details, or specific environment constants. Any change here affects how the bot explores and learns within the PPO framework.

4. **Initiate Training**  
   After configuring your environment and creating the `SimpleAgent` instance, start the training loop by calling:

   ```python
   agent.train()
   ```

   This process leverages any existing model, retrains it with the updated settings, and logs progress details.

## Training Execution

When you call `agent.train()`, the following actions occur:

- The bot environment (defined via `rlgym` and your configuration) initializes using the `make_env()` method. It's important to note that PPO requires a specific environment setup; the `make_env()` method cannot create a training environment if, for example, the bot was previously trained to play against another bot or in a training loop reacting to human input.
- The previously trained model (if available) is loaded to continue its training.
- Data (observations, rewards, etc.) is continuously collected, and the agent updates its policy using PPO.
- Periodically or upon completion, the agent saves checkpoints of the model.

**Configuration Note:**

Ensure that the `make_env()` function correctly returns the environment (`env`). All accessible variables and parameters for configuring the training loop are located in the `settings.cfg` file. Only make changes within this file to alter training configurations, as everything else has been preconfigured.

## Parameters and Their Effects

In the `setting.cfg` file and within your code, you can adjust various parameters. Key parameters include:

- **realtime**: Boolean (`true`/`false`) that determines whether to run training in accelerated mode. Setting to `true` causes game time to be sped up (e.g., 1 second of real time corresponds to 1000 seconds in the game).

- **modelName**: String that specifies the name of the model being used or saved. This allows easy management of different training models.

- **timesteps**: Number of steps that defines how many environment steps occur before a model update. Adjusting this can affect the frequency and efficiency of policy updates.

- **human**: Boolean that specifies whether the bot is being trained to play against a human player. Setting this to `true` enables training scenarios where the bot competes against human input, enhancing its adaptability.

Tweaking these parameters can lead to different training outcomes in terms of speed, stability, and bot performance.

## Additional Information

- **Automatic Model Upload**: When training finishes (or at certain checkpoints), the final model can be automatically pushed to Google Drive. Ensure you have set up `credentials.json` and provided the necessary access for your email.
- **Monitoring**: Check logs and console output for training progress. This can help identify if the agent is converging or if adjustments to parameters are needed.
- **Further Reading**: Refer to `stable_baselines3` documentation for advanced PPO configurations, or consult `rlgym` documentation to customize the training environment further.
- **Development Origin**: The bot was developed following the instructions from the creators of `rlgym` ([https://rlgym.org/docs-page.html#tutorials](https://rlgym.org/docs-page.html#tutorials)) and was modeled after the sample bot from the repository: [https://github.com/RLBot/RLBotPythonExample](https://github.com/RLBot/RLBotPythonExample).
