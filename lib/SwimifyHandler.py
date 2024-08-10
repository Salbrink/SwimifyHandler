import driver_handler
import html_renderer

from Club import club
from Competition import competition
from Event import event
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Session import session
from Swimmer import swimmer


####______________________________________________________________________________________________________####

'''

The following serves as a class with properites for acquiring data from webpages
live.swimify.com and www.tempusopen.se. 


'''

####______________________________________________________________________________________________________####

swimify_url = "https://live.swimify.com"

tempus_url = "https://www.tempusopen.se/index.php?r=Swimmer"

competition_section_div_selector = 'div[class^="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 "]'
competitions_this_week_div_selector = 'div[class^="MuiBox-root css-"][role="article"][aria-labelledby^="competition-title-"]'
upcoming_competitions_div_selector = "div.MuiGrid-root.MuiGrid-container.MuiGrid-wrap-xs-nowrap.css-3s91ag"
finished_competitions_div_selector = upcoming_competitions_div_selector
competition_title_p_selector = 'p[class^="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-"]'

session_div_selector = 'div[class="MuiBox-root css-qlbhet"]'
session_name_p_selector = 'p.MuiTypography-root.MuiTypography-body1.css-xu169k'
session_time_and_date_p_selector = 'p.MuiTypography-root.MuiTypography-body1.css-bxnpil'
event_XPATH = "//a[@display='flex']"
start_time_div_selector = 'div.MuiBox-root.css-z9ki6v > p'
event_name_div_selector = 'div.MuiBox-root.css-6771j6 > p'

swimmers_button_XPATH = '//button[.//p[contains(text(), "Swimmers")]]'
club_div_selector = 'div.MuiBox-root.css-1eukt2p'
last_club_div_selector = 'div.MuiBox-root.css-1fis6zz' # Do not know why this is different
club_name_p_selector = 'p.MuiTypography-root.MuiTypography-body1.MuiTypography-noWrap.css-1bpwwm7'

swimmer_div_selector = 'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-1hbn5fk'
swimmer_name_p_selector = 'p.MuiTypography-root.MuiTypography-body1.MuiTypography-noWrap.css-lc08jz'

swimmer_event_div_selector = 'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-h9dk79'
swimmer_event_name_div_selector = 'div.MuiBox-root.css-2ijh4t > p.MuiTypography-root.MuiTypography-body1.css-151uy7p'

class swimify_handler():

    def __init__(self, wait_time: float) -> None:
        self._driver, self._wait = driver_handler.setup_driver(swimify_url, wait_time)
        self._competition_sections =  html_renderer.find_all_elements(self._wait, competition_section_div_selector, By.CSS_SELECTOR)
        
    def get_competitions_this_week(self) -> list[competition]:
        competitions = []

        competition_div_list = html_renderer.find_all_sub_elements(self._competition_sections[0],\
                                    competitions_this_week_div_selector, By.CSS_SELECTOR)
        
        competition_div_map = html_renderer.string_web_element_map(competition_div_list, \
                                competition_title_p_selector, By.CSS_SELECTOR)
        
        for competition_name, competition_div in competition_div_map.items():
            competitions.append(competition(competition_name, competition_div))

        return competitions

    def get_finished_competitions(self) -> list[competition]:
        competitions = []

        competition_div_list = html_renderer.find_all_sub_elements(self._competition_sections[2],\
                                    finished_competitions_div_selector, By.CSS_SELECTOR)
        
        competition_div_map = html_renderer.string_web_element_map(competition_div_list, \
                                competition_title_p_selector, By.CSS_SELECTOR)
        
        for competition_name, competition_div in competition_div_map.items():
            competitions.append(competition(competition_name, competition_div))

        return competitions

    def get_upcoming_competitions(self) -> list[competition]:
        competitions = []

        competition_div_list = html_renderer.find_all_sub_elements(self._competition_sections[1],\
                                    upcoming_competitions_div_selector, By.CSS_SELECTOR)
        
        competition_div_map = html_renderer.string_web_element_map(competition_div_list, \
                                competition_title_p_selector, By.CSS_SELECTOR)
        
        for competition_name, competition_div in competition_div_map.items():
            competitions.append(competition(competition_name, competition_div))

        return competitions
    
    def select_competition(self, competition_to_select: competition) -> str:
        html_renderer.click_element(self._driver, competition_to_select.div_element)
        return self._driver.current_url


    def get_all_sessions(self) -> list[session]:
        sessions = []
        
        session_divs = html_renderer.find_all_elements(self._wait, \
                                    session_div_selector, By.CSS_SELECTOR)
        
        for session_div in session_divs:
            session_name = html_renderer.find_sub_element(session_div, \
                                        session_name_p_selector, By.CSS_SELECTOR).text
            session_time  = ' '.join([string.text for string in html_renderer.find_all_sub_elements(session_div, \
                                        session_time_and_date_p_selector, By.CSS_SELECTOR)])
            sessions.append(session(session_name, session_time, div_element=session_div))
        
        return sessions

    def get_session_schedule(self, selected_session: session) -> list[event]:
        events = []

        html_renderer.click_element(self._driver, selected_session.div_element)

        event_web_elements = html_renderer.find_all_elements(self._wait, event_XPATH, By.XPATH)

        for event_web_element in event_web_elements:
            event_name = html_renderer.find_sub_element(event_web_element, event_name_div_selector, By.CSS_SELECTOR).text
            start_time = html_renderer.find_sub_element(event_web_element, start_time_div_selector, By.CSS_SELECTOR).text
            events.append(event(event_name, start_time=start_time))

        return events

    def get_all_clubs(self) -> list[club]:
        clubs = []

        html_renderer.click_element(self._driver, \
            html_renderer.find_element(self._wait, swimmers_button_XPATH, By.XPATH))
        club_divs = html_renderer.find_all_elements(self._wait, club_div_selector, By.CSS_SELECTOR)
        club_divs.append(html_renderer.find_element(self._wait, last_club_div_selector, By.CSS_SELECTOR))

        for club_div in club_divs:
            clubs.append(club(html_renderer.find_sub_element(club_div, club_name_p_selector, By.CSS_SELECTOR).text, \
                div_element=club_div))
            
        return clubs

    def select_club(self, selected_club: club) -> str:
        html_renderer.click_element(self._driver, selected_club.div_element)
        return self._driver.current_url


    def get_all_swimmers(self, selected_club: club) -> list[swimmer]:
        swimmers = []

        swimmer_divs = html_renderer.find_all_elements(self._wait, swimmer_div_selector, By.CSS_SELECTOR)
        swimmer_div_map = html_renderer.string_web_element_map(swimmer_divs, swimmer_name_p_selector, By.CSS_SELECTOR)

        for swimmer_name, swimmer_div in swimmer_div_map.items():
            try:
                first_name, last_name = swimmer_name.split(' ', 1)
                swimmers.append(swimmer(first_name, last_name, selected_club, div_element=swimmer_div))
            except ValueError:
                print("Found entry that is not parsed as swimmer")

        return swimmers

    def get_swimmer_events(self, selected_swimmer: swimmer) -> list[event]:
        events = []
       
        html_renderer.click_element(self._driver, selected_swimmer.div_element)

        event_divs = html_renderer.find_all_elements(self._wait, swimmer_event_div_selector, By.CSS_SELECTOR)

        if event_divs is None:
            return events
        
        for event_div in event_divs:
            event_name = ''.join(html_renderer.find_sub_element(event_div, swimmer_event_name_div_selector, By.CSS_SELECTOR).text)
            events.append(event(event_name))

        return events

    @property
    def driver(self) -> webdriver:
        return self._driver
    
    @property
    def wait(self) -> WebDriverWait:
        return self._wait


# # Some testing material
# handler = swimify_handler(10)

# finished_competitions = handler.get_finished_competitions()

# for f in finished_competitions:
#     print(f.competition_name)
# url = handler.select_competition(finished_competitions[19])

# print(handler.driver.current_url)
# session_list = handler.get_all_sessions()

# for s in session_list:
#     print(s.name + '|' + s.time)

#     e_list = handler.get_session_schedule(s)

#     for e in e_list:
#         try:
#             print(e.event_name + e.start_time)
#         except AttributeError:
#             print("Not an event")
# clubs = handler.get_all_clubs()

# for c in clubs:
#     print(c.club_name)

# club_url = handler.select_club(clubs[0])
# print(club_url)

# swimmer_list = handler.get_all_swimmers(clubs[0])
# for s in swimmer_list:
#     s.events = handler.get_swimmer_events(s)
#     print(s.to_string())
#     for e in s.events:
#         print(e.event_name)
