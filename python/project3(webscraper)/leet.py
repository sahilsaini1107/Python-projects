import requests
from bs4 import BeautifulSoup

# specify the URL of the website you want to scrape
url = "https://leetcode.com/contest/"

# send a request to the website to get its HTML content
response = requests.get(url)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find the HTML element that contains the information you want to scrape
results=soup.findAll("div",{'class':"flex items-center min-h-[80px] px-4 lc-md:min-h-[84px]"})
pan = 0;
sun = ["","","","","",""];
for result in results:
    #   print(result.get_text("   ",strip=True))
    #   print( "    ")
      
      sun[pan] = result.get_text("""   
                                 
""",strip=True)
      pan = pan + 1
print( "   ")
print(sun[0])
print( "   ")
print( "   ")
print(sun[1])
print( "   ")

