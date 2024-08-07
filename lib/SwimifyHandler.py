import driver_handler
import html_renderer

from Club import club
from Event import event
from Swimmer import swimmer


####______________________________________________________________________________________________________####

'''

The following serves as a class with properites for acquiring data from webpages
live.swimify.com and www.tempusopen.se. 


'''

####______________________________________________________________________________________________________####

swimify_url = "https://live.swimify.com"

tempus_url = "https://www.tempusopen.se/index.php?r=Swimmer"

class swimify_handler():

    def __init__(self, wait_time: float) -> None:
        self._driver, self._wait = driver_handler.setup_driver(swimify_url, wait_time)
        
    def get_competitions_this_week() -> list[map]:
        pass

    def get_finished_competitions() -> list[map]:
        pass

    def get_upcoming_competitions() -> list[map]:
        pass

    def get_session_schedule(session_selector: str) -> list[event]:
        pass

    def get_all_session_schedules() -> map:
        pass

    def get_club() -> club:
        pass

    def get_all_clubs() -> list[club]:
        pass

    def get_swimmers(club) -> list[swimmer]:
        pass