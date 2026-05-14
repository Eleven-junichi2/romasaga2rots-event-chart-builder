from dataclasses import dataclass


@dataclass
class Event:
    id: str
    name: str


class EventChart:
    def __init__(self):
        self.events = []


def create_event_chart() -> list[Event]:
    return list()
