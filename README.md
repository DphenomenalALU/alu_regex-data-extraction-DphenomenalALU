
# Regex Data Extraction — Onboarding Hackaton

## Project Overview

This Python project demonstrates the use of Regular Expressions (Regex) for extracting various types of data from text input. It includes regex patterns for extracting:

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time formats (12-hour and 24-hour)
- HTML tags
- Hashtags
- Currency amounts

## Features

- Extracts various data types from a sample text:
  - Email addresses
  - URLs
  - Phone numbers (supports different formats)
  - Credit card numbers (supports different formats)
  - Time formats (supports both 12-hour and 24-hour formats)
  - HTML tags
  - Hashtags
  - Currency amounts
- Each type of data is extracted using a regular expression pattern, and the results are displayed clearly.
- Unit tests are included to verify the correctness of each regex pattern against different edge cases.

## Prerequisites

- Python 3.x
- Python `unittest` library (included in the standard library)
- No external dependencies are required.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DphenomenalALU/alu_regex-data-extraction-DphenomenalALU.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd alu_regex-data-extraction-DphenomenalALU
   ```

3. **Ensure Python 3.x is installed:**
   ```bash
   python3 --version
   ```

## File Structure

```
alu_regex-data-extraction-DphenomenalALU/
│
├── extractor.py        # Script that contains the regex patterns and extraction logic
├── tests.py            # Unit test file to validate regex patterns
└── README.md           # Project overview and setup instructions
```

## Usage

1. **Run the extraction script:**

   To run the script and see the data extraction in action, simply run the `extractor.py` file:

   ```bash
   python3 extractor.py
   ```

   This will output the extracted data, such as email addresses, URLs, phone numbers, etc., based on the sample text in the script.

2. **Run the unit tests:**

   To ensure the accuracy of your regex patterns, you can run the tests using the `unittest` module:

   ```bash
   python3 -m unittest tests.py
   ```

   This will run all the test cases and output the results, confirming whether the regex patterns are working as expected.

## How It Works

### Extractor Script (`extractor.py`)

1. **Regex Patterns:**
   The script uses Python's `re` library to define regex patterns for each data type. Each pattern is designed to match specific formats (e.g., email, URL, phone number).

2. **Text Processing:**
   The script processes a sample string (`sample_text`) that contains various data examples. It applies the regex patterns to find all matches and stores the results in corresponding variables.

3. **Output:**
   The extracted data is printed in a labeled format for easy reading.

### Unit Tests (`tests.py`)

1. **Test Setup:**
   The test file uses Python's built-in `unittest` module to define test cases for each regex pattern. Each test verifies that the regex correctly identifies valid data and ignores invalid data.

2. **Test Cases:**
   - **Emails:** Checks for various valid and invalid email formats.
   - **URLs:** Validates that only well-formed URLs are extracted.
   - **Phone Numbers:** Verifies multiple phone number formats.
   - **Credit Card Numbers:** Tests different formats of credit card numbers.
   - **Times:** Ensures correct extraction of time formats (12-hour and 24-hour).
   - **HTML Tags:** Validates the extraction of HTML tags.
   - **Hashtags:** Checks if hashtags are correctly identified.
   - **Currency Amounts:** Ensures proper extraction of currency amounts.

## Edge Cases Handled

- **Emails:**
  - Handles different valid email formats (e.g., with subdomains, aliases).
  - Ignores invalid email formats (e.g., missing "@" symbol).
  
- **URLs:**
  - Supports both HTTP and HTTPS URLs.
  - Ignores invalid URLs without a valid scheme or domain.

- **Phone Numbers:**
  - Supports various formats like `(123) 456-7890`, `123-456-7890`, and `123.456.7890`.
  - Handles international numbers and non-standard formats.

- **Credit Cards:**
  - Recognizes both spaced and hyphenated formats for credit card numbers.
  - Ignores numbers that don't match typical credit card patterns.

- **Times:**
  - Supports 24-hour (`HH:MM`) and 12-hour (`HH:MM AM/PM`) formats.
  - Ignores invalid times (e.g., 25:99 or 99:99 PM).

- **HTML Tags:**
  - Matches standard HTML tags.
  - Ignores malformed or unrecognized tags.

- **Hashtags:**
  - Correctly identifies hashtags in text.
  - Ignores non-hashtag words.

- **Currency Amounts:**
  - Recognizes dollar amounts with or without commas and decimal places.
  - Ignores non-currency values (e.g., "100dollars" or "€45.00").

## Contributing

If you wish to contribute to this project, feel free to fork the repository and submit pull requests. Please make sure to include unit tests for any new functionality or changes.

## Author

Developed by D'phenomenal 🚀