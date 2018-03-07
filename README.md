# robot-demo
Robot Framework demo in Python

## How to Run the Tests
1. Clone the repo
2. In a terminal window, navigate into the robot-demo folder
3. Execute the following at the prompt: `robot batch_message_test.robot`

## Components
[AppUnderTest](../master/AppUnderTest.py): Demo app that mocks message publishing and receiving  
[robot_batch_message_test.robot](../master/robot_batch_message_test.robot): Robot test case file  
[TestDataLibrary](../master/TestDataLibrary.py): Utilities for test data generation  
[AppUnderTestLibrary](../master/AppUnderTestLibrary.py): Test fixture that enables Robot test cases to interact with the app under test

