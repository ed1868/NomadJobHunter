# Nomad LinkedIn Job Application Automation Script

## Overview
This Python script, powered by Selenium, automates the process of applying for jobs on LinkedIn. It logs into your LinkedIn account, browses job listings, and automatically applies to the jobs while tracking the applications in a CSV file.

## Features
- Automated LinkedIn sign-in.
- Navigates and applies to job listings on LinkedIn.
- Extracts details such as job title, company name, and job description.
- Submits job applications and navigates different application forms.
- Records and tracks job applications in a CSV file.
- Handles pagination to apply to jobs across multiple pages.

## Prerequisites
- Python 3
- Selenium WebDriver
- ChromeDriver compatible with the installed version of Chrome
- Required Python packages: `selenium`, `os`, `csv`, `time`, `dotenv`

## Installation
1. Clone this repository or download the script.
2. Install the necessary Python packages:
   ```bash
   pip install selenium python-dotenv
3. Ensure ChromeDriver is installed and its path is set in the .env file

## Configuration

1. Create a .env file in the script directory with the following variables:
   ```bash
   ACCOUNT_EMAIL: Your LinkedIn account email.
   ACCOUNT_PASSWORD: Your LinkedIn password.
   PHONE: Your phone number for job applications.
   URL: URL to the LinkedIn job listings page.
   CHROMEDRIVER_PATH: Path to your ChromeDriver executable.

## Usage

- To run the script, execute the following command:
   ```bash
   python nomad_agent.py

## CSV Format

- The script generates a nomadJobHunter_applications.csv file with the following columns:
    1. Job Title
    2. Company Name
    3. Job Details
    4. Date Applied
    5. Status