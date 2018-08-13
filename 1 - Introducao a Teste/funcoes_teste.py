def eh_par(val:int) -> bool:
    '''

    Função que verifica se o numero é par

    Arg:
        - val: Valor de entrada do tipo inteiro
    '''
    try:
        return True if val % 2 == 0 else False
    except TypeError:
        return False