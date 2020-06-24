from selenium import webdriver

# from selenium import webdriver
base_url="https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&entitySelectingHelper.selectedEntity=d2568&zip=75243"
# declare and initialize driver variable
driver=webdriver.Chrome(r"C:\Users\241306\Documents\GitHub\webscraping\chromedriver.exe")


driver.maximize_window()
driver.get(base_url)
driver.implicitly_wait(10) #10 is in seconds
# test whether correct URL/ Web Site has been loaded or not
assert "cargurus" in driver.title


# -- Steps --
#
# -- Post - Condition --
# # to close the browser
# driver.close()