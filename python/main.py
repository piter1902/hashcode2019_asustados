import fileinput
import pic

def a_ver_esa_lectura(pics):
	for line in fileinput.input():
		if not fileinput.isfirstline(): #a tomar viento la primera linea
			print(line)
			separada = line[:len(line)-1].split(' ')		# Separamos por ' '
			print(separada)
			fila = fileinput.lineno() #nº de fila
			picLeido = Pic(fila-1, separada) # construyo el leido...
			pics.append(picLeido) # y lo añado a la lista
			




if __name__ == "__main__":
	print ("Holi")
	pics = []
	a_ver_esa_lectura(pics)
	for pic in pics:
		print(pic)


