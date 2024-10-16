# Unexpected problems and delays

[@Garikmal](https://github.com/Garikmal) and I ([@Oruniarz](https://github.com/Oruniarz)) were assigned issue
[#39](https://github.com/bot-wheels/bot-wheels-core/issues/39). During our work on it, we discovered that
adding a bot controlled by some AI isn't as easy as we thought and also isn't exactly supported by RLGym
package. This will prevent this issue from being completed until a decision is made on how this problem should be
addressed. </br>
There are some packages that allow for adding some already existent bots as opponents in the process of training
our own such as: </br>

- [rlgym-ppo](https://github.com/AechPro/rlgym-ppo),
- [rocket-learn](https://github.com/Rolv-Arild/rocket-learn).

The first one uses a simulator of Rocket League [RocketSim](https://github.com/ZealanL/RocketSim)
and RLGym Wrapper [rocket-league-gym-sim](https://github.com/AechPro/rocket-league-gym-sim) and would require
to move from the main game and RLGym library. The second one would require some additional setup and modifications
of the main project. It would also mean that all contributors will need to learn how to use this library.

## Some useful links found while making this research

- [RLGym-PPO-Guide](https://github.com/ZealanL/RLGym-PPO-Guide) - useful guide that could help with creating the bot
