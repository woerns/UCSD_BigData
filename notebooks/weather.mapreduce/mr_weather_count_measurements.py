"""
count the number of measurements of each type
"""
from mrjob.job import MRJob

elementType = 'TMAX'

class MRWeatherCountMeasurements(MRJob):

    def mapper(self, _, line):
        self.increment_counter('MrJob Counters','mapper',1)
        elements=line.split(',')
        measurements_per_line = 0
        if elements[1]==elementType:    
            for j in range(365):
                if isinstance(elements[j+3], basestring):
                    measurements_per_line += 1        
        if elements[0]!='station':
            yield(elements[0],measurements_per_line)
            
    def combiner(self, word, counts):
        self.increment_counter('Mrjob Counters','combiner',1)
        yield (word, sum(counts))

    def reducer(self, word, counts):
        self.increment_counter('MrJob Counters','reducer',1)
        yield (word, sum(counts))

if __name__ == '__main__':
    MRWeatherCountMeasurements.run()