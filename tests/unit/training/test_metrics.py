"""Tests for VLM evaluation metrics."""

import pytest

from training.evaluation.metrics import calculate_exact_match, calculate_f1_score


def test_calculate_exact_match() -> None:
    """Verify exact match metric on different string combinations."""
    assert calculate_exact_match("hello", "hello") == 1.0
    assert calculate_exact_match("  hello  ", "hello") == 1.0
    assert calculate_exact_match("hello", "world") == 0.0


def test_calculate_f1_score() -> None:
    """Verify token-level F1 score calculation."""
    assert calculate_f1_score("hello world", "hello world") == 1.0
    assert calculate_f1_score("hello", "") == 0.0
    assert calculate_f1_score("", "") == 1.0
    assert calculate_f1_score("hello", "world") == 0.0
    # Common F1 assertion
    f1_partial = calculate_f1_score("hello world", "hello")
    assert f1_partial == pytest.approx(0.666666, abs=1e-4)
