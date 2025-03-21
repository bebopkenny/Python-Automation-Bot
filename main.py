from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

username_input = "kennygarcia15"
password_input = "Leviackerman123."

class CanvasBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_canvas(self):
        self.driver.get('https://www.fullerton.edu/')
        sleep(3)  # wait for the page to load

        portal_page = self.driver.find_element(By.XPATH, '/html/body/div[2]/header[3]/nav/p[1]/a[1]')
        portal_page.click()
        print("Clicked on Portal link!")
        self.portal_login()
        sleep(10)

    def portal_login(self):
        login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[2]/input')
        login.click()
        sleep(3)

        # Fill in the username
        username_field = self.driver.find_element(By.ID, 'username')
        username_field.send_keys(username_input)

        # Fill in the password
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password_input)

        # Click on the login button
        login_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[6]/button')
        login_button.click()
        sleep(3)

bot = CanvasBot()
bot.open_canvas()
