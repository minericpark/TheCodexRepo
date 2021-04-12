from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

# Find the search bar (html element)
searchBar = driver.find_element_by_name("q")
# Enter a key into the object / field
searchBar.send_keys("jobs")
# Press submit
# searchBar.submit()

# Press specific key (Enter)
searchBar.send_keys(Keys.RETURN)