import re



line_re = r'^\>[a-z]+\_(\d{0,4})'
gc_re = r'^[ATGC]+$'

# data = []

# found = True
# count = 0
# for i in nucleotides:
# 	m = re.search(gc_re, i, flags=re.I)
# 	if m:
# 		count += len(m.group())
# 	else:
# 		if count:
# 			data.append(count)
# 			count = 0


def count(nucleotides):
	count = 0
	data1 = ''
	for i in nucleotides:
		m = re.search(gc_re, i, flags=re.I)
		if m:
			pass
		else:
			strings(data1)
			data1 = ''
		data1 += i
	strings(data1)

		
def strings(content):
	finalData = []
	realData = content.splitlines()
	dicti = {}
	count = 0
	for nucleo in realData:
		name = re.search(line_re, nucleo, flags=re.I)
		if name:
			dicti['name'] = name.group()
		count = re.search(gc_re, nucleo, flags=re.I)
		if count:
			length = str(count.group())
			print(length)
			# count += length
	gcContent = len(re.findall(r'[GC]', content))
	if gcContent:
		dicti['GC'] = gcContent
	# dicti['count'] = count
	print(dicti, "This is dicti")



if __name__ == '__main__':
	nucleotides = open('data.txt', 'r')
	count(nucleotides)

