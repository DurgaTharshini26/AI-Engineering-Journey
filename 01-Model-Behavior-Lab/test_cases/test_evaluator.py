from src.evaluator import evaluate_response

expected = "2.413 bar"

response1 = "The answer is approximately 2.413174 bar."
response2 = "The answer is 24.14 bar."

print(evaluate_response(expected, response1))
print(evaluate_response(expected, response2))