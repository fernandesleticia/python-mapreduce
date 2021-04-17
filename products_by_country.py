from mrjob.job import MRJob 
from mrjob.step import MRStep

class ProductsByCountry(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]
        
    def mapper(self, _, line):
        
    def reducer(self, key, values):
        
    def reducer2(self, key, values):
        
if __name__=='__main__':
    ProductsByCountry.run()