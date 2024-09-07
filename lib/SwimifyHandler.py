import driver_handler
import html_renderer

from Club import club
from Competition import competition
from Event import event
from logging import debug
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

tempus_url = "https://www.tempusopen.se/swimmers"

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

tempus_search_button_XPATH = "//button[@type='submit' and contains(text(), 'Sök')]"
tempus_search_result_XPATH = "//tr[@class='even:bg-gray-50 odd:bg-white border-b border-gray-200'][1]"
tempus_table_div_selector = "div > h5.font-semibold.text-xl.mb-2"
tempus_rows_div_selector = "tr.even\\:bg-gray-50, tr.odd\\:bg-white"

class swimify_handler():

    def __init__(self, wait_time: float) -> None:
        self._driver, self._wait = driver_handler.setup_driver(swimify_url, wait_time)
        self._tempus_driver, self._tempus_wait = driver_handler.setup_driver(tempus_url, wait_time)
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
                debug("Found entry that is not parsed as swimmer " + swimmer_name)

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
    
    ## Should be done in parallell
    def get_swimmer_personal_bests(self, selected_swimmer: swimmer) -> list[map]:
        personal_bests = []

        self._tempus_driver.get(tempus_url)
        while True:
            try:
                first_name = html_renderer.find_element(self._tempus_wait, "first_name", By.NAME)
                first_name.send_keys(selected_swimmer.first_name)

                last_name  = html_renderer.find_element(self._tempus_wait, "last_name", By.NAME)
                last_name.send_keys(selected_swimmer.last_name)
                
                club_name  = html_renderer.find_element(self._tempus_wait, "club", By.NAME)
                club_name.send_keys(selected_swimmer.swimmer_club.club_name)

                search_button = html_renderer.find_element(self._tempus_wait, tempus_search_button_XPATH, By.XPATH)
                html_renderer.click_element(self._tempus_driver, search_button)
                break
            except AttributeError:
                debug('Tempus page not properly loaded')


        # Find the first <tr> element in the table
        top_search = html_renderer.find_element(self._tempus_wait, tempus_search_result_XPATH, By.XPATH)

        if top_search is None:
            debug("Swimmer Tempus not found for: " + selected_swimmer.to_string())
            return personal_bests
        
        # Find the "Visa" link inside the first <tr> and click it
        visa_link = html_renderer.find_sub_element(top_search, ".//a[@class='text-tempus-dark-blue']", By.XPATH)
        html_renderer.click_element(self._driver, visa_link)

        selected_swimmer.tempus_url = self._tempus_driver.current_url
        print(selected_swimmer.tempus_url)

        event_name_list = [e.event_name for e in selected_swimmer.events]
        print(event_name_list)

        # Find the tables of "Kortbana (25m)" and "Långbana (50m)" as element 0 and 1 respectively in the 
        # returned list
        try:
            [sc_table, lc_table] = html_renderer.find_all_elements(self.wait, tempus_table_div_selector, By.CSS_SELECTOR)
        except TypeError:
            debug("Tables of Tempus not properly loaded")
            return personal_bests

        sc_map = self._search_tempus_table(self._tempus_wait, sc_table, event_name_list)
        lc_map = self._search_tempus_table(self._tempus_wait, lc_table, event_name_list)
        
        for event_object in selected_swimmer.events:
            # List with type [Personal best time, Date of race, Competition]
            pb_list = []
            try: 
                pb_list.append(sc_map[event_object.event_name])
            except KeyError: 
                pb_list.append('No personal best SCM')
            try:
                pb_list.append(lc_map[event_object.event_name])
            except KeyError:
                pb_list.append('No personal best LCM')

            personal_bests.append({event_object : pb_list})

        return personal_bests

    def _search_tempus_table(self, wait: WebDriverWait, table: WebElement, event_name_list: list[str]) -> map:
        '''
        Private method for creating a map given a section in tempus page of a swimmer.

        Input:
            wait: active selenium.webdriver.WebdriverWait object
            table: WebElement of Tempus table with personal bests
            event_list: list of event_string names

        Return:
            Key-Value map with event name as key and time and date of personal best as value.
        '''
        event_map = {}
        
        try:
            parent_div = table.find_element(By.XPATH, "./..")  # Select the parent <div> of the <h5>
    
            # Find all <tr> elements inside the table within this div
            rows = parent_div.find_elements(By.CSS_SELECTOR, tempus_rows_div_selector)
            
            for row in rows:
                #Find the first <td> and fourth <td> for 'Sample string' and 'Sample time'
                event_name = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text

                # Check if the event name is in the predefined list
                if event_name.lower() in event_name_list:
                    # Extract the date and time from the respective cells
                    event_comp = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                    event_date = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                    event_time = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
                    # Add the date and time as a tuple to the list
                    event_map[event_name] = [event_time, event_date, event_comp]
                    
            return event_map
        except Exception as e:
            debug(f"An error occurred: {e}")
            return event_map
        
    @property
    def driver(self) -> webdriver:
        return self._driver
    
    @property
    def wait(self) -> WebDriverWait:
        return self._wait


# Some basic testing material
handler = swimify_handler(10)

finished_competitions = handler.get_finished_competitions()


while len(finished_competitions) == 0:
    print("No finished competitions found, retrying:")
    finished_competitions = handler.get_finished_competitions()

for f in finished_competitions:
    print(f.competition_name)
url = handler.select_competition(finished_competitions[6])

print(handler.driver.current_url)
session_list = handler.get_all_sessions()

for s in session_list:
    print(s.name + '|' + s.time)

    e_list = handler.get_session_schedule(s)

    for e in e_list:
        try:
            print(e.event_name + ' ' + e.start_time)
        except AttributeError:
            print("Not an event")
clubs = handler.get_all_clubs()

for c in clubs:
    print(c.club_name)

club_url = handler.select_club(clubs[0])
print(club_url)

swimmer_list = handler.get_all_swimmers(clubs[0])
for s in swimmer_list:
    s.events = handler.get_swimmer_events(s)
    print(s.to_string())
    for e in s.events:
        print(e.event_name)
    print(handler.get_swimmer_personal_bests(s))
