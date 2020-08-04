def main(): 
    entrada=0
    while (entrada < 1) or (entrada > 65535):
        entrada=int(input("Digite obrigatoriamente um número entre 1 e 65.535:"))
    def binrio(entrada):
        binario=[]
        numero=entrada
        while numero != 0:
            if numero %2 == 1:
                binario.append(1)
                
            else:
                binario.append(0)
            numero=numero//2

        binario_invertido=binario[::-1]
        print("O número",entrada,"em binário é:")
        for i in range(0,len(binario),1):
            print(binario_invertido[i], end = '',)
    binrio(entrada)
    print(" \n")

    def hexadecimal(entrada):
        hexa=[]
        numero=entrada

        while numero!=0:
            if numero%16==10:
                hexa.append("A")
                
            elif numero%16==11:
                hexa.append("B")
                
            elif numero%16==12:
                hexa.append("C")
                
            elif numero%16==13:
                hexa.append("D")
                
            elif numero%16==14:
                hexa.append("E")
                
            elif numero%16==15:
                hexa.append("F")
                
            else:
                hexa.append(numero%16)
                
            numero=numero//16
        hexa_invertido=hexa[::-1]
        print("O número",entrada,"em hexadecimal é:")
        for i in range(0,len(hexa),1):
            print(hexa_invertido[i], end = '',)
        
    
    hexadecimal(entrada)
    print(" \n")
main()