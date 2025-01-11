
import os
from mrjob.job import MRJob
from mrjob.step import MRStep

class MaxSentenceLength(MRJob):

    def mapper_init(self):
        self.current_sentence = ''

    def mapper(self, _, value):
        file_name, line = os.getenv('map_input_file'), ' '.join(value.encode("ascii", "ignore").decode().split())
        self.current_sentence = ''
        yield None, line

    def reducer(self, key, value):
        yield key, list(value)
#         current_sentence =''
#         for line in value:
#             if '.' in line:      
#                 dot_split = line.split('.')
#                 current_sentence1 = current_sentence + ' ' if current_sentence else ''    
#                 current_sentence = '. '.join(dot_split[1:]) if len(dot_split) > 1 else ''
#                 yield len(max((current_sentence1 + ' ' + dot_split[0]).split('. '))), max((current_sentence1 + ' ' + dot_split[0]).split('. '))
#             else:
#                 current_sentence += ' ' + line if line != '' else '. ' + line
    
        
    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MaxSentenceLength.run()


