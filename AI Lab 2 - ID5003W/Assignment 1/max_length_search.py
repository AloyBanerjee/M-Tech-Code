from mrjob.job import MRJob
from mrjob.step import MRStep
import os
import re

class FindMaxSentenceLength(MRJob):
     
    def mapper(self, _, line):
        filename = os.getenv('mapreduce_map_input_file')
        sentences = re.split(r'(?<=[.])\s+', line)
        file_name = filename.split('/')[-1]
        for sentence in sentences:
            yield file_name, len(sentence)

    def reducer(self, key, values):
        yield key, f" file has sentence of maximum {max(values)} length"

if __name__ == '__main__':
    FindMaxSentenceLength.run()
