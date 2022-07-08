#web Crawling->
#Request->wait->response->fetch
import urllib.request as url
import bs4#BeautifulSoup

choice = input("Enter Product Name you wanna Search : ")
choice = choice.replace(" ","+")
path="https://www.flipkart.com/search?q="+choice
response=url.urlopen(path)

data = bs4.BeautifulSoup(response,'lxml')

itemNameDiv = data.find('div',class_="_4rR01T")
print("Item Name : ",itemNameDiv.text)

itemPriceDiv = data.find('div',class_="_30jeq3 _1_WHN1")
print("Item Price : ",itemPriceDiv.text)

ul=data.find('ul',class_="_1xgFaf")
FeaturesList= ul.findAll('li',class_="rgWa7D")
print("*********<><><> Features <><><>*********")
for i in range(len(FeaturesList)):
    print(f"{i+1}.  {FeaturesList[i].text}")


a=data.find('a',class_="_1fQZEK")['href']
path = "https://www.flipkart.com"+a
response=url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
div1=data.find('div',class_="col JOpGWq")
a=div1.find('a')['href']
path = "https://www.flipkart.com"+a

