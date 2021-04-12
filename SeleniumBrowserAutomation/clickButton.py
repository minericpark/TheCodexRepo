from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

# Find the specific element by html
download = driver.find_element_by_link_text("Downloads")
# Clicks the element
download.click()
