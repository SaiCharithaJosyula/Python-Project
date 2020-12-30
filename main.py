from selenium import webdriver
from webdriver.chrome import ChromeDriverManager
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


# Condition to check for store number is a digit and it should be of <=5 digits

NSN = input('Enter the store number: ')
try:
    while not NSN.isdigit():
        NSN = input("Enter a valid store number: ")
finally:
    print(NSN)
while len(str(NSN)) > 5:
    NSN = int(input("Store Number should be less than or equal to 5 digits, please enter again: "))
# Adding zeros to NSN when needed
NSN = format(int(NSN), '05')
print(NSN)
# Input from user
user_name = input('Enter the username: ')
pwd = input('Enter the password: ')

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=r"C:\Users\Sai Charitha Josyula\PycharmProjects\Netops", options=options)
# Opening of Chrome Browser
# options = webdriver.chromeoptions()
# driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome(r"C:\ATT\chromedriver.exe")
# driver.implicitly_wait(100)
# driver.maximize_window()

# network.mcd.com
driver.get(
    "https://gas.mcd.com/adfs/ls/idpinitiatedsignon.aspx?logintoRP=https://my-wifi.attwifi.com")
# sending username given by user to username txt box
input_txt = driver.find_element_by_xpath('//*[@id="UsernameInputTxt"]')
input_txt.send_keys(user_name)
# sending password given by user to password txt box
pwd_txt = driver.find_element_by_xpath('//*[@id="PasswordInput"]')
pwd_txt.send_keys(pwd)
# Clicking of submit button on login page
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
# Clicking of Venue tab on Navigation Side Bar
venue = driver.find_element_by_xpath('//*[@id="sidebar-nav-wrapper"]/ul/li[2]/a').click()
sleep(30)
# Entering of Store Number in Search by venue text box
store_number = driver.find_element_by_xpath('//*[@id="search-text"]')
store_number.send_keys(NSN)
# Search of venue - click event
driver.find_element_by_xpath('//*[@id="j_id0:j_id2:j_id41"]/div/div[2]/div[2]/div[1]/div[2]/a').click()
try:
    # venue status
    venue_status = "//*[contains(text(),'%s')][1]//following::div[@data-header='Status']"
    venue_status = venue_status.replace("%s", NSN)
    element = driver.find_element_by_xpath(venue_status)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print('Venue Status is: ', element.text)
    # # Circuit Status
    Circuit_status = "//*[contains(text(),'%s')][1]//following::div[@data-header='Circuit Status']"
    Circuit_status = Circuit_status.replace("%s", NSN)
    element = driver.find_element_by_xpath(Circuit_status)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print("Circuit Status is: ", element.text)
    # selecting of NSN and scroll down
    ele = "//div[@class='dataTable-row dataTable-header']//following::*[contains(text(),'%s')][1]"
    ele = ele.replace("%s", NSN)
    element = driver.find_element_by_xpath(ele)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    # UP Devices
    print("Status of Network Devices:")
    element = driver.find_element_by_xpath('//*[@id="j_id0:j_id1:j_id85:j_id86:j_id90"]')
    sleep(15)
    print(element.text)
    # DOWN Devices
    element = driver.find_element_by_xpath('//*[@id="j_id0:j_id1:j_id85:j_id86:j_id94"]')
    print(element.text)
    # Clicking on Metrics Tab
    try:
        driver.find_element_by_xpath('//*[@id="myDiv"]/ul[1]/li[3]/a').click()
        # Clicking on arp table drop down icon
        driver.find_element_by_xpath('//*[@id="arpChev"]').click()
        sleep(30)
        # To find ARP Table and download
        refresh = driver.find_element_by_xpath('//*[contains(text(), "ARP table - private VLANs")]')
        driver.execute_script("arguments[0].scrollIntoView(true);", refresh)

        arp_download = driver.find_element_by_xpath("(//span[contains(@class, 'glyphicon icon-downloads')])[1]")
        try:
            sleep(30)
            driver.execute_script('arguments[0].click();', arp_download)
            action = ActionChains(driver)
            action.move_to_element(arp_download)
            action.click()
            sleep(15)
            driver.close()
            print("ARP Table downloaded Successfully.......")
            time.sleep()
        except NoSuchElementException:
            driver.execute_script('arguments[0].click();', arp_download)
            print("No element found")
    except:
        print('No such Store Number')
        driver.close()
except:
    print('No such Store Number')
    driver.close()
