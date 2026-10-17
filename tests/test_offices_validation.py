import csv
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "offices.csv"
)

REQUIRED_COLUMNS = {"name", "room", "hours"}


def load_offices():
    with DATA_FILE.open(
        newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        return reader.fieldnames, rows


def test_required_columns_exist():
    columns, _ = load_offices()
    assert columns is not None
    assert REQUIRED_COLUMNS.issubset(set(columns))


def test_required_values_are_not_empty():
    _, rows = load_offices()
    assert rows

    for row in rows:
        for column in REQUIRED_COLUMNS:
            assert row[column] is not None
            assert row[column].strip() != ""


def test_office_names_are_unique():
    _, rows = load_offices()
    names = [row["name"].strip().casefold()
             for row in rows]

    assert len(names) == len(set(names))


def test_valid_office_records_pass():
    columns, rows = load_offices()

    assert REQUIRED_COLUMNS.issubset(set(columns or []))
    assert rows
    for row in rows:
        assert all(
            row[column] is not None
            and row[column].strip()
            for column in REQUIRED_COLUMNS
        )