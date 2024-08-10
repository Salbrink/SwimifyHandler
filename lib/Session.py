from Event import event
from selenium.webdriver.remote.webelement import WebElement

class session:

    def __init__(self, name: str, time: str, events=None, schedule=None, div_element=None) -> None:
        self._events = events
        self._div_element = div_element
        self._name = name
        self._time = time
        self._schedule = schedule
    
    @property
    def div_element(self) -> WebElement:
        return self._div_element
    
    @div_element.setter
    def div_element(self, element: WebElement) -> None:
        self._div_element = element

    @property
    def events(self) -> list[event]:
        return self._events
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def time(self) -> str:
        return self._time
    
    @property
    def schedule(self) -> list[str]:
        return self._schedule
    
    @schedule.setter
    def schedule(self, schedule: list[str]) -> None:
        self._schedule = schedule