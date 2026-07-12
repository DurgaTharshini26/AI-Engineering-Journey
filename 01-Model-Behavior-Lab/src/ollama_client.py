import ollama
import time


def get_response(model, prompt, temperature):
    """
    Send a prompt to an Ollama model and return
    the response along with latency.

    Args:
        model (str): Ollama model name.
        prompt (str): User prompt.
        temperature (float): Sampling temperature.

    Returns:
        dict
    """

    start_time = time.time()

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": temperature
        }
    )

    end_time = time.time()

    latency = round(end_time - start_time, 3)

    return {
        "response": response["message"]["content"],
        "latency": latency
    }