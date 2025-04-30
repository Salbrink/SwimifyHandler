import re

from get_my_html import GetMyHtml
from enum import Enum

TEMPUS_URL = "https://www.tempusopen.se"
TEMPUS_SWIMMER = TEMPUS_URL + "/swimmers/{0}/swimming"
TEMPUS_EVENT = TEMPUS_URL + "{0}/events/{1}"

REGEX_SWIM_TIME = '"swim_time":"\d{1,2}:\d{1,2}.\d{1,2}"'
REGEX_EVENT_CODE = '"event_code":\d{1,2}'


class TempusOpen:

    def __init__(self):
        # Start an request helper
        self.get_my_html = GetMyHtml()

    def get_swimmer(self, tempus_id):
        url = TEMPUS_SWIMMER.format(tempus_id)

        resp = self.get_my_html.call_this_url(url)

        # Do a raw regex that gets the times and it's corresponding event code defined by tempus
        times = [t[13:-1] for t in re.findall(REGEX_SWIM_TIME, resp)]
        codes = [int(c[13:]) for c in re.findall(REGEX_EVENT_CODE, resp)]

        # Most ugly parsing possible of the extracted data above
        pbs = {}
        for c, t in zip(codes, times):
            pbs[TempusEvent(c).name] = t

        return pbs


class TempusEvent(Enum):
    SC_25_FREESTYLE = 4
    SC_25_BREASTSTROKE = 5
    SC_25_BACKSTROKE = 6
    SC_25_BUTTERFLY = 7

    SC_50_FREESTYLE = 11
    LC_50_FREESTYLE = 12
    SC_100_FREESTYLE = 13
    LC_100_FREESTYLE = 14
    SC_200_FREESTYLE = 15
    LC_200_FREESTYLE = 16
    SC_400_FREESTYLE = 17
    LC_400_FREESTYLE = 18
    SC_800_FREESTYLE = 19
    LC_800_FREESTYLE = 20
    SC_1500_FREESTYLE = 21
    LC_1500_FREESTYLE = 22

    SC_50_BREASTSTROKE = 31
    LC_50_BREASTSTROKE = 32
    SC_100_BREASTSTROKE = 33
    LC_100_BREASTSTROKE = 34
    SC_200_BREASTSTROKE = 35
    LC_200_BREASTSTROKE = 36

    SC_50_BACKSTROKE = 41
    LC_50_BACKSTROKE = 42
    SC_100_BACKSTROKE = 43
    LC_100_BACKSTROKE = 44
    SC_200_BACKSTROKE = 45
    LC_200_BACKSTROKE = 46

    SC_50_BUTTERFLY = 51
    LC_50_BUTTERFLY = 52
    SC_100_BUTTERFLY = 53
    LC_100_BUTTERFLY = 54
    SC_200_BUTTERFLY = 55
    LC_200_BUTTERFLY = 56

    SC_100_INDIVIDUAL_MEDLEY = 61
    SC_200_INDIVIDUAL_MEDLEY = 63
    LC_200_INDIVIDUAL_MEDLEY = 64
    SC_400_INDIVIDUAL_MEDLEY = 65
    LC_400_INDIVIDUAL_MEDLEY = 66
