class Helper:
    @staticmethod
    def read_processes(processes_file):
        try:
            fl = open(processes_file, "r")
        except:
            print("Could not open file")
        procs = [x.split(", ")[:-1] for x in fl.readlines()]
        fl.close()
        return procs

    @staticmethod
    def read_files(files_file):
        try:
            fl = open(files_file, "r")
        except:
            print("Could not open file")
        files = [fl.readline()[:-1], fl.readline()[:-1]]
        files += [x.split(", ")[:-1] for x in fl.readlines()]
        fl.close()
        return files
