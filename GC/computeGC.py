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
	final_data = []
	for i in nucleotides:
		m = re.search(gc_re, i, flags=re.I)
		if m:
			pass
		else:
			dictionary = strings(data1)
			if dictionary not in final_data:
				if dictionary:
					final_data.append(dictionary)
			data1 = ''
		data1 += i
	dictionary = strings(data1)
	if dictionary not in final_data:
		final_data.append(dictionary)
	sorted_data = sorted(final_data, key = lambda i: i['gc_percent'],reverse=True)
	print(sorted_data)
	print(sorted_data[0]['name'])
	print(sorted_data[0]['gc_percent'])

		
def strings(content):
	finalData = []
	realData = content.splitlines()
	dicti = {}
	count1 = 0
	for nucleo in realData:
		name = re.search(line_re, nucleo, flags=re.I)
		if name:
			dicti['name'] = name.group()
		count = re.search(gc_re, nucleo, flags=re.I)
		if count:
			length = int(len(str(count.group())))
			count1 += length
	gcContent = len(re.findall(r'[GC]', content))
	if gcContent:
		dicti['GC'] = gcContent
		gc_percent = (gcContent / count1) * 100
		dicti['gc_percent'] = gc_percent
	return dicti



if __name__ == '__main__':
	nucleotides = open('data.txt', 'r')
	count(nucleotides)

