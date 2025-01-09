# Welcome to Bot Wheels Documentation

![Bot Wheels](https://raw.githubusercontent.com/bot-wheels/docs/refs/heads/main/docs/assets/BoT.png)

## Project's purpose

The goal of the project is to create a bot for the game Rocket League, which will compete at an assumed average player level.

* The bot will use the PPO (Proximal Policy Optimization) algorithm for learning, with a possible switch to alternatively DQN or A3C.
* The main goal is to achieve >50% wins in 20 matches against Silver level players (locally or if possible in online play)/Bot Psyonix Rookie (if successful Psyonix Allstar).
* The bot will be optimized to run at 30 FPS on hardware with i9-14900HX and RTX 4080.
* Create visualization of the bot's states.

### [Example of a rocket league bot](https://www.youtube.com/watch?v=2mb97Zo-8uA "Example of a rocket league bot")

## Work plan

| Week       | Scope of Work                                                                                     |
|------------|---------------------------------------------------------------------------------------------------|
| Week 1     | - Setting up a repository on GitHub; Environment configuration (Python, TensorFlow, RLGym)         |
|            | - Analysis of Rocket League game mechanics                                                         |
| Week 2     | - Defining key tasks for the bot                                                                  |
|            | - Initial implementation of the PPO algorithm                                                     |
| Week 3     | - Implementation of basic bot functions (movement, ball interaction)                              |
|            | - Introducing simple game logs (console logs)                                                     |
| **Milestone 1**| - Progress report on project assumptions and preliminary results                              |
| Week 4     | - Implementing the PPO algorithm – agent training                                                 |
|            | - Testing different approaches (e.g. different rewards, parameters)                               |
| Week 5     | - PPO training and optimization (testing in more games)                                           |
|            | - Results analysis                                                                                |
| Week 6     | - Further PPO optimization                                                                        |
|            | - Analyzing bot efficiency in different game scenarios (e.g. 1v1 local, bots)                     |
| **Milestone 2**| - Report on PPO test results                                                                  |
|            | - Bot performance evaluation                                                                      |
| Week 7     | - Fine-tuning the bot (adjusting strategy, changing parameters in the algorithm                   |
| Week 8     | - Implementation of a system for visualizing bot states and actions, along with fine-tuning       |
| Week 9     | - Bug fixes and tests against various opponents|
|            | - Introducing logs to monitor bot actions|
| Week 10    | - Final fixes  |
|            | - Project documentation; preparation of the final report and presentation|
| **Deadline**   | - Final bot presentation and report|

## [Bot-Wheels Github](https://github.com/bot-wheels "Repository link")

* [bot-wheels-core](bot-wheels-core "https://github.com/bot-wheels/bot-wheels-core")
* [docs](docs "https://github.com/bot-wheels/docs")

## Team

* Ivanytska Anna
* Jakub Cisoń
* Kacper Drozdowski
* Konrad Siemiątkowski
* Dawid Mielewczyk
* Mateusz Gościniecki
* Max Nadir
* Michał Pryba
* Michał Zarzycki
* Igor Malkovsky
* Wojtek Szamocki

## Used tools

* Python 3.9.13 - Used programming language
* RLGym - Open-sourced Python API for Reinforcement Learning Environments
* RLBot - Create and share Rocket League bots for offline play
* Ruff - Linter
* rocket-learn/Redis - attempt to implement

## Summary of the Project

The implementation of **PPO** and **A2C** algorithms was completed. However, the absence of a functional test environment hindered the ability to verify the bot's performance against the target win rate of 50%. Despite this, the bot achieved a stable runtime of over 30 **FPS**, meeting a critical technical requirement. Visualizations were successfully delivered as planned.

A significant issue arose due to the release of a new version of a key library just days before the project deadline. This incompatibility with the existing setup resulted in the project's failure to operate as intended.

Team performance varied significantly, with delays in task completion and insufficient communication of progress from some members. These factors, coupled with over-reliance on individual accountability, contributed to the project's shortcomings. Out of the three planned algorithm implementations, two were completed, but none of the trained models met the target objectives due to insufficient training time.

The project failed to achieve its primary objectives. Limited contributions from certain team members, especially near the project's conclusion, had a severe impact. The team's dynamics revealed a division between committed contributors and those who disengaged. The lack of full engagement prevented the team from meeting the intended goals, despite partial progress in algorithm development and achieving stable bot performance.

Estimated completion of approximately 65% of the intended goal.
