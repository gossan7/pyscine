#!/usr/bin/env python3
import random
import time


def game_event_stream(num_events):
    print(f"Processing {num_events} game events...")
    print()

    players = ['alice', 'bob', 'charlie']
    event_types = ['killed monster', 'found treasure', 'leveled up']

    for i in range(num_events):
        player = random.choice(players)
        event = random.choice(event_types)
        level = random.randint(1, 15)
        event_str = f"Event {i + 1}: Player {player} (level {level}) {event}"
        event_data = {'player': player, 'level': level, 'event': event}
        yield event_str, event_data


def display_analitics(high_level_count: int,
                      event_type_count: dict,
                      n_events: int,
                      duration: float):
    print("=== Stream Analytics ===")
    print(f"Total events processed: {n_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {event_type_count['found treasure']}")
    print(f"Level-up events: {event_type_count['leveled up']}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")
    print()


def fibonacci_stream(n_elem):
    a, b = 0, 1
    for _ in range(n_elem):
        yield a
        a, b = b, a + b


def prime_stream(n_elem):
    def check_prime(n):
        for i in range(1, n):
            if n / i == n // i:
                return True
            if i * i > n:
                return False
    n = 2
    count = 0
    while count < n_elem:
        if check_prime(n):
            yield n
            count += 1
        n += 1


def main():
    print("=== Game Data Stream Processor ===")
    print()

    high_level_count = 0
    event_type_count = {'killed monster': 0, 'found treasure': 0, 'leveled up': 0}
    start_time = time.time()
    n_events = 1000
    events_generator = game_event_stream(n_events)
    for event_str, event_data in events_generator:
        print(event_str)
        if event_data['level'] >= 10:
            high_level_count += 1
        event_type_count[event_data['event']] += 1
    print()

    end_time = time.time()

    display_analitics(high_level_count, event_type_count,
                      n_events, end_time - start_time)

    print("=== Generator Demonstration ===")
    n_fib = 10
    fibonacci_generator = fibonacci_stream(n_fib)
    print(f"Fibionacci sequence (first {n_fib}): ", end="")
    i = 0
    for n in fibonacci_generator:
        print(n, end="")
        i += 1
        if i != n_fib:
            print(", ", end="")
    print()

    n_prime = 10
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
    main()
