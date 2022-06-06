from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os

from selenium.webdriver.support.wait import WebDriverWait

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
    button = browser.find_element(By.ID,"book")
    button.click()




    # sbmt = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # sbmt.click()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR,"span[id='input_value']")
    x = x.text
    print(x)
    field = browser.find_element(By.CSS_SELECTOR,"input[id='answer']")
    field.send_keys(calc(x))
    button1 = browser.find_element(By.CSS_SELECTOR,"button[id='solve']")
    button1.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()