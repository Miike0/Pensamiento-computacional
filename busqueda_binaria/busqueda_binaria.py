def main():
    objetivo =  int(input('Ingresa un numero: '))
    
    respuesta = busqueda_binaria(objetivo)
    
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    

def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    
    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
            
        respuesta = (alto + bajo) / 2
        
    return respuesta


if __name__ == '__main__':
    main()