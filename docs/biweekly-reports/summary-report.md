# Subject: Project Summary

**Project Title**: BotWheels

**Report Number**: 6

**Date**: January 8, 2025

## 1. Progress Overview

### Project Objectives

The goal of this project is to develop a Rocket League bot that competes at the skill level of an average player. The bot primarily uses the Proximal Policy Optimization (PPO) algorithm for learning, with the possibility of transitioning to alternative algorithms.

The main objectives are:

- **Implementation of Reinforcement Learning Algorithm**  
  PPO, DQN, and A3C algorithm implementations are underway, with a focus on PPO for training.

- **Achieve a win rate of over 50% in 20 matches**  
  The bot is being tested against both local silver-level players and Psyonix bots, with the potential to compete against Allstar-level bots if performance allows.

- **Optimize the bot's performance**  
  The bot is being optimized to run at 30 FPS on a system with an Intel i9-14900HX CPU and RTX 4080 GPU.

- **Develop visualizations**  
  Visualizations of the bot's states and actions are being developed to improve decision-making and performance analysis.

The approaches based on A2C and PPO algorithms were implemented, but the lack of a test environment prevented full testing. As a result, it is not possible to conclude whether the bots would have achieved the target of 50% win rate. On the positive side, the bots run stably at over 30 FPS, which meets the objective. Visualizations were delivered as planned.

---

## 2. Team Member Contributions, Previous Grades, and Proposed Final Grade

| **Team Member**          | **Previous Grades**                                         | **Average from Previous Periods** | **Overall Grade** | **Summary of Contributions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Proposed Final Grade** |
|--------------------------|-------------------------------------------------------------|-----------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| **Jakub Cisoń**          | 4.5, 4.5, 4, 4.5, 4                                       | 4.3                               | 5                 | Project management, conducting weekly status meetings, task distribution, project oversight, work organization, reporting, and preparing presentations and documentation. The downside was limited involvement in coding, though the focus was on management tasks while maintaining adequate availability and delivering documents on time.                                                                                                           | 4.5                      |
| **Kacper Drozdowski**    | 3.5, 3.5, 3, 4, 4                                         | 3.6                               | 3.5               | Work on implementing the A2C algorithm, specifically creating the reward module, which played a key role in training. From early December, assigned the task of training the bot using this algorithm, but late start led to a bot with minimal functionality (moving but stuck in loops). Overall, relatively little code was written, and communication issues were noted.                                                                                        | 3.5                      |
| **Mateusz Gościniecki**  | 4, 5, 4, 4, 3                                             | 4.0                               | 4                 | Key implementations include attempting to integrate Rocket-Learn, an alternative library, but this was not successfully implemented. Assigned the task of training with PPO in early December, but delayed start led to unsatisfactory results.                                                                                              | 4                        |
| **Anna Ivanytska**       | 2, 3.5, 3.5, 3, 3                                         | 3.0                               | 3.5               | Assisted with bot's diagnostic visualizations in gameplay, including the creation of an event logger for gameplay events. Explored DQN, but late start resulted in the abandonment of its implementation. Poor communication, with multiple reminders required for task initiation. Attempted documentation creation but failed to integrate it properly into the main branch.                                                                                           | 3                        |
| **Igor Malkovskiy**      | 4.5, 4, 2, 4, 3                                           | 3.5                               | 2                 | Initially engaged well, but later reduced involvement with frequent absences from meetings and communication issues. Assigned to train the bot using PPO but failed to deliver any results, with a late start and poor follow-through.                                                                                           | 3                        |
| **Dawid Mielewczyk**     | 5, 5, 4.5, 4.5, 4                                         | 4.6                               | 5                 | Co-leader, primarily responsible for managing the code, including support, code reviews, ensuring correct coding practices, and integrating Discord bots and linters. Assigned the task of creating a simple CLI for switching between gameplay and training with different algorithms. However, due to issues with task deliveries by other team members, the task was simplified.                                                                                                   | 5                        |
| **Camille Nadir**        | 3, 3, 2, 3.5, 3                                           | 2.9                               | 2                 | Large discrepancy between declared tasks and actual code delivery. Failure to complete tasks significantly impacted project results. Informed about writing code but kept it private and refused to push it to the repository.                                                                                                                                                                                                                                    | 2                        |
| **Michał Pryba**         | 5, 5, 5, 5, 5                                             | 5.0                               | 5                 | Key contributor, with primary responsibility for A2C algorithm implementation and excellent communication. Took initiative in the development process and later shifted to support role to assist with workload reduction and provide assistance to other team members.                                                                                                                                                                                       | 5                        |
| **Wojciech Szamocki**    | 5, 5, 5, 4.5, 4.5                                         | 4.8                               | 5                 | Main developer for diagnostic visualizations, effective communication, no need for reminders. Also shifted to support role as his general engagement increased.                                                                                                                                                                                                                                                                        | 5                        |
| **Konrad Siemiątkowski** | 2, 4, 4, 4, 3.5                                           | 3.5                               | 3.5               | Worked on A2C implementation, documentation, and metrics collection. Limited contribution to the actual project, assigned task of training with A2C, but no satisfactory results due to the late start.                                                                                                                                                                                     | 3.5                      |
| **Michał Zarzycki**      | 3.5, 5, 4.5, 4.5, 3.5                                     | 4.2                               | 4.5               | Good start with involvement in setting up PPO algorithm foundations. Reduced contribution around project deadline, affecting the flow of information and project progress.                                                                                                                                                                                                                                                        | 4                        |

---

## 3. Challenges and Problems Encountered

A new version of a key library was released just a few days before the project deadline, which caused significant issues as the current setup could not run with the new version. Consequently, the project is not functioning as expected at this time.  

Overall, the project was hindered by delays in task completion by individual team members. A major contributing factor was a lack of communication regarding problems, despite repeated requests to update progress. A key mistake in management was placing too much trust in human factors.

Out of the three planned algorithm implementations, two were completed, but none of the trained models met the target objectives due to insufficient training hours. Further details on the implementation can be found in the documentation.

---

## 4. Summary

The project did not meet the planned objectives. The lack of contribution from certain team members, particularly toward the end, and the failure to deliver key metrics hampered progress. The team dynamics clearly divided into two groups: those who were committed and engaged with the project, and those who abandoned it close to the deadline. The latter group severely impacted the project's success.  
