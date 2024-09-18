from excel import ExcelSheet
from group import Group
from swimify import Swimify
from tempus import TempusParser
import time

if __name__ == "__main__":

    time0 = time.time()

    # Create group from json definition
    club = Group("hs")

    # Open and prepare excel sheet for export
    ecxel_sheet = ExcelSheet()

    # Fetch competition events from swimify
    swimify = Swimify("swedish-swim-games-2024-grand-prix-2024-09-20")

    # Get only the club that we are interested in
    swimify_entries = swimify.get_club_entries("12")

    # Get a parser up and running
    parser = TempusParser()

    # Parse the pbs from tempus codes and add them to spreadsheet
    for entry in swimify_entries:
        event_name = entry[1]
        name = entry[3]
        pbs = club.swimmers[name].pbs
        sheet, pb_sc, pb_lc = parser.parse_pbs(pbs, event_name)

        ecxel_sheet.save_one_swimmer(sheet, name, pb_sc, pb_lc, event_name)

    time1 = time.time()

    print("Time to fetch all swimmers and add to heat list: " + str(time1 - time0))
