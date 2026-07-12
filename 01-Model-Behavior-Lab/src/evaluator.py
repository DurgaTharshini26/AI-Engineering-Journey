import re

def extract_number(text):

    if text is None:
        return None

    numbers = re.findall(r"\d+(?:\.\d+)?", str(text))

    if not numbers:
        return None

    return float(numbers[-1])


def is_correct(expected, response, tolerance=0.01):
    """
    Compare expected answer and model response.
    """

    expected_num = extract_number(expected)
    response_num = extract_number(response)

    if expected_num is None or response_num is None:
        return False

    return abs(expected_num - response_num) <= tolerance


def evaluate_response(expected, response):
    """
    Returns evaluation dictionary.
    """

    expected_num = extract_number(expected)
    response_num = extract_number(response)

    return {
        "expected_number": expected_num,
        "response_number": response_num,
        "correct": is_correct(expected, response)
    }