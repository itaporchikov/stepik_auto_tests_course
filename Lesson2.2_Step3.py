from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

# это для варианта №2
def sum(x, y):
    return str(int(x)+int(y))

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # вариант №1
    # x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    # x = x_element.text
    # y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    # y = y_element.text
    # sum = (int(x) + int(y))

    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_visible_text(str(sum))

    # вариант №2 (через def)
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum(x, y)))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()