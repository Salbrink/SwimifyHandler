from Session import session
from selenium.webdriver.remote.webelement import WebElement

class competition:

    def __init__(self, competition_name: str, swimmer_club, div_element=None) -> None:
        
        self._competition_name = competition_name
        self._div_element = div_element
        self._swimmer_club = swimmer_club
        self._events = []


    @property
    def competition_name(self) -> str:
        return self._competition_name
    
    @competition_name.setter
    def competition_name(self, name: str) -> None:
        self._competition_name = name
        
    @property
    def div_element(self) -> WebElement:
        return self._div_element
    
    @div_element.setter
    def div_element(self, element: WebElement) -> None:
        self._div_element = element