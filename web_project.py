from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# task 1
driver = webdriver.Chrome()
url = 'http://yanigen.com.ua/ru/productstoorder'
driver.get(url)
driver.maximize_window()

# task 2
home_ru = "//a[contains(text(),'ГЛАВНАЯ')]"
home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_ru)
    )
)
home_ru_button.click()

product_ru = "//a[contains(text(),'ИЗДЕЛИЯ НА ЗАКАЗ')]"
product_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, product_ru)
    )
)
product_ru_button.click()

catalog_ru = "//ul[@class='menumain']/li/a[contains(text(),'КАТАЛОГ')]"
catalog_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_ru)
    )
)
catalog_ru_button.click()

clients_ru = "//ul[@class='menumain']/li/a[contains(text(),'КЛИЕНТАМ')]"
clients_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, clients_ru)
    )
)
clients_ru_button.click()

about_ru = "//a[contains(text(),'О НАС')]"
about_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, about_ru)
    )
)
about_ru_button.click()

contacts_ru = "//a[contains(text(),'КОНТАКТЫ')]"
contacts_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, contacts_ru)
    )
)
contacts_ru_button.click()

# task 3
home_ru_footer = "//a[contains(text(),'Главная')]"
home_ru_footer_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_ru_footer)
    )
)
home_ru_footer_button.click()

product_ru_footer = "//a[contains(text(),'Изделия на заказ')]"
product_ru_footer_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, product_ru_footer)
    )
)
product_ru_footer_button.click()

catalog_ru_footer = "//a[contains(text(),'Каталог')]"
catalog_ru_footer_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_ru_footer)
    )
)
catalog_ru_footer_button.click()

clients_ru_footer = "//ul[@class='menu']/li/a[contains(text(),'КЛИЕНТАМ')]"
clients_ru_footer_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, clients_ru_footer)
    )
)
clients_ru_footer_button.click()

about_ru_footer = "//a[contains(text(),'О нас')]"
about_ru_footer_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, about_ru_footer)
    )
)
about_ru_footer_button.click()

contacts_ru_footer = "//a[contains(text(),'Контакты')]"
contacts_ru_footer_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, contacts_ru_footer)
    )
)
contacts_ru_footer_button.click()

# task 4

ua_lang = "//ul[@class='lang-inline']/li/a[contains(text(),'UA')]"
ua_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, ua_lang)
    )
)
ua_lang_button.click()

ua_home_xpath = "//ul[@class='menumain']/li/a[contains(text(),'ГОЛОВНА')]"
ua_home = driver.find_element('xpath', ua_home_xpath)
print(ua_home.text)

ru_lang = "//ul[@class='lang-inline']/li/a[contains(text(),'RU')]"
ru_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, ru_lang)
    )
)
ru_lang_button.click()

ru_home_xpath = "//a[contains(text(),'ГЛАВНАЯ')]"
ru_home = driver.find_element('xpath', ru_home_xpath)
print(ru_home.text)

en_lang = "//ul[@class='lang-inline']/li/a[contains(text(),'EN')]"
en_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, en_lang)
    )
)
en_lang_button.click()

en_home_xpath = "//ul[@class='menumain']/li/a[contains(text(),'HOME')]"
en_home = driver.find_element('xpath', en_home_xpath)
print(en_home.text)
en_home.click()

# task 5

ua_cost = "//div[@class='moduletablevaluta']/span[contains(text(),'грн.')]"
ua_cost_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, ua_cost)
    )
)
ua_cost_button.click()

ua_prise_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/span"
ua_prise = driver.find_element('xpath', ua_prise_xpath)
print(ua_prise.text)

en_cost = "//div[@class='moduletablevaluta']/span[contains(text(),'$')]"
en_cost_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, en_cost)
    )
)
en_cost_button.click()

en_prise_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/span"
en_prise = driver.find_element('xpath', en_prise_xpath)
print(en_prise.text)

logo = '//img[@src="http://yanigen.com.ua/images/logo-2015.png"]'
WebDriverWait(driver, 30).until_not(
    EC.presence_of_element_located(
        (By.XPATH, logo)
    )
)
driver.quit()


