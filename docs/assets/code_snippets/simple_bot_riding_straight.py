import rlgym
from rlgym.utils.terminal_conditions.common_conditions import TimeoutCondition

default_tick_skip = 8  # value dictated by the tutorial
physics_ticks_per_second = 120  # value dictated by the tutorial

ep_len_seconds = 20  # number of seconds before the game resets, can be modified

max_steps = int(round(ep_len_seconds * physics_ticks_per_second / default_tick_skip))
condition1 = TimeoutCondition(max_steps)

throttle = 1
steer = 0
yaw = 0
pitch = 0
roll = 0
jump = 0
boost = 0
handbrake = 0

env = rlgym.make(
    spawn_opponents=False,
    game_speed=1,
    terminal_conditions=[],
)

while True:
    obs = env.reset()
    done = False

    while not done:
        # Here we sample a random action. If you have an agent, you would get an action from it here.
        # action = env.action_space.sample()
        action = [throttle, steer, yaw, pitch, roll, jump, boost, handbrake]  # throttle, steer, yaw, pitch, roll, jump, boost, handbrake

        next_obs, reward, done, gameinfo = env.step(action)
        obs = next_obs
