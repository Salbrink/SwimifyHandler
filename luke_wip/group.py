import json

from swimmer import Swimmer
from tempus import TempusOpen


class Group:

    def __init__(self, groups):
        self.swimmers = {}
        tempus_open = TempusOpen()

        # Load team from file
        self.team = {}
        for group in groups:
            with open(group + ".json") as f:
                self.team.update(json.load(f))
                f.close()

        # Populate the group with swimmer objects
        for name in self.team:
            tempus_id = self.team[name]
            pbs = tempus_open.get_swimmer(tempus_id)
            self.swimmers[name] = Swimmer(name, tempus_id, pbs)
