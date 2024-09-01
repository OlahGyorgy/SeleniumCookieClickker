Cookie Clicker Bot

This is a Cookie Clicker bot implemented in Python 3.12 using Selenium 4.31.1. The bot automates the process of clicking the cookie and purchasing upgrades in the Cookie Clicker game. Please note that this bot is currently designed to handle up to one million cookies and may not function correctly above this limit.
Features

    Automatically clicks the big cookie to generate cookies.
    Purchases available upgrades and products to maximize cookie generation.
    Handles cookies efficiently up to a limit of one million.

Requirements

    Python 3.12
    Selenium 4.31.1
    WebDriver for your preferred browser (e.g., ChromeDriver for Chrome)

Installation

    Install Python: Make sure Python 3.12 is installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

    Install Selenium: Open a terminal or command prompt and run the following command to install Selenium:

    bash

    pip install selenium==4.31.1

    Install WebDriver: Download the WebDriver for your preferred browser and ensure it is in your system's PATH. For Chrome, you can download ChromeDriver from: https://sites.google.com/chromium.org/driver/

Setup

    Clone or download this repository to your local machine.
    Place the chromedriver.exe (or the equivalent WebDriver for your browser) in the same directory as your script or add it to your system's PATH.

Usage

    Open a terminal or command prompt.

    Navigate to the directory containing the script.

    Run the bot script using Python:

    bash

python cookie_clicker_bot.py

The bot will open the Cookie Clicker game in a browser window and start clicking the cookie to generate cookies. It will also purchase upgrades and products when enough cookies are available.