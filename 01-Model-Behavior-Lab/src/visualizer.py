import os

import matplotlib.pyplot as plt
import pandas as pd


def create_charts(csv_path="results/results.csv"):

    os.makedirs("results/charts", exist_ok=True)

    df = pd.read_csv(csv_path)

    # Accuracy by Temperature

    accuracy = (
        df.groupby("temperature")["correct"]
        .mean()
        * 100
    )

    plt.figure(figsize=(6,4))
    accuracy.plot(kind="bar")
    plt.title("Accuracy by Temperature")
    plt.ylabel("Accuracy (%)")
    plt.tight_layout()
    plt.savefig("results/charts/accuracy_by_temperature.png")
    plt.close()

    # Average Latency

    latency = (
        df.groupby("temperature")["latency"]
        .mean()
    )

    plt.figure(figsize=(6,4))
    latency.plot(kind="bar")
    plt.title("Average Latency")
    plt.ylabel("Seconds")
    plt.tight_layout()
    plt.savefig("results/charts/latency_by_temperature.png")
    plt.close()

    # Correct vs Incorrect

    counts = df["correct"].value_counts()

    plt.figure(figsize=(5,5))
    counts.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.title("Correct vs Incorrect")
    plt.tight_layout()
    plt.savefig("results/charts/correct_vs_incorrect.png")
    plt.close()

    # Accuracy by Category

    category = (
        df.groupby("category")["correct"]
        .mean()
        * 100
    )

    plt.figure(figsize=(6,4))
    category.plot(kind="bar")
    plt.title("Accuracy by Category")
    plt.ylabel("Accuracy (%)")
    plt.tight_layout()
    plt.savefig("results/charts/accuracy_by_category.png")
    plt.close()

    print("Charts saved successfully!")