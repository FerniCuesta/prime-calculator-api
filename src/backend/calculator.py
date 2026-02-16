def is_prime(n):
    """Verifica si un número es primo (Lógica de Q1)"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_next_prime(n: int) -> int:
    """Busca el próximo número primo (ESTE CÓDIGO TIENE UN ERROR)."""
    next_num = n  # ERROR: Debería ser n + 1, si n es 11, devolverá 11 en vez de 13
    while not is_prime(next_num):
        next_num += 1
    return next_num
