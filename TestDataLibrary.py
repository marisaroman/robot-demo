from random import *


def generate_test_messages(message_count):
    message_count = int(message_count)
    # Each test message needs a pid and an eid
    # For the purposes of these tests, the pid and eid values can be any integer values, as
    # long as pid values are distinct in the set of messages generated, and eid values
    # are distinct as well.

    # Generate a random number between 1000 and 5000 for the pid_start value
    pid_start = randint(1000, 5000)

    # Generate a random number between 100 and 500 for the eid_start value
    eid_start = randint(100, 500)

    # Generate a list of pid values starting with pid_start,
    # using the supplied message_count as the list length
    pids = [x for x in range(pid_start, pid_start + message_count)]

    # Generate a list of eid values starting with eid_start,
    # using the supplied message_count as the list length
    eids = [x for x in range(eid_start, eid_start + message_count)]

    # Return a list of test messages with length equal to the supplied message_count
    return [{'pid': str(pids[x]), 'eid': str(eids[x])} for x in range(message_count)]
