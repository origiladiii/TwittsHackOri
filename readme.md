# Twitter Data Collection Script

## Overview

This Python script is designed to collect tweets from specified Twitter accounts. It uses the `twscrape` library to interact with Twitter's API and gather tweets from specified users. The script requires a list of Twitter account names and saves the tweets in JSON format.

## Requirements

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`

## Installation

Clone the repository or download the project files to your local machine. Install the required Python packages:

```bash
pip install -r requirements.txt
```
## Usage

### Setting Up

1. Ensure you have a file named `names.txt` in your project directory. This file should contain the Twitter account names from which you want to collect tweets, with each name on a new line.
2. Modify the `output_dir` variable in the script to specify the directory where the JSON files containing the tweets will be saved.
3. Set the `end_date` variable to define the earliest date for the tweets you want to collect.

### Running the Script

To execute the script, run the following command in your terminal:
```bash
python get_twitts_hack.py
