# Movement Testing Script

Code implements a mock testing framework for a bot in the context of a Rocket League-style simulation. It tests various bot actions such as moving forward, using boost, turning, and stopping. Here is an overview of the key components:

Key Imports

- SimpleControllerState: Imported from rlbot.agents.base_agent. This class represents the controller's state (e.g., throttle, steer, boost).
- MagicMock: From unittest.mock. It’s used to mock the game's data structures, enabling isolated unit testing without actual game data.
- time: Used for handling time intervals and simulating the passage of time in tests.

Mock Classes

- MockPhysics: Mocks the physics state of a car. It has location and velocity, both mocked with MagicMock. The position starts at the origin (0, 0, 0), and the velocity is initially zero.
- MockCar: Represents a car in the game, using MockPhysics to simulate its physical state.
= MockGameTickPacket: Simulates the data structure that provides information about the game state. It contains a list of game cars (game_cars), in this case, only one MockCar.
- MockLogger: A mocked logger that captures logs for testing. It stores logs in a list so they can be checked after tests.

MovementTestBot Class
This class simulates a bot that performs a series of tests on its movement capabilities.

Attributes:

- index, team, name: Basic information about the bot.
- logger: An instance of MockLogger, used to log information during the tests.
- controller_state: An instance of SimpleControllerState that controls the bot's movement commands (throttle, steer, boost).
- test_duration: Duration of each individual test, set to 1 second.
- log: A list to store test results.
- tests: A list of movement test methods (test_move_forward, test_use_boost, etc.).
- current_test_index: Tracks which test is currently running.
- test_start_time and test_logged: Variables to handle the timing and logging of tests.

Methods:

- get_output(packet): Called every frame to update the bot's behavior. It runs the current test, checks if the test duration has passed, logs the results, and moves to the next test.
- test_move_forward(packet): Simulates moving forward by increasing the car's x-coordinate.
- test_use_boost(packet): Simulates using boost, increasing both the x- and z-coordinates.
- test_turn_left(packet): Simulates turning left by decreasing the y-coordinate.
- test_turn_right(packet): Simulates turning right by increasing the y-coordinate.
- test_stop(packet): Stops the bot by setting throttle and boost to 0, and velocity to 0.
- log_test_result(packet): Logs the results of the current test, including the car's position and velocity.

SimpleControllerState Class
This mock version of the SimpleControllerState mimics the behavior of the controller, with attributes for throttle, steer, and boost. It is manipulated by the bot during tests.

run_test() Function
This function simulates a test environment:

1. Creates a MockLogger to capture logs.
2. Instantiates MovementTestBot with test parameters.
3. Simulates game frames by calling get_output(packet) 300 times (with a 100ms delay per frame) to allow all tests to run.
4. Prints the logged test results after the test loop completes.

Summary of Bot Tests
Test 1: Move Forward — The bot moves forward by increasing its x-coordinate.
Test 2: Use Boost — The bot moves faster using boost, increasing both x and z.
Test 3: Turn Left — The bot steers left, decreasing its y-coordinate.
Test 4: Turn Right — The bot steers right, increasing its y-coordinate.
Test 5: Stop — The bot stops by setting velocity to zero and turning off throttle and boost.

The main objective of this code is to provide a unit test framework for the bot’s movement using mocked data structures for game physics and a simulated environment.
