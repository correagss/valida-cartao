def valida_cartao(numero: str) -> bool:

    if not (numero.isdigit() and 13 <= len(numero) <= 19):
        return False
    
    
    invertido = numero[::-1] #inverte
    impares = invertido[1::2]  #volta ao normal dps de invertido
    pares= invertido[0::2]
    #resultado= [int(caracteres) * 2 for caracteres in fatiamento]

    # terceiro= fazer a soma do resultado do fatiamento com o restante dos números do cartão
    # terceiro/1= fatiamento dos outros números e depois soma
    
    soma_dos_impares = sum(sum(int(x) for x in str(int(y)*2)) for y in impares)
    print(soma_dos_impares)
    soma_dos_pares = sum(int(y) for y in pares)
    print(soma_dos_pares)
    soma_total = soma_dos_impares + soma_dos_pares
    
    #quarto= o resultado precisa ser um múltiplo de 10 para que o número do cartão seja válido
    return soma_total % 10 ==0

cartoes = [
    "378282246310005",  
         
]

for cartao in cartoes:
    certo= "válido" if valida_cartao(cartao) else "inválido"
    print(f"Cartão {cartao}: {certo}")




