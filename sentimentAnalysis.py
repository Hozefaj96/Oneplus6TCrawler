from textblob import TextBlob
from bucketClassifier import classifierSearch

def sentimentAnalysis(feedback):
    blob = TextBlob(str(feedback))
    blobF = blob.polarity
    if blobF>0:
        return "Positive"
    elif blobF<0:
        return "Negative"
    else:
        return "Neutral"


def bucketClassifier(review):
    # Review Collection buckets after Classification
    batteryLife = []
    pictureQuality = []
    valueForMoney = []
    soundQuality = []
    fingerPrint = []

    for i in review:
        # classifying review for battery life
        if classifierSearch(i,'battery life'):
            batteryLife.append(i)
    
    for j in review:
        # classifying review for picture quality
        if classifierSearch(j,"camera"):
            pictureQuality.append(j)
    
    for k in review:
        # classifying review for sound quality
        if classifierSearch(k,"sound quality"):
            soundQuality.append(k)
    
    for l in review:
        # comparing all the reviews to find out value for money
        valueForMoney.append(l)
        # classifying review for finger print
        if classifierSearch(l,"finger print"):
            fingerPrint.append(l)
            

    return ([batteryLife,pictureQuality,soundQuality,fingerPrint,valueForMoney])



def sentimentPercentage(reviewList):
    sentimentCollection = []
    sentimentPercent = []
    for i in reviewList:
        sentiment = sentimentAnalysis(i)
        sentimentCollection.append(sentiment)
    #return sentimentCollection
    if (len(sentimentCollection)>0):
        postive = (sentimentCollection.count("Positive")/len(sentimentCollection))*100
        negative = (sentimentCollection.count("Negative")/len(sentimentCollection))*100
        neutral = (sentimentCollection.count("Neutral")/len(sentimentCollection))*100

        sentimentPercent.append(str(postive)+"%"+" of positive reviews")
        sentimentPercent.append(str(negative)+"%"+" of negative reviews")
        sentimentPercent.append(str(neutral)+"%"+" of neutral reviews")
        return sentimentPercent
    else:
        return "No Reviews in this section"


def bucketpercentages(bucketList):
    bucketPercentageDict = []

    # Fetching the first bucket list of battery life  
    batteryLife = bucketList[0]
    # Performing sentiment Analysis on it
    batteryLifeSAP = sentimentPercentage(batteryLife)
    #bucketPercentageDict.append("Battery Life")
    bucketPercentageDict.append(batteryLifeSAP)

    # fetching bucket list of picture quality
    pictureQuality = bucketList[1]
    # Performing SA
    pictureQualitySAP = sentimentPercentage(pictureQuality)
    #bucketPercentageDict.append("Picture Quality")
    bucketPercentageDict.append(pictureQualitySAP)

    # Fetching the bucket list of sound quality
    soundQuality = bucketList[2]
    # Performing SA
    soundQualitySAP = sentimentPercentage(soundQuality)
    #bucketPercentageDict.append('Sound Quality')
    bucketPercentageDict.append(soundQualitySAP)

    # Fetching the bucket list of finger print
    fingerPrint = bucketList[3]
    # performing SA
    fingerPrintSAP = sentimentPercentage(fingerPrint)
    #bucketPercentageDict.append('Finger Print')
    bucketPercentageDict.append(fingerPrintSAP)

    # Fetching the bucket list for value for money
    valueForMoney = bucketList[4]
    # performing SA
    valueForMoneySAP = sentimentPercentage(valueForMoney)
    #bucketPercentageDict.append('Value for money')
    bucketPercentageDict.append(valueForMoneySAP)

    return bucketPercentageDict


#reviews = ["picture quality great",'picture quality is bad',"finger print doesnt work fast","battery life is great","value for money","great phone"]

#bucketList=bucketClassifier(reviews)

#print(bucketpercentages(bucketList))