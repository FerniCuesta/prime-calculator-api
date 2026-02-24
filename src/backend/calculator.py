def is_prime(n):
    """Verifica si un número es primo (Lógica de Q1)"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
