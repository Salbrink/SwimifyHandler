class Swimmer:
    def __init__(self, first_name, last_name, club):
        self._first_name = first_name
        self._last_name = last_name
        self._club = club
        self._events = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def club(self):
        return self._club
    
    @property
    def events(self):
        return self._events

    @club.setter
    def club(self, value):
        self._club = value

    def to_string(self):
        return self._first_name + " " + self._last_name + " " + self._club
    
    def add_event(self, event):
        self._events.append(event)

    def print_events(self):
        for e in self._events:
            print("\t" + e.to_string())
