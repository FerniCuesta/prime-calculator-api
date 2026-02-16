from behave import given, when, then
from src.backend.calculator import is_prime


@given('the input number is {number:d}')
def step_given_input_number(context, number):
    # Guardamos el número en el objeto 'context' para usarlo en los siguientes pasos
    context.input_number = number


@when('I check the prime status')
def step_when_check_prime(context):
    # Ejecutamos la lógica de nuestra "Unit of Software" (UoSW)
    context.result = is_prime(context.input_number)


@then('the result should be "{expected_status}"')
def step_then_check_status(context, expected_status):
    actual_status = "Prime" if context.result else "Not Prime"
    assert actual_status == expected_status, f"Error: Se esperaba {expected_status} pero se obtuvo {actual_status}"


@then('the discount eligibility should be "{expected_eligibility}"')
def step_then_check_discount(context, expected_eligibility):
    # Lógica de negocio: si es primo, es elegible para descuento
    actual_eligibility = "Eligible" if context.result else "Not Eligible"
    assert actual_eligibility == expected_eligibility, f"Error: Se esperaba {expected_eligibility}"
