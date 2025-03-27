import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Browser Initialization
driver = webdriver.Chrome()
driver.maximize_window()

#Variable Declaration
wait = 10
Url = "https://automationplayground.com/crm/login.html"
customer_email = "uti.dennis3@gmail.com"
customer_Pass= "jemimah"
first_name = "Topsy"
last_name = "Jones"
Place = "London"
State = "Virginia"



#Login Details
driver.get(Url)
customer_email  =driver.find_element(By.ID, "email-id")
customer_email.send_keys("uti.dennis3@gmail.com")
customer_Pass  =driver.find_element(By.ID, "password")
customer_Pass.send_keys("jemimah")
driver.find_element(By.ID, "submit-id").click()
time.sleep(wait)

#Creating New Customer
driver.find_element(By.ID, "new-customer").click()
driver.find_element(By.ID, "EmailAddress").send_keys("uti.dennis3@gmail.com")
first_name =driver.find_element(By.ID, "FirstName")
first_name.send_keys("Topsy")
last_name =driver.find_element(By.ID, "LastName")
last_name.send_keys("Jones")
Place =driver.find_element(By.ID, "City")
Place.send_keys("London")
State =driver.find_element(By.ID, "StateOrRegion")
State.send_keys("Virginia")
driver.find_element("css selector", 'input[name="gender"]').click()
driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(wait)






