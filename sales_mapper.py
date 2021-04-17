from mrjob.job import MRJob

class SalesMapper:
    def do_map(self, _, line):
        country, product = line.split(',')
        
        yield country, 
        
    
        
    