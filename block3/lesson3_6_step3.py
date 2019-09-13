from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
import math

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    browser.quit()

@pytest.mark.parametrize('links', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, links):
    link = f"https://stepik.org/lesson/236{links}/step/1"
    browser.get(link)
    field = browser.find_element_by_css_selector("textarea.textarea")
    answer = str(math.log(int(time.time())))
    field.send_keys(answer)

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()

    text = browser.find_element_by_css_selector("pre.smart-hints__hint").text

    assert text == "Correct!", "Not good"
