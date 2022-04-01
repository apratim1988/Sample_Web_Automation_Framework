import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def anandrathi_login():
    s = Service("C:\\Users\\aprat\\OneDrive\\Desktop\\selenium\\chromedriver98\\chromedriver.exe")
    chrome_options = Options()
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(service=s, options=chrome_options)
    url = "https://sarathiaapka.com/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[@href='login.php'])[1]").click()
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("9998887776")
    driver.find_element(By.NAME, "password").send_keys("qwerty123")
    driver.find_element(By.XPATH, "//button[@class='btn btn-theme']").click()
    time.sleep(3)
