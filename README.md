# Overview
Script developed in Python that gets the count of all unique devices that start with 'UHM-' on the Strongsville MR and MS network in Meraki within the last day. It exports a report with the information by each day. Unfortunately due to the limitations of the Meraki API, this script will need to be run daily to get the information you're looking for.

# Prerequisites
Python and the Python modules listed in the requirements.txt file need to be installed on the computer that will run this script. You will need to also set up an API key on the Meraki console which will give you an API key. Make sure you save these key values in a .env file.

# Setup

## Virtual Environment Setup
A virtual environment is a containerized environment for a Python project. The main benefit of a virtual environment set up like this is you can install all of the Python modules required for a project to work in the virtual environment which is independent of the rest of the modules installed outside of the virtual environment. To create a new virtual environment, create a new folder locally on your system where this Python script and project will live. Copy the file into that directory along with the requirements.txt file which will be used in the next step. Open the terminal on your computer and go to that directory. Once there, type in this command to create a new virtual environment for this Python project, if you are on Windows: ```python -m venv .venv```

If you are on Linux or MacOS, type this command in your terminal:
```python3 -m venv .venv```

Once you see the command line return, and the folder called .venv is created, you can move onto the next step.

## Module Install
Included in this project is a requirements.txt file. This file is used to install the modules required for this script to run. Before installing the modules, we'll need to activate the virtual environment. To do that, while having the terminal open in the project directory, if you're on Windows type this command:
```.venv\Scripts\activate```

If you're on Linux or MacOS type in this command:
```source.venv/bin/activate```

If you see a (.venv) in front of the terminal then you know it's working.

To install the modules, type in this command, if you're on Windows:
```pip install -r requirements.txt```

If you're on Linux or MacOS, type in this command:
```pip3 install -r requirements.txt```

This command will install all modules in the requirements.txt file that are required for this project to run. Once you can interact with the terminal again, that means the modules are all installed.

## Environment Variables
One of the modules that were installed is called python-dotenv. This module is used to store environment variables like the access key and secret access key CloudConnexa gave us when setting up the project. To use this module, create a file in the project directory called .env and open the file in a text editor and set up the file as shown below:
```
MERAKI_API_KEY="your access key"
NETWORK_ID="your secret key"
```

These keys are only used in the authorize function where you see they are loaded with:
```os.getenv("Name-of-key")```

# Execution of Script
For the Python script, activate the virutal environment and run the Python script. 