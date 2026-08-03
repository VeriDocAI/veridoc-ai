"""Metric calculation utilities for evaluation of Vision-Language Models."""


def calculate_exact_match(prediction: str, reference: str) -> float:
    """Calculate if the prediction matches the reference exactly.

    Args:
        prediction: The predicted text string.
        reference: The ground-truth reference text string.

    Returns:
        1.0 if they match exactly (after whitespace stripping), 0.0 otherwise.
    """
    return 1.0 if prediction.strip() == reference.strip() else 0.0


def calculate_f1_score(prediction: str, reference: str) -> float:
    """Calculate the token-level F1 score between prediction and reference.

    Args:
        prediction: The predicted text string.
        reference: The ground-truth reference text string.

    Returns:
        The token-level F1 score (between 0.0 and 1.0).
    """
    pred_tokens = prediction.strip().lower().split()
    ref_tokens = reference.strip().lower().split()

    if not pred_tokens or not ref_tokens:
        return 1.0 if pred_tokens == ref_tokens else 0.0

    common = set(pred_tokens) & set(ref_tokens)
    num_same = sum(min(pred_tokens.count(w), ref_tokens.count(w)) for w in common)

    if num_same == 0:
        return 0.0

    precision = num_same / len(pred_tokens)
    recall = num_same / len(ref_tokens)
    return 2 * (precision * recall) / (precision + recall)
