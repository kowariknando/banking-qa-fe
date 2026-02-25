# QA Automation Task - Banking Project

This repository contains the automated tests for the XYZ Bank application, developed as part of the QA Engineer technical task.

## Approach & Architecture

To ensure the tests are **reliable, maintainable, and scalable**, I implemented the **Page Object Model (POM)** design pattern using **Python** and **Playwright** (with `pytest`). 

* UI selectors and page interactions are separated from the test logic. If the UI changes, updates are only needed in the `pages/` directory.
*  The `BasePage` class handles common interactions. 
* Instead of static sleeps, I used Playwright's auto-waiting mechanisms and explicit waits (e.g., `page.get_by_text().wait_for()`) to handle UI state transitions (like waiting for the withdrawal form to fully render before interacting). This prevents race conditions.

*Note on application code:* During the inspection, I noticed a typo in the application's source code for the withdrawal button (`ng-click='withdrawl()'`). The selector in `account_page.py` uses this exact spelling to interact successfully with the current state of the DOM.

## Prerequisites
* Python 3.8+
* pip

## Setup Instructions

1. **Clone/Extract the project** and navigate to the project directory.
2. **Create a virtual environment:**
   `python -m venv venv`
3. **Activate the virtual environment:**
   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
4. **Install dependencies:**
   `pip install pytest-playwright`
5. **Install Playwright browsers:**
   `playwright install`
6. **Parallel Execution**
    To significantly reduce test execution time, you can run tests in parallel using multiple browser windows at the same time. This project uses `pytest-xdist` for this purpose.
    Make sure to install it first if you haven't:
    `pip install pytest-xdist`
7. **Test report generation**
   This project uses `pytest-html` to generate clean and shareable HTML test reports.
   Ensure you have the reporting plugin installed:
   `pip install pytest-html`

## Running the Tests

To run the tests in headless mode (background):
`pytest tests/`

To run the tests in headed mode (visible browser):
`pytest tests/ --headed`

Run the 3 tests simultaneously (using 3 workers):
`pytest tests/ -n 3 --headed`

To execute the test suite and generate a standalone HTML report, run the following command in your terminal:
`pytest --html=report.html --self-contained-html`

To run tests and capture a trace only if a test fails, use:
`pytest --tracing=retain-on-failure`

To view the generated trace file, run:
`playwright show-trace test-results/<test-folder-name>/trace.zip`



## Debugging
**Slow Motion (Visual Debugging)**
If you want to watch the tests execute but find Playwright is too fast, you can slow down each action (e.g., by 1000 milliseconds):
`pytest tests/ --headed --slowmo 1000`

**Step-by-Step Debugging (Playwright Inspector)**
To run your tests in debug mode with the Playwright Inspector tool, you need to set the `PWDEBUG` environment variable to `1` and run pytest with the `-s` flag to prevent output capturing:

**To enable Debug Mode:**

**Windows (PowerShell):**
`$env:PWDEBUG="1"`
`pytest tests/ -s`

**Mac/Linux (Bash):**
`export PWDEBUG=1`
`pytest tests/ -s`

To disable the environment variable and run it without Playwright Inspector just disable the variable: In Powershell: `$env:PWDEBUG="0"` or in Bash `export PWDEBUG=0`


## Test Execution with Tags (Markers)

To keep the test execution efficient and organized, this framework uses **Pytest Markers** to categorize tests. This allows you to run specific subsets of tests without executing the entire suite.

### Defined Markers
We have registered the following markers in the `pytest.ini` file:

* **`smoke`**: Quick, critical tests to ensure core functionality is working (e.g., Login).
* **`regression`**: Comprehensive tests to verify that recent code changes haven't broken existing features.
* **`customer`**: Tests exclusively related to the Customer flows and accounts.
* **`manager`**: Tests exclusively related to the Bank Manager flows (adding customers, opening accounts).

### How to Run Specific Tests

You can filter which tests to run by using the `-m` (marker) flag in your terminal. 

Run only Smoke tests:
`pytest -m smoke`

Run tests for a specific domain (e.g., Manager):
`pytest -m manager`

Run everything EXCEPT a specific tag:
`pytest -m "not customer"`

Combine tags (e.g., Run Manager tests that are also marked as Smoke):
`pytest -m "manager and smoke"`

Note: You can combine these markers with the HTML reporting flag to generate targeted reports (e.g., `pytest -m smoke --html=report.html --self-contained-html`).