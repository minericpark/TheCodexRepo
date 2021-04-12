from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://jqueryui.com/droppable/")

# Switch to frame view
driver.switch_to.frame(0)

ac = ActionChains(driver)

# When using frames, use frame source inspector to determine their id / name
source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")

# Drag and drop source (block) 100px to right, 200 px down
ac.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)
# Drag and drop source to target. Call perform since it is an action chain
ac.drag_and_drop(source, target).perform()
time.sleep(2)