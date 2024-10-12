# Rocket League RLGym-Sim Setup

## Objective

Set up the environment necessary for bot learning in linux

---

## 1. Requirements

Before we begin setting up the environment, ensure that you have the following:

- **Python:** Version between 3.7 and 3.9 is required (version 3.10 is not supported). We recommend using the stable version 3.8.19.

### Detailed Steps

#### 1.1 Install RocketSim

     pip install rocketsim

#### 1.2 Install rlgym_sim

     pip install git+https://github.com/AechPro/rocket-league-gym-sim@main
  
#### 1.3 Download Asset Dumper

[Download the asset dumper](https://github.com/ZealanL/RLArenaCollisionDumper/releases/tag/v1.0.0) and [follow its usage instructions](https://github.com/ZealanL/RLArenaCollisionDumper/blob/main/README.md) to make the `collision_meshes` folder (we will move this later)

#### 1.4 Install Pytorch

- If you have an NVIDIA GPU, install [CUDA v11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
- Install PyTorch from [its website](https://pytorch.org/get-started/locally/) (if you installed CUDA, select the CUDA version, otherwise select CPU)
