from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv() 

username_input = os.getenv("USERNAME")
password_input = os.getenv("PASSWORD")

class CanvasBot():
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)  # Keeps Chrome open
        self.driver = webdriver.Chrome(options=options)

    # Open CSUF on a new Chrome window 
    def open_canvas(self):
        self.driver.get('https://www.fullerton.edu/')
        sleep(3)

        # Direct user to the login webpage
        portal_page = self.driver.find_element(By.XPATH, '/html/body/div[2]/header[3]/nav/p[1]/a[1]')
        portal_page.click()
        print("Clicked on Portal link!")
        self.portal_login()
        sleep(10)

    # Logging user into the account and 2FA process
    def portal_login(self):
        login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[2]/input')
        login.click()
        sleep(3)

        # Enter username
        username_field = self.driver.find_element(By.ID, 'username')
        username_field.send_keys(username_input)
        print("Entered username")

        # Enter password
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password_input)
        print("Entered password")

        # Click login button 
        login_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[6]/button')
        login_button.click()
        print("Logged in. Waiting for 2FA duo iframe to load...")
        sleep(5)

        # Switching to DUO Security webpage
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.url_contains("duosecurity.com"))
        print("On duo page, will click on 'send a passcode' button")

        # Clicking on the "send a passcode" button
        authentication_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/div[3]/button')
        authentication_button.click()
        print("Clicked on 'Send a Passcode'")
        with open("cookies.pkl", "wb") as f:
            pickle.dump(self.driver.get_cookies(), f)

        sleep(3)

bot = CanvasBot()
bot.open_canvas()

# This keeps the terminal alive so Chrome doesn’t close
input("Press Enter to exit and close the browser...")
