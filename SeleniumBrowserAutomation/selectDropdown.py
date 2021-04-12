from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# There exists a html tag for select called 'birthday_month' in the example
driver = webdriver.Firefox()
driver.get("https://www.facebook.com")

signup = driver.find_element_by_link_text("Create New Account")
signup.click()
time.sleep(2)

# Create a select object by finding birthday_month object and encasing it with Select
monthSelect = Select(driver.find_element_by_name("birthday_month"))
# Select dropdown object by index 1
monthSelect.select_by_index(1)
time.sleep(2)
# Select dropdown object of value '7'
monthSelect.select_by_value("7")
time.sleep(2)
# Select dropdown object visibly called 'Dec'
monthSelect.select_by_visible_text("Dec")
time.sleep(2)

print(monthSelect.options)