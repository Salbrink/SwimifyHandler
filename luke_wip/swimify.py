import re

from requests_html import HTMLSession

SWIMIFY_URL = "https://live.swimify.com/competitions/"
SWIMIFY_COMP = SWIMIFY_URL + "{0}"

SWIMIFY_CLUBS = SWIMIFY_COMP + "/swimmers/clubs"
SWIMIFY_CLUB = SWIMIFY_CLUBS + "/{1}"
SWIMIFY_CLUB_EVENTS = SWIMIFY_CLUB + "/entries/events"

EVENT_NUMBER = '"MuiTypography-root MuiTypography-body1 css-19rk9gv"'
EVENT_NAME = '"MuiTypography-root MuiTypography-body1 css-1270wsa"'
ENTRY_NAME = '"MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-lc08jz"'
ENTRY_RANK = '"MuiTypography-root MuiTypography-body1 css-9l3uo3"'

COMBINATION = r"{0}>(\d+?)<|{1}>(.*?)<|{2}>(\d+?)<|{3}>(.*?)<".format(
    EVENT_NUMBER, EVENT_NAME, ENTRY_RANK, ENTRY_NAME
)


class Swimify:

    def __init__(self, competition):
        # Start an request helper
        self.session = HTMLSession()
        self.competition = competition

    def get_event(self):
        url = SWIMIFY_COMP.format(self.competition)

        resp = self.get_my_html.call_this_url(url)

        print(resp)

        return 0

    def get_club_entries(self, club_id):
        url = SWIMIFY_CLUB_EVENTS.format(self.competition, club_id)
        print(url)

        resp = self.session.get(url)
        resp.html.render(sleep=5)

        combination = [en for en in re.findall(COMBINATION, resp.html.html)]

        self.session.close()

        event_number = 0
        event_name = ""
        entry_rank = 0
        entry_name = ""

        entries = []

        for s in combination:
            if s[0] != "":
                event_number = s[0]
            elif s[1] != "":
                event_name = s[1]
            elif s[2] != "":
                entry_rank = s[2]
            elif s[3] != "":
                entry_name = s[3]
                entries.append([event_number, event_name, entry_rank, entry_name])

        return entries
