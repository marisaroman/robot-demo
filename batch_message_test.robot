*** Settings ***
Documentation     Example Batch Message test cases using the Given/When/Then syntax.
...
...               Messages should be batched in sets of 10.
...
Library           AppUnderTestLibrary.py
Library           TestDataLibrary.py
Library           Collections

*** Test Cases ***
Batching
    Given "10" individual messages posted to the topic
    When the batch messages are retrieved
    Then "1" batch message should be returned
    And the batch message should contain "10" individual messages
    And the messages should match those posted to the topic

*** Keywords ***
"${message_count}" individual messages posted to the topic
    ${messages} =      Generate test messages   ${message_count}
    Set Test Variable   ${EXPECTED_MESSAGES}    ${messages}  # From Robot BuiltIn library
    Set Test Variable   ${EXPECTED_MESSAGE_COUNT}   ${message_count}
    Post messages to app under test     ${EXPECTED_MESSAGES}

The batch messages are retrieved
    ${messages} =      Retrieve batch messages from app under test
    Set Test Variable   ${ACTUAL_BATCH_MESSAGES}  ${messages}

"${expected_batch_message_count}" batch messages should be returned
    Length should be    ${ACTUAL_BATCH_MESSAGES}    ${expected_batch_message_count}  # From Robot BuiltIn library

# Shortcut to handle single message case
"1" batch message should be returned
    "1" batch messages should be returned

The batch message should contain "${expected_message_count}" individual messages
    ${first_batch_message} =    Get From List   ${ACTUAL_BATCH_MESSAGES}    0  # From Robot Collections Library
    Set Test Variable   ${ACTUAL_BATCH_MESSAGE}     ${first_batch_message}
    the count of individual messages in batch should be     ${first_batch_message}  ${EXPECTED_MESSAGE_COUNT}

The messages should match those posted to the topic
    ${actual_messages} =    Get individual messages in batch    ${ACTUAL_BATCH_MESSAGE}
    Message lists should be equal   ${actual_messages}  ${EXPECTED_MESSAGES}
