import requests
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)
# list of URLs to scrape
urls = ['https://leetcode.com/contest/', 'https://codeforces.com/contests', 'https://atcoder.jp/contests/']

arr = ['','','','','','','','','','','','','','','','','','','','','','','','']
i = 0
for url in urls:
    # send request to website and retrieve HTML content
    response = requests.get(url)
    html_content = response.content

    # use BeautifulSoup to extract relevant information
    soup = BeautifulSoup(html_content, 'html.parser')
    # extract data here
    arr[i] = soup
    i = i+1   
    # save data to file or database
results = arr[0].findAll("div",{'class':"flex items-center min-h-[80px] px-4 lc-md:min-h-[84px]"})

pan = 0;
sun = ["","","","","",""];
for result in results:
    #   print(result.get_text("   ",strip=True))
    #   print( "    ")
      
      sun[pan] = result.get_text("""   
                                 
""",strip=True)
      pan = pan + 1
print( "   ")
print( "   ")
print( "####Leetcode####")
print( "   ")
print(sun[0])
print( "   ")
print( "   ")
print(sun[1])
print( "   ")


results2 = arr[1].findAll("div",{'class' : "datatable"})


pan2 = 0;
sun2 = ["","","","","",""];
for result in results2:
    #   print(result.get_text("   ",strip=True))
    #   print( "    ")
      
      sun2[pan2] = result.get_text("""
""",strip=True)
      pan2 = pan2 + 1
print( "  ")
print( "  ")
print( "####Codeforces####")
print( "  ")
print(sun2[0])
print( "   ")


results3 = arr[2].findAll("div", {'id': "contest-table-upcoming"})


pan3 = 0;
sun3 = ["","","","","",""];
for result in results3:
    #   print(result.get_text("   ",strip=True))
    #   print( "    ")
      
      sun3[pan3] = result.get_text("""   
""",strip=True)
      pan3 = pan3 + 1
print( "  ")
print( "  ")
print( "####Atcoder#### ")
print( "   ")
print(sun3[0])
print( "   ")

@app.route('/leetcode')
def hello():
    s = [0,1]
    for si in s:
        return sun[si]
@app.route('/codeforce')
def codeforce():
    return sun2[0]
@app.route('/atcoder')
def atcoder():
    return sun3[0]

if __name__ == '__main__':
    app.run()