from mrjob.job import MRJob
from mrjob.step import MRStep
import os

class FindMaxToken(MRJob):
     
    def mapper(self, _, line):
        filename = os.getenv('mapreduce_map_input_file')
        tokens = line.strip().split()
        file_name = filename.split('/')[-1]
        yield file_name, len(tokens)

    def reducer(self, key, values):
        yield key, f" file has token value of : {sum(values) }"

if __name__ == '__main__':
    FindMaxToken.run()

