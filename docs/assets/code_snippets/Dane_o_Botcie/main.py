from rlbot.agents.base_agent import SimpleControllerState
from unittest.mock import MagicMock
import time

# Mock data structure for testing the bot with just one car
class MockPhysics:
    def __init__(self):
        self.location = MagicMock(x=0, y=0, z=0)  # Start at origin
        self.velocity = MagicMock(x=0, y=0, z=0)  # No movement initially

class MockCar:
    def __init__(self):
        self.physics = MockPhysics()

class MockGameTickPacket:
    def __init__(self):
        self.game_cars = [MockCar()]  # Simulate a game with only 1 car

# Mock logger to capture logs for testing
class MockLogger:
    def __init__(self):
        self.logs = []

    def info(self, message):
        self.logs.append(message)

# MovementTestBot adapted to use mock data
# Adjust the test duration in the bot initialization if needed
class MovementTestBot:
    def __init__(self, index, team, name, logger):
        self.index = index
        self.team = team
        self.name = name
        self.logger = logger
        self.controller_state = SimpleControllerState()
        self.test_duration = 1  # Reduce test duration to match overall frame count
        self.log = []
        self.tests = [
            self.test_move_forward,
            self.test_use_boost,
            self.test_turn_left,
            self.test_turn_right,
            self.test_stop
        ]
        self.current_test_index = 0
        self.test_start_time = time.time()
        self.test_logged = False  # To ensure the log happens only once per test

    def get_output(self, packet: MockGameTickPacket) -> SimpleControllerState:
        """Called every frame with the latest game data."""
        # If all tests are done, log and stop
        if self.current_test_index >= len(self.tests):
            if not self.test_logged:
                self.logger.info("All tests completed!")
                self.logger.info("\n".join(self.log))
                self.test_logged = True
            return SimpleControllerState()  # Stop bot

        # Get the test function and run it
        test_function = self.tests[self.current_test_index]
        self.controller_state = test_function(packet)

        # Simulate the passage of time in test
        if time.time() - self.test_start_time > self.test_duration:
            # Log the result at the end of the test duration
            if not self.test_logged:
                self.log_test_result(packet)  # Log the result once per test
                self.test_logged = True  # Ensure logging happens once

            # Move to the next test
            self.logger.info(f"Completed test {self.current_test_index + 1}")
            self.current_test_index += 1
            self.test_start_time = time.time()  # Reset time for the next test
            self.test_logged = False  # Reset log flag for the next test

        return self.controller_state

    def test_move_forward(self, packet):
        """Test moving forward."""
        self.controller_state.throttle = 1.0
        # Simulate forward movement by changing position (increase x)
        packet.game_cars[self.index].physics.location.x += 100
        return self.controller_state

    def test_use_boost(self, packet):
        """Test using boost."""
        self.controller_state.boost = True
        self.controller_state.throttle = 1.0
        # Simulate fast movement due to boost (increase x and z)
        packet.game_cars[self.index].physics.location.x += 200
        packet.game_cars[self.index].physics.location.z += 50
        return self.controller_state

    def test_turn_left(self, packet):
        """Test turning left."""
        self.controller_state.steer = -1.0
        # Simulate turning left by modifying y-position
        packet.game_cars[self.index].physics.location.y -= 50
        return self.controller_state

    def test_turn_right(self, packet):
        """Test turning right."""
        self.controller_state.steer = 1.0
        # Simulate turning right by modifying y-position
        packet.game_cars[self.index].physics.location.y += 50
        return self.controller_state

    def test_stop(self, packet):
        """Test stopping the bot."""
        self.controller_state.throttle = 0.0
        self.controller_state.boost = False
        self.controller_state.steer = 0.0
        # Simulate stopping by setting velocity to 0
        packet.game_cars[self.index].physics.velocity.x = 0
        packet.game_cars[self.index].physics.velocity.y = 0
        packet.game_cars[self.index].physics.velocity.z = 0
        return self.controller_state

    def log_test_result(self, packet):
        """Logs the results of a test at the end."""
        car = packet.game_cars[self.index]  # Get bot's car data
        position = car.physics.location
        velocity = car.physics.velocity
        action_name = self.tests[self.current_test_index].__name__.replace('test_', '').replace('_', ' ').capitalize()
        log_entry = f"{action_name}: Position = ({position.x}, {position.y}, {position.z}), Velocity = ({velocity.x}, {velocity.y}, {velocity.z})"
        self.log.append(log_entry)
        self.logger.info(log_entry)

# Mock version of SimpleControllerState
class SimpleControllerState:
    def __init__(self):
        self.throttle = 0.0
        self.steer = 0.0
        self.boost = False

# Test runner function to simulate bot's behavior
def run_test():
    logger = MockLogger()  # Mocked logger to capture the output
    bot = MovementTestBot(index=0, team=0, name="TestBot", logger=logger)

    packet = MockGameTickPacket()  # Simulate a game packet with car data

    # Run the loop for a longer duration to allow all tests to complete
    total_frames = 300  # Simulate enough frames for all tests to finish
    for _ in range(total_frames):  # Increase the number of frames
        bot.get_output(packet)
        time.sleep(0.1)  # Simulate time passing for each frame (100ms per frame)

    # Output the results
    print("Test Results:")
    for log in logger.logs:
        print(log)

# Run the test
run_test()




