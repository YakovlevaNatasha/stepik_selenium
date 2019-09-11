import os 
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/file_input.html"

try: 

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля  
    
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("My")

    lastName = browser.find_element_by_css_selector("[name='lastname']")
    lastName.send_keys("dear")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("@friend")
    
    addFile = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    addFile.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

