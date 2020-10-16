import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

WebDriverWait(browser, 50).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)
browser.find_element_by_css_selector('#book').click()

result = calc(browser.find_element_by_css_selector('#input_value').text)
browser.find_element_by_css_selector('#answer').send_keys(str(result))
browser.find_element_by_css_selector('button[type="submit"]').click()
