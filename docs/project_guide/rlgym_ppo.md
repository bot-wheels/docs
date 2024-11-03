# Installation of RLGym-PPO and rlgym-sim

## Step 1: Install RLGym

To install RLGym and ensure it works, follow the instructions in the [installation guide](https://github.com/bot-wheels/bot-wheels-core?tab=readme-ov-file#installation).

## Step 2: Install RLGym-PPO and rlgym-sim

Follow these steps to install all necessary components.

1. **Install the RocketSim package** using:

    ```sh
    pip install rocketsim
    ```

2. **Install the rlgym_sim package** using:

    ```sh
    pip install git+https://github.com/AechPro/rocket-league-gym-sim@main
    ```

3. **Download the asset dumper** from [here](https://github.com/ZealanL/RLArenaCollisionDumper/releases/tag/v1.0.0) and follow its instructions to create the `collision_meshes` folder (we will move it later).
4. If you have an NVIDIA graphics card, **install CUDA** from the [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive).
5. **Install PyTorch** from the [official website](https://pytorch.org/get-started/locally/). If you installed CUDA, choose the CUDA version; otherwise, choose the CPU version.
6. **Install RLGym-PPO** using:

    ```sh
    pip install git+https://github.com/AechPro/rlgym-ppo
    ```

7. **Move `collision_meshes` to your bot's folder**.
8. **Copy `example.py` from RLGym-PPO** and verify it works. You can find the `example.py` file [here](https://github.com/AechPro/rlgym-ppo/blob/main/example.py).
