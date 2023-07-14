# ISP-Speed-Watcher Bot

The ISP Speed Tweet Bot is a Python script that automatically tweets the speed of your ISP router. It periodically measures the download speed and tweets only when it falls below the advertised speed of 150 Mbp every 24 hours.

# Features

- Measures the ISP router's download speed automatically.
- Tweets the speed every 24 hours, but only if it is below the advertised speed of 140 Mbps.
- Integrates with the Twitter API using the Tweepy library to compose and post tweets.
- Script is automated to run at regular intervals using Linux's cronjob

# Prerequisites

- Python 3.x
- Tweepy library (install via `pip install tweepy`)

# Getting Started

1. Clone the repository.
2. Set up your Twitter Developer Account and obtain the necessary API keys and access tokens.
3. Update the keys with your Twitter API credentials.
4. Add this to Windows Task Scheduler or Linux Crontab to automatically run it.
