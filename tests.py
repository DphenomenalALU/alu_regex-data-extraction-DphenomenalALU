#!/usr/env/python3

import unittest
import re
from extractor import (
    email_pattern, url_pattern, phone_pattern,
    credit_card_pattern, time_pattern, html_pattern,
    hashtag_pattern, currency_pattern
)

class TestRegexPatterns(unittest.TestCase):
    """
    This class contains unit tests for regex patterns used in extracting specific data types.
    Each test method verifies the correctness of regex patterns in handling various formats and edge cases.
    """
    
    def test_emails(self):
        """Test extraction of valid and invalid email addresses."""
        emails = [
            "user@example.com", "firstname.lastname@company.co.uk", "user+alias@sub.example.net",
            "invalid-email@.com", "@missinguser.com", "user@com"
        ]
        expected = ["user@example.com", "firstname.lastname@company.co.uk", "user+alias@sub.example.net"]
        self.assertEqual(re.findall(email_pattern, ' '.join(emails)), expected)
    
    def test_urls(self):
        """Test extraction of valid and invalid URLs."""
        urls = [
            "https://www.example.com", "http://test.io/path?query=1", "ftp://invalid.com",
            "https://sub.example.org/page", "not a url", "www.missinghttp.com"
        ]
        expected = ["https://www.example.com", "http://test.io/path?query=1", "https://sub.example.org/page"]
        self.assertEqual(re.findall(url_pattern, ' '.join(urls)), expected)
    
    def test_phone_numbers(self):
        """Test extraction of phone numbers in different formats."""
        phones = [
            "(123) 456-7890", "123-456-7890", "123.456.7890", "+1-800-555-0199", "8005550199",
            "123456789", "abcd-1234-efgh"
        ]
        expected = ["(123) 456-7890", "123-456-7890", "123.456.7890", "+1-800-555-0199", "8005550199"]
        self.assertEqual(re.findall(phone_pattern, ' '.join(phones)), expected)
    
    def test_credit_cards(self):
        """Test extraction of valid credit card numbers."""
        cards = [
            "1234 5678 9012 3456", "1234-5678-9012-3456", "4111111111111111", "12345678901234"
        ]
        expected = ["1234 5678 9012 3456", "1234-5678-9012-3456", "4111111111111111"]
        self.assertEqual(re.findall(credit_card_pattern, ' '.join(cards)), expected)
    
    def test_times(self):
        """Test extraction of valid time formats (12-hour and 24-hour)."""
        times = ["14:30", "2:30 PM", "23:59", "12:00 AM", "25:99", "99:99 PM"]
        expected = ["14:30", "2:30 PM", "23:59", "12:00 AM"]
        self.assertEqual(re.findall(time_pattern, ' '.join(times)), expected)
    
    def test_html_tags(self):
        """Test extraction of HTML tags."""
        html = "<p>Hello</p> <div class='test'>Test</div> <invalidTag>Oops</invalidTag>"
        expected = ["<p>", "</p>", "<div class='test'>", "</div>", "<invalidTag>", "</invalidTag>"]
        self.assertEqual(re.findall(html_pattern, html), expected)
    
    def test_hashtags(self):
        """Test extraction of hashtags."""
        hashtags = "#example #ThisIsAHashtag #123HashTag #not a hashtag"
        expected = ["#example", "#ThisIsAHashtag", "#123HashTag"]
        self.assertEqual(re.findall(hashtag_pattern, hashtags), expected)
    
    def test_currency(self):
        """Test extraction of different currency formats."""
        currency = "$19.99 $1,234.56 €45.00 ¥5000 100dollars"
        expected = ["$19.99", "$1,234.56", "€45.00", "¥5000"]
        self.assertEqual(re.findall(currency_pattern, currency), expected)

if __name__ == "__main__":
    unittest.main()
