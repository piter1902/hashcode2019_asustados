import fileinput


if __name__ == "__main__":
	firstLine = True
	for line in fileinput.input():
		if firstLine:
			firstLine = False
			print(line[:len(line)-1])
		else:
			num = int(line)
			num -= 1
			print(str(num))
