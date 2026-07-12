import os
import pandas as pd

from src.loader import load_test_cases
from src.ollama_client import get_response
from src.evaluator import evaluate_response


def run_experiment():

    test_cases = load_test_cases("data/data.yaml")

    # REMOVE THIS AFTER TESTING
    test_cases = test_cases[:2]

    temperatures = [0, 0.5, 1.0]

    results = []

    for test_case in test_cases:

        for temperature in temperatures:

            for run in range(1, 4):

                print("=" * 60)
                print(f"Test Case ID : {test_case['id']}")
                print(f"Category     : {test_case['category']}")
                print(f"Difficulty   : {test_case['difficulty']}")
                print(f"Prompt       : {test_case['prompt']}")
                print(f"Expected     : {test_case['expected']}")
                print(f"Temperature  : {temperature}")
                print(f"Run          : {run}")

                result = get_response(
                    model="tinyllama:latest",
                    prompt=test_case["prompt"],
                    temperature=temperature
                )

                print("\nResponse:")
                print(result["response"])

                print(f"\nLatency : {result['latency']:.2f} seconds")

                evaluation = evaluate_response(
                    test_case["expected"],
                    result["response"]
                )

                print(f"Correct : {evaluation['correct']}")

                print("=" * 60)

                results.append({
                    "id": test_case["id"],
                    "category": test_case["category"],
                    "difficulty": test_case["difficulty"],
                    "prompt": test_case["prompt"],
                    "expected": test_case["expected"],
                    "temperature": temperature,
                    "run": run,
                    "response": result["response"],
                    "latency": result["latency"],
                    "expected_number": evaluation["expected_number"],
                    "response_number": evaluation["response_number"],
                    "correct": evaluation["correct"]
                })

    os.makedirs("results", exist_ok=True)

    df = pd.DataFrame(results)

    df.to_csv(
        "results/tinyllama_results.csv",
        index=False
    )

    print("\nExperiment Finished!")
    print(f"Total Results : {len(results)}")
    print("Results saved to results/results.csv")

    return results


if __name__ == "__main__":
    run_experiment()