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

        self._relay = ("4x" in string.lower())

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
    
    def to_string(self):
        return self._distance

    def find_stroke(self, string):
        if ("butterfly" in string.lower()) or ("fjäril" in string.lower()):
            return Stroke_enum.FLY

        elif ("backstroke" in string.lower()) or ("ryggsim" in string.lower()):
            return Stroke_enum.BACK
        
        elif ("breaststroke" in string.lower()) or ("bröstsim" in string.lower()):
            return Stroke_enum.BREAST
        
        elif ("freestyle" in string.lower()) or ("frisim" in string.lower()):
            return Stroke_enum.FREE
        
        elif "medley" in string.lower():
            return Stroke_enum.MEDLEY
        
        else:
            return None
        
    def find_distance(self, string, stroke, relay):
        match stroke:
            case Stroke_enum.FLY:

                if "50" in string:
                    return Event_enums._50_BUTTERFLY
                
                if "100" in string:
                    return Event_enums._100_BUTTERFLY
                
                if "200" in string:
                    return Event_enums._200_BUTTERFLY
                
            case Stroke_enum.BACK:
                
                if "50" in string:
                    return Event_enums._50_BACKSTROKE
                
                if "100" in string:
                    return Event_enums._100_BACKSTROKE
                
                if "200" in string:
                    return Event_enums._200_BACKSTROKE
                
            case Stroke_enum.BREAST:
                
                if "50" in string:
                    return Event_enums._50_BREASTSTROKE
                
                if "100" in string:
                    return Event_enums._100_BREASTSTROKE
                
                if "200" in string:
                    return Event_enums._200_BREASTSTROKE
                
            case Stroke_enum.FREE:
                if "50" in string:
                    if "1500" in string:
                        return Event_enums._1500_FREESTYLE
                    
                    return Event_enums._50_FREESTYLE
                
                if "100" in string:
                    return Event_enums._100_FREESTYLE
                
                if "200" in string:
                    return Event_enums._200_FREESTYLE
                
                if "400" in string:
                    return Event_enums._400_FREESTYLE
                
                if "800" in string:
                    return Event_enums._800_FREESTYLE
                
            case Stroke_enum.MEDLEY:
                if "100" in string:
                    return Event_enums._100_INDIVIDUAL_MEDLEY

                if "200" in string:
                    return Event_enums._200_INDIVIDUAL_MEDLEY

                if "400" in string:
                    return Event_enums._400_INDIVIDUAL_MEDLEY

            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Distance not found")
                return None
    
