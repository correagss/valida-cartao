# Validação de cartão

A ideia principal é detectar se o número do cartão é válido ou não através da teoria Luhn.

## Como funciona o código?
 - Inverte a sequência de dígitos do número do cartão.
 - Começando da direita (após a inversão, as posições ímpares são os segundos, quartos, sextos dígitos, etc.), multiplica cada dígito por 2.
 - Se o resultado da multiplicação for maior que 9, subtrai 9 desse resultado (ou, equivalentemente, some os dois dígitos do resultado).
 - O código soma todos os dígitos do número original (nas posições pares após a inversão) e os resultados das operações dos passos 2 e 3.
 - E por último, se o resultado da soma total for divisível por 10, o número do cartão é considerado válido. Caso contrário, é inválido.
