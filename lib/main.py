from Club import club
from Competition import competition
from Entry import entry, entry_list
from Event import event
from logging import debug
from Session import session
from SwimifyHandler import swimify_handler

from Excel import ExcelSheet

import subprocess, re

LUKE_ENTRY_LIST = []

##____ Choose competition section depending on input ____##
def choice_index(list_of_choices):
    '''
    Private method to allow interactive choice in list from 
    terminal.

    Input:
        list_of_choices: list with found objects to choose from

    Return:
        index of choice.
    '''
    index = -1
    last_index   = len(list_of_choices) - 1
    while ((index < 0) or (last_index < index)):
        try:
            if last_index < index: 
                print("Not a valid input\n\n") 
                index = -1
            else: 
                index = int(input("\nEnter index to click: ")) - 1
        except ValueError:
            print("\nPlease enter a valid integer index.\n")
    
    return list_of_choices[index]

    # Print iterations progress
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def interact_with_terminal(handler: swimify_handler):
    print("1: Competitions This Week")
    print("2: Upcoming Competitions")
    print("3: Finished Competitions")

    index = -1
    while ((index < 0) or (2 < index)):
        try:
            if  2 < index: 
                print("Not a valid input\n\n") 
                index = -1
            else: 
                match int(input("\nEnter index to click: ")) - 1:
                    case 0:
                        index = 0
                        print(index)
                        competitions = handler.get_competitions_this_week()
                    case 1:
                        index = 1
                        competitions = handler.get_upcoming_competitions()
                    case 2:
                        index = 2
                        competitions = handler.get_finished_competitions()
        except ValueError:
            print("\nPlease enter a valid integer index.\n")
    subprocess.run('clear', shell=True)
    print("Available Competitions:")
    for i, comp in enumerate(competitions):
        print(f'\t{i + 1}: ' + comp.competition_name)

    selected_competition = choice_index(competitions)
    subprocess.run('clear', shell=True)
    print(selected_competition.competition_name + '\n')
    handler.select_competition(selected_competition)
    sessions = handler.get_all_sessions()
    nbr_sessions = len(sessions)

    print("CURRENTLY LOADING EVENT SCHEDULE")
    all_events = []

    # Initial call to print 0% progress
    printProgressBar(0, nbr_sessions, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, sess in enumerate(sessions):
        sess.events = handler.get_session_schedule(sess)
        for e in sess.events:
            all_events.append(e)

        # Update Progress Bar
        printProgressBar(i + 1, nbr_sessions, prefix = 'Progress:', suffix = 'Complete', length = 50)
    subprocess.run('clear', shell=True)

    clubs = handler.get_all_clubs()

    print("Entered Clubs: \n")
    for i, swim_club in enumerate(clubs):
        print(f'\t{i + 1}: ' + swim_club.club_name)

    selected_club = choice_index(clubs)
    subprocess.run('clear', shell=True)

    print(selected_club.club_name + '\n')
    handler.select_club(selected_club)
    return sessions, all_events, selected_club


if __name__ == "__main__":
    subprocess.run('clear', shell=True)
    handler = swimify_handler(10)
    competitions = []
    sessions, all_events, selected_club = interact_with_terminal(handler)
    
    club_swimmers = handler.get_all_swimmers(selected_club)
    nbr_swimmers = len(club_swimmers)

    # Step 1 of mapping swimmers entered events to event in all_events: Create a dictionary of all_events for O(1) lookup
    event_dict = {event: event for event in all_events}

    print("CURRENTLY LOADING ENTERED SWIMMERS")
    print("NOTE: This might take some time as Tempus Open is read for each swimmer")
    
    # Initial call to print 0% progress
    printProgressBar(0, nbr_swimmers, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, swimmer_object in enumerate(club_swimmers):
        subprocess.run('clear', shell=True)
        print("CURRENTLY LOADING ENTERED SWIMMERS")
        print("NOTE: This might take some time as Tempus Open is read for each swimmer")
        # Update Progress Bar
        printProgressBar(i, nbr_swimmers, prefix = 'Progress:', suffix = 'Complete', length = 50)
        swimmer_object.events = handler.get_swimmer_events(swimmer_object)

        ### TAR TID___________________________________________________________________________###

        swimmer_object.personal_bests = handler.get_swimmer_personal_bests(swimmer_object)

        ###___________________________________________________________________________________###

        # Step 2: Iterate over swimmer_object.events and find the corresponding event in all_events
        for swimmer_event in swimmer_object.events:
            if swimmer_event in event_dict:
                # Step 3: Call the add_swimmer method on the corresponding event
                event_dict[swimmer_event].add_swimmer(swimmer_object)
            else:
                debug(f"Event {swimmer_event.event_name} not found in all_events")
    printProgressBar(nbr_swimmers, nbr_swimmers, prefix = 'Progress:', suffix = 'Complete', length = 50)
    subprocess.run('clear', shell=True)

    for s in sessions:
        print("CURRENTLY LOADING: " + s.name)
        events = s.events
        nbr_events = len(events)

        # Initial call to print 0% progress
        printProgressBar(0, nbr_events, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i, session_event in enumerate(events):
            event_entry_list = entry_list(session_event)
            for e in entry_list(session_event).entries:
                LUKE_ENTRY_LIST.append(e.information)
            # Update Progress Bar
            printProgressBar(i + 1, nbr_events, prefix = 'Progress:', suffix = 'Complete', length = 50)
        subprocess.run('clear', shell=True)
print(LUKE_ENTRY_LIST)

excel_sheet = ExcelSheet()

# Entries from Filps list are objects such as ["Name", "PB SC", "PB LC", "Event name", "Start time"]
for e in LUKE_ENTRY_LIST:
    name = e[0]
    pb_sc = e[1]
    pb_lc = e[2]
    event_string = e[4] + ": " + e[3]
    race = re.findall('\d{1,4}m', e[3])[0]
    excel_sheet.save_one_swimmer(race, name, pb_sc, pb_lc, event_string)

print("You can now find your Excel sheet as test.xlsx")