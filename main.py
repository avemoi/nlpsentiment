from tweet import TwitterClient
from settings import (
    CONSUMER_API_KEY,
    CONSUMER_API_KEY_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)


def main():
    # creating object of TwitterClient Class
    api = TwitterClient(
        CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    # calling function to get tweets
    tweets = api.get_tweets(query="Donald Trump", count=200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet["sentiment"] == "positive"]
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet["sentiment"] == "negative"]
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
    print(
        "Neutral tweets percentage: {} % \
        ".format(
            100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)
        )
    )

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet["text"])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet["text"])


if __name__ == "__main__":
    # calling main function
    main()
