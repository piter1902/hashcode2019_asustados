import fileinput
import pic

def a_ver_esa_lectura(pics):
	i = 0
	for line in fileinput.input():
		print(line)
		separada = line.split(' ')		# Separamos por ' '
		print(separada.insert(0, [i]))
		pics.append(separada.insert(0, i)) # Le meto el id al principio
		i+=1 # No me dejaba hacer i++  >:(


# de "lista de listas de strings" a "lista de pics"
def ll_to_lp(input, output):
	for pic in input:
		for atrib in pic:
			a


if __name__ == "__main__":
	print ("Holi")
	pics = []
	a_ver_esa_lectura(pics)
	for pic in pics:
		print(pic)


