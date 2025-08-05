"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return list((number, number + 1, number + 2))
    pass


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2
    pass


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    for i in rounds:
        if number == i:
            return True
    return False
    pass


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)
    pass


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    if (hand[0] + hand[len(hand) - 1] == 2 * card_average(hand) or hand[len(hand) // 2] == card_average(hand)):
        return True
    return False
    pass


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_counter = 0
    even_counter = 0
    sum_odd = 0
    sum_even = 0
    for i in range(0, len(hand), 2):
        sum_odd += hand[i]
        odd_counter += 1
    for i in range(1, len(hand), 2):
        sum_even += hand[i]
        even_counter += 1
    avg_odd = sum_odd / odd_counter
    avg_even = sum_even / even_counter
    print(avg_odd, avg_even)
    if (avg_odd == avg_even):
        return True
    return False
    pass


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    for i in range(len(hand)):
        if i == len(hand) - 1 and hand[i] == 11:
            hand[i] = hand[i] * 2
    return hand
    pass
