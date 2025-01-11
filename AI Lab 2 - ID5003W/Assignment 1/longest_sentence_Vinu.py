from mrjob.job import MRJob
from mrjob.step import MRStep
import re

p = re.compile("[\n$]")
tmplen = 0

class longest_sentenc(MRJob):
    
    def mapper_init(self):        
        self.concat = str()
        self.flag = int()
        self.tmplen = 0
        self.longest_sent = str()
        self.longest_len = 0

    def mapper(self, key, value): 
        file_name = os.getenv('mapreduce_map_input_file')
        value = ' '.join(value.encode("ascii", "ignore").decode().split())
        yield file_name, value
#         self.concat = self.concat + ' ' + value    
#         self.flag = self.flag + 1
#         sentences = [n.strip() for n in p.split(self.concat) if n]
#         sent_period = [x.strip() for x in re.split('[\.$]', sentences[0]) if x]
#         for sent in sent_period:
#             if len(sent)>self.tmplen:
#                 self.longest_sent = sent
#                 #self.longest_len = (len(sent))
#                 self.tmplen = len(self.longest_sent)
#             else:
#                 self.longest_sent = self.longest_sent
#                 #self.longest_len = self.longest_len
#                 #long_sent = self.longest_sent
#                 #long_len = self.longest_len
#         yield self.longest_sent, len(self.longest_sent)
    
    def reducer(self, key, value):
        yield key, value
    
    def steps(self):
        return [
                MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)
            ]     

if __name__ == "_main_":
    longest_sentenc.run()
