import fileinput
from pic import Pic
from slide import Slide
from slideshowAlgoritmo2 import slideshow


def a_ver_esa_lectura(pics):
    for line in fileinput.input():
        if not fileinput.isfirstline(): #a tomar viento la primera linea
            # print(line)
            separada = line[:len(line)-1].split(' ') # Separamos por ' '
            # print(separada)
            fila = fileinput.lineno()   # n de fila
            picLeido = Pic(fila-1, separada) # construyo el leido...
            pics.append(picLeido) # y lo anado a la lista
            
# devuelve el pic de verticales con menor interseccion de tags con elto; y lo elimina de
# la lista
def maximizarTags(elto1: Pic, verticales: list) -> Pic:
    # ESTO ESTA MU FEO  
    minIntersec = 10000 # vergonzoso
    encontrado = False
    elto2 = verticales[0] # asignacion de mas
    longLista = len(verticales) 
    i=0 # uf
    while (not encontrado) and (i<longLista): #esto no es muy pythonesco pero vamos
        elto2 = verticales[i]
        lIntersec = len(elto1.tags() & elto2.tags()) # nº de tags compartidos (interseccion)
        if lIntersec < minIntersec:
            minIntersec = lIntersec
            if lIntersec == 0: # es el minimo posible, dejamos de buscar
                encontrado = True
        i += 1 # cries in python
    return verticales.pop(i-1) # devolvemos el elto (y lo quitamos de verticales)


def unirVerticales(slides: list, picsV: list):
    while(picsV): # no esta vacia
        elto1 = picsV.pop(0)
        elto2 = maximizarTags(elto1, picsV) # no tengo en cuenta verticales impares...
        #No existen las verticales impares. Mira que bien
        slides.append(Slide(elto1, elto2))


#meencantacopiarypegarcodigo
def estoTeSacaUnaListaDeSlides(slides):
    picsVerticales = []
    for line in fileinput.input():
        if not fileinput.isfirstline(): #a tomar viento la primera linea
            separada = line[:len(line)-1].split(' ') # Separamos por ' '
            fila = fileinput.lineno() # n de fila
            picLeido = Pic(fila-2, separada) # construyo el leido...
            if (picLeido.orientation()): # es vertical, pa la lista de verticales
                picsVerticales.append(picLeido)
            else: # no lo es, a los slides directo
                slides.append(Slide(picLeido)) 
    # unimos lo verticales a los slides, maximizando tags
    unirVerticales(slides, picsVerticales) 





if __name__ == "__main__":
    #print ("Holi")
    # pics = []

    #ejemploPic = Pic(1, ['la', 'fsahn', 'oaga'])


    # a_ver_esa_lectura(pics)
    # for pic in pics: 
    #   print(pic) # no tenemos funcion que los muestre pero weno


    slides = []
    estoTeSacaUnaListaDeSlides(slides)
    #slidesh = slideshow(slides)
    slidesh = slideshow(slides)
    # slidesh = slidesh.ordenarMax()
    # slidesh = slidesh.ordenarEstadisticamente()
    slidesh.escribir()
