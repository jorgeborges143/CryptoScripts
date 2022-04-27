import sys

class reader:
    def __init__(self,file):
        self.file = file

    def get_address(self,line):
        line = line.split("name\"")[1]
        return line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17]+line[18]+line[19]+line[20]+line[21]+line[22]+line[23]+line[24]+line[25]+line[26]+line[27]+line[28]+line[29]+line[30]+line[31]+line[32]+line[33]

    def open_read(self):
        with open(self.file,"r",encoding="latin-1", errors = 'ignore') as a:
            for line in a.read().split("\n"):
                if "name\"" in line:
                    print(self.get_address(line))
                
reader(sys.argv[1]).open_read()
