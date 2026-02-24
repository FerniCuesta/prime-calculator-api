from src.backend.calculator import is_prime
from src.backend.calculator import get_next_prime


def test_is_prime_basic():
    # Test simple para validar que el pipeline funciona
    assert is_prime(13) is True
    assert is_prime(4) is False
