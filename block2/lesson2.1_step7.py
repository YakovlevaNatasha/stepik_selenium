from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля  
    
    image = browser.find_element_by_css_selector("#treasure")
    x = image.get_attribute("valuex")
    y = calc(x)

    field = browser.find_element_by_css_selector("#answer")
    field.send_keys(y)

    check = browser.find_element_by_css_selector("#robotCheckbox")
    check.click()

    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

