#Define a function that will scrape information about an array of topics
#This cuntiong was taken from instructors becuase it is cleaner than mine
import os
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import json


# def get_news_articles():
    
#     file = 'news_articles.json'
    
#     if os.path.exists(file):
        
#         with open(file) as f:
            
#             return json.load(f)
    
#     topic_list = ['business', 'sports', 'technology', 'entertainment']
    
#     final_list = []
    
#     for topic in topic_list:
        
#         final_list.extend(scrape_one_page(topic))
        
#     with open(file, 'w') as f:
        
#         json.dump(final_list, f)
        
#     return final_list

# #Define a function to scrape articles from one topic
# #Taken from instructors because it was cleaner than 
# def scrape_one_page(topic):
    
#     base_url = 'https://inshorts.com/en/read/'
    
#     response = get(base_url + topic)
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     titles = soup.find_all('span', itemprop='headline')
    
#     summaries = soup.find_all('div', itemprop='articleBody')
    
#     summary_list = []
    
#     for i in range(len(titles)):
        
#         temp_dict = {}
        
#         temp_dict['title'] = titles[i].text
        
#         temp_dict['content'] = summaries[i].text
        
#         temp_dict['category'] = topic
        
#         summary_list.append(temp_dict)
        
#     return summary_list   
################ Acquire Helper Functions ################
def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML returning a soup object.
    '''
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_news_articles(cached=False):
    '''
    This function with default cached == False does a fresh scrape of inshort pages with topics 
    business, sports, technology, and entertainment and writes the returned df to a json file.
    cached == True returns a df read in from a json file.
    '''
    # option to read in a json file instead of scrape for df
    if cached == True:
        df = pd.read_json('articles.json')
        
    # cached == False completes a fresh scrape for df    
    else:
    
        # Set base_url that will be used in get request
        base_url = 'https://inshorts.com/en/read/'
        
        # List of topics to scrape
        topics = ['business', 'sports', 'technology', 'entertainment']
        
        # Create an empty list, articles, to hold our dictionaries
        articles = []

        for topic in topics:
            
            # Create url with topic endpoint
            topic_url = base_url + topic
            
            # Make request and soup object using helper
            soup = make_soup(topic_url)

            # Scrape a ResultSet of all the news cards on the page
            cards = soup.find_all('div', class_='news-card')

            # Loop through each news card on the page and get what we want
            for card in cards:
                title = card.find('span', itemprop='headline' ).text
                author = card.find('span', class_='author').text
                content = card.find('div', itemprop='articleBody').text

                # Create a dictionary, article, for each news card
                article = ({'topic': topic, 
                            'title': title, 
                            'author': author, 
                            'content': content})

                # Add the dictionary, article, to our list of dictionaries, articles.
                articles.append(article)
            
        # Create a DataFrame from list of dictionaries
        df = pd.DataFrame(articles)
        
        # Write df to json file for future use
        df.to_json('articles.json')
    
    return df



