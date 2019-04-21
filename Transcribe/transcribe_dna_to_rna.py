import re

string = 'GATGGAACTTGACTACGTAAATT'

transcribed = re.sub('T', 'U', string)

print(transcribed)