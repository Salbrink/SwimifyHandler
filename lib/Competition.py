from Session import session
from selenium.webdriver.remote.webelement import WebElement

class competition:

    def __init__(self, competition_name: str, div_element=None) -> None:
        
        self._competition_name = competition_name
        self._div_element = div_element
        self._sessions = []


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

    @property
    def sessions(self) -> list[session]:
        return self._sessions
    
    def add_session(self, session_object: session) -> None:
        self._sessions.append(session_object)