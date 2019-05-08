import re

nucleotides = open('data.txt', 'r')

line_re = r'^\>[a-z]+\_(\d{0,4})'
gc_re = r'^[ATGC]+$'

data = []

found = True
for i in nucleotides:
	count = 0
	m = re.search(gc_re, i, flags=re.I)
	if m:
		
		


