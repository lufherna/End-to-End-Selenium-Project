from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("./chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")
# picked css since it's the fastest way to select a dom element within the page
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    product.find_element_by_xpath("div/h4/a")