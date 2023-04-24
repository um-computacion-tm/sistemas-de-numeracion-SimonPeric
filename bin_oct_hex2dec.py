def bin2dec(bin):
    bin = str(bin) #str: Convierte lo ingresado a un caracter
    decimal = 0
    potencia = 0
    for i in range(len(bin)-1,-1,-1):
        if bin[i] == "1":
            decimal += 2**potencia
        potencia += 1
    decimal = str(decimal)
    return decimal 

def oct2dec(oct):
    oct = str(oct)
    long = len(oct)
    exp = long-1
    resultado = 0
    for i in range(long):
        resultado = (8**exp*int(oct[i]))+resultado  #oct[i]: Representa cada uno de los numeros del numero a convertir
        #print(f'e={exp} oct={oct[i]}') # Sirve para ver que pasa durante el for con las var
        exp = exp-1
    return resultado

def hex2dec(hex):
    hex = str(hex)
    long = len(hex)
    exp = long-1
    resultado = 0
    for i in range(long):
        
        if hex[i]=="A":
            valor=10
        elif hex[i]=="B":
            valor=11
        elif hex[i]=="C":
            valor=12
        elif hex[i]=="D":
            valor=13
        elif hex[i]=="E":
            valor=14
        elif hex[i]=="F":
            valor=15
        else: 
            valor=int(hex[i])
        
        resultado = (16**exp*valor)+resultado  
        exp = exp-1
    return resultado
print(hex2dec("FC2"))
