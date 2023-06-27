import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import constants

website = 'https://webapp4.asu.edu/myasu/'
path = '/Users/shashankreddy/Desktop/Projects/chromedriver_mac_arm64/chromedriver'
driver = webdriver.Chrome()
driver.implicitly_wait(1)

driver.get(website)

username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')

passwordText = constants.password
usernameText = constants.username

username.send_keys(usernameText)
password.send_keys(passwordText)

submit = driver.find_element(By.XPATH, '//*[@value="Sign In"]')

submit.click()

# print("enter any key to continue")
# userInput = input()

time.sleep(10)

campusServices = driver.find_element(
    By.XPATH, '//*[@id="asu-header-nav"]/ul/li[3]/a')
campusServices.click()

# time.sleep(3)

jobSearchLink = driver.find_element(
    By.XPATH, '//*[@id="resources-Jobs & Careers-content"]/div/div[3]/div/div[1]/a')
jobSearchLink.click()

# time.sleep(3)

onCampusLink = driver.find_element(
    By.XPATH, '//*[@id="node-16685"]/div/div[1]/div/div/div/div[1]/a/button')
onCampusLink.click()

# time.sleep(5)

advacedSearch = driver.find_element(
    By.XPATH, '//*[@id="initialSearchBox"]/div/div[1]/div[2]/a')
advacedSearch.click()

# time.sleep(5)

dateInput = driver.find_element(By.XPATH, '//*[@placeholder="m/d/yyyy"]')
dateInput.send_keys(constants.date)

searchButton = driver.find_element(
    By.XPATH, '//*[@id="bottomControlWrapper_BUTTON_0"]')
searchButton.click()

# time.sleep(5)

jobs = driver.find_elements(By.XPATH, '//*[@class="jobProperty jobtitle"]')

for job in jobs:

    link = job.get_attribute('href')

    driver.execute_script("window.open('');")

    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)

    testElement = driver.find_elements(
        By.XPATH, '//*[@id="applyFromDetailBtn"]')

    if len(testElement) == 0:
        driver.close()

        # Switching to old tab
        driver.switch_to.window(driver.window_handles[0])
        continue

    applyButon = driver.find_element(By.XPATH, '//*[@id="applyFromDetailBtn"]')
    applyButon.click()

    startButton = driver.find_element(By.XPATH, '//*[@id="startapply"]')
    startButton.click()

    showNext = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    showNext.click()

    eligibleRadio = driver.find_element(
        By.XPATH, '//*[@id="radio-44674-Yes"]')
    eligibleRadio.click()

    fwsNo = driver.find_element(By.XPATH, '//*[@id="radio-61829-No"]')
    fwsNo.click()

    # Searching ASU Website
    howSelectbox = driver.find_element(
        By.XPATH, '//*[@id="custom_44925_1291_fname_slt_0_44925-button_text"]')
    howSelectbox.send_keys("Searching ASU Website")

    nextBtn = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    nextBtn.click()

    uploadResumeLink = driver.find_element(
        By.XPATH, '//*[@id="AddResumeLink"]')
    uploadResumeLink.click()

    time.sleep(3)

    driver.switch_to.frame(driver.find_element(
        By.XPATH, '//*[@id="profileBuilder"]'))

    browseBtn = driver.find_element(By.XPATH, '//*[@type="file"]')
    browseBtn.send_keys(constants.resumePath)

    time.sleep(3)

    driver.switch_to.parent_frame()

    uploadCLLink = driver.find_element(By.XPATH, '//*[@id="AddCLLink"]')
    uploadCLLink.click()

    time.sleep(3)

    driver.switch_to.frame(driver.find_element(
        By.XPATH, '//*[@id="profileBuilder"]'))

    browseBtn = driver.find_element(By.XPATH, '//*[@type="file"]')
    CLPath = constants.cvpath + row["jobId"] + ".pdf"
    browseBtn.send_keys(CLPath)

    time.sleep(3)

    driver.switch_to.parent_frame()

    saveContBtn = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    saveContBtn.click()

    time.sleep(2)

    saveContBtn = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    saveContBtn.click()

    time.sleep(2)

    saveContBtn = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    saveContBtn.click()

    time.sleep(2)

    saveContBtn = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    saveContBtn.click()

    time.sleep(2)

    saveContBtn = driver.find_element(By.XPATH, '//*[@id="shownext"]')
    saveContBtn.click()

    saveContBtn = driver.find_element(By.XPATH, '//*[@id="save"]')
    saveContBtn.click()

    print("applied to job")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
