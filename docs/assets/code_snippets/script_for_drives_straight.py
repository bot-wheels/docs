import rlgym

# Initialize the environment
env = rlgym.make(
    spawn_opponents=False,  # Disable spawning opponents
    game_speed=1,  # Set game speed to normal
    terminal_conditions=[],  # No terminal conditions, the game will run indefinitely
)

while True:
    obs = env.reset()  # Reset the game state to start a new episode
    done = False  # Variable to check if the episode is over

    while not done:
        # Define the action for moving straight:
        # Example action (acceleration forward, no rotation):
        action = [1, 0, 0, 0, 0, 0, 0, 0]

        # Perform the action in the environment
        next_obs, reward, done, gameinfo = env.step(action)

        # Update the observation
        obs = next_obs  # Set the current observation to the new one
