#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event_index = random.randrange(len(events))
        yield events.pop(event_index)


print("=== Game Data Stream Processor ===")

event_stream = gen_event()
for event_index in range(1000):
    event = next(event_stream)
    print(f"Event {event_index}: Player {event[0]} did action {event[1]}")

event_stream = gen_event()
event_list = []
for event_index in range(10):
    event_list.append(next(event_stream))

print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
