# TAREA 1 - MT7003
# ADRIAN OROZCO RIVERA- KARINA AZOFEIFA AMPIE


# FUNCION MULTIPLE_OP
# ENTRADA: NUMERO ENTERO
# SALIDA: ARREGLO DE NUMEROS
def multiple_op(x):
    Arreglo = []
    contador = 1
    factorial = 1
    # PRIMERO SE VERIFICA QUE EL TIPO DE DATO ES VALIDO
    if(type(x) != int):
        # CODIGO DE ERROR 805: TIPO DE DATO INVALIDO
        return 805
    else:
        Arreglo.append(x*x)
        Arreglo.append(pow(2, x))
        while (contador <= x):
            factorial = factorial * contador
            contador = contador + 1
        else:
            Arreglo.append(factorial)
            return Arreglo

# FUNCION VERIFY_ARRAY_OP
# ENTRADA: UN ARREGLO DE NUMEROS
# SALIDA: UN ARREGLO DE ARREGLOS


def verify_array_op(Arreglo):
    Resultado = []
    contador = 0
    while(contador < 3):
        # PARA CADA ELEMENTO DE LA LISTA SE VALIDA EL TIPO DE DATO
        if(type(Arreglo[contador]) != int):
            # CODIGO DE ERROR 508: DATO INVALIDO EN LISTA
            return 508
        else:
            Resultado.append(multiple_op(Arreglo[contador]))
            contador = contador + 1
    return Resultado
