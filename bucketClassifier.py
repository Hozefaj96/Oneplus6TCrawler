import re 

def classifierSearch(review,queryWord):
    """
    This bucket takes a review string and a query word,
    if word is present in the review it returns true else false
    """
    reviewLower = review.lower()
    # searching the review for the specific word
    matchResult = bool(re.search(queryWord,reviewLower))
    return matchResult

#print(batteryLife("battery life is not good","battery life"))
