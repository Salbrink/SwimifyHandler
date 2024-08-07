from selenium.webdriver.remote.webelement import WebElement
from Swimmer import swimmer

class club:

    def __init__(self, club_name: str, div_element=None) -> None:
        self._club_name = club_name
        self._swimmers  = []
        self._div_element = div_element

    @property
    def club_name(self) -> str: 
        return self._club_name
    
    @club_name.setter
    def club_name(self, name: str):
        self._club_name = name

    @property
    def div_element(self) -> WebElement:
        return self._div_element
    
    @div_element.setter
    def div_element(self, element: WebElement) -> None:
        self._div_element = element

    @property
    def swimmers(self) -> list[swimmer]:
        return self._swimmers
    
    @swimmers.setter
    def swimmers(self, swimmer_list: list[swimmer]) -> None:
        self._swimmers = swimmer_list

    def add_swimmer(self, swimmer_object: swimmer) -> None:
        self._swimmers.append(swimmer_object)