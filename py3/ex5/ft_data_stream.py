#!/usr/bin/env python3

import random
import time
from typing import Generator


def game_event_stream(num_events: int) -> Generator[tuple, None, None]:
    """
    Generate a stream of simulated game events.

    This generator produces game events one at a time instead of storing
    them all in memory. Each event contains a player name, player level,
    and an event type.

    Args:
        num_events (int): Number of events to generate.

    Yields:
        tuple: A tuple containing:
            - event_str (str): Human-readable event description.
            - event_data (dict): Structured event data with keys
              'player', 'level', and 'event'.
    """
    print(f"Processing {num_events} game events...")
    print()

    players = ['alice', 'bob', 'charlie']
    event_types = ['killed monster', 'found treasure', 'leveled up']

    for i in range(num_events):
        player = random.choice(players)
        event = random.choice(event_types)
        level = random.randint(0, 15)

        event_str = f"Event {i + 1}: Player {player} (level {level}) {event}"
        event_data = {'player': player, 'level': level, 'event': event}

        yield event_str, event_data


def display_analitics(high_level_count: int,
                      event_type_count: dict,
                      n_events: int,
                      duration: float) -> None:
    """
    Display analytics computed from the streamed game events.

    This function summarizes statistics gathered while processing
    the event stream, including counts of specific event types and
    total processing time.

    Args:
        high_level_count (int): Number of events involving players
            with level 10 or higher.
        event_type_count (dict): Dictionary counting occurrences
            of each event type.
        n_events (int): Total number of processed events.
        duration (float): Time spent processing the event stream
            in seconds.
    """
    print("=== Stream Analytics ===")

    print(f"Total events processed: {n_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {event_type_count['found treasure']}")
    print(f"Level-up events: {event_type_count['leveled up']}")
    print()

    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")
    print()


def fibonacci_stream(n_elem) -> Generator[int, None, None]:
    """
    Generate a Fibonacci number sequence.

    This generator yields the first `n_elem` numbers of the Fibonacci
    sequence, producing values on demand.

    Args:
        n_elem (int): Number of Fibonacci values to generate.

    Yields:
        int: Next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for _ in range(n_elem):
        yield a
        a, b = b, a + b


def prime_stream(n_elem) -> Generator[int, None, None]:
    """
    Generate a sequence of prime numbers.

    This generator yields the first `n_elem` prime numbers using
    a simple primality test.

    Args:
        n_elem (int): Number of prime numbers to generate.

    Yields:
        int: Next prime number.
    """
    def check_prime(n) -> bool:
        """
        Check whether a number is prime.

        Args:
            n (int): Number to test.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        for i in range(2, n):
            if n / i == n // i:
                return False
            if i * i > n:
                return True
        return True

    n = 2
    count = 0
    while count < n_elem:
        if check_prime(n):
            yield n
            count += 1
        n += 1


def main() -> None:
    """
    Entry point of the Stream Wizard program.

    This function:
    - Processes a stream of simulated game events
    - Computes analytics in a streaming fashion
    - Demonstrates generator usage with Fibonacci and prime sequences
    """
    print("=== Game Data Stream Processor ===")
    print()

    high_level_count = 0
    event_type_count = {
        'killed monster': 0,
        'found treasure': 0,
        'leveled up': 0
    }

    start_time = time.time()
    n_events = 1000
    events_generator = game_event_stream(n_events)

    i = 0
    for event_str, event_data in events_generator:
        if i < 3:
            print(event_str)
        elif i == 3:
            print("...")
        if event_data['level'] >= 10:
            high_level_count += 1
        event_type_count[event_data['event']] += 1
        i += 1

    print()

    end_time = time.time()

    display_analitics(
        high_level_count,
        event_type_count,
        n_events,
        end_time - start_time
    )

    print("=== Generator Demonstration ===")

    n_fib = 10
    fibonacci_generator = fibonacci_stream(n_fib)

    print(f"Fibonacci sequence (first {n_fib}): ", end="")

    i = 0
    for n in fibonacci_generator:
        print(n, end="")
        i += 1
        if i != n_fib:
            print(", ", end="")

    print()

    n_prime = 5
    prime_generator = prime_stream(n_prime)

    print(f"Prime numbers (first {n_prime}): ", end="")

    i = 0
    for n in prime_generator:
        print(n, end="")
        i += 1
        if i != n_prime:
            print(", ", end="")

    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected exception occurred ({e})")
