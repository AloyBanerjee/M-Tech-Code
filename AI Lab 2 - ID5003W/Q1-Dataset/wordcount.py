from mrjob.job import MRJob
import re

class WordCount(MRJob):
    def mapper(self, key, value):
        words = [s.strip() for s in re.split('[\s]', value) if s]
        for word in words:
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
     WordCount.run()
