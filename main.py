# building a test case where it goes to a shopping site
# selects a specific product, adds it to the cart
# and then checks out
# will be using different methods to select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("./chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")
# picked css since it's the fastest way to select a dom element within the page
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# loops through the products shown on the page
# and gets the 'Blackberry' item then adds it to the cart
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        # Add item into cart
        product.find_element_by_xpath("div/button").click()


driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("aus")

# need to add an explicit wait so it can hold off until a specific
# dom element is shown and then it'll continue
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Austria")))
driver.find_element_by_link_text("Austria").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText

# how can i take a screenshot though?
# below is super useful to see what is going on
# generally though the best time to take a screenshot is on failure
# driver.get_screenshot_as_file("screenshot.png")

