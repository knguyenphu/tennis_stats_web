from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
opt = Options()
opt.add_argument(r"--silent")
opt.add_argument(r"--no-sandbox")
opt.add_argument(r"--disable-dev-shm-usage")
opt.add_argument(r'--ignore-certificate-errors')
opt.add_experimental_option("detach", True)
#opt.add_argument('headless')
#opt.add_argument(f'user-agent={user_agent}')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opt)


url = 'https://www.espn.com/tennis/players'
driver = webdriver.Chrome(options = opt)

driver.get(url)

search_box = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/form/div/input'
element = (By.XPATH, search_box)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(element)).send_keys('Alcaraz' + '\n')

go_button = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/form/input'
element = (By.XPATH, go_button)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(element)).click()

driver.find_element(By.XPATH, "//a[text()='Carlos Alcaraz']").click()

results_button = '/html/body/div[1]/div[2]/div/div[2]/div[6]/ul/li[2]/a'
element = (By.XPATH, results_button)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(element)).click()