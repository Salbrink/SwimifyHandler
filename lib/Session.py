from Event import event

class session:

    def __init__(self, events: list[event], name: str, schedule=None) -> None:
        self._events = events
        self._name = name
        self._schedule = schedule
    
    @property
    def events(self) -> list[event]:
        return self._events
    
    @event.setter
    def events(self, events: list[event]) -> None:
        self._events = events

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def schedule(self) -> list[str]:
        return self._schedule
    
    @schedule.setter
    def schedule(self, schedule: list[str]) -> None:
        self._schedule = schedule