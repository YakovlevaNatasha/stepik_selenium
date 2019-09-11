from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля  
    
    x = browser.find_element_by_css_selector("#num1").text
    y = browser.find_element_by_css_selector("#num2").text
    
    result = str(int(x) + int(y))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result) # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

