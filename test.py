if __name__ == "__main__":
	in_file = open("input.txt")
	out_file = open("output.txt", 'w')
	l = in_file.readline()[:-1]
	s = in_file.readline()[:-1]
	count = 0
	for i in range(len(l)):
		print(l[0:i])
		if i != 0 and l[i] in l[0:i]:
			continue
		for j in s:
			if l[i] == j:
				count += 1
	out_file.write(str(count))