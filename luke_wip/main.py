from excel import ExcelSheet
from group import Group
from swimify import Swimify
from tempus_parser import TempusParser
import json, time

if __name__ == "__main__":

    time0 = time.time()

    # Read data from configuration file
    config = {}
    with open("config.json") as f:
        config = json.load(f)
        f.close()

    # Create group from json definition
    club = Group(config["groups"])

    # Open and prepare excel sheet for export
    excel_sheet = ExcelSheet(config["club_name"], config["comp_name"], config["comp_date"])

    # Fetch competition events from swimify
    swimify = Swimify(config["comp_url"])

    # Get only the club that we are interested in
    swimify_entries = swimify.get_club_entries(config["club_nbr"])

    # Get a parser up and running
    parser = TempusParser()

    # Add Levente as a nice touch for Sebbe
    excel_sheet.save_one_swimmer('25m', 'Levente a király Nagy', '4:20.69', '4:20.69', '400m Ungersk Special')

    # Parse the pbs from tempus codes and add them to spreadsheet
    for entry in swimify_entries:
        pbs = club.swimmers[entry.entry_name].pbs
        sheet, pb_sc, pb_lc = parser.parse_pbs(pbs, entry.event_name)

        excel_sheet.save_one_swimmer(sheet, entry.entry_name, pb_sc, pb_lc, entry.event_name)

    time1 = time.time()

    print("Time to fetch all swimmers and add to heat list: " + str(time1 - time0))
