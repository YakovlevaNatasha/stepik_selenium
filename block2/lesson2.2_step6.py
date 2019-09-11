from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
   
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля  
    
    x = browser.find_element_by_css_selector("#input_value").text
    result = calc(x);
    
    field = browser.find_element_by_css_selector("#answer")
    field.send_keys(result)
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)

    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click()

    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
