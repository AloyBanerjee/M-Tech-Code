
import os
from mrjob.job import MRJob
from mrjob.step import MRStep

class MaxSentenceLength(MRJob):

    def mapper_init(self):
        self.current_sentence = ''

    def mapper(self, _, value):
        file_name, line = os.getenv('mapreduce_map_input_file'), ' '.join(value.encode("ascii", "ignore").decode().split())
        if '.' in line:      
            dot_split = line.split('.')
            current_sentence = self.current_sentence + ' ' if self.current_sentence else ''    
            self.current_sentence = '. '.join(dot_split[1:]) if len(dot_split) > 1 else ''
            yield file_name, max((current_sentence + ' ' + dot_split[0]).split('. '))
        else:
            self.current_sentence += ' ' + line if line != '' else '. ' + line

    def reducer(self, key, values):
        sentence = max(list(values), key=len)
        sentence_length = len(sentence)
        yield key, f"Maximum length of sentence is {sentence_length} from {key} file. Longest Sentence of {key} file is :{sentence}"

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MaxSentenceLength.run()


