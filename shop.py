# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # Задание 1
# driver.get("http://practice.automationtesting.in/")
# # Задание 2
# myaccount = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# username = driver.find_element_by_xpath('//*[@id="username"]')
# username.send_keys("Vovan123test@gmail.com")
# passwordlogin = driver.find_element_by_xpath('//*[@id="password"]')
# passwordlogin.send_keys('Vovan123!!&&')
# # Заданиие 3
# shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# # Задание 4
# book = driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a[1]/h3').click()
# # Задание 5
# bookname = driver.find_element_by_xpath('//*[@id="product-181"]/div[2]/h1')
# bookname_text = bookname.text
# assert "HTML5 Forms" in bookname_text
# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # Задание 1
# driver.get("http://practice.automationtesting.in/")
# # Задание 2
# myaccount = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# username = driver.find_element_by_xpath('//*[@id="username"]')
# username.send_keys("Vovan123test@gmail.com")
# passwordlogin = driver.find_element_by_xpath('//*[@id="password"]')
# passwordlogin.send_keys('Vovan123!!&&')
# # Заданиие 3
# shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# # Задание 4
# html = driver.find_element_by_xpath('//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a').click()
# # Задание 5
# items_count = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
# if len(items_count) == 3:
#     print("Количество товара соответствует")
# else:
#     print("Количество товара не соответствует")
# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # Задание 1
# driver.get("http://practice.automationtesting.in/")
# # Задание 2
# myaccount = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# username = driver.find_element_by_xpath('//*[@id="username"]')
# username.send_keys("Vovan123test@gmail.com")
# passwordlogin = driver.find_element_by_xpath('//*[@id="password"]')
# passwordlogin.send_keys('Vovan123!!&&')
# # Заданиие 3
# shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# # Задание 4
# sorting = driver.find_element_by_xpath('//*[@id="content"]/form/select')
# sorting_select = sorting.get_attribute("value")
# if sorting_select == "menu_order":
#     print('Сортировка по умолчанию')
# else:
#     print('Любая другая сортировка')
# # Задание 5
# from selenium.webdriver.support.select import Select
# price = driver.find_element_by_xpath('//*[@id="content"]/form/select')
# select = Select(price)
# select.select_by_value('price-desc')
# # Задание 6
# # Задание 7
# sortingtwo = driver.find_element_by_xpath('//*[@id="content"]/form/select')
# sortingtwo_select = sortingtwo.get_attribute("value")
# if sortingtwo_select == "price-desc":
#     print('Верная сортировка')
# else:
#     print('Неверная сортировка')
# driver.quit()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # Задание 1
# driver.get("http://practice.automationtesting.in/")
# # Задание 2
# myaccount = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# username = driver.find_element_by_xpath('//*[@id="username"]')
# username.send_keys("Vovan123test@gmail.com")
# passwordlogin = driver.find_element_by_xpath('//*[@id="password"]')
# passwordlogin.send_keys('Vovan123!!&&')
# # Заданиие 3
# shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# # Задание 4
# android = driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[1]/h3').click()
# # Задание 5
# oldprice = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/del/span')
# oldprice_text = oldprice.text
# assert oldprice_text == "₹600.00"
# # Задание 6
# newprice = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
# newprice_text = newprice.text
# assert newprice_text == "₹450.00"
# # Задание 7
# run_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="product-169"]/div[1]/a/img')) ).click()
# # Задание 8
# run_close = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) ).click()
# driver.quit()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # Задание 1
# driver.get("http://practice.automationtesting.in/")
# # Задание 2
# shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# # Задание 3
# add = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# # Задание 4
# time.sleep(5)
# price = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[2]')
# price_text = price.text
# assert price_text == "₹180.00"
# item = driver.find_element_by_class_name('cartcontents')
# item_text = item.text
# assert item_text == "1 Item"
# # Задание 5
# cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# # Задание 6
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'), "180.00"))
# # Задание 7
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span'), "189.00"))
# driver.quit()
import time


# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # Задание 1
# driver.get("http://practice.automationtesting.in/")
# # Задание 2
# shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# # Задание 3
# driver.execute_script("window.scrollBy(0, 300);")
# add = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(5)
# add_two = driver.find_element_by_xpath('//*[@id="content"]/ul/li[5]/a[2]').click()
# # Задание 4
# cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# # Задание 5
# time.sleep(5)
# remove = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a').click()
# # Задание 6
# time.sleep(5)
# undo = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[1]/a').click()
# # Задание 7
# clear = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input').clear()
# clear = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# clear.send_keys("3")
# # Задание 8
# update = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[3]/td/input[1]').click()
# # Задание 9
# test = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# test_test = test.get_attribute("value")
# assert test_test == "3"
# # Задание 10
# time.sleep(5)
# apply = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[3]/td/div/input[2]').click()
# # Задание 11
# time.sleep(5)
# messedge = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/ul/li')
# messedge_text = messedge.text
# assert messedge_text == "Please enter a coupon code."
# driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Задание 1
driver.get("http://practice.automationtesting.in/")
# Задание 2
shop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
driver.execute_script("window.scrollBy(0, 300);")
# Задание 3
addbook = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# Задание 4
time.sleep(5)
cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# Задание 5
proceed = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/div/a')) ).click()
# Задание 6
firstname = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, 'billing_first_name')) )
firstname.send_keys("Vladimir")
lastname = driver.find_element_by_id('billing_last_name')
lastname.send_keys("P")
email = driver.find_element_by_id('billing_email')
email.send_keys("Vovan123test@gmail.com")
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('00000000000')
country = driver.find_element_by_id('select2-chosen-1').click()
select = driver.find_element_by_xpath('//*[@id="s2id_autogen1_search"]')
select.send_keys('Russia')
russia = driver.find_element_by_class_name("select2-match").click()
adress = driver.find_element_by_xpath('//*[@id="billing_address_1"]')
adress.send_keys("Rostov-on-Don")
town = driver.find_element_by_xpath('//*[@id="billing_city"]')
town.send_keys("Taganrog")
state = driver.find_element_by_xpath('//*[@id="billing_state"]')
state.send_keys("Malibu")
postcode = driver.find_element_by_xpath('//*[@id="billing_postcode"]')
postcode.send_keys("319437")
# Задание 7
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check = driver.find_element_by_xpath('//*[@id="payment_method_cheque"]').click()
# Задание 8
placeorder = driver.find_element_by_id('place_order').click()
# Задание 9
messedge = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/p[1]'), "Thank you. Your order has been received."))
payment = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/ul/li[4]/strong'), "Check Payments"))
driver.quit()