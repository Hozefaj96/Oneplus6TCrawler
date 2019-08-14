import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()

def roboCheck(useragent, url):

  """
  
  It uses the urllib.robotparser package to check the robots.txt file.

  It takes a url and useragent as input.
  It checks if the url is in the robots.txt or not
  If it is present it denies the access to crawler by returning False else True

  """

  rp.set_url("https://amazon.in/robots.txt")
  rp.read()
  op = rp.can_fetch(useragent, url)
  return op
