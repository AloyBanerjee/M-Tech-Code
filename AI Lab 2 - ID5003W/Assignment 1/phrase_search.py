from mrjob.job import MRJob
from mrjob.step import MRStep
import os

class FindPhrase(MRJob):
     
    def configure_args(self):
        super(FindPhrase, self).configure_args()
        self.add_passthru_arg('--phrase', type=str, help='Phrase to find in files')

    def mapper_init(self):
        self.phrase = self.options.phrase

    def mapper(self, _, line):
        filename = os.getenv('mapreduce_map_input_file')
        file_name = filename.split('/')[-1]
        if self.phrase in line:
            yield (self.phrase,file_name), 1

    def reducer(self, key, values): 
        yield key, f"{sum(values)} occurance of : {key[0]} phrase, is present in : {key[1]} file"

if __name__ == '__main__':
    FindPhrase.run()
