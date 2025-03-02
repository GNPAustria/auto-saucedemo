# Code Number 0018
# Function: Remove At Least One Item in SauceDemo
# Browser Mode: Incognito
# Author: GPA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PREREQUISITE CODE (NECESSARY FOR INITIALIZATION) -- do not include in automation test steps

# PRQ 1: Create an instance of Edge Options
edge_options = Options()

# PRQ 2: Add the InPrivate argument
edge_options.add_argument("--inprivate")

# PRQ 3: Provide the path to your EdgeDriver executable -- note to always keep the driver updated.
edge_driver_path = "C:\\Users\\giana\\Downloads\\edgedriver_win64\\msedgedriver.exe"
service = Service(executable_path=edge_driver_path)

# PRQ 4: Create new instance of the Edge driver
driver = webdriver.Edge(service=service, options=edge_options)  # Use Edgedriver

# AUTOMATION SUITE (Test Steps start here)

# 1. Access the website: SauceDemo.
driver.get("https://www.saucedemo.com/")
time.sleep(3) # allot enough time to load page

# 2. Input email or username.
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# 3. Input password.
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# 4. Click Sign in.
wait = WebDriverWait(driver, 5)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# 5. Add to cart every item.
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(1)

# 6. Remove at least one of the items.
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(1)
driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
time.sleep(1)

# 7. Click the cart icon to view the checked-out items.
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() # Note the class name, not the data-test.
time.sleep(1.5)

# 8. Click Checkout.
driver.find_element(By.ID, "checkout").click()
time.sleep(1.5)

# 9. Fill in your First Name, Last Name, and ZIP Code.
driver.find_element(By.ID, "first-name").send_keys("Fe\u00F6d\u00F8\u0159")
driver.find_element(By.ID, "last-name").send_keys("Dr\u0101\u017E\u00F0\u00E5\u00F1\u00FD")
driver.find_element(By.ID, "postal-code").send_keys("50917")

# 10. Click Continue.
driver.find_element(By.ID, "continue").click()
time.sleep(1.5)

# 11. Click Finish.
driver.find_element(By.ID, "finish").click()
time.sleep(5)

# 12. Click Back Home.
driver.find_element(By.ID, "back-to-products").click()
time.sleep(3)

# End result: Successful end-to-end checkout of "Removed At Least One". Removed items: Backpack and Bolt T-shirt.
