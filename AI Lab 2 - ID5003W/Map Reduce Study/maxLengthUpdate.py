
import os
import re
from mrjob.job import MRJob
from mrjob.step import MRStep

p = re.compile("[\n$]")
tmplen = 0

class MaxSentenceLength(MRJob):

    def mapper_init(self):
        self.current_sentence = ''

    def mapper(self, _, value):
        file_name, line = os.getenv('map_input_file'), ' '.join(value.encode("ascii", "ignore").decode().split())
        self.current_sentence = ''
        yield None, line

    def reducer(self, key, value):
        concat = str()
        flag = int()
        tmplen = 0
        longest_sent = str()
        longest_len = 0

        current_sentence =''
        
        for line in value:        
            concat = concat + ' ' + line    
            flag = flag + 1
            sentences = [n.strip() for n in p.split(concat) if n]
            sent_period = [x.strip() for x in re.split('[\.$]', sentences[0]) if x]
            for sent in sent_period:
                if len(sent)>tmplen:
                    longest_sent = sent
                    tmplen = len(longest_sent)
                else:
                    longest_sent = longest_sent
        yield longest_sent, len(longest_sent)

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MaxSentenceLength.run()


