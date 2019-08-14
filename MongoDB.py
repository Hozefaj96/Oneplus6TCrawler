import pymongo

# Importing the main crawler function
from spider import spider
# Importing the sentiment analysis function
from sentimentAnalysis import sentimentPercentage,bucketClassifier,bucketpercentages

userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
url = "http://tiny.cc/sck34y"

spiderData = spider(url,userAgent)
#print(spiderData[9])
client = pymongo.MongoClient("mongodb://localhost:27017/")

scrapedAmazonData = client.productDataScraped

# Product Title In DB
productTitle = scrapedAmazonData.title
title = {
    "Title":spiderData[0]
}
titleInsert = productTitle.insert_one(title)

# Product Description in DB
productDescription = scrapedAmazonData.description
description = {
    "Description":spiderData[1]
}
descriptionInsert = productDescription.insert_one(description)

# Product Image in DB
productImage = scrapedAmazonData.image
image = {
    "image":spiderData[2]
}
imageInsert = productImage.insert_one(image)

# Product Price in DB
productPrice = scrapedAmazonData.price
price = {
    "Price":spiderData[3]
}
priceInsert = productPrice.insert_one(price)

# Product Color in DB
productColor = scrapedAmazonData.color
color = {
    "Color":spiderData[4]
}
colorInsert = productColor.insert_one(color)

# Product Review Count
productReviewCount = scrapedAmazonData.reviewCount
reviewCount = {
    "Review Count": spiderData[5]
}
reviewCountInsert = productReviewCount.insert_one(reviewCount)

# Product Star Rating
productStarRating = scrapedAmazonData.starRating
starRating = {
    "Star Rating": spiderData[6]
}
starRatingInsert = productStarRating.insert_one(starRating)

# Product Technical Details
productTechnicalDetails = scrapedAmazonData.technicalDetails
technicalDetails = {
    "Technical Details": spiderData[7]
}
technicalDetailsInsert = productTechnicalDetails.insert_one(technicalDetails)

# Product Most Recent 100 Reviews
productMostRecentReviews = scrapedAmazonData.recent100reviews
recent100reviews = {
    "Most Recent Reviews": spiderData[8]
}
recentReviewsInsert = productMostRecentReviews.insert_one(recent100reviews)

# Sentiment Analysis and DB
reviewText = spiderData[9]
# Classifying the reviews into buckets
bucketList = bucketClassifier(reviewText)
# performing sentiment analysis on all of the bucket list
sentiments = bucketpercentages(bucketList)

reviewSentimentAnalysis = scrapedAmazonData.sentimentAnalysis

sentimentAnalysis = {
    "Battery Life": sentiments[0],
    "Picture Quality": sentiments[1],
    "Sound Quality": sentiments[2],
    "Finger Print": sentiments[3],
    "Value for money": sentiments[4]
}
reviewSentimentsInsert = reviewSentimentAnalysis.insert_one(sentimentAnalysis)
