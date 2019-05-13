import re

nucleotides = open('data.txt', 'r')

line_re = r'^\>[a-z]+\_(\d{0,4})'
gc_re = r'^[ATGC]+$'

data = []

found = True
count = 0
for i in nucleotides:
	m = re.search(gc_re, i, flags=re.I)
	if m:
		count += len(m.group())
	else:
		if count:
			data.append(count)
			count = 0


def count(nucleotides):
	count = 0
	for i in nucleotides:
		m = re.search(line_re, i, flags=re.I)
		if m:
			

		


