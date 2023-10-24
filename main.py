from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
first_name.click()
first_name.send_keys("sounder narayana samy")

last_name = driver.find_element(By.NAME, value="lName")
last_name.click()
last_name.send_keys("K")

email = driver.find_element(By.NAME, value="email")
email.click()
email.send_keys(Yourmail)

signup_button = driver.find_element(By.CSS_SELECTOR, "form button")
signup_button.send_keys(Keys.ENTER)
driver.quit()