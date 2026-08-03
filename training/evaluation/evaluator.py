"""Base evaluator definitions for Vision-Language Models in VeriDoc AI."""

from abc import ABC, abstractmethod
from typing import Any


class BaseEvaluator(ABC):
    """Abstract base class for all evaluation harnesses.

    All model/task-specific evaluation classes should inherit from this.
    """

    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize the evaluator with a configuration dictionary.

        Args:
            config: A dictionary containing evaluation parameters.
        """
        self.config = config

    @abstractmethod
    def evaluate(self, model: Any, dataset: Any) -> dict[str, float]:
        """Run evaluation of a model on a dataset.

        Args:
            model: The Vision-Language Model or model pipeline to evaluate.
            dataset: The dataset or data loader to evaluate against.

        Returns:
            A dictionary mapping metric names to their calculated scores.
        """
        pass

    @abstractmethod
    def log_results(self, results: dict[str, float]) -> None:
        """Log evaluation results to the console or an external service.

        Args:
            results: The metrics dictionary to log.
        """
        pass
