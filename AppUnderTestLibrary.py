from AppUnderTest import AppUnderTest
from operator import itemgetter
import time
import json


app = AppUnderTest()


def post_messages_to_app_under_test(messages):
    app.post_messages(messages)


def retrieve_batch_messages_from_app_under_test():
    # Poll the endpoint until a batch message is returned, or 10 seconds elapses,
    # whichever comes first
    batch_messages = app.retrieve_batch_messages()
    tries = 1

    while len(batch_messages) < 1 and tries <= 10:
        time.sleep(1)
        batch_messages = app.retrieve_batch_messages()
        tries = tries + 1

    return batch_messages


def get_individual_messages_in_batch(batch_message):
    batch_message = json.loads(batch_message)
    return batch_message['messages']


def the_count_of_individual_messages_in_batch_should_be(batch_message, expected_count):
    assert len(get_individual_messages_in_batch(batch_message)) == int(expected_count)


def message_lists_should_be_equal(actual, expected):
    # Sort both lists by pid values
    actual, expected = [sorted(l, key=itemgetter('pid')) for l in (actual, expected)]

    # Compare each 'pid': 123, 'eid': 234 pair from each list and assert
    # that there are no differences in pid or eid values
    pairs = zip(actual, expected)
    assert any(x != y for x, y in pairs) == False
