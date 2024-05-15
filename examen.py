class Pilaa:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0
# Definición de la matriz
Matriz = {
    "<dirección postal>": {
         "<nombre_destinatario>": ["<personal> <apellido> [<trato>] <EOL>", "<personal> <apellido>"],
 "<dirección>": ["[<Acronimo>] <nombre_de_calle> <número de la casa>"],
         "<apartado postal>": ["<ciudad> ',' <código postal> <EOL>",
"<código postal> <ciudad> <EOL>"]
    },
    "<personal>": {
        "<primer nombre>": ["<nombre>"],
        "<inicial>": ["."]
    },
    "<nombre_de_calle>": {
     "<calle>": []
    },
    "<número de la casa>": {
     "(1-9)(0-9)*": [],
     "sn": [],
     "s/n": []
    }
}

def analisis_sintaxis(cadena):
 pila = Pilaa()
 pila.push("<dirección postal>")
 tokens = cadena.split()
 for token in tokens:
     while not pila.is_empty():
        X = pila.pop()
        if X in Matriz:
            if token in Matriz[X]:
                for produccion in reversed(Matriz[X][token]):
                    pila.push(produccion)
                break
            else:
                return False 
        elif X == token:
            break
        else:
            return False 
 if not pila.is_empty():
     return False 
 return True
# Casos sometido a prueba
casos_validos = [
 "B. Beto Gonzalez", 
 "Pedro Ruiz, 98765" 
]
caso_invalido = "B. Beto G." # Caso inválido
for caso in casos_validos:
 resultado = analisis_sintaxis(caso)
 if not resultado:
    print(f"Felicidades, La Sintaxis ha sido válida para: {caso}")
 else:
    print(f"La Sintaxis  ha sido inválida para: {caso}")
resultado_invalido = analisis_sintaxis(caso_invalido)
if not resultado_invalido:
 print(f"La Sintaxis ha sido inválida para: {caso_invalido}")
else:
 print(f"wow, La Sintaxis ha sido válida para: {caso_invalido}")