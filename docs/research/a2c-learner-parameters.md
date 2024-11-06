# Parameters in A2C Learner Configuration

## 1. `a2c_batch_size`

- **New Value**: `5000`
- **Why Changed**: Smaller batches mean the model updates more often and uses less memory.
- **Effect**:
  - **Faster Learning**: The model can adjust quicker to new information.
  - **More Stable Training**: Reduces the chance of errors during updates.
- **Guidelines**:
  - **Increase `a2c_batch_size` When**:
    - You have more memory and computational power.
    - You observe that larger batches lead to more stable gradient estimates.
    - Training is too slow, and larger batches can speed it up without causing memory issues.
  - **Decrease `a2c_batch_size` When**:
    - Memory constraints prevent using larger batches.
    - Training becomes unstable with larger batch sizes.
    - You need more frequent updates to capture rapid changes in the environment.

---

## 2. `ts_per_iteration`

- **New Value**: `25000`
- **Why Changed**: Fewer timesteps per iteration allow the model to update more frequently.
- **Effect**:
  - **Quick Adaptation**: The model can respond faster to changes in the environment.
  - **Better Learning Flow**: Keeps the training process smooth and continuous.
- **Guidelines**:
  - **Increase `ts_per_iteration` When**:
    - You want the model to collect more experiences before each update, which can improve learning quality.
    - The environment is complex, and more data per iteration helps in better policy updates.
  - **Decrease `ts_per_iteration` When**:
    - You need more frequent updates to adapt quickly to changing environments.
    - Training is too slow due to the high number of timesteps per iteration.
    - You observe diminishing returns with larger timesteps per iteration.

---

## 3. `policy_lr` and `critic_lr`

- **New Values**:
  - **`policy_lr`**: `1e-3`
  - **`critic_lr`**: `1e-3`
- **Why Changed**: Higher learning rates help the model make bigger updates when needed.
- **Effect**:
  - **Faster Improvement**: The policy and value estimates improve more quickly.
  - **Effective Updates**: Prevents the model from getting stuck without making progress.
- **Guidelines**:
  - **Increase Learning Rates When**:
    - The model is learning too slowly, and updates are too small to make significant progress.
    - You have a stable training process and can handle larger updates without causing instability.
  - **Decrease Learning Rates When**:
    - The training becomes unstable, with loss values fluctuating wildly or diverging.
    - The model overshoots optimal values, leading to poor performance.
    - Gradient updates are too large, causing the learning process to fail.

---

## 4. `a2c_ent_coef`

- **New Value**: `0.01`
- **Why Changed**: Increasing entropy helps the model explore more actions.
- **Effect**:
  - **Better Exploration**: The model tries a wider variety of actions, finding better strategies.
  - **Prevents Early Stopping**: Avoids the model settling on bad solutions too soon.
- **Guidelines**:
  - **Increase `a2c_ent_coef` When**:
    - The agent is not exploring enough and is stuck in suboptimal policies.
    - You want to encourage more diversity in the actions taken by the policy.
  - **Decrease `a2c_ent_coef` When**:
    - The agent is exploring too much and not exploiting learned strategies effectively.
    - Training converges too slowly due to excessive exploration.
    - The environment requires more exploitation of known good actions rather than exploration.

---

## 5. `exp_buffer_size`

- **New Value**: `50000`
- **Why Changed**: Adjusting the experience buffer size ensures that enough experiences are stored for effective learning.
- **Effect**:
  - **Sufficient Experience Storage**: Maintains a diverse set of experiences for training, preventing overfitting to recent experiences.
  - **Improved Learning Quality**: A larger buffer provides more varied data, enhancing the model's ability to generalize.
- **Guidelines**:
  - **Increase `exp_buffer_size` When**:
    - You have ample memory and want to store more experiences for better learning.
    - The environment is highly variable, requiring a larger buffer to capture diverse experiences.
  - **Decrease `exp_buffer_size` When**:
    - Memory constraints limit the size of the buffer.
    - A smaller buffer suffices for the complexity of the environment and task.

---

## 6. `policy_layer_sizes` and `critic_layer_sizes`

- **New Values**:
  - **`policy_layer_sizes`**: `(256, 128)`
  - **`critic_layer_sizes`**: `(256, 128)`
- **Why Changed**: Adjusting the size of the neural network layers can help the model better capture complex patterns in the data.
- **Effect**:
  - **Enhanced Representation**: Larger layers can learn more detailed and nuanced strategies.
  - **Improved Generalization**: Better capacity to generalize from training data to unseen situations.
- **Guidelines**:
  - **Increase Layer Sizes When**:
    - The model is underfitting, failing to capture complex patterns in the data.
    - You have sufficient computational resources to handle larger networks.
    - The task requires modeling intricate relationships within the data.
  - **Decrease Layer Sizes When**:
    - The model is overfitting, memorizing the training data instead of generalizing.
    - Computational resources are limited, leading to long training times.
    - The task is relatively simple and does not require deep or wide networks.

---

## 7. `gae_lambda` and `gae_gamma`

- **New Values**:
  - **`gae_lambda`**: `0.95`
  - **`gae_gamma`**: `0.99`
- **Why Changed**: These parameters control the balance between bias and variance in the advantage estimation.
- **Effect**:
  - **Balanced Advantage Estimation**: Proper settings help in reducing the variance without introducing too much bias.
  - **Stable Learning**: Leads to more reliable updates by providing accurate advantage estimates.
- **Guidelines**:
  - **Increase `gae_lambda` When**:
    - You want to reduce bias in advantage estimation, potentially at the cost of increased variance.
    - The environment requires more accurate advantage calculations for effective learning.
  - **Decrease `gae_lambda` When**:
    - High variance in advantage estimates is causing instability in training.
    - A lower lambda helps in stabilizing the learning process by introducing more bias.
  - **Increase `gae_gamma` When**:
    - Long-term rewards are more important for the task.
    - The agent needs to consider future rewards more significantly.
  - **Decrease `gae_gamma` When**:
    - Short-term rewards are more critical.
    - The environment rewards immediate actions more than future ones.

---

## Summary of Key Changes

```python
learner = Learner(
    build_rocketsim_env,
    n_proc=n_proc,
    min_inference_size=min_inference_size,
    metrics_logger=metrics_logger,
    a2c_batch_size=5000,
    ts_per_iteration=25000,
    exp_buffer_size=50000,
    policy_layer_sizes=(256, 128),
    critic_layer_sizes=(256, 128),
    log_to_wandb=False,
    render=True,
    add_unix_timestamp=False,
    render_delay=0.02,
    continuous_var_range=(0.1, 1.0),
    a2c_ent_coef=0.01,
    gae_lambda=0.95,
    gae_gamma=0.99,
    policy_lr=1e-3,
    critic_lr=1e-3,
)
```
