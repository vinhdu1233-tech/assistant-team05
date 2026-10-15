
import importlib.util
from pathlib import Path

import pytest

W1_DIR = (
    Path(__file__).resolve().parents[1]
    / "members"
    / "vinhdu1233_tech"
    / "w1"
)


def load_module(name):
    path = W1_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_grades_empty_input():
    grades = load_module("grades")

    with pytest.raises(ValueError):
        grades.summary([])


def test_grades_single_score():
    grades = load_module("grades")

    result = grades.summary([8])
    assert result["min"] == 8
    assert result["max"] == 8
    assert result["mean"] == 8
    assert result["median"] == 8


def test_word_counter_alphabetical_tie():
    text_tools = load_module("text_tools")

    result = text_tools.top_k(
        "Banana apple banana apple",
        2
    )
    assert result == [("apple", 2), ("banana", 2)]


def test_thesis_boundary():
    rules = load_module("rules")

    assert rules.can_register_thesis(120, 2.0)
    assert not rules.can_register_thesis(119, 2.0)


def test_binary_search_empty_input():
    translate = load_module("translate")

    assert translate.binary_search([], 5) == -1


def test_timetable_empty_input():
    timetable = load_module("timetable")

    assert timetable.by_day([]) == {}
