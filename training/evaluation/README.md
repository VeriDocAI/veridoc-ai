# VeriDoc AI — Evaluation Harness

This directory contains the scaffolding and utilities for evaluating Vision-Language Models (VLMs) and document intelligence pipelines.

## 📂 Core Components

*   **`evaluator.py`**: Defines [BaseEvaluator](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/training/evaluation/evaluator.py), which is the abstract base class specifying the evaluation lifecycle interface (`evaluate` and `log_results`).
*   **`metrics.py`**: Contains helper functions for standard NLP/VLM metrics (e.g. token-level [calculate_f1_score](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/training/evaluation/metrics.py#L16), exact match [calculate_exact_match](file:///c:/Users/Mohmmed%20Aarif/projects/Ai%20ComputerVision/veridoc-ai/training/evaluation/metrics.py#L4)).

## ⚙️ How to Implement a New Evaluator

All task-specific evaluators (e.g., `DocVQAEvaluator`, `IdentityVerificationEvaluator`) must inherit from `BaseEvaluator` and implement its abstract methods.

Example:

```python
from training.evaluation.evaluator import BaseEvaluator
from training.evaluation.metrics import calculate_f1_score, calculate_exact_match

class DocVQAEvaluator(BaseEvaluator):
    def evaluate(self, model, dataset) -> dict[str, float]:
        # Custom prediction loop
        predictions = model.generate(dataset)
        references = dataset.get_references()
        
        # Calculate scores
        f1 = sum(calculate_f1_score(p, r) for p, r in zip(predictions, references)) / len(predictions)
        em = sum(calculate_exact_match(p, r) for p, r in zip(predictions, references)) / len(predictions)
        
        return {"f1": f1, "exact_match": em}
        
    def log_results(self, results -> dict[str, float]) -> None:
        print(f"DocVQA F1: {results['f1']:.4f} | EM: {results['exact_match']:.4f}")
```
