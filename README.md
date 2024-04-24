# ADSS-Cryptocurrencies
Group 2

# Table of Contents
1. Project Description
2. Explanation of the Files
3. Initial Requirements
4. Use
5. Additional Information

# Project Description
This project was developed for the Advanced Data Structures and Storage class. It consists on creating a web in which the user selects one of the available cryptocurrencies, and the web displays information about it. Users must be able not only to select the crypto from the drop-down menu, but also to search it manually. Not all cryptocurrencies have the same information (is a non-sql project). 

The project was created using a free account in PythonAnywhere with Python version 3.10 and TinyDB.

# Explanation of the Files
In the Github there are 3 files:
- flask_app_running.py (with the code of the project)
- index.html (the template of the web)
- crypto_db.json (the json file created when running flask_app_running.py
Note that the json file and the flask_app_running.py file must be in the same directory ("CryptoProject/" in my case)

# Initial Requirements
1. Create an account in Python anywhere and select Python 3.10
2. Before running the flask_app_running.py file, install the following libraries in the bash console:
python -m pip install flask
python -m pip install pandas
python -m pip install tinydb

# Use
1. Download and upload files to your pythonanywhere (be careful with directories and paths). Json and flask_app_running.py must be in the same directory.
2. Save and reload all files to make sure everything is working.
3. Access to your website using your Python Anywhere web link (for example: https://alegova.pythonanywhere.com/)

# Additional Information
At first we try to create the database using MongoDB (instead of TinyDB) and connect PythonAnywhere. However, MongoDB uses its a protocol that is not HTTP/HTTPS, so it was not supported by the free acount of Python Anywhere. 
