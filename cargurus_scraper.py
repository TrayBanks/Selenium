#########################################################
import pandas as pd
import warnings
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas
import time
import os
import csv

chromedriver = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


################# Enter Values Here #####################

#########################################################
zipcode = 75243
pages = 27
data_name = "NewTyperPrices"
#########################################################
link = "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=75243&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=100&sortType=DEAL_SCORE&entitySelectingHelper.selectedEntity=d2568".format(zipcode)
driver.maximize_window()
driver.get(link)

raw_data = "_data/_{}_raw.csv".format(data_name)
clean_data = "_data/_{}_clean.csv".format(data_name)


print(
	"\n ** ready to extract data from: {}...{}".format(link[:20], link[-20:]))
print("\n ** pages processing: {}".format(pages))


data = []
print("\n 3...")
time.sleep(1)
print("\n 2...")
time.sleep(1)
print("\n 1...")
time.sleep(1)
assert "CarGurus" in driver.title

for i in range(pages):

	html = driver.page_source
	soup = BeautifulSoup(html, "html.parser")
	cars = soup.find_all("div", {"class"="_4yP575 _2PDkfp"})


	for car in cars:
     
		name = []
		price = []
		miles = []
		location = []
		contactInfo = []
		
		# Getting the keywords section 
		keyword_section = soup.find(class_="keywords-section")
		# Same as: soup.select("div.article-wrapper grid row div.keywords-section")

		# Getting a list of all keywords which are inserted into a keywords list in line 7.
		name_raw = cars.find_all("class": "srp-listing-blade-title")
		name_list = [word.get_text() for word in name_raw]
     
     
     
		name= car.find('div', attrs={'class':'_4BPaqe'})
		price=car.find('h4', attrs={'class':'_3H76RL'})
  		price= car.find("div", {"class":"srp-listing-blade-price"}) 
		miles= car.find("div", {"class":"srp-listing-blade-price"}) 
  		location= car.find("div", {"class":"srp-listing-blade-price"}) 

		mileage=a.find('p', attrs={'class':'qUF2aQ'})
		products.append(name.text)
		prices.append(price.text)
		ratings.append(rating.text) 
     	df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
		df.to_csv('products.csv', index=False, encoding='utf-8')
		
  		# row = {}
		# #title = car.find_all("h4", {"class":"cg-dealFinder-result-model"})
   		# #Selector path cargurus-listing-search > div:nth-child(1) > div > div.FwdiZf > div._5K96zi._3QziWR > div._3LnDeD > div:nth-child(1) > div > a > div._4yP575._2PDkfp > div > div._4BPaqe > h4
		# #JS PATH document.querySelector("#cargurus-listing-search > div:nth-child(1) > div > div.FwdiZf > div._5K96zi._3QziWR > div._3LnDeD > div:nth-child(1) > div > a > div._4yP575._2PDkfp > div > div._4BPaqe > h4")
		# #xpath //*[@id="cargurus-listing-search"]/div[1]/div/div[2]/div[2]/div[4]/div[1]/div/a/div[3]/div/div[1]/h4
		# title = car.find_element_by_xpath('//*[@id="cargurus-listing-search"]')
		# CarTitle = title.text
		# print(CarTitle)
		# info = car.find_all("div", {"class":"cg-dealFinder-result-stats"})
		# deal = car.find_all("div", {"class":"cg-dealFinder-result-deal" })

		# for item in info:
		# 	pre_price = item.find_all("span", {"class": "cg-dealFinder-priceAndMoPayment"})[0].text
		# 	row["price"] = pre_price[pre_price.index("$"):] 
		# 	row["mileage"] = item.find_all("p")[1].text
		# 	row["address"] = item.find_all("span",{"class":"cg-dealFinder-result-stats-distance"})[0].text
		# 	row["dealer_rating"] = str(item.find_all("span", {"class": "cg-dealFinder-result-sellerRatingValue"})[0])
   
		# for item in title:	
		# 	row["year"] = title[0].text
		# 	row["make"] = title[0].text
		
		# for item in deal:
		# 	row["market_price"] = item.find_all("p",{"class": "cg-dealfinder-result-deal-imv"})[0].text
		# 	row["days_listed"] = item.find_all("p", {"class": "cg-dealfinder-result-deal-imv"})[1].text
		
		data.append(row)

	print("\n page {} scraping finished".format(i+1))
	next_page = driver.find_element_by_xpath('//*[@id="cargurus-listing-search"]')
	next_page.click()
	assert "CarGurus" in driver.title

driver.close()


df = pandas.DataFrame(data)
df.to_csv(raw_data, encoding="ascii")


# creating csv
# outfile = open(raw_data,"w",newline='')
# writer = csv.writer(outfile)

print("\n ** data extraction success!")
print("\n ** raw data added: {}".format(raw_data))

# storing data in csv file


# coding: utf-8

# In[1]:

#########################################################

#################### Data Cleaning ######################

#########################################################

warnings.filterwarnings("ignore")


data = pd.read_csv(raw_data)
print("\n ** starting cleaning data: {}".format(raw_data))
time.sleep(3)


def remove_dollar_and_comma(string):
	string = string.replace("$", "")
	string = string.replace(",", "")
	return string


def star_counter(string):
	num = 5 - string.count("star_disabled") - 0.5 * string.count("star_half")
	return num


def print_finish_message(cleanee):
	message = "\n finished cleaning \"{}\"".format(cleanee)
	print(message)
	time.sleep(1)


# extract year from title
data["year"] = data["year"].str[:4]
data["year"] = data["year"].astype("int")
print_finish_message("year")

# extract price


def price_clean(price):
	price = price.split()[0]
	price = remove_dollar_and_comma(price)
	return price


data["price"] = data["price"].apply(price_clean).astype("int")
print_finish_message("price")

# extract market_price


def market_price_clean(market_price):
	market_price = market_price[market_price.index("$"):]
	market_price = remove_dollar_and_comma(market_price)
	return market_price


data["market_price"] = data["market_price"].apply(
	market_price_clean).astype("int")
print_finish_message("market_price")

# extract mileage


def mileage_clean(mileage):
	mileage = mileage[mileage.index(" ")+1:]
	mileage = mileage[:mileage.index(" ")]
	mileage = mileage.replace(",", "")
	return(mileage)


data["mileage"] = data["mileage"].apply(mileage_clean).astype("int")
print_finish_message("mileage")

# extract make


def make_clean(make):
	make = make.split()[1]
	if make == "Land":
		make = "Land Rover"
	return make


data["make"] = data["make"].apply(make_clean).astype("str")
print_finish_message("make")

# calculate rating


def dealer_rating_clean(dealer_rating):
	return star_counter(dealer_rating)


data["dealer_rating"] = data["dealer_rating"].apply(
	dealer_rating_clean).astype("float")
print_finish_message("dealer_rating")

# extract days_listed


def days_listed_clean(days_listed):
	days_listed = days_listed.split()[0]
	if days_listed == "<":
		days_listed = 1
	return days_listed


data["days_listed"] = data["days_listed"].apply(
	days_listed_clean).astype("int")
print_finish_message("days_listed")

# create column state
data["state"] = data["address"][:]
data["city"] = data["address"][:]
print_finish_message("address")

address = data["address"]
state = data["state"]
city = data["city"]

print("\n data reformatting...")
for i in range(len(state)):
	city[i] = address[i][:address[i].index(",")]
	state[i] = address[i][address[i].index(","):]
	state[i] = state[i].replace(", ", "")

# remove address column
data = data.drop("address", 1)

# rearrange columns
cols = ["year", "make", "mileage", "dealer_rating",
		"days_listed", "price", "market_price", "city", "state"]
data = data[cols]

data.to_csv(clean_data)
print("\n** data cleaning finished")
print("\n** clean data available as {}".format(clean_data))
