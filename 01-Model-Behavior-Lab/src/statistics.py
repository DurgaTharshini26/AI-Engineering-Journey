import pandas as pd


def generate_statistics(csv_path="results/results.csv"):

    df = pd.read_csv(csv_path)

    total = len(df)

    correct = df["correct"].sum()

    incorrect = total - correct

    accuracy = (correct / total) * 100

    avg_latency = df["latency"].mean()

    print("=" * 50)
    print("EXPERIMENT SUMMARY")
    print("=" * 50)

    print(f"Total Tests      : {total}")
    print(f"Correct          : {correct}")
    print(f"Incorrect        : {incorrect}")
    print(f"Accuracy         : {accuracy:.2f}%")
    print(f"Average Latency  : {avg_latency:.2f} sec")

    print("\nAccuracy by Temperature")

    accuracy_temp = (
        df.groupby("temperature")["correct"]
        .mean()
        .mul(100)
    )

    print(accuracy_temp)

    print("\nAverage Latency by Temperature")

    latency_temp = (
        df.groupby("temperature")["latency"]
        .mean()
    )

    print(latency_temp)

    print("\nAccuracy by Category")

    category = (
        df.groupby("category")["correct"]
        .mean()
        .mul(100)
    )

    print(category)

    return df