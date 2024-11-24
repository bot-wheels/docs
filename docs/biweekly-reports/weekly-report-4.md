# Biweekly Report for the Bot Project

**Subject**: Milestone I - Summary of Current Work, Further Implementation of Algorithms and Visualizations, Project Unification

**Project Title**: BotWheels

**Report Number**: 4

**Date**: November 24, 2024

**Week Range**: Weeks 7-8

## 1. Progress Overview

The team is now almost entirely focused on training the models to achieve the project's defined goals. Available hardware resources were shared on the forum, and based on this information, specific team members were assigned to dedicate 100% of their efforts to training both models. Out of the initially planned algorithms (PPO, DQN, and A2C/A3C), only PPO and A2C remain, as implementation challenges led to the exclusion of DQN.

Low engagement from most team members persists, likely due to overlapping deadlines for engineering theses and other projects. If possible, an extension of the project deadline would be strongly preferred. Although it is likely that the project will be delivered as a whole, achieving the primary goal—a win rate of over 50% in 20 matches against Psyonix Rookie bots—might be challenging. An additional few weeks would significantly increase the likelihood of reaching this objective. Nonetheless, the team will strive to meet the target within the current timeline, but this situation is being communicated at this stage.

## 2. Team Member Contributions, Marks, and Linked Issues

| **Team Member**          | **Mark** | **Summary of Contributions**                                                                                                                                                                                  | **Linked Issues**                                                                                                                                                                                                        |
|--------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Jakub Cisoń**         | 4.5      | Project leadership, meetings, management, and code reviews. Improved task allocation compared to the previous phase.                                                                                         |                                                                                                                                                                                                                          |
| **Kacper Drozdowski**   | 4        | Implementation of the reward function module. Currently training the A2C model.                                                                                                                              | - [Implement Additional Reward Functions](https://github.com/bot-wheels/bot-wheels-core/issues/78) - [A2C Initial Training & Testing via Local](https://github.com/bot-wheels/bot-wheels-core/issues/95)                 |
| **Mateusz Gościniecki** | 4        | Completed the implementation of the algorithm using Rocket Learn. Conducted research and is now working on establishing communication between shared hardware resources.                                      | - [Remote Training Setup for Rocket League Bot](https://github.com/bot-wheels/docs/issues/55)                                                                                                                            |
| **Anna Ivanytska**      | 3        | Very poor communication. Over the past two weeks, it has been almost impossible to contact her. Currently working on improving the event logger.                                                             | - [Expansion of Event Logger](https://github.com/bot-wheels/bot-wheels-core/issues/74)                                                                                                                                   |
| **Igor Malkovskiy**     | 4        | Introduced a configurable training parameter file instead of hardcoding values. Currently integrating the reward module with the PPO algorithm and training the model.                                       | - [Transition Training Parameterization from In-Code to Config File](https://github.com/bot-wheels/bot-wheels-core/issues/62) - [PPO Model Training and Testing](https://github.com/bot-wheels/bot-wheels-core/issues/90) |
| **Dawid Mielewczyk**    | 4.5      | Code reviews, technical support, and management assistance. Implemented the CLI and improved project structure. Had slightly limited availability due to a delegation, which was communicated in advance.       | - [Develop CLI for Training and Gameplay Modes](https://github.com/bot-wheels/bot-wheels-core/issues/73)                                                                                                                 |
| **Camille Nadir**       | 3.5      | Relatively poor communication. Worked on implementing diagnostic metrics after gameplay. Currently training the PPO model.                                                                                   | - [PPO Model Training and Testing](https://github.com/bot-wheels/bot-wheels-core/issues/90) - [Diagnostic Matches for Bot Performance Evaluation](https://github.com/bot-wheels/bot-wheels-core/issues/65)                |
| **Michał Pryba**        | 5        | Provided significant technical support, maintained high communication standards, and proactively identified project needs. Currently without a specific project task due to heavy involvement in earlier phases. | - [Technical Project Support](https://github.com/bot-wheels/bot-wheels-core/issues/94)                                                                                                                                   |
| **Wojciech Szamocki**   | 4.5      | Added a heatmap to visualization. Currently working on enhancing model management and ensuring training continuity.                                                                                          | - [Enhance Model Management and Training Continuity](https://github.com/bot-wheels/bot-wheels-core/issues/92) - [Heatmap of Bot and Opponent Activity](https://github.com/bot-wheels/bot-wheels-core/issues/75)           |
| **Konrad Siemiątkowski**| 4        | Refined data collection for the A2C algorithm and integrated game event metrics. Currently training the A2C model.                                                                                           | - [Initial A2C Model Training and Testing (via Remote Connection)](https://github.com/bot-wheels/bot-wheels-core/issues/91)                                                                                              |
| **Michał Zarzycki**     | 4.5      | Integrated PPO into the project, introduced necessary changes and fixes to his code, and provided training resources.                                                                                         | - [Task: Fix Issues in CustomObsBuilder Class](https://github.com/bot-wheels/bot-wheels-core/issues/64) - [Implement PPO Training Against Human Players](https://github.com/bot-wheels/bot-wheels-core/issues/49)        |

## 3. Challenges and Problems Encountered

Communication and motivational issues persist. A lack of information flow often causes bottlenecks and delays in other tasks, though not universally, as this issue applies to specific cases. These challenges were already highlighted in the previous report.

Training remains resource-intensive, and at times, the team struggles to maintain the continuity of training loops due to limited resources. To address this, a solution for saving checkpoints is currently being developed, which will allow training to resume in smaller segments. Additionally, it may be necessary to improve and expand reward functions to enhance model performance

## 4. Plans for the Next Period (Weeks 9-10)

In the upcoming weeks, the team will focus on delivering the project as a complete and functional solution. Efforts will be directed towards achieving the primary goal of a win rate of over 50% in 20 matches against Psyonix Rookie bots, ensuring the models are trained and tested to meet this target.

Additionally, the project will be summarized, highlighting the approaches used, the results achieved, and the challenges encountered. The entire codebase will be documented in detail, including explanations of the structure, key functionalities, and usage instructions, to ensure it is clear, maintainable, and ready for presentation.

If time allows, further refinements to reward functions and additional training adjustments will be considered to improve model performance and better align outcomes with project goals. The team will aim to balance these priorities to deliver a polished and well-prepared final product.

## 5. Summary

The team is making steady progress towards completing the project, with the main focus now on model training to meet the defined goals, particularly achieving a win rate of over 50% in matches against Psyonix Rookie bots. While challenges with communication and resource constraints have slowed progress, solutions are being implemented, including the development of checkpoint saving to manage training more efficiently. Despite these difficulties, the team remains committed to delivering the project in its complete form, with a well-documented codebase and a comprehensive project summary. The next period will focus on finalizing the training, improving model performance, and ensuring the project is ready for delivery.