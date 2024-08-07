
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

events_english = []

class event:

    def __init__(self, event_name, language='Swedish') -> None:
        if language=='Swedish':

            if ('damer' in event_name) or ('flickor' in event_name):
                self._gender = 'damer'
            else: 
                self.gender = 'herrar'
            for event in events_swedish:
                if event in event_name:
                    self._event_name = event
        else:  
            self._event_name = None
            self._gender = None
    
    def __eq__(self, other) -> bool:
        return self._event_name in other.event_name
    
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

    
