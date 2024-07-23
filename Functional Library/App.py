import club_selector
import competition_selector
import session_scraper
import swimmer_event_finder
import tempus_scraper

def main():
    swimify_url = "https://live.swimify.com"

    tempus_url = "https://www.tempusopen.se/index.php?r=Swimmer"

    competition_url  = competition_selector.run(swimify_url)

    i = input("Enter 1 to load event schedule: ")

    if i == '1': session_scraper.run(competition_url)

    club_name, club_url = club_selector.run(competition_url)

    swimmers = swimmer_event_finder.run(club_url, club_name)

    for swimmer_string, swimmer_object in swimmers.items():
        print("\nSwimmer: " + swimmer_string)
        swimmer_event_list = swimmer_object.events

        swimmer_event_string_list = [e.distance for e in swimmer_event_list]
        tempus_scraper.run(tempus_url, swimmer_object, swimmer_event_string_list)

main()