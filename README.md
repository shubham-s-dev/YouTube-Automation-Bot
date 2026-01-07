# YouTube Automation Bot

A Python automation tool that opens YouTube, searches for a topic using user input, and extracts the top 5 video links into a CSV file.

## Features
* **Dynamic Input:** Asks the user what to search for.
* **Selenium Interaction:** Automates typing and key presses (`ENTER`).
* **Smart Waits:** Uses `WebDriverWait` to handle YouTube's heavy loading times.
* **Data Extraction:** Scrapes Video Titles and Links using ID selectors.
* **CSV Export:** Saves the results automatically with a dynamic filename.

## Tech Stack
* **Python 3**
* **Selenium WebDriver**
* **Pandas** (For CSV handling)

## How to Run
1. Install dependencies:
   ```bash
   pip install selenium pandas
