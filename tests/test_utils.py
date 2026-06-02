import pytest
from src.utils import count_words, truncate


def test_count_words_basic():
    assert count_words("hello world") == 2


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_multiple_spaces():
    assert count_words("one  two  three") == 3


def test_truncate_short_text():
    assert truncate("hello", 200) == "hello"


def test_truncate_long_text():
    text = "a" * 300
    result = truncate(text, 200)
    assert len(result) == 203  # 200 chars + "..."
    assert result.endswith("...")


def test_truncate_exact_boundary():
    text = "a" * 200
    assert truncate(text, 200) == text
