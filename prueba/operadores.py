from sys import stdin


def is_number_prime(input):
    try:
        # Convertir el input a entero y eliminar espacios extra
        num = int(input.strip())
        if num <= 1:
            return "NO_ES_PRIMO"  # 0 y 1 no son primos
        elif num == 2:
            return "PRIMO"  # 2 es primo
        elif num % 2 == 0:
            return "NO_ES_PRIMO"  # Los números pares mayores que 2 no son primos

        # Comprobar si num es divisible por algún número impar desde 3 hasta su raíz cuadrada
        i = 3
        while i * i <= num:
            if num % i == 0:
                return "NO_ES_PRIMO"  # No es primo
            i += 2  # Pasamos al siguiente número impar

        return "PRIMO"  # Si no se encontró ningún divisor, es primo
    except ValueError:
        return "NO_ES_PRIMO"  # Si no se pudo convertir a entero, no es un número válido


# Leer de stdin línea por línea
for line in stdin:
    print(is_number_prime(line), end='')


numero = 17
resultado = is_number_prime(numero)
