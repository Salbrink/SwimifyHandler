from tempus import TempusEvent

FREESTYLE = ["freestyle", "frisim", "frisvømning"]
BREASTSTROKE = ["breaststroke", "bröstsim", "brystsvømning"]
BACKSTROKE = ["backstroke", "ryggsim", "rygsvømning"]
BUTTERFLY = ["butterfly", "fjäril"]
MEDLEY = ["medley"]


class TempusParser:
    def __init__(self):
        pass

    def stroke_check(self, event_name, matches):
        event_name = event_name.lower()
        return any([stroke in event_name for stroke in matches])

    def is_freestyle(self, event_name):
        return self.stroke_check(event_name, FREESTYLE)

    def is_breaststroke(self, event_name):
        return self.stroke_check(event_name, BREASTSTROKE)

    def is_backstroke(self, event_name):
        return self.stroke_check(event_name, BACKSTROKE)

    def is_butterfly(self, event_name):
        return self.stroke_check(event_name, BUTTERFLY)

    def is_medley(self, event_name):
        return self.stroke_check(event_name, MEDLEY)

    def safe_get(self, pbs, race):
        if race in pbs:
            return pbs[race]
        else:
            return None

    def parse_pbs(self, pbs, event_name):
        try:
            if "4x50m" in event_name:
                return ("200m", None, None)

            elif "4x100m" in event_name:
                return ("400m", None, None)

            elif "4x200" in event_name:
                return ("800m", None, None)

            elif "25m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "25m",
                        self.safe_get(pbs, TempusEvent.SC_25_FREESTYLE.name),
                        None,
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "25m",
                        self.safe_get(pbs, TempusEvent.SC_25_BREASTSTROKE.name),
                        None,
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "25m",
                        self.safe_get(pbs, TempusEvent.SC_25_BACKSTROKE.name),
                        None,
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "25m",
                        self.safe_get(pbs, TempusEvent.SC_25_BUTTERFLY.name),
                        None,
                    )

            elif "50m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "50m",
                        self.safe_get(pbs, TempusEvent.SC_50_FREESTYLE.name),
                        self.safe_get(pbs, TempusEvent.LC_50_FREESTYLE.name),
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "50m",
                        self.safe_get(pbs, TempusEvent.SC_50_BREASTSTROKE.name),
                        self.safe_get(pbs, TempusEvent.LC_50_BREASTSTROKE.name),
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "50m",
                        self.safe_get(pbs, TempusEvent.SC_50_BACKSTROKE.name),
                        self.safe_get(pbs, TempusEvent.LC_50_BACKSTROKE.name),
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "50m",
                        self.safe_get(pbs, TempusEvent.SC_50_BUTTERFLY.name),
                        self.safe_get(pbs, TempusEvent.LC_50_BUTTERFLY.name),
                    )

            elif "100m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "100m",
                        self.safe_get(pbs, TempusEvent.SC_100_FREESTYLE.name),
                        self.safe_get(pbs, TempusEvent.LC_100_FREESTYLE.name),
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "100m",
                        self.safe_get(pbs, TempusEvent.SC_100_BREASTSTROKE.name),
                        self.safe_get(pbs, TempusEvent.LC_100_BREASTSTROKE.name),
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "100m",
                        self.safe_get(pbs, TempusEvent.SC_100_BACKSTROKE.name),
                        self.safe_get(pbs, TempusEvent.LC_100_BACKSTROKE.name),
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "100m",
                        self.safe_get(pbs, TempusEvent.SC_100_BUTTERFLY.name),
                        self.safe_get(pbs, TempusEvent.LC_100_BUTTERFLY.name),
                    )
                elif self.is_medley(event_name):
                    return (
                        "100m",
                        self.safe_get(pbs, TempusEvent.SC_100_INDIVIDUAL_MEDLEY.name),
                        None,
                    )

            elif "200m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "200m",
                        self.safe_get(pbs, TempusEvent.SC_200_FREESTYLE.name),
                        self.safe_get(pbs, TempusEvent.LC_200_FREESTYLE.name),
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "200m",
                        self.safe_get(pbs, TempusEvent.SC_200_BREASTSTROKE.name),
                        self.safe_get(pbs, TempusEvent.LC_200_BREASTSTROKE.name),
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "200m",
                        self.safe_get(pbs, TempusEvent.SC_200_BACKSTROKE.name),
                        self.safe_get(pbs, TempusEvent.LC_200_BACKSTROKE.name),
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "200m",
                        self.safe_get(pbs, TempusEvent.SC_200_BUTTERFLY.name),
                        self.safe_get(pbs, TempusEvent.LC_200_BUTTERFLY.name),
                    )
                elif self.is_medley(event_name):
                    return (
                        "200m",
                        self.safe_get(pbs, TempusEvent.SC_200_INDIVIDUAL_MEDLEY.name),
                        self.safe_get(pbs, TempusEvent.LC_200_INDIVIDUAL_MEDLEY.name),
                    )

            elif "400m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "400m",
                        self.safe_get(pbs, TempusEvent.SC_400_FREESTYLE.name),
                        self.safe_get(pbs, TempusEvent.LC_400_FREESTYLE.name),
                    )
                elif self.is_medley(event_name):
                    return (
                        "400m",
                        self.safe_get(pbs, TempusEvent.SC_400_INDIVIDUAL_MEDLEY.name),
                        self.safe_get(pbs, TempusEvent.LC_400_INDIVIDUAL_MEDLEY.name),
                    )

            elif "800m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "800m",
                        self.safe_get(pbs, TempusEvent.SC_800_FREESTYLE.name),
                        self.safe_get(pbs, TempusEvent.LC_800_FREESTYLE.name),
                    )

            elif "1500m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "1500m",
                        self.safe_get(pbs, TempusEvent.SC_1500_FREESTYLE.name),
                        self.safe_get(pbs, TempusEvent.LC_1500_FREESTYLE.name),
                    )

        except KeyError:
            print("One or more personal best not found!")

        return "400m", None, None
