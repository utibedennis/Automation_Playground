import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Browser Initialization
driver = webdriver.Chrome()
driver.maximize_window()

#Variable Declaration
wait = 10
Url = "https://automationplayground.com/crm/login.html"
Email = "uti.dennis3@gmail.com"
Password= "jemimah"
FirstName= "Tope"
Lastname = "Jones"
Place = "London"
State1 = "Virginia"


#Login Details
driver.get(Url)
customer_email  =driver.find_element(By.ID, "email-id")
customer_email.send_keys(Email)
customer_Pass  =driver.find_element(By.ID, "password")
customer_Pass.send_keys(Password)
driver.find_element(By.ID, "submit-id").click()
time.sleep(wait)

#Creating New Customer
driver.find_element(By.ID, "new-customer").click()
driver.find_element(By.ID, "EmailAddress").send_keys(Email)
name1 =driver.find_element(By.ID, "FirstName")
name1.send_keys(FirstName)
name2 =driver.find_element(By.ID, "LastName")
name2.send_keys(Lastname)
Place1 =driver.find_element(By.ID, "City")
Place1.send_keys(Place)
State =driver.find_element(By.ID, "StateOrRegion")
State.send_keys(State1)
driver.find_element(By.CSS_SELECTOR, '#loginform > div > div > div > div > form > div:nth-child(6) > input[type=radio]:nth-child(3)').click()
driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(wait)

driver.quit()




