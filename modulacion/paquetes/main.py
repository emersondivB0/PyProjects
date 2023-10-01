import my_pack.aritmetica as a

def main():
    suma = a.suma(1,2,3,4,5)
    resta = a.resta(10,2)
    power = a.potencia(3,3)

    print("La suma es ", suma)
    print("La resta es ", resta)
    print("La potencia es ", power)

#Defino mi entry point
if __name__ == '__main__':
    main()

