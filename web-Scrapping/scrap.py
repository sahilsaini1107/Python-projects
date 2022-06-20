import requests
from bs4 import BeautifulSoup


url1 = "https://leetcode.com/contest/"   
url2 = "https://codeforces.com/contests"
url3 = "https://www.codechef.com/contests?itm_medium=navmenu&itm_campaign=allcontests"
url4 = "https://atcoder.jp/contests/"
url5 = "https://www.hackerrank.com/contests"


r1 = requests.get(url1)
r2 = requests.get(url2)
r3 = requests.get(url3)
r4 = requests.get(url4)
r5 = requests.get(url5)


htmlcontent1 = r1.content
htmlcontent2 = r2.content
htmlcontent3 = r3.content
htmlcontent4 = r4.content
htmlcontent5 = r5.content


soup = BeautifulSoup(htmlcontent1, 'html.parser')
# print(soup.find_all('div', class_="jsx-3209139589"))
soup.select("head > title")
"p > a:nth-of-type(2)"
# print(soup.select("div > div:nth-of-type(8)").text())
bestdiv = soup.select("div > div:nth-of-type(8)")
