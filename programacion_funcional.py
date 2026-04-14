
def saluda(nombre):
    print( "Hola " + nombre + "!" )

saluda("Iván")
saluda("Menchu")

nombre = "Ivan"
    # Asigno la variable nombre al valor "Ivan"
        #       "Ivan". Crear un dato de tipo str en RAM con el valor "Ivan"... en algún lado de la RAM (npi dónde).
                        # La RAM Es como un cuaderno de cuadrícula
        #       nombre. Creo una variable llamada nombre
                        # Una variable es como un postit... en el que escribo "nombre"
        #       =       Asignar la variable al dato.
                        # Pego el postit en la RAM, apuntando al dato "Ivan"
nombre = "Menchu"
        #       "Menchu". Crear un dato de tipo str en RAM con el valor "Menchu"... en algún lado de la RAM (npi dónde).
                 # Es en el mismo sitio que don de estaba "Iván" o en otro?     En otro
                 # En este momento tenemos 2 objetos de tipos String en RAM: "Menchu" y "Ivan"
                 # nombre = Muevo el postit que tenía pegado a "Ivan" y lo pego apuntando a "Menchu"

mivariable = saluda
    # Lo que tengo es mi variable apuntando a una función.
mivariable("Federico") # Llamo a la función a través de la variable, y le paso el argumento "Iván"


def imprimir_saludo(funcion_generadora_de_saludo, nombre):
    saludo = funcion_generadora_de_saludo(nombre)
    print(saludo)


def saluda(nombre):
    saludo= "Hola " + nombre + "!"
    print( saludo)

def generar_saludo_formal(nombre):
    return "Buenos días, " + nombre + "!"

def generar_saludo_informal(nombre):
    return "Qué pasa, " + nombre + "!"

imprimir_saludo(generar_saludo_formal,"Iván")
imprimir_saludo(generar_saludo_informal, "Iván")