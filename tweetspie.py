import tweepy, sys
from textblob import TextBlob
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part) / float(whole)


consumer_key = 'eGu88MqSA60fZ7BIkK0cytTZM'
consumer_secret = 'qdGhBgSlS3CoPRDl6uupMuRUFB7DHr167SZnVcNaKvvoHweXLd'
access_token = '950737366305533952-Jri13OHMGahjRJvHARX9Ds4ezvKuSUq'
access_token_secret = 'BKAX4r9t3TtQciOEUHlpfVllzCwvYLwa78jjZNBLq1fSY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searchKeyword = input("Enter Your Keyword or Hashtag : ")
noOfTweets = int(input("Enter Number Of Tweets : "))

tweets = tweepy.Cursor(api.search, q=searchKeyword).items(noOfTweets)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfTweets)
negative = percentage(negative, noOfTweets)
neutral = percentage(neutral, noOfTweets)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How peoples are reacting on" + searchKeyword + "by analysing" + str(noOfTweets) + "Tweets")

if (polarity == 0):
    print("Neutral")
elif (polarity < 0):
    print("Negative")
elif (polarity > 0):
    print("Positive")

labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]', 'Netural [' + str(neutral) + '%]']
sizes = [positive, negative, neutral]
colors = ['yellow', 'red', 'green']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc='best')
plt.title("How peoples are reacting on" + searchKeyword + "by analysing" + str(noOfTweets) + "Tweets")
plt.axis('axis')
plt.tight_layout()
plt.show()
