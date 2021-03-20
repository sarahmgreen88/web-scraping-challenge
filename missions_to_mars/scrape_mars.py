import pandas as pd 
from splinter import Browser
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_= "content_title")
    first_title = titles[1].text.strip()
    par = soup.find_all('div', class_ = "article_teaser_body")
    first_par = par[0].text
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url2 = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url2)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')

    image = soup2.find('img', class_= "headerimage")
    image_link = image['src']
    featured_image = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + image_link
    browser.quit()



    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url3 = "https://space-facts.com/mars/"
    browser.visit(url3)
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')

    table = soup3.find('aside', class_ = 'widget')
    mars_table = table.text
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url4)
    html4 = browser.html
    soup4 = BeautifulSoup(html4, 'html.parser')

    img_links = soup4.find_all('h3')


    asto_url_prefix = 'https://astrogeology.usgs.gov/'

    hemisphere_image_urls = []

    for img_link in img_links:
        image_page = browser.click_link_by_partial_text(img_link.text)
        html4= browser.html
        soup4 = BeautifulSoup(html4, 'html.parser')
        img_url_suffix = soup4.find('img', class_='wide-image')['src']
        img_url = asto_url_prefix + img_url_suffix
        title = soup4.find('h2', class_='title').text
        img_dict = {'title': title, 'img_url': img_url}
        hemisphere_image_urls.append(img_dict)
        browser.back()

    mars_data = {
        'news_title' : first_title,
        'description' : first_par,
        'featured_image' : featured_image,
        'mars_table' : mars_table,
        'hemisphere_image_urls' : hemisphere_image_urls
    }
    browser.quit()

    return(mars_data)

