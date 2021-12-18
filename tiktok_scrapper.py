# Import webdriver manager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



from rich.traceback import install
install()

# Use the `install()` method to set `executabe_path` in a new `Service` instance:
# check for more info https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
service = Service(executable_path=GeckoDriverManager().install())


#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox(service=service) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.tiktok.com/")
    driver.implicitly_wait(10) 



    # driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))
  