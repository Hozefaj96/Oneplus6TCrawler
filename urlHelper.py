from selenium import webdriver
from bs4 import BeautifulSoup

def urlHelper(link):
    """
    This function takes a link as an input and 
    returns a BeautifulSoup Object as output
    """
    driver = webdriver.Chrome(executable_path=r'E:\Crawler\chromedriver.exe')
    driver.get(link)
    html = driver.page_source
    bsObj = BeautifulSoup(html,'html.parser')
    
    return bsObj