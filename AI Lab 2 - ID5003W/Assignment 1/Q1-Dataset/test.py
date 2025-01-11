import os
from mrjob.job import MRJob
from mrjob.step import MRStep

class MaxSentenceLength(MRJob):

    def mapper_init(self):
        self.current_sentence = ''

    def mapper(self, _, value):
        file_name = os.getenv('mapreduce_map_input_file')
        line = ' '.join(value.encode("ascii", "ignore").decode().split())
        #current_sentence = line
        #yield file_name, current_sentence
        
        if '.' in line:
            dot_split = line.split('.')
            current_sentence = '' + self.current_sentence
            if len(dot_split) > 1:
                self.current_sentence = '. '.join(dot_split[1:])
            else:
                self.current_sentence = ''
            yield file_name, max((current_sentence + ' ' + dot_split[0]).split('. '))
        else:
            if line != '':
                self.current_sentence += ' ' + line
            else:
                self.current_sentence += '. ' + line

    def reducer(self, key, value):
        sentence = max(list(value), key=len)
        sentence_length = len(sentence)
        yield key, f"Maximum length of sentence is {sentence_length} from {key} file. Longest Sentence of {key} file is :{sentence}"
        #yield key, list(value)

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MaxSentenceLength.run()

