from tempus import TempusOpen

if __name__ == "__main__":
    tempus_open = TempusOpen()

    pbs_filip = tempus_open.get_swimmer("Filip")

    print("Personal best for Filip")
    print(pbs_filip)

    pbs_hanna = tempus_open.get_swimmer("Hanna")
    print(pbs_hanna)


