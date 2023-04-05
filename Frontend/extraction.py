import requests
from bs4 import BeautifulSoup
import re
import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import smtplib
import time
import os

# List of social media accounts to notify
social_media = ['twitter', 'facebook', 'instagram']

# Load existing blacklist of websites
try:
    blacklist = pd.read_csv('blacklist.csv')
except FileNotFoundError:
    blacklist = pd.DataFrame(columns=['Website'])

# Make a request to the website
url = 'https://www.scam-detector.com/article/list-of-scamming-websites/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data you need from the HTML content
# For example, let's say you want to scrape the email and link data from the website
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
links = soup.find_all('a', href=True)
data = []
for email in emails:
    email = email.lower() # convert email to lowercase
    email = email.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
    email = re.sub(r'\d+', '', email) # remove numbers
    data.append({'Email': email, 'Link': '', 'IsSuspicious': None})
for link in links:
    data.append({'Email': '', 'Link': link['href'], 'IsSuspicious': None})

# Create a pandas DataFrame from the data
df = pd.DataFrame(data, columns=['Email', 'Link', 'IsSuspicious'])

# Split the email IDs into words for feature extraction
df['Words'] = df['Email'].str.split()

# Define the target labels for classification
target = ['Legitimate'] * len(emails) + ['Suspicious'] * len(links)

# Extract features from the email IDs using TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
features = vectorizer.fit_transform(df['Email'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Make predictions on the testing data and evaluate the model
y_pred = clf.predict(X_test)

# Assign a suspiciousness score to each email ID
scores = clf.predict_proba(features)[:, 1]
df['IsSuspicious'] = scores

# Save the DataFrame to a CSV file
filename = f"{url.split('//')[1].split('/')[0]}.csv"
path = 'C:/Users/vinee/Desktop/UI hackathon/'
df.to_csv(os.path.join(path, filename), index=False)


# Check if any email IDs are suspicious
if any(df['IsSuspicious'] > 0.5):
    # Send an email notification alert
    sender_email = 'moulik.academic01@gmail.com'
    sender_password = 'yrgflirjeucveoec'
    receiver_email = 'moulikarora07@gmail.com'
    subject = 'Romance scam alert'
    body = f'The web scraping data contains suspicious email IDs and/or links related to romance scam for {url} website.'
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, receiver_email, message)
    print('Email notification has been sent.')
    # Add suspicious website to the blacklist
    website = url.split('//')[1].split('/')[0]
    if website not in blacklist['Website'].values:
        new_website = pd.DataFrame({'Website': [website]})
        blacklist = pd.concat([blacklist, new_website], ignore_index=True)
        blacklist.to_csv('blacklist.csv', index=False)
        
        # Send notification to social media accounts
        message = f"ALERT: Romance scam website {website} has been added to the blacklist."
        for account in social_media:
            if account == 'twitter':
                # Code to send notification to Twitter account
                pass
            elif account == 'facebook':
                # Code to send notification to Facebook account
                pass
            elif account == 'instagram':
                # Code to send notification to Instagram account
                pass
            
        print('Notification sent to social media accounts.')
    else:
        print('Website already in blacklist.')
else:
    print('No suspicious email IDs or links found.')





# import tweepy
# import facebook

# # Twitter credentials
# consumer_key = 'your_consumer_key'
# consumer_secret = 'your_consumer_secret'
# access_token = 'your_access_token'
# access_token_secret = 'your_access_token_secret'

# # Facebook credentials
# app_id = 'your_app_id'
# app_secret = 'your_app_secret'
# access_token_fb = 'your_access_token_fb'

# # Authenticate with Twitter API
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Authenticate with Facebook API
# graph = facebook.GraphAPI(access_token=access_token_fb, version="3.0")

# # List of social media accounts to notify
# social_media = ['twitter', 'facebook']

# # Send notification to social media accounts
# message = f"ALERT: Romance scam website {website} has been added to the blacklist."
# for account in social_media







# from instapy import InstaPy
# from instapy.util import smart_run

# # Set Instagram credentials
# insta_username = 'your_username'
# insta_password = 'your_password'

# # Set message to post on Instagram
# message = "ALERT: Romance scam website {website} has been added to the blacklist."

# # Set list of followers to notify
# followers = ['follower1', 'follower2', 'follower3']

# # Set up InstaPy session
# session = InstaPy(username=insta_username, password=insta_password)

# with smart_run(session):
#     # Follow followers to increase visibility
#     session.follow_by_list(followers, times=1)

#     # Post notification message to Instagram story
#     session.upload_story_photo('path_to_image', caption=message)


# [Note: you will need to install the instapy package first using pip install instapy. Also, make 
# sure to replace your_username and your_password with your own Instagram credentials, and path_to_image
#  with the file path to the image you want to upload as the story.]