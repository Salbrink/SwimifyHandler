from excel import ExcelSheet
from tempus import TempusOpen, TempusEvent
import time

if __name__ == "__main__":

    time0 = time.time()

    ecxel_sheet = ExcelSheet()
    tempus_open = TempusOpen()

    name1 = "Filip"
    name2 = "Hanna"
    name3 = "Olivia"

    pbs_filip = tempus_open.get_swimmer(name1)
    pb_sc = str(pbs_filip[TempusEvent.SC_50_FREESTYLE.name])
    pb_lc = str(pbs_filip[TempusEvent.LC_50_FREESTYLE.name])
    ecxel_sheet.save_one_swimmer("50m", name1, pb_sc, pb_lc, "50m Freestyle")

    pbs_hanna = tempus_open.get_swimmer(name2)
    pb_sc = str(pbs_hanna[TempusEvent.SC_100_FREESTYLE.name])
    pb_lc = str(pbs_hanna[TempusEvent.LC_100_FREESTYLE.name])
    ecxel_sheet.save_one_swimmer("100m", name2, pb_sc, pb_lc, "100m Freestyle")

    pbs_olivia = tempus_open.get_swimmer(name3)
    pb_sc = str(pbs_olivia[TempusEvent.SC_200_BUTTERFLY.name])
    pb_lc = str(pbs_olivia[TempusEvent.LC_200_BUTTERFLY.name])
    ecxel_sheet.save_one_swimmer("200m", name3, pb_sc, pb_lc, "200m Butterfly")

    time1 = time.time()

    print("Time to fetch 3 swimmers and add to heat list: " + str(time1 - time0))
