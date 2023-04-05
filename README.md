# RomanceSdetector
CYBER FORENSICS T20 SERIES - Hackathon

The purpose of our project is to find out suspicious Romance scam webpages, emails and link. We have used different process for data extraction, Initially the data has been collected from Maltego tool using various transforms and has been extracted in the form of csv files. Later on we have used those datasets of emails and links to get tags and verify whether they are suspicious or not using various transforms such as IPQS. 

On the other side, We have generated our own algorithm to Design and develop a technological solution/software tool that read information on web pages using Web scrapping tool, and identify possible instances of romance scams. The system may send notifications. Over a period of time, a dynamic infringing website list (IWL) may be developed and maintained. The system may send notifications to online social media like Facebook for blacklisting of such websites, thereby discouraging romance scams.

# Details about our Algorithm:

Our code imports necessary libraries such as requests, BeautifulSoup, re, string, pandas, sklearn, smtplib, time, and os to scrape scamming websites and notify social media accounts if there is any suspicious email or link.

It starts by defining a list of social media accounts to notify and loading the existing blacklist of websites from the CSV file. Then, it makes a GET request to a scam detector website and uses BeautifulSoup to parse the HTML content. After that, it extracts the email and link data from the website and cleans them up for further processing. It then creates a pandas DataFrame from the extracted data and splits the email IDs into words for feature extraction.

It defines the target labels for classification and extracts features from the email IDs using TF-IDF vectorization. It then splits the data into training and testing sets, trains a logistic regression model on the training data, and makes predictions on the testing data to evaluate the model. The script assigns a suspiciousness score to each email ID, saves the DataFrame to a CSV file, and checks if any email IDs are suspicious.

If any suspicious email IDs or links are found, it sends an email notification alert, adds the suspicious website to the blacklist, and sends notification to social media accounts. If the website is already in the blacklist, it prints "Website already in blacklist." If no suspicious email IDs or links are found, it prints "No suspicious email IDs or links found."

# Thankyou for visiting my repository.....!
