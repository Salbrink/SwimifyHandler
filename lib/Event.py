events_swedish = [
    "50m fjärilsim", 
    "100m fjärilsim", 
    "200m fjärilsim", 

    "50m ryggsim", 
    "100m ryggsim", 
    "200m ryggsim", 

    "50m bröstsim", 
    "100m bröstsim", 
    "200m bröstsim",

    "50m frisim",
    "100m frisim",
    "200m frisim",
    "400m frisim",
    "800m frisim",
    "1500m frisim",

    "100m medley",
    "200m medley",
    "400m medley",

    "4x50m medley",
    "4x100m medley",

    "4x50m frisim",
    "4x100m frisim",
    "4x200m frisim",
]

events_english = [
    "50m butterfly", 
    "100m butterfly", 
    "200m butterfly", 

    "50m backstroke", 
    "100m backstroke", 
    "200m backstroke", 

    "50m breaststroke", 
    "100m breaststroke", 
    "200m breaststroke",

    "50m freestyle",
    "100m freestyle",
    "200m freestyle",
    "400m freestyle",
    "800m freestyle",
    "1500m freestyle",

    "100m medley",
    "200m medley",
    "400m medley",

    "4x50m medley",
    "4x100m medley",

    "4x50m freestyle",
    "4x100m freestyle",
    "4x200m freestyle",
]

class event:
    def __init__(self, event_name, language='Swedish', start_time=None) -> None:
        self._event_name = None # Initialize to avoid AttributeError
        event_name = event_name.lower()
        if language=='Swedish':

            if ('damer' in event_name) or ('flickor' in event_name) or ('women' in event_name) or ('woman' in event_name):
                self._gender = 'damer'
            else: 
                self._gender = 'herrar'

            for event in events_swedish:
                if event in event_name:
                    self._event_name = event
                    break

            for index, event in enumerate(events_english):
                if event in event_name:
                    self._event_name = events_swedish[index]
                    break

            if self._event_name is None:
                self._event_name = event_name
        else:  
            self._event_name = event_name
            self._gender = None

        self._entered_swimmers = []
        self._start_time = start_time
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, event):
            return False
        return self._event_name == other.event_name and self._gender == other.gender

    def __hash__(self) -> int:
        # Combine the hashes of the event_name and gender attributes
        return hash((self._event_name, self._gender))
    
    @property
    def event_name(self) -> str:
        return self._event_name
    
    @event_name.setter
    def event_name(self, event_name: str) -> None:
        self._event_name = event_name

    @property
    def gender(self) -> str:
        return self._gender
    
    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender

    @property 
    def entered_swimmers(self) -> list:
        return self._entered_swimmers
    
    @entered_swimmers.setter
    def entered_swimmers(self, swimmer_list) -> None:
        self._entered_swimmers = swimmer_list

    @property
    def start_time(self) -> str:
        return self._start_time
    
    @start_time.setter
    def start_time(self, time) -> None:
        self._start_time = time
    
    def add_swimmer(self, swimmer_object) -> None:
        self._entered_swimmers.append(swimmer_object)