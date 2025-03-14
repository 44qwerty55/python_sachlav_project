# TakeNote and FakeStoreApi Applications Test Automation Project

This project contains automated tests for the two applications using Playwright for load ui testing, Requests to load api testing and Allure for reporting.

## GitHub Repository

https://github.com/44qwerty55/python_sachlav_project

## Prerequisites

Before running the tests, make sure you have the following installed:

1. Node.js (Latest LTS version)
2. Java (Required for Allure reporting)
3. Allure Command Line Tool:
   ```bash
   npm install -g allure-commandline
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/44qwerty55/python_sachlav_project.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create .env file:
   ```bash
   BASE_URL_API=https://fakestoreapi.com
   BASE_URL_UI=https://takenote.dev/app
   DEFAULT_PASSWORD=m38rmF$
   DEFAULT_USER=johnd
   ```

## Running Tests

   all tests: 
   ```bash
   pytest --headed
   ```
   api tests:
   ```bash
   pytest -m api
   ```
   ui tests:
   ```bash
   pytest -m ui --headed
   ```

### Allure Report
1. Generate Allure report:
   ```bash
   allure generate .\allure-results --clean -o allure-report

   ```
2. Open Allure report:
   ```bash
   allure open --host 127.0.0.1 allure-report
   ```

You can view the latest Allure report on GitHub Pages:
[GitHub Pages Allure Report](https://44qwerty55.github.io/python_sachlav_project/5/index.html)

## GitHub Actions

The project uses GitHub Actions for continuous integration. You can view the CI/CD pipeline and test results at:
[GitHub Actions Dashboard](https://github.com/44qwerty55/python_sachlav_project/actions)

The CI pipeline runs automated tests on every push and pull request to ensure code quality and functionality.

## Project Structure

- `/tests/api/` - API test files
- `/tests/ui/` - UI test files
- `/data/api/` - API Test Framework (helpers, model, requests, constants)
- `/data/ui/` - UI Test Framework (helpers, model, pages, constants)
- `/allure-results/` - Raw test results for Allure reporting
