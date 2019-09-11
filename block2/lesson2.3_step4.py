from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector("#input_value").text
    result = calc(x)

    textField = browser.find_element_by_tag_name("input")
    textField.send_keys(result)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

