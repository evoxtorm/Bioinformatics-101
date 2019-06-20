import re

span = []


def find_motif(seq, sub_seq):
	s = seq
	t = sub_seq
	for i in range(0, len(s)-len(t)+1):
		if s[i:i+len(t)] == t:
			span.append(str(i+1))
	return span





if __name__ == '__main__':
	seq = "GATATATGCATATACTT"
	sub_seq = "ATAT"
	data = find_motif(seq, sub_seq)
	print(' '.join(data))




