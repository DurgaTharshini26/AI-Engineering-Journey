from src.ollama_client import get_response

result = get_response(
    model="phi3:latest",
    prompt="Convert 45 psi to bar.",
    temperature=0
)

print(result)