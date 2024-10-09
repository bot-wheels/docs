# Rocket League AI Agent Setup

## Objective

Set up the environment necessary for integrating an AI agent with Rocket League. We will walk through installing the game, relevant mods, and setting up the development environment.

---

## 1. Requirements

Before we begin setting up the environment, ensure that you have the following:

- **A Windows 10 PC:** The setup is tested and supported on Windows 10.
- **Rocket League:** Both Steam and Epic versions of Rocket League are supported.
- **Bakkesmod:** A popular mod for Rocket League that allows integration of Python scripts and other plugins with the game.
- **RLGym plugin for Bakkesmod:** Essential for interfacing with the game. If you install RLGym via pip, this will be installed automatically.
- **Python:** Version between 3.7 and 3.9 is required (version 3.10 is not supported). We recommend using the stable version 3.8.19.

### Detailed Steps

#### 1.1 Install Rocket League

- Install Rocket League from either **Steam** or **Epic Games Store**. This will serve as the base game that the AI agent will interact with.

#### 1.2 Install Bakkesmod

- **Bakkesmod** is a tool that enables external modding capabilities, including Python script integration with Rocket League. It’s a critical mod for controlling aspects of the game programmatically.
- Download and install Bakkesmod from the official [Bakkesmod website](https://bakkesmod.com/).
  
#### 1.3 Install RLGym Plugin

- **RLGym** is a framework that allows you to develop and train AI agents for Rocket League. It interacts with Bakkesmod and provides a streamlined interface for AI development.
- If you are installing RLGym via pip, the necessary plugin for Bakkesmod will be installed automatically. Otherwise, you can manually install the plugin from the RLGym GitHub repository.

#### 1.4 Install Python

- Download and install Python, ensuring you have a version between 3.7 and 3.9. The recommended version for this setup is **Python 3.8.19**.
- You can download Python from the official [Python website](https://www.python.org/downloads/release/python-3819/).
- During installation, ensure that you check the box **"Add Python to PATH"** for ease of use in command-line operations.

## 2. Configuring Rocket League and Bakkesmod

Once the installation is complete, follow these steps to launch the game and configure Bakkesmod:

### 2.1 Launch Rocket League

- Open the **Epic Games Launcher** and launch **Rocket League** from your library.
  
### 2.2 Configure Bakkesmod

- After launching Rocket League, open **Bakkesmod** by pressing the default hotkey **F2**.
- Navigate to the **"Python Scripts"** tab. This is where you will manage Python script integration with the game.
  
### 2.3 Plugin Configuration

- Once in the Bakkesmod window, go to the **"Plugins"** section.
- Open the **Plugin Manager** and search for the **Rocket League Gym** plugin.
- Check the box next to **Rocket League Gym** to enable the plugin.

At this stage, you should have Rocket League and Bakkesmod running, with the necessary plugins configured. The game is now ready for interaction with AI scripts.

## 3. Setting up the Python Environment

To ensure smooth interaction between Python and Rocket League, we recommend using a virtual environment like **Conda**. This will help manage dependencies and prevent conflicts with other projects.

### 3.1 Install Python 3.8.19

- First, download and install **Python 3.8.19** from the official [Python website](https://www.python.org/downloads/release/python-3819/). This is the most stable version for our setup.

### 3.2 Create a Virtual Environment using Conda

- If you have **Conda** installed, create a new virtual environment by running the following commands in your terminal:

  ```bash
  conda create --name rocketleague_env python=3.8.19
  conda activate rocketleague_env
  
This will create and activate a new virtual environment with Python 3.8.19.

### 3.3 Install Required Packages

- Once the environment is activated, install the necessary packages by running the following commands:

  1. Install **pywin32** version 228, which is required for certain Windows-specific operations:

     ```bash
     pip install pywin32==228
     ```

  2. Install **RLGym**, the key package that interfaces with Rocket League:

     ```bash
     pip install rlgym
     ```

With these steps completed, your Python environment is fully configured and ready for development with Rocket League.

## 4. Example Code for Agent Interaction

In this section, we'll walk through the basic structure of a Python bot for Rocket League. The setup consists of two main files:

- `main.py`: This file handles the creation of the agent object and determines whether to train the agent or simply run it.
- `Agent.py`: This file defines the `SimpleAgent` class, which contains the logic for training and running the agent.

### 4.1 `main.py`

Here is the content of the `main.py` file, which initializes the agent and provides an option to train or run it:

  ```python
    from Agent import SimpleAgent
    
    if __name__ == "__main__":
        agent = SimpleAgent(real_time=True)
        mode = input("Enter 'train' to train or 'run' to run the agent: ").strip().lower()
    
        if mode == "train":
            agent.train(timesteps=10000)
        elif mode == "run":
            agent.run_infinite()
  ```

### 4.2 `Agent.py`

The `SimpleAgent` class is responsible for creating and managing the agent. It includes methods for training, loading models, and running the agent in the Rocket League environment. Below is the key implementation of the agent class:

```python
import os
import rlgym
from stable_baselines3 import PPO
import time
from rlgym.utils.reward_functions.common_rewards import VelocityBallToGoalReward
from rlgym.utils.terminal_conditions.common_conditions import TimeoutCondition
from rlgym.utils.obs_builders import DefaultObs
from rlgym.utils.action_parsers import ContinuousAction

def make_env():
    return rlgym.make(
        obs_builder=DefaultObs(),
        action_parser=ContinuousAction(),
        reward_fn=VelocityBallToGoalReward(),
        terminal_conditions=[TimeoutCondition(225)]
    )

class SimpleAgent:
    def __init__(self, model_path="ppo_rlgym_model.zip", real_time=True):
        self.model_path = model_path
        self.real_time = real_time
        self.env = make_env()
        self.model = None

    def train(self, timesteps=10000):
        if os.path.exists(self.model_path):
            print(f"Loading existing model from {self.model_path}")
            self.model = PPO.load(self.model_path, env=self.env)
        else:
            print("No existing model found, training from scratch.")
            self.model = PPO("MlpPolicy", self.env, verbose=1)

        self.model.learn(total_timesteps=timesteps)
        self.model.save(self.model_path)
        print(f"Model saved to {self.model_path}")

    def load_model(self):
        self.model = PPO.load(self.model_path)
        print(f"Model loaded from {self.model_path}")

    def run(self, episodes=100):
        if self.model is None:
            self.load_model()

        for _ in range(episodes):
            obs = self.env.reset()
            done = False
            while not done:
                start_time = time.time()
                action, _ = self.model.predict(obs)
                next_obs, reward, done, gameinfo = self.env.step(action)
                obs = next_obs

                if self.real_time:
                    elapsed = time.time() - start_time
                    time.sleep(max(0, 1/60.0 - elapsed))  # Adjust to match 60 FPS

    def run_infinite(self):
        while True:
            self.run(episodes=1)
```

### 4.3 Detailed Explanation of the Code

1. **`make_env()`**:
   - This function creates the Rocket League environment that the agent interacts with. It uses the following key components:
     - **`DefaultObs()`**: Defines how observations are generated for the agent. This includes the positions, velocities, and other relevant data of the ball and cars.
     - **`ContinuousAction()`**: Defines the action space as continuous, allowing the agent to make precise adjustments to the car’s movement.
     - **`VelocityBallToGoalReward()`**: A reward function that encourages the agent to push the ball towards the goal. The faster the ball moves towards the goal, the higher the reward.
     - **`TimeoutCondition(225)`**: Ends the episode after 225 game ticks (approximately 3.75 minutes). This serves as a terminal condition to ensure that the agent doesn’t train indefinitely in a single episode.

   When the `make_env()` function is called, it sets up the environment with these components, which are critical for defining how the agent perceives the game and what actions it can take.

2. **`SimpleAgent.__init__()`**:
   - The constructor (`__init__`) initializes the `SimpleAgent` object. Here’s what happens step by step:
     - **`model_path="ppo_rlgym_model.zip"`**: The path where the trained model will be saved or loaded from. If the model exists, it will be loaded from this path when the agent is run.
     - **`real_time=True`**: A flag that determines whether the agent will run in real-time, syncing actions with a 60 FPS frame rate.
     - **`self.env = make_env()`**: Calls the `make_env()` function to set up the Rocket League environment.
     - **`self.model = None`**: The model is initialized as `None`, and will later be set when the agent trains or loads a pre-existing model.

3. **`train(timesteps=10000)`**:
   - This method is used to train the agent. Here’s what happens in sequence:
     - **Check for existing model**: The code first checks if a model already exists at `self.model_path`. If so, it loads the existing model using `PPO.load(self.model_path, env=self.env)`. This allows for continued training from where the previous model left off.
     - **Training from scratch**: If no model is found, the agent will start training from scratch using the **Proximal Policy Optimization (PPO)** algorithm. It initializes a new model with the policy type `MlpPolicy` (a multi-layer perceptron) and the environment created earlier.
     - **Learning**: The agent is trained for a specified number of timesteps (10,000 in this case). During this process, the agent interacts with the environment and learns how to maximize the reward (in this case, pushing the ball towards the goal).
     - **Saving the model**: After training, the model is saved to the specified path (`self.model_path`) for future use. This allows the agent to load the trained model and continue improving or directly use it later.

4. **`load_model()`**:
   - This method is used to load a pre-trained model from `self.model_path`. Here’s what happens:
     - **Loading the model**: The model is loaded from the saved file using `PPO.load(self.model_path)`.
     - **Model ready for use**: After loading, the agent can use the model to predict actions and interact with the environment without further training.

5. **`run(episodes=100)`**:
   - This method runs the agent in the Rocket League environment for a specified number of episodes (100 by default). Here’s what happens step by step:
     - **Model loading**: If the model hasn’t been loaded yet, `self.load_model()` is called to load the pre-trained model.
     - **Environment reset**: At the beginning of each episode, the environment is reset using `obs = self.env.reset()`. This provides the agent with a fresh start for each episode.
     - **Agent action loop**: The agent repeatedly takes actions in the environment until the episode is over:
       - **Action prediction**: The agent predicts the next action based on the current observation (`action, _ = self.model.predict(obs)`).
       - **Step in environment**: The agent applies the action and steps forward in the environment (`next_obs, reward, done, gameinfo = self.env.step(action)`). This returns the next observation (`next_obs`), the reward for the action, and whether the episode is done (`done`).
       - **Update observation**: The observation is updated for the next step (`obs = next_obs`).
     - **Real-time adjustment (if `real_time=True`)**: The loop is adjusted to run at 60 FPS by calculating the time it took to predict and step, then sleeping for the remaining time in the frame (`time.sleep(max(0, 1/60.0 - elapsed))`).
     - **Episode completion**: Once the episode is done, the loop moves to the next episode and resets the environment.

6. **`run_infinite()`**:
   - This method continuously runs the agent without stopping. It calls `run(episodes=1)` in an infinite loop:
     - **Infinite loop**: The agent keeps running one episode at a time in an infinite loop. This is useful for long-term testing or for scenarios where the agent needs to run indefinitely.
     - **Real-time interaction**: If `real_time=True`, the agent’s actions will be synced with 60 FPS, simulating real-time gameplay as closely as possible.
