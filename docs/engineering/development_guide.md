# 🛠️ VeriDoc AI — Development Guide

Welcome! This guide outlines the setup instructions, coding standards, testing workflows, and machine learning development conventions for contributing to VeriDoc AI.

---

## 🚀 Getting Started

### Prerequisites
*   **Python**: 3.12 or newer.
*   **Git**: For source control.
*   **uv**: Our package manager of choice (version 0.3.0+ recommended).

### Environment Setup

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/VeriDocAI/veridoc-ai.git
    cd veridoc-ai
    ```

2.  **Synchronize Dependencies**:
    `uv` automatically handles creating the virtual environment (`.venv`) and synchronizing the pinned lockfile (`uv.lock`):
    ```bash
    uv sync
    ```

3.  **Activate Environment**:
    *   **Windows (PowerShell)**:
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    *   **macOS / Linux**:
        ```bash
        source .venv/bin/activate
        ```

---

## 🎨 Coding Standards & Code Quality

We enforce high-quality code standards via linter gates. Code configurations are defined in [ruff.toml](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/ruff.toml) and checked in CI pipelines.

### Linting & Formatting

*   **Ruff** is used for both linting and formatting. Run the following checks locally before committing:

    ```bash
    # Run linter check
    uv run ruff check .

    # Automatically fix fixable violations
    uv run ruff check --fix .

    # Check formatting
    uv run ruff format --check .

    # Apply formatting
    uv run ruff format .
    ```

### Code Style Requirements
*   **Static Typing**: Type hints are required for all function signatures and public APIs. Avoid the use of `Any` unless strictly necessary.
*   **Docstrings**: All modules, classes, and public functions must have docstrings following the Google Style Python guide.
*   **Imports**: Imports are sorted automatically by Ruff.

---

## 🧪 Testing Framework

We use `pytest` for all levels of testing. The test suite is located in the [tests/](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/tests) directory.

### Running Tests

```bash
# Run all unit tests
uv run pytest

# Run tests and output a coverage report
uv run pytest --cov=training --cov=models --cov-report=xml
```

### Writing New Tests
*   **Unit Tests**: Put unit tests under [tests/unit/](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/tests/unit).
*   **Naming Convention**: Match the folder structure under code layers (e.g. tests for `training/evaluation/metrics.py` go in `tests/unit/training/test_metrics.py`).
*   **Mocking**: Use `unittest.mock` or pytest fixtures to mock out external calls, GPU tensor operations, and weight downloading to keep unit tests fast and deterministic.

---

## 📊 Dataset Conventions

To ensure reproducible machine learning experiments, all datasets must be registered and described using a standardized manifest structure.

### Manifest Schema
Datasets must include a `manifest.json` file conforming to the [schema.json](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/data/manifests/schema.json) structure. A template is available in [template.json](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/data/manifests/template.json).

Required properties include:
*   `name`: Unique string name of the dataset.
*   `version`: Semantic version (e.g., `1.0.0`).
*   `task`: Type of task (e.g., `document_understanding`, `ocr`).
*   `splits`: Maps dataset split names (e.g., `train`, `validation`, `test`) to count integers.

### Folder Layout
Keep datasets organized in the `data/` subdirectory:
*   `raw/`: Immutable, original raw images/annotations.
*   `interim/`: Intermediate representations during transformations.
*   `processed/`: Final serialized tensors/tokens ready for model ingestion.

---

## 🧠 ML Workflows & Extensions

### 1. Adding a New Metric
To add an evaluation metric:
1.  Define the metric function in [metrics.py](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/training/evaluation/metrics.py). Ensure the function is typed and fully documented.
2.  Add corresponding unit tests in [test_metrics.py](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/tests/unit/training/test_metrics.py).
3.  Register the metric or import it in your task-specific evaluator.

### 2. Creating a Custom Evaluator
To write a task-specific evaluation harness:
1.  Subclass the abstract base class [BaseEvaluator](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/training/evaluation/evaluator.py).
2.  Implement the abstract methods:
    *   `evaluate(self, model, dataset)`: Executes inferences on the dataset and returns a dictionary of metrics.
    *   `log_results(self, results)`: Handles console output or integration with Weights & Biases (W&B).
