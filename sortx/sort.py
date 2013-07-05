import csv
from optparse import OptionParser

class sortx(object):
    def __init__(self):
        usage = "usage: %prog dst_file src_file dst_cmp dst_to src_cmp src_from\n     dst_cmp ... use letters of the column in excel: a,b,ab..."
        self.parser = OptionParser(usage)
        (self.options, self.args) = self.parser.parse_args()
        
        if len(self.args) != 6:
            self.parser.error("please do -h for help information")
            
        self.destination = self.args[0]
        self.source = self.args[1]
        self.cmp_d = self.to_int(self.args[2])
        self.cp_d = self.to_int(self.args[3])
        self.cmp_s = self.to_int(self.args[4])
        self.cp_s = self.to_int(self.args[5])
        
        self.do()
        pass
  
    def to_int(self, letters):
        count = len(letters)
        intager = 0
        intager_of_a = 96
        numbers_of_letters = 26
        
        for char in letters.lower():
            intager += (ord(char) - intager_of_a)*(numbers_of_letters**(count-1))
            count -= 1
        return intager

    def do(self):
        reader = csv.reader(open(self.destination))
        writer = csv.writer(open("sortx.csv", 'wb'))
        
        for row in reader:
            for row1 in csv.reader(open(self.source)):
                if row[self.cmp_d-1] == row1[self.cmp_s-1]:
                    row[self.cp_d-1] = row1[self.cp_s - 1]
            writer.writerow(row)

if __name__ == "__main__":
    s = sortx()


            
