from bs4 import BeautifulSoup
from selenium import webdriver
from urlHelper import urlHelper

def productTitle(bsObj):
    # to scrape the product title
    title = bsObj.find("div",{"id":"titleSection"})
    return title.text

def productDescription(bsObj):
    # to scrape the product description
    description = bsObj.find("div",{"id":"feature-bullets"})
    descriptionF = description.find("ul",{"class":"a-unordered-list"})
    return descriptionF.text

def productImage(bsObj):
    # to scrape the product image
    image = bsObj.find("div",{"id":"imgTagWrapperId"})
    imageF = image.find("img")
    return imageF['src']

def productPrice(bsObj):
    # to scrape the product price
    price = bsObj.find("div",{'id':'availability'})
    priceF = price.find("span",{'class':'a-color-price'})
    return(priceF.text)

def productColor(bsObj):
    # to scrape the product color
    color = bsObj.find("div",{"id":"variation_color_name"})
    colorF = color.find("span",{"class":"selection"})
    return(colorF.text)

def productNoReviews(bsObj):
    # to scrape the number of reviews for product 
    noReview = bsObj.find("span",{'id':"acrCustomerReviewText"})
    return(noReview.text)

def productStarRatings(bsObj):
    # to scrape the product star rating
    starRatingF = bsObj.find('span',{'class':'a-icon-alt'})
    return (starRatingF.text)

def productTechnicalDetails(bsObj):
    # to scrape the product's technical details
    tDetailsDiv = bsObj.find("div",{'class':'techD'}).find("table").find('tbody').find_all('tr')
    
    tDetails = []
    for row in tDetailsDiv:
        for cell in row.find_all('td'):
            tDetails.append(cell.text)
    return(tDetails)

def mostRecent100Review(bsObj):
    # to scrape the most 100 reviews of product
    reviewsLinkTag = bsObj.find('div',{'id':"reviews-medley-footer"}).find('a',{'class':"a-link-emphasis"})

    fullReviewList = []
    sentimentList = []
    pageNo = 1
    
    while pageNo<11:    
        reviewsLink = "https://www.amazon.in"+reviewsLinkTag['href']+"&sortBy=recent&pageNumber="+str(pageNo) 
        bsObjReview = urlHelper(reviewsLink)

        profileReviewDiv = bsObjReview.find_all('div',{'data-hook':"review"})

        for i in profileReviewDiv:
            # List for storing single profile review
            reviewContents = []
            # Reviewers Name
            profileReviewName = i.find("span",{'class':"a-profile-name"})
            reviewContents.append("Name: "+profileReviewName.text)
            # Reviewers Star Rating
            profileReviewStarRating = i.find("div",{'class':"a-row"}).find("span",{"class":"a-icon-alt"}) 
            reviewContents.append("Star Ratings: "+profileReviewStarRating.text)
            # Reviewers Review Title
            profileReviewTitle = i.find("a",{"data-hook":"review-title"}).find("span",{"class":""})
            reviewContents.append("Review Title: "+profileReviewTitle.text)
            # Reviewers Review Date
            profileReviewDate = i.find("span",{"data-hook":"review-date"})
            reviewContents.append("Review Date: "+profileReviewDate.text)
            # Reviewers Phone info
            profileReviewInfo = i.find("a",{"data-hook":"format-strip"})
            reviewContents.append("Reviewers Phone Info: "+profileReviewInfo.text)
            # Reviewers Verification of Purchase
            #profileVerifiedPurchase = i.find("span",{"data-hook":"avp-badge"})
            #reviewContents.append("Verification Info: "+profileVerifiedPurchase.text)
            # Reviewers Review Text
            profileReviewText = i.find("span",{"data-hook":"review-body"}).find("span",{"class":""})
            reviewContents.append("Review: "+profileReviewText.text)
            sentimentList.append(profileReviewText.text)
            # Review Category
            profileReviewCategory = i.find("div",{"class":"cr-helpful-text"})
            reviewContents.append("Category: "+profileReviewCategory.text)

            fullReviewList.append(reviewContents)
        pageNo = pageNo+1
    fullReviewList.append(sentimentList)
    return fullReviewList
