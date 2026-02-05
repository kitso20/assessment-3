import pytest
from main import *
# ==================================================
# TESTS FOR QUESTION 1: Student Score Analyzer
# ==================================================

def test_student_score_analyzer_basic():
    data = {
        "Alice": [80, 90, 100],
        "Bob": [70, 75, 85]
    }

    result = student_score_analyzer(data)

    assert result["Alice"] == 90.00
    assert result["Bob"] == 76.67


def test_student_score_analyzer_single_score():
    data = {"Tom": [50]}
    assert student_score_analyzer(data) == {"Tom": 50.00}


# ==================================================
# TESTS FOR QUESTION 2: Sales Data Cleanup
# ==================================================

def test_clean_sales_data_mixed_values():
    sales = [10, -5, 0, 3.5, "20", 8]
    assert clean_sales_data(sales) == [10, 8]


def test_clean_sales_data_all_invalid():
    sales = [-1, 0, "abc", 2.5]
    assert clean_sales_data(sales) == []


# ==================================================
# TESTS FOR QUESTION 3: Recursive Countdown
# ==================================================

def test_recursive_countdown(capsys):
    recursive_countdown(3)
    captured = capsys.readouterr()

    assert captured.out == "3\n2\n1\n0\n"


# ==================================================
# TESTS FOR QUESTION 4: Nested List Flattener
# ==================================================

def test_flatten_list_simple():
    nested = [1, [2, 3], 4]
    assert flatten_list(nested) == [1, 2, 3, 4]


def test_flatten_list_deeply_nested():
    nested = [1, [2, [3, [4]]]]
    assert flatten_list(nested) == [1, 2, 3, 4]


def test_flatten_list_empty():
    assert flatten_list([]) == []


# ==================================================
# TESTS FOR QUESTION 5: Username Formatter
# ==================================================

def test_format_username_basic():
    assert format_username("John", "Smith") == "jsmith"


def test_format_username_with_spaces_and_symbols():
    assert format_username("Mary Jane", "O'Connor") == "moconnor"


# ==================================================
# TESTS FOR QUESTION 6: Email Validator
# ==================================================

def test_email_validator_mixed():
    emails = [
        "test@example.com",
        "invalid-email",
        "user@domain.co",
        "user@domain"
    ]

    result = email_validator(emails)

    assert "test@example.com" in result["valid"]
    assert "user@domain.co" in result["valid"]
    assert "invalid-email" in result["invalid"]
    assert "user@domain" in result["invalid"]


# ==================================================
# TESTS FOR QUESTION 7: Inventory Restock Alert
# ==================================================

def test_restock_alert_basic():
    inventory = {
        "apples": 5,
        "bananas": 2,
        "oranges": 10
    }

    assert restock_alert(inventory, 5) == ["bananas"]


def test_restock_alert_none_needed():
    inventory = {"milk": 10, "bread": 8}
    assert restock_alert(inventory, 5) == []


# ==================================================
# TESTS FOR QUESTION 8: Message Encoder
# ==================================================

def test_encode_message_basic():
    assert encode_message("hello") == "h3ll0"


def test_encode_message_uppercase_and_spaces():
    assert encode_message("I Love You") == "! L0v3 Y0^"


def test_encode_message_no_vowels():
    assert encode_message("rhythm") == "rhythm"
