from bs4 import BeautifulSoup
from selenium import webdriver

# Robots.txt Check Module
from roboCheck import roboCheck

# DataHelper functions
from dataHelpers import *

# URL helper function
from urlHelper import urlHelper

def spider(seed,useragent):
        """
        This function takes a seed url link and useragent information.

        Seed url is passed to every function to scrape the needed data.

        Useragent is passed to the roboCheck function to check whether the 
        required page is allowed to crawl or not.

        """
        data = []
        if (roboCheck(useragent,seed)==True): # If Allowed
                bsObj = urlHelper(seed)
                # Product Title
                title = productTitle(bsObj)
                data.append(title)
                # Product Description
                description = productDescription(bsObj)
                data.append(description)
                # Product Image
                image = productImage(bsObj)
                data.append(image)
                # Product Price
                price = productPrice(bsObj)
                data.append(price)
                # Product Color
                color = productColor(bsObj)
                data.append(color)
                # Product Review Count
                reviewCount = productNoReviews(bsObj)
                data.append(reviewCount)
                # Product Star Rating
                starRatings = productStarRatings(bsObj)
                data.append(starRatings)
                # Product Technical Details
                technicalDetails = productTechnicalDetails(bsObj)
                data.append(technicalDetails)
                # Product Recent 100 Reviews
                recent100Reviews = mostRecent100Review(bsObj)
                data.append(recent100Reviews)
                # Only Product review Text
                onlyReviews = recent100Reviews[len(recent100Reviews)-1] # To extarct the last list element 
                data.append(onlyReviews)
                # Returning json file
                return(data)
        else: # If Not
                return("Cant Crawl")

#userAgent = bytes('Mozilla','utf-8')
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
url = "http://tiny.cc/sck34y"

#print(spider(url,userAgent))
