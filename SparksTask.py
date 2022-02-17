from selenium import webdriver
import time

from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Users\riddh\Downloads\chromedriver_win32\chromedriver_win32.exe")

driver.get("https://www.thesparksfoundationsingapore.org/")
print("\n---------------- Testing Started ---------------------\n")

# 1] Testing Tile of the Website
print("Testing Title:")
if driver.title:
    print("Title Present: ", driver.title)
else:
    print("Title is absent\n")
time.sleep(2)

# 2] Testing logo of the website
print("\nTesting Logo:")
if driver.find_element(By.XPATH, "//*[@id='home']/div/div[1]/h1/a/img").is_displayed():
    print("Logo Displayed")
else:
    print("Logo Not Visible\n")
time.sleep(2)

# 3] Testing Navigation Bar
print("\nTesting Navigation Bar:")
if driver.find_element(By.TAG_NAME, 'nav').is_displayed():
    print("Navigation Bar Displayed")
else:
    print("Navigation Bar Not Visible")
time.sleep(2)

# 4] Testing Scroll Bar
print("\nScrolling down:")
for i in range(0, 1500, 100):
    driver.execute_script(f"window.scrollTo(0, window.scrollY + {i})")
    time.sleep(1)
print("Scrolled Down")
print("\nScrolling up:")
driver.find_element(By.ID, "toTopHover").click()
time.sleep(1)
print("Scrolled Up")

# 5] Testing About us page
print("\nTesting About Us page: ")
try:
    driver.find_element(By.LINK_TEXT, 'About Us').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a').click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(2)

# 6] Testing Policies and Code page
print("\nTesting Policies and Code page: ")
try:
    driver.find_element(By.LINK_TEXT, 'Policies and Code').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Policies").click()
    driver.execute_script("window.scrollBy(0,1000)", "")
    time.sleep(2)
    print('Policy page exists. Success!')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!')
    time.sleep(2)

# 7] Testing Join Us page and form
print("\nTesting Join Us page: ")
driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[5]/a').click()
print("Clicked on Join Us")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[5]/ul/li[1]/a').click()
print("Clicked on Why join us")
time.sleep(2)

name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
email = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
role = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/form/select')

driver.execute_script("arguments[0].scrollIntoView();", name)
time.sleep(1)

name.send_keys('Shreya Thakur')
time.sleep(2)

email.send_keys('Shr@19')
time.sleep(2)

choose = Select(role)
choose.select_by_visible_text('Student')
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'button-w3layouts').click()
time.sleep(2)
print("Why Join us page Tested")

# 8] Testing Programs Page
print("\nTesting Programs Page: ")
actions = ActionChains(driver)
program = driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[3]/a')
mentor = driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[3]/ul/li[2]/a')

actions.move_to_element(program).click().move_to_element(mentor).click().perform()
time.sleep(5)

driver.execute_script("window.scrollBy(0,1450)", "")
print("Programs page Tested")

# 9] Testing Contact Us page
print("\nTesting Contact Us Page: ")
driver.find_element(By.LINK_TEXT, "Contact Us").click()
time.sleep(1)
info = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
time.sleep(1)

if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
    print('contact Information Correct!')
else:
    print('Contact Information Incorrect!')

print("Contact Page Tested")

# 10] Testing Home page Button
print("\nBack to Home Page:")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/h1/a").click()
print("Returned to home page")
time.sleep(3)

# 11] Clicking the Carousel numbers
print("\nTesting Carousel:")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[2]/a").click()
print(" Clicked 2 Internships ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[3]/a").click()
print(" Clicked 3 Mentorship ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[4]/a").click()
print(" Clicked 4 Support ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[5]/a").click()
print(" Clicked 5 Scholarships ")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/section/div/ol/li[6]/a").click()
print(" Clicked 6 Community ")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
print("scrolled 500px")

print("\n---------------- Testing Completed ---------------------\n")

driver.close()
