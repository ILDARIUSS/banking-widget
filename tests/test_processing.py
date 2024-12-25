import pytest

from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, get_mask_account, get_mask_card_number, mask_account_card


# --- Тесты для filter_by_state ---
@pytest.mark.parametrize(
    "data, state, expected",
    [
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}],
        ),
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}],
            "CANCELED",
            [{"id": 2, "state": "CANCELED"}],
        ),
        ([{"id": 1, "state": "EXECUTED"}], "FAILED", []),
    ],
)
def test_filter_by_state(data, state, expected):
    assert filter_by_state(data, state) == expected


# --- Тесты для sort_by_date ---
@pytest.mark.parametrize(
    "data, reverse, expected",
    [
        (
            [{"id": 1, "date": "2024-01-01"}, {"id": 2, "date": "2024-01-02"}],
            True,
            [{"id": 2, "date": "2024-01-02"}, {"id": 1, "date": "2024-01-01"}],
        ),
        (
            [{"id": 1, "date": "2024-01-01"}, {"id": 2, "date": "2024-01-02"}],
            False,
            [{"id": 1, "date": "2024-01-01"}, {"id": 2, "date": "2024-01-02"}],
        ),
    ],
)
def test_sort_by_date(data, reverse, expected):
    assert sort_by_date(data, reverse) == expected


def test_sort_by_date_invalid_date():
    with pytest.raises(ValueError):
        sort_by_date([{"id": 1, "date": "INVALID_DATE"}])


# --- Тесты для get_mask_card_number ---
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# --- Тесты для get_mask_account ---
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


# --- Тесты для mask_account_card ---
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


# --- Тесты для get_date ---
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-05-01T12:00:00.000000", "01.05.2022"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("INVALID_DATE")
