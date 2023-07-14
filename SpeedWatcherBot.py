import tweepy
import speedtest

# Authenticate with Twitter API
api_key = ''
api_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Speedtest definition
st = speedtest.Speedtest(secure=True)

# Find the best server
best_server = st.get_best_server()

# Perform the speed test with the best server
download_speed = st.download() / 10**6  # Convert to Mbps

# Print the download speed
finalspeed = "Today's Download Speed: {:.2f} Mbps".format(download_speed)
print(finalspeed)

if download_speed < 120:
    print("ISP Fails, speed lower than advertised!")
    client.create_tweet(text = finalspeed)
