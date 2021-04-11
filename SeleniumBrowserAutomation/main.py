from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.python.org/")
download = driver.find_element_by_link_text("Downloads")
download.click()
