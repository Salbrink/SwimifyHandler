from Event import event
from selenium.webdriver.remote.webelement import WebElement

class swimmer:
    def __init__(self, first_name: str, last_name: str, swimmer_club, div_element=None) -> None:
        
        self._div_element = div_element
        self._first_name = first_name
        self._last_name = last_name
        self._swimmer_club = swimmer_club
        self._events = []
        self._tempus_url = None


    @property
    def div_element(self) -> WebElement:
        return self._div_element
    
    @div_element.setter
    def div_element(self, element: WebElement) -> None:
        self._div_element = element

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    @property
    def swimmer_club(self):
        return self._swimmer_club

    @swimmer_club.setter
    def club_name(self, club_object) -> None:
        self._swimmer_club = club_object

    def to_string(self) -> str:
        return self._first_name + " " + self._last_name + " " + self.swimmer_club.club_name
    
    @property
    def events(self) -> list[event]:
        return self._events
    
    @events.setter
    def events(self, event_list: list[event]) -> None:
        self._events = event_list
    
    def add_event(self, event) -> None:
        self._events.append(event)

    @property
    def tempus_url(self):
        return self._tempus_url
    
    @tempus_url.setter
    def tempus_url(self, tempus_url):
        self._tempus_url = tempus_url