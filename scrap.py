from selenium import webdriver
import os,json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
#import mysql.connector
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def get_chromedriver(headless=True):
	path = os.path.dirname(os.path.abspath(__file__))
	print(path,'---------------------path')
	chrome_options = Options()
	# chrome_options.add_argument("--disable-extensions")
	# chrome_options.add_argument("--disable-gpu")
	# chrome_options.add_argument("--no-sandbox")
	# chrome_options.add_argument("--start-maximized")
	# chrome_options.add_argument("--disable-infobars")
	# chrome_options.add_argument("--disable-notifications");
	# chrome_options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications":1})

	# if headless:
	# 	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(
os.path.join(path, 'drivers/chromedriver'),chrome_options=chrome_options)
	return driver


driver=get_chromedriver()


# *********** MYSQL Connect ***************
# db_connection = mysql.connector.connect(
#   host="localhost",
#   user="indiamart",
#   passwd="WIgHnXHN6DeayO@m",
#   database="indiamart"
#   )
# db_cursor = db_connection.cursor()




# def scroll(driver, SCROLL_PAUSE_TIME):
# # Get scroll height
# 	last_height = driver.execute_script("return document.body.scrollHeight")
# 	print("last_height",last_height)
# 	while True:
# 		# Scroll down to bottom
# 		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 		# Wait to load page
# 		sleep(SCROLL_PAUSE_TIME)
# 		# Calculate new scroll height and compare with last scroll height
# 		new_height = driver.execute_script("return document.body.scrollHeight")
# 		print("new_height",new_height)
# 		if new_height == last_height:
# 			break
# 		last_height = new_height



def data(driver, wait):
	
	try:
		link="https://www.bing.com/"

		driver.get(link)
		sleep(5)
		a = driver.find_element_by_id('sb_form_q')
		print(a,'----------------------aaaa')

	except Exception as e:
		raise e
	finally:
		driver.close()
		driver.quit()


if __name__== "__main__":
	driver=get_chromedriver()
	wait = WebDriverWait(driver,10)
	data(driver, 10)