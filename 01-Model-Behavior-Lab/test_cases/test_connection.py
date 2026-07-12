import ollama

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": "Convert 45 psi to bar."
        }
    ],
    options={"temperature": 0}
)

print(response["message"]["content"])