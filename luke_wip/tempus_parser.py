from tempus import TempusEvent


class TempusParser:
    def __init__(self):
        pass

    def is_freestyle(self, event_name):
        return "freestyle" in event_name.lower() or "frisim" in event_name.lower()

    def is_breaststroke(self, event_name):
        return "breaststroke" in event_name.lower() or "bröstsim" in event_name.lower()

    def is_backstroke(self, event_name):
        return "backstroke" in event_name.lower() or "ryggsim" in event_name.lower()

    def is_butterfly(self, event_name):
        return "butterfly" in event_name.lower() or "fjäril" in event_name.lower()

    def is_medley(self, event_name):
        return "medley" in event_name.lower()

    def parse_pbs(self, pbs, event_name):
        try:
            if "25m" in event_name:
                if self.is_freestyle(event_name):
                    return "25m", pbs[TempusEvent.SC_25_FREESTYLE.name], None
                elif self.is_breaststroke(event_name):
                    return "25m", pbs[TempusEvent.SC_25_BREASTSTROKE.name], None
                elif self.is_backstroke(event_name):
                    return "25m", pbs[TempusEvent.SC_25_BACKSTROKE.name], None
                elif self.is_butterfly(event_name):
                    return "25m", pbs[TempusEvent.SC_25_BUTTERFLY.name], None

            elif "50m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "50m",
                        pbs[TempusEvent.SC_50_FREESTYLE.name],
                        pbs[TempusEvent.LC_50_FREESTYLE.name],
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "50m",
                        pbs[TempusEvent.SC_50_BREASTSTROKE.name],
                        pbs[TempusEvent.LC_50_BREASTSTROKE.name],
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "50m",
                        pbs[TempusEvent.SC_50_BACKSTROKE.name],
                        pbs[TempusEvent.LC_50_BACKSTROKE.name],
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "50m",
                        pbs[TempusEvent.SC_50_BUTTERFLY.name],
                        pbs[TempusEvent.LC_50_BUTTERFLY.name],
                    )

            elif "100m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "100m",
                        pbs[TempusEvent.SC_100_FREESTYLE.name],
                        pbs[TempusEvent.LC_100_FREESTYLE.name],
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "100m",
                        pbs[TempusEvent.SC_100_BREASTSTROKE.name],
                        pbs[TempusEvent.LC_100_BREASTSTROKE.name],
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "100m",
                        pbs[TempusEvent.SC_100_BACKSTROKE.name],
                        pbs[TempusEvent.LC_100_BACKSTROKE.name],
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "100m",
                        pbs[TempusEvent.SC_100_BUTTERFLY.name],
                        pbs[TempusEvent.LC_100_BUTTERFLY.name],
                    )
                elif self.is_medley(event_name):
                    return "100m", pbs[TempusEvent.SC_100_INDIVIDUAL_MEDLEY.name], None

            elif "200m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "200m",
                        pbs[TempusEvent.SC_200_FREESTYLE.name],
                        pbs[TempusEvent.LC_200_FREESTYLE.name],
                    )
                elif self.is_breaststroke(event_name):
                    return (
                        "200m",
                        pbs[TempusEvent.SC_200_BREASTSTROKE.name],
                        pbs[TempusEvent.LC_200_BREASTSTROKE.name],
                    )
                elif self.is_backstroke(event_name):
                    return (
                        "200m",
                        pbs[TempusEvent.SC_200_BACKSTROKE.name],
                        pbs[TempusEvent.LC_200_BACKSTROKE.name],
                    )
                elif self.is_butterfly(event_name):
                    return (
                        "200m",
                        pbs[TempusEvent.SC_200_BUTTERFLY.name],
                        pbs[TempusEvent.LC_200_BUTTERFLY.name],
                    )
                elif self.is_medley(event_name):
                    return (
                        "200m",
                        pbs[TempusEvent.SC_200_INDIVIDUAL_MEDLEY.name],
                        pbs[TempusEvent.LC_200_INDIVIDUAL_MEDLEY.name],
                    )

            elif "400m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "400m",
                        pbs[TempusEvent.SC_400_FREESTYLE.name],
                        pbs[TempusEvent.LC_400_FREESTYLE.name],
                    )
                elif self.is_medley(event_name):
                    return (
                        "400m",
                        pbs[TempusEvent.SC_400_INDIVIDUAL_MEDLEY.name],
                        pbs[TempusEvent.LC_400_INDIVIDUAL_MEDLEY.name],
                    )

            elif "800m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "800m",
                        pbs[TempusEvent.SC_800_FREESTYLE.name],
                        pbs[TempusEvent.LC_800_FREESTYLE.name],
                    )

            elif "1500m" in event_name:
                if self.is_freestyle(event_name):
                    return (
                        "1500m",
                        pbs[TempusEvent.SC_1500_FREESTYLE.name],
                        pbs[TempusEvent.LC_1500_FREESTYLE.name],
                    )

        except KeyError as e:
            print("We found a key error: ", e.what())

        return None, None
