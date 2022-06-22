def factorial(n):
    
    if n == 1:
        return 1

    return n * factorial(n -1)

def main():
    n = int(input("Ingrese un número a calcular el factorial: "))
    respuesta = factorial(n)
    print(f'El factorial de {n} es {respuesta}')
    

if __name__ == '__main__':
    main()