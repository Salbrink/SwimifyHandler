class Stroke_enum:
    FLY = 0
    BACK = 1
    BREAST = 2
    FREE = 3
    IM = 4
    MEDLEY = 5 

class Event_enums:
    _50_BUTTERFLY  = "50m fjäril"
    _100_BUTTERFLY = "100m fjäril"
    _200_BUTTERFLY = "200m fjäril"

    _50_BACKSTROKE  = "50m ryggsim"
    _100_BACKSTROKE = "100m ryggsim"
    _200_BACKSTROKE = "200m ryggsim"

    _50_BREASTSTROKE  = "50m bröstsim"
    _100_BREASTSTROKE = "100m bröstsim"
    _200_BREASTSTROKE = "200m bröstsim"

    _50_FREESTYLE  = "50m frisim"
    _100_FREESTYLE = "100m frisim"
    _200_FREESTYLE = "200m frisim"
    _400_FREESTYLE = "400m frisim"
    _800_FREESTYLE = "800m frisim"
    _1500_FREESTYLE = "1500m frisim"

    _100_INDIVIDUAL_MEDLEY = "100m medley"
    _200_INDIVIDUAL_MEDLEY = "200m medley"
    _400_INDIVIDUAL_MEDLEY = "400m medley"

    _4x50_MEDLEY = "4X50m medley"
    _4x100_MEDLEY = "4x100m medley"

    _4x50_FREESTYLE = "4x50m frisim"
    _4x100_FREESTYLE = "4x100m frisim"
    _4x200_FREESTYLE = "4x200m frisim"

    
class Event:
    def __init__(self, string):

        self._relay = string.lower().contains("4x")

        self._stroke = self.find_stroke(string)
            
        self._distance = self.find_distance(string, self._stroke, self._relay)
        
    @property
    def distance(self):
        return self._distance
    
    @property
    def stroke(self):
        return self._stroke
    
    @property
    def relay(self):
        return self._relay
    

    def find_stroke(string):
        if string.lower().contains("butterfly") or string.lower().contains("fjäril"):
            print("Butterfly found")
            return Stroke_enum.FLY

        elif string.lower().contains("backstroke") or string.lower().contains("ryggsim"):
            print("Backstroke found")
            return Stroke_enum.BACK
        
        elif string.lower().contains("breaststroke") or string.lower().contains("bröstsim"):
            print("Breaststroke found")
            return Stroke_enum.BREAST
        
        elif string.lower().contains("freestyle") or string.lower().contains("frisim"):
            print("Freestyle found") 
            return Stroke_enum.FREE
        
        elif string.lower().contains("medley"):
            print("Medley found")
            return Stroke_enum.MEDLEY
        
        else:
            print("Stroke not identified")
            return None
        
    def find_distance(string, stroke, relay):
        match stroke:
            case Stroke_enum.FLY:
                return None
            case Stroke_enum.BACK:
                return None
            case Stroke_enum.BREAST:
                return None
            case Stroke_enum.FREE:
                return None
            case Stroke_enum.MEDLEY:
                return None

            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Distance not found")
                return None
    
