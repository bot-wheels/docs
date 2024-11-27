# Guide how to train Rocket League Bot

To start training the bot you have to run A2C.py file. Every reward is defined in rewards.py file. The weights and parameters of every single reward is defined in reward-config.json file. To run the visual simulation you have to enter RocketSimVis folder in your project and open RUN file. 

## Early Stages of Training (Bronze - Silver)

### Defining Early Stages

The early stages of training refer to the period when your bot is not yet trying to score goals. At this stage, bots typically cannot push or shoot the ball into the goal. The primary focus should be on:

1. **Learning to touch the ball (TouchBallReward)**
2. **Ensuring the bot doesn't forget how to jump (FlipReward)**

### Why Do Bots Forget How to Jump

Controlling the car in the air is challenging and less forgiving compared to ground driving. A fresh bot tasked with reaching the ball often learns quickly to avoid jumping altogether. Unfortunately, this makes it harder for the bot to rediscover jumping later.

### Rewards for Early Stages

Here are some effective rewards to help a fresh bot learn to hit the ball quickly:

```python
REWARD_FUNCTIONS = {
    "TouchBallReward": TouchBallReward, # Giant reward for actually hitting the ball
    "FlipReward": FlipReward, # Jumping reward
    "BallPossessionReward": BallPossessionReward, # Possesing the ball
    "DistanceToBallReward": DistanceToBallReward, # Move towards the ball
}
```

> **Note:** Avoid rewards for scoring or moving the ball toward the goal at this stage. These add noise and slow down learning.

#### Weights

Try to increase the weights of touching the Ball first! After a few dozen million steps, your bot should frequently hit the ball.

&#x20;&#x20;
---

## Learning to Score

Once your bot reliably hits the ball, introduce rewards for moving the ball toward the goal and scoring. Decrease the **TouchBallReward** significantly so it is no longer the bot's primary objective.

### Recommended Rewards

- **VelocityBallToGoalReward**: Use this for continuous encouragement to move the ball toward the goal.&#x20;

#### Warning: Avoid Massive Goal Rewards

Avoid assigning excessive weight to goal rewards, such as:

```python
 "name": "GoalReward",
        "params": {
            "weight": 10
          },
          "weight": 100.0 
```

#### Why

Massive goal rewards drown out other rewards, reducing exploration and slowing learning. Instead, use a reasonable weight (e.g., 10 or 20) for goal rewards. Note that a bot can be trained to high levels without goal rewards at all.

---

## Middle Stages (Gold - Plat)

### Defining Middle Stages

Once your bot can push the ball into the net, it enters the middle stages. This stage involves more complexity and refinement.

### Objectives

1. **Basic shots**
2. **Basic saves**
3. **Simple jump-touches and aerials**
4. **Effective 50-50s**
5. **Boost collection and management**
6. **Giving space to teammates (if not 1v1)**

### Improved Ball-Touch Reward

The default touch reward from TouchBallReward becomes less effective as bots improve. To address this, scale the reward based on the strength of the touch. For example:

1. Use `ball_touched` (a property of players) to detect ball interactions.
2. Calculate the ball’s velocity change between steps.

### Encouraging Air Touches

Bots often fear the air, requiring encouragement to hit the ball high up.  Combine time spent in the air with the ball’s height:

```python
MAX_TIME_IN_AIR = 1.75  # Maximum aerial time
air_time_frac = min(player.air_time, MAX_TIME_IN_AIR) / MAX_TIME_IN_AIR
height_frac = ball.position[2] / CommonValues.CEILING_Z
reward = min(air_time_frac, height_frac)
```

### Boost Management

#### Encourage Boost Pickup

Use **EventReward’s boost\_pickup** for rewarding boost collection. Increase the reward for small pads to ensure bots don’t ignore them.

#### Encourage Boost Conservation

Reward bots based on boost levels, emphasizing lower amounts:

```python
reward = sqrt(player.boost_amount)
```

#### Tips

- Increase the reward if the bot wastes boost.
- Decrease it if the bot hoards boost unnecessarily.

---

## Developing Outplays

Outplays are critical for advancing to later stages. This involves mechanics like:

- **Dribbling and flicking** (common among bots)
- **Cuts and passes**
- **Air dribbles and flip resets**

### Custom Rewards

Introduce specific rewards for mechanics you want your bot to learn. For example, if teaching flip resets, reward proper alignment, car positioning, and ball contact during a reset.

---

## Conclusion

By following these steps, you can guide your bot from basic ball touches to advanced mechanics and competitive gameplay. Each stage builds on the previous one, ensuring steady and meaningful progress. Use the provided rewards and techniques as a foundation, and feel free to experiment to achieve the behavior you desire.

