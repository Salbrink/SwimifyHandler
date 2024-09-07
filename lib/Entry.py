from Event import event
from Swimmer import swimmer
from logging import debug
import time
# [name, pb_sc, pb_lc, event_name, start_time]
# @return list[entry]

class entry: 

    def __init__(self, name: str, pb_sc: str, pb_lc: str, event_name: str, start_time: str):
        self._information = [name, pb_sc, pb_lc, event_name, start_time]

    @property
    def information(self): 
        return self._information


class entry_list:

    def __init__(self, current_event: event):
        self._entries = []
        event_name = current_event.event_name
        start_time = current_event.start_time
        for swimmer in current_event.entered_swimmers:
            name = swimmer.first_name + ' ' + swimmer.last_name
            try: 
                personal_best_information = swimmer.find_event_times(event_name)
                sc_info = personal_best_information[0]
                lc_info = personal_best_information[1]
                self.entries.append(entry(name, sc_info[0], lc_info[0], event_name, start_time))
            except TypeError:
                debug("Personal bests not found in entries")
                self.entries.append(entry(name, '00:00.00', '00:00.00', event_name, start_time))

    @property
    def entries(self):
        return self._entries