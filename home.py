from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Задание 1
driver.get("http://practice.automationtesting.in/")
# Задание 2
driver.execute_script("window.scrollBy(0, 600);")
# Задание 3
ruby = driver.find_element_by_xpath('//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[1]/h3').click()
# Задание 4
reviews = driver.find_element_by_xpath('//*[@id="product-160"]/div[3]/ul/li[2]/a').click()
# Задание 5
stars = driver.find_element_by_xpath('//*[@id="commentform"]/p[2]/p/span/a[5]').click()
# Задание 6
yourreview = driver.find_element_by_xpath('//*[@id="comment"]')
yourreview.send_keys("Nice book!")
# Задание 7
name = driver.find_element_by_xpath('//*[@id="author"]')
name.send_keys('Vova')
# Задание 8
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('test@gmail.com')
# Задание 9
submit = driver.find_element_by_xpath('//*[@id="submit"]').click()
#driver.quit()