import itertools
import random
import math
from collections import Counter

DIGITS = '0123456789'

def generate_secret():
    """
    Generates a random 4-digit secret number with unique digits.
    """
    return ''.join(random.sample(DIGITS, 4))

def bulls_and_cows(secret, guess):
    """
    Calculates the Bulls and Cows for a given secret and guess.
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows

def compute_entropy(probabilities):
    """
    Computes entropy for a given set of probabilities.
    """
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def generate_outcomes(possibilities, guess=None):
    """
    Generates (bulls, cows) outcomes for all pairs of possibilities or a specific guess.
    """
    if guess:
        return Counter(bulls_and_cows(p, guess) for p in possibilities)
    return Counter(
        bulls_and_cows(p1, p2) for p1 in possibilities for p2 in possibilities
    )

def calculate_entropy(possibilities):
    """
    Calculates the entropy of the current game state.
    """
    if not possibilities:
        return 0
    outcome_counts = generate_outcomes(possibilities)
    total = sum(outcome_counts.values())
    probabilities = (count / total for count in outcome_counts.values())
    return compute_entropy(probabilities)

def calculate_mutual_information(possibilities, guess):
    """
    Calculates the mutual information for a given guess.
    """
    if not possibilities:
        return 0
    outcomes = generate_outcomes(possibilities, guess)
    total = sum(outcomes.values())
    probabilities = (count / total for count in outcomes.values())

    pre_entropy = calculate_entropy(possibilities)
    expected_entropy = compute_entropy(probabilities)

    return max(pre_entropy - expected_entropy, 0)

def filter_possibilities(guess, bulls, cows, possibilities):
    """
    Filters the list of possible answers based on the current guess and its outcome.

    Parameters:
    - guess (str): The guessed number.
    - bulls (int): The number of bulls from the guess.
    - cows (int): The number of cows from the guess.
    - possibilities (list): List of all possible valid 4-digit numbers.

    Returns:
    - list: Updated possibilities that match the (bulls, cows) criteria for the guess.
    """
    return [
        p for p in possibilities
        if bulls_and_cows(p, guess) == (bulls, cows)
    ]

def initialize_game():
    """
    Initializes the game state.
    """
    secret = generate_secret()
    possibilities = [''.join(p) for p in itertools.permutations(DIGITS, 4)]
    return {
        "secret": secret,
        "possibilities": possibilities,
        "attempts": 0,
        "attempts_history": [],
    }
