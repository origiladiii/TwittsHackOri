import json
import os
from datetime import datetime, timezone, timedelta
import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import get_accounts as get

async def get_tweets(account_name, output_dir, end_date):
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.add_account("sami123632331", "samisami123", "samihacabay8@gmail.com", "samisami123")
    await api.pool.login_all()

    # get user by login
    user_login = account_name
    user = await api.user_by_login(user_login)

    if user is None:
        return
    user_id = user.id

    # Initialize an empty list to hold tweet data
    tweets_data = []

    async for tweet in api.user_tweets(user_id, limit=100):
        if tweet.date > end_date:
            # Append tweet data to the list
            tweets_data.append({'content': tweet.rawContent, 'date': tweet.date.isoformat()})

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the path for the JSON file
    json_file_path = os.path.join(output_dir, f'{account_name}.json')

    # Write tweet data to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump({account_name: tweets_data}, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    all_accounts = get.get_names_from_txt(file_path='names.txt') # Change the names.txt to your txt file with the names of the accounts
    output_dir = "/home/nehoray/PycharmProjects/Shaback/twitter/tweets_most_followed" # Change it to your output dir
    end_date = datetime(2023, 10, 7, 9, 30, 0, tzinfo=timezone.utc) # Change it to the earliest date you want

    for account_name in all_accounts:
        asyncio.run(get_tweets(account_name,output_dir, end_date))
