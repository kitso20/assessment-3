import re

# ==================================================
# QUESTION 1: Student Score Analyzer 🟢 EASY
# Topic: Data Structures (Dictionaries & Lists)
# ==================================================
# PURPOSE:
# Calculate the average score for each student.
#
# INPUT:
# student_scores (dict)
# - keys: student names (strings)
# - values: lists of integers representing test scores
#
# OUTPUT:
# A new dictionary where:
# - keys are student names
# - values are the average score rounded to 2 decimal places
#
def student_score_analyzer(student_scores):
    pass


# ==================================================
# QUESTION 2: Sales Data Cleanup 🟢 EASY
# Topic: Data Manipulation
# ==================================================
# PURPOSE:
# Filter out invalid sales entries.
#
# RULES:
# - Valid sales are positive integers only
# - Ignore negative numbers, zero, floats, and non-numeric values
#
# INPUT:
# sales_data (list) – mixed data types
#
# OUTPUT:
# A list containing only valid sales values
#
def clean_sales_data(sales_data):
    pass


# ==================================================
# QUESTION 3: Recursive Countdown 🟡 MEDIUM
# Topic: Recursion
# ==================================================
# PURPOSE:
# Print a countdown from a given number to zero using recursion.
#
# INPUT:
# n (integer) – starting number
#
# OUTPUT:
# None (prints each number on a new line)
#
# CONSTRAINTS:
# - Must use recursion
# - Loops are not allowed
#
def recursive_countdown(n):
    pass


# ==================================================
# QUESTION 4: Nested List Flattener 🟡 MEDIUM
# Topic: Recursion + Data Structures
# ==================================================
# PURPOSE:
# Convert a nested list of integers into a single flat list.
#
# INPUT:
# nested_list (list)
# - Contains integers or other lists
#
# OUTPUT:
# A flat list containing all integers in order
#
# EXAMPLE:
# [1, [2, [3, 4]], 5] → [1, 2, 3, 4, 5]
#
def flatten_list(nested_list):
    pass


# ==================================================
# QUESTION 5: Username Formatter 🟢 EASY
# Topic: String Formatting
# ==================================================
# PURPOSE:
# Generate a username from a person's name.
#
# RULES:
# - Username format: first letter of first name + last name
# - Convert to lowercase
# - Remove spaces and special characters
#
# INPUT:
# first_name (string)
# last_name (string)
#
# OUTPUT:
# A formatted username string
#
def format_username(first_name, last_name):
    pass


# ==================================================
# QUESTION 6: Email Validator 🟡 MEDIUM
# Topic: Strings + Data Manipulation
# ==================================================
# PURPOSE:
# Separate valid and invalid email addresses.
#
# INPUT:
# email_list (list of strings)
#
# OUTPUT:
# A dictionary with two keys:
# - "valid": list of valid email addresses
# - "invalid": list of invalid email addresses
#
# NOTE:
# - Use regular expressions
#
def email_validator(email_list):
    pass


# ==================================================
# QUESTION 7: Inventory Restock Alert 🟢 EASY
# Topic: Data Structures
# ==================================================
# PURPOSE:
# Identify products that need to be restocked.
#
# RULES:
# - A product needs restocking if its stock is below the threshold
#
# INPUT:
# inventory (dict)
# - keys: product names (strings)
# - values: stock counts (integers)
# threshold (integer)
#
# OUTPUT:
# A list of product names that need restocking
#
def restock_alert(inventory, threshold):
    pass


# ==================================================
# QUESTION 8: Message Encoder 🔵 MEDIUM+
# Topic: String Formatting
# ==================================================
# PURPOSE:
# Encode a message by replacing vowels with symbols.
#
# RULES:
# a → @
# e → 3
# i → !
# o → 0
# u → ^
#
# INPUT:
# message (string)
#
# OUTPUT:
# Encoded string
#
def encode_message(message):
    pass
