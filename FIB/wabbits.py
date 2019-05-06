


def wabbits(n, k):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return wabbits(n-1, k) + int(k)*int(wabbits(n-2, k))



if __name__ == '__main__':
	print(wabbits(29, 5))