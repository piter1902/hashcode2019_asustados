import fileinput


if __name__ == "__main__":
	firstLine = True

	for line in fileinput.input():
		if firstLine:
			firstLine = False
			print(line[:len(line)-1])
		else:
			sp = line.split()
			if len(sp) == 2:
				n1 = str(int(sp[0])-1)
				n2 = str(int(sp[1])-1)
				print(n1 + " " + n2)
			else:
				n1 = str(int(sp[0])-1)
				print(n1)
