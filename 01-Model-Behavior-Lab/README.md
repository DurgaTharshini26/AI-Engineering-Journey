# Model Behavior Lab

## Overview

This project evaluates the behavior of local Large Language Models (LLMs) using Ollama.

It benchmarks models on multiple prompts, evaluates correctness, measures latency, and compares different models.

## Features

- YAML-based test cases
- Automated experiment runner
- Response evaluation
- Accuracy calculation
- Latency measurement
- CSV result generation
- Statistical analysis
- Visualization using Matplotlib
- Model comparison (Phi-3 vs TinyLlama)

## Models Evaluated

- Phi-3
- TinyLlama

## Technologies Used

- Python
- Ollama
- Pandas
- Matplotlib
- YAML

## Project Structure

```
01-Model-Behavior-Lab
│
├── data/
├── results/
├── src/
├── test_cases/
└── README.md
```

## How to Run

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run:

```bash
python -m test_cases.test_runner
```

Generate statistics:

```bash
python -m test_cases.test_statistics
```

Generate charts:

```bash
python -m test_cases.test_visualizer
```

Compare models:

```bash
python -m test_cases.test_model_comparison
```

## Results

- Accuracy comparison
- Latency comparison
- Charts
- CSV reports

## Author

Durga Tharshini