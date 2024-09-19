from excel import ExcelSheet
from group import Group
from swimify import Swimify
from tempus_parser import TempusParser
import time

if __name__ == "__main__":

    time0 = time.time()

    # Create group from json definition
    club = Group("hs")

    # Open and prepare excel sheet for export
    excel_sheet = ExcelSheet()

    # Fetch competition events from swimify
    swimify = Swimify("swedish-swim-games-2024-grand-prix-2024-09-20")

    # Get only the club that we are interested in
    swimify_entries = swimify.get_club_entries("12")

    # Get a parser up and running
    parser = TempusParser()

    # Parse the pbs from tempus codes and add them to spreadsheet
    for entry in swimify_entries:
        pbs = club.swimmers[entry.entry_name].pbs
        sheet, pb_sc, pb_lc = parser.parse_pbs(pbs, entry.event_name)

        excel_sheet.save_one_swimmer(sheet, entry.entry_name, pb_sc, pb_lc, entry.event_name)

    time1 = time.time()

    print("Time to fetch all swimmers and add to heat list: " + str(time1 - time0))
