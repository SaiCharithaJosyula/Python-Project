from selenium import webdriver

driver = webdriver.Chrome(r"C:\ATT\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

