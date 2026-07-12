import os
import pandas as pd
import matplotlib.pyplot as plt


def compare_models():

    phi3 = pd.read_csv("results/results.csv")
    tiny = pd.read_csv("results/tinyllama_results.csv")

    comparison = pd.DataFrame({
        "Model": ["Phi-3", "TinyLlama"],
        "Accuracy (%)": [
            phi3["correct"].mean() * 100,
            tiny["correct"].mean() * 100
        ],
        "Average Latency (s)": [
            phi3["latency"].mean(),
            tiny["latency"].mean()
        ]
    })

    print("\nMODEL COMPARISON")
    print("=" * 50)
    print(comparison)

    os.makedirs("results/charts", exist_ok=True)

    # Accuracy Chart
    plt.figure(figsize=(6, 4))
    plt.bar(comparison["Model"], comparison["Accuracy (%)"])
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy (%)")
    plt.tight_layout()
    plt.savefig("results/charts/model_accuracy.png")
    plt.close()

    # Latency Chart
    plt.figure(figsize=(6, 4))
    plt.bar(comparison["Model"], comparison["Average Latency (s)"])
    plt.title("Average Latency Comparison")
    plt.ylabel("Seconds")
    plt.tight_layout()
    plt.savefig("results/charts/model_latency.png")
    plt.close()

    comparison.to_csv(
        "results/model_comparison.csv",
        index=False
    )

    print("\nComparison saved successfully!")