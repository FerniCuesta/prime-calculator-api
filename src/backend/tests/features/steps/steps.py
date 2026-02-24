from behave import given, when, then
from src.backend.calculator import is_prime


@given('the input number is {number:d}')
def step_given_input_number(context, number):
    # Guardamos el número en el contexto
    context.input_number = number

# Caso 1: Verificar si el número es primo


@when('I check the prime status')
def step_when_check_prime(context):
    # Ejecutamos la lógica de nuestra UoSW
    context.result = is_prime(context.input_number)


@then('the result should be "{expected_status}"')
def step_then_check_status(context, expected_status):
    actual_status = "Prime" if context.result else "Not Prime"
    error_msg = f"Esperaba {expected_status} pero obtuvo {actual_status}"
    assert actual_status == expected_status, error_msg


@then('the discount eligibility should be "{expected_eligibility}"')
def step_then_check_discount(context, expected_eligibility):
    # Lógica: si es primo, es elegible
    actual_eligibility = "Eligible" if context.result else "Not Eligible"
    error_msg = f"Esperaba {expected_eligibility}"
    assert actual_eligibility == expected_eligibility, error_msg
