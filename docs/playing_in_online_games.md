# Use of Bots in Online Gaming (Rocket League)

## RLBot Framework: Online Play Restrictions

According to the official documentation, **RLBot** cannot be used in online Rocket League matches. The framework works by disabling online play when activated through a special setting. Attempts to circumvent this restriction may result in a ban, as the developers (Psyonix) actively discourage using bots in ways that might be perceived as malicious (e.g., farming, leveling accounts). This restriction makes it impossible to use RLBot for online matches with random players, as it conflicts with Psyonix's terms of service. Information found in the [RLBot FAQ](https://rlbot.org/faq/#:~:text=The%20RLBot%20framework%20cannot%20be,setting%20which%20disables%20online%20play).

### Impact on Our Project

Given these restrictions, we cannot test our bots online against real players. Instead, we will adapt our approach by running matches locally, either:

- **Against team members** participating in the project
- **Against members of the RLBot community** or friends who can participate in LAN or VLAN settings

This setup will allow us to fulfill the project goal of competing against silver-level players while adhering to the restrictions placed by Psyonix. Testing in a controlled, local environment ensures compliance and protects the integrity of the project.

## Alternatives: LAN/VLAN Matches

While **RLBot** cannot be used for online play, it is possible to set up local matches using a LAN or VLAN connection, allowing us to play with others, but only within the same network. This ensures that we still have access to human opponents, even though cross-platform play is not supported in these setups.

## Conclusion

Due to the limitations of the RLBot framework and the anti-cheat policies of Rocket League, we will conduct our bot matches locally. We plan to involve project members, community players, or friends to provide the necessary competition. This approach ensures compliance with all regulations while still allowing us to achieve the core goals of our project.
