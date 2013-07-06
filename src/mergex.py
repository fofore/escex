import csv
import os
from optparse import OptionParser

debug = 1

class sortx(object):
    def __init__(self):
        self.get_opt()
        self.do()
        pass
    
    def opt_get(self):
        usage = "usage: %prog dst_file src_file dst_cmp dst_to src_cmp src_from\n     dst_cmp ... use letters of the column in excel: a,b,ab..."
        self.parser = OptionParser(usage)
        (self.options, self.args) = self.parser.parse_args()
        
        self.arg_len = len(self.args)
        if len(self.args) == 0:
            pass
        elif self.arg_len == 6:
            self.parser.error("please do -h for help information")
            self.destination = self.args[0]
            self.source = self.args[1]
            self.cmp_d = self.to_int(self.args[2])
            self.cp_d = self.to_int(self.args[3])
            self.cmp_s = self.to_int(self.args[4])
            self.cp_s = self.to_int(self.args[5])
            
        pass
    
    def get_drows(self):
        self.drows = []
        with open(self.destination) as dst:
            reader = csv.reader(dst)
            for row in reader:
                row.append("")
                self.drows.append(row)
                if debug: print row
        if debug: print self.drows
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
        if debug:
            print self.destination
            print self.source
        writer = csv.writer(open(self.destination, 'wb'))
        
        for row in self.drows:
            if debug: print row
            for row1 in csv.reader(open(self.source)):
                if debug: print row1
                if row[self.cmp_d-1] == row1[self.cmp_s-1]:
                    if debug: print "cp_d %d cp_s %d"%(self.cp_d, self.cp_s)
                    row[self.cp_d-1] = row1[self.cp_s - 1]
            pass
            writer.writerow(row)
        if debug: print "finish the cmp and sort"

class mergex(sortx):
    def __init__(self):
        self.cmp_d = 1
        self.cmp_s = 1
        self.get_file()
        self.do_all_col()
        pass
    
    def get_file(self):
        """get the file in the same folder"""
        self.filelist = [i for i in os.listdir(os.getcwd()) if "csv" in i]
        if debug: print "get the file list", self.filelist
        self.destination = self.filelist[0]
        self.source = self.filelist[1]
        pass
    
    def get_cp_d(self):
        max_len = self.get_col_max_count(self.destination)
        with open(self.destination) as dst:
            reader = csv.reader(dst)
            for row in reader:
                row.append("")
                if debug: print row
                self.cp_d = len(row)
        pass
    
    def fulfill(self, row, len):
        pass
    
    def get_col_max_count(self, file):
        with open(file) as it:
            max_len = 0
            reader = csv.reader(it)
            for row in reader:
                if max_len < len(row):
                    max_len = len(row)
            return max_len
        pass
    
    def do_all_col(self):
        len_s = self.get_col_max_count(self.source)
        len_d = self.get_col_max_count(self.destination)
        for self.cp_s in range(2, len_s+1):
            if debug: print "will copy the",self.cp_s
            self.get_cp_d()
            self.get_drows()
            self.do()
            
        pass
    
if __name__ == "__main__":
    #s = sortx()
    m = mergex()


            
