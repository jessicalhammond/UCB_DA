from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
import time
from selenium import webdriver
from datetime import datetime

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False) 

def scrape():
    browser = init_browser()
    mars_data = {}

    # MARS IMAGE
    img_url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)
    time.sleep(1)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()
    image_page = browser.html
    soup = bs(image_page, 'lxml')
    image_link = soup.find('figure', class_='lede').find('img')['src']
    image_link
    featured_image_url = ("https://www.jpl.nasa.gov/" + image_link)
    featured_image_url
    
    print('===================')
    print(featured_image_url)

    mars_data['featured_image']= featured_image_url

    # MARS WEATHER
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)
    twitter_page = browser.html
    twitter_soup = bs(twitter_page, 'lxml')
    time.sleep(1)
    mars_weather = twitter_soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_weather

    print('===================')
    print(mars_weather)
    mars_data['weather'] = mars_weather

    # MARS FACTS
    read_mars = pd.read_html('https://space-facts.com/mars/')
    df = pd.DataFrame.to_html(read_mars[0])
    df
    
    print('===================')
    print(df)
    mars_data['facts'] = df

    # USGS
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # go to url and find item by css; collect items into driver element list
    browser.visit(usgs_url)
    items = browser.find_by_css('a.product-item h3') 
    time.sleep(1)

    hemisphere = []
    for i in range(len(items)):
        data = {}
        browser.find_by_css('a.product-item h3')[i].click()
        time.sleep(1)
        img_url = browser.find_link_by_text('Sample').first
        data['url'] = img_url['href']
        data['title'] = browser.find_by_css('h2.title').text
        hemisphere.append(data)
        browser.back()
    
    mars_data['hemisphere'] = hemisphere
    
    print('===================')
    print(hemisphere)
    print('===================')
    print(mars_data)

    browser.quit()

    return mars_data