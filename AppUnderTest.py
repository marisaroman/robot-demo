from random import *
import json


class AppUnderTest(object):
    def __init__(self):
        self.received_messages = []

    def post_messages(self, messages):
        self.received_messages = messages

    def retrieve_batch_messages(self):
        # If there are at least 10 messages, a batch message will
        # be created. Each batch message contains exactly 10 messages.
        batches = len(self.received_messages)//10  # Integer division works in this case since we want the floor
        batch_messages = []
        for x in range(batches):
            print(self.received_messages)
            batch_message = {'name': 'batch message', 'messages': self.received_messages[x*10:(x+1)*10]}
            batch_messages.append(json.dumps(batch_message))

        # In order to simulate the conditions of an actual test - that some time may need to elapse
        # before a batch message is returned by the app under test - randomly decide whether or not
        # the batch_messages will be returned.
        return_batch_messages = randint(0, 1)
        if return_batch_messages:
            return batch_messages
        else:
            return []
