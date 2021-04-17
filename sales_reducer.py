from mrjob.job import MRJob

class SalesReducer:
    def do_reduce(self, key ,values):