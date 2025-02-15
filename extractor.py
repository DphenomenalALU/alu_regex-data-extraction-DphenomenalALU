#!/usr/env/python3

import re

"""
This script extracts specific types of data from a given text input using Regular Expressions (Regex).
The extracted data includes:
    - Email addresses
    - URLs
    - Phone numbers
    - Credit card numbers
    - Time (12-hour and 24-hour formats)
    - HTML tags
    - Hashtags
    - Currency amounts

Regex patterns are used to find occurrences of these data types, and the results are displayed.
"""

# Sample text containing different data types for testing
sample_text = """
Email: user@example.com, firstname.lastname@company.co.uk
URL: https://www.example.com, https://subdomain.example.org/page
Phone: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Card: 1234 5678 9012 3456, 1234-5678-9012-3456
Time: 14:30, 2:30 PM
HTML: <p>Hello</p>, <div class="example">Content</div>, <img src="image.jpg" alt="description">
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56
"""

# Defining regex patterns for different data types

# Email addresses pattern (matches common email formats)
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  

# URL pattern (matches standard web URLs, supporting http and https)
url_pattern = r"https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?"

# Phone numbers pattern (matches different formats like (123) 456-7890, 123-456-7890, and 123.456.7890)
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

# Credit card numbers pattern (matches formats like 1234 5678 9012 3456 and 1234-5678-9012-3456)
credit_card_pattern = r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"

# Time pattern (matches 24-hour and 12-hour formats with AM/PM)
time_pattern = r"(?:\d{1,2}:\d{2}(?:\s?[APMapm]{2})?)"

# HTML tags pattern (matches any simple HTML tags)
html_pattern = r"<.*?>"

# Hashtags pattern (matches words preceded by #)
hashtag_pattern = r"#\w+"

# Currency amounts pattern (matches dollar values with optional commas and decimals)
currency_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

# Extract data using regex
emails = re.findall(email_pattern, sample_text)
urls = re.findall(url_pattern, sample_text)
phones = re.findall(phone_pattern, sample_text)
credit_cards = re.findall(credit_card_pattern, sample_text)
times = re.findall(time_pattern, sample_text)
html_tags = re.findall(html_pattern, sample_text)
hashtags = re.findall(hashtag_pattern, sample_text)
currency_amounts = re.findall(currency_pattern, sample_text)

# Display results with clear labels
print("Extracted Data:")
print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("Credit Card Numbers:", credit_cards)
print("Time Formats:", times)
print("HTML Tags:", html_tags)
print("Hashtags:", hashtags)
print("Currency Amounts:", currency_amounts)