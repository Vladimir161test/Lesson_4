from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Задание 1
driver.get("http://practice.automationtesting.in/")
# Задание 2
myaccount = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# Задание 3
email = driver.find_element_by_xpath('//*[@id="reg_email"]')
email.send_keys('Vovan123test@gmail.com')
# Задание 4
password = driver.find_element_by_xpath('//*[@id="reg_password"]')
password.send_keys('Vovan123!!&&')
# Задание 5
registr = driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
driver.quit()

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Задание 1
driver.get("http://practice.automationtesting.in/")
# Задание 2
myaccount = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# Задание 3
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("Vovan123test@gmail.com")
# Задание 4
passwordlogin = driver.find_element_by_xpath('//*[@id="password"]')
passwordlogin.send_keys('Vovan123!!&&')
# Задание 5
loginbtn = driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
# Задание 6
logout = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')
if logout is None:
    print('Кнопка отсутствует')
else:
    print('Кнопа присутствует')
#driver.quit()

