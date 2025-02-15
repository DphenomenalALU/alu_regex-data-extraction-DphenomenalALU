# Regex Data Extraction — Onboarding Hackaton

## Project Overview
This project is a powerful regex-based data extraction system designed to parse structured information from large volumes of text. The application extracts the following types of data:

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time (12-hour and 24-hour formats)
- HTML tags
- Hashtags
- Currency amounts

## Features
- **Accurate regex patterns** to identify and extract key data points.
- **Edge-case handling** to ensure the extractor works when the input is malformed.
- **Unit tests** to validate pattern correctness.
- **Structured and well-documented codebase** for clarity and maintainability.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/DphenomenalALU/alu_regex-data-extraction-DphenomenalALU.git
   ```
2. Navigate into the project directory:
   ```sh
   cd alu_regex-data-extraction-DphenomenalALU
   ```

## Usage
To extract data, modify and run `extractor.py`:
```sh
python extractor.py
```

## Running Tests
To validate the regex patterns, execute:
```sh
python tests.py
```
The test suite (`tests.py`) includes sample inputs and expected outputs to demonstrate pattern accuracy.

## Repository Structure
```
├── extractor.py        # Main script containing regex patterns
├── tests.py            # Unit tests for regex validation
└── README.md           # Project documentation
```

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit changes with meaningful messages.
4. Submit a pull request for review.

## Author
Developed by D'phenomenal 🚀

