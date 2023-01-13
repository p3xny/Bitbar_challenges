import os
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r'C:/SeleniumDrivers'


driver = webdriver.Chrome()
driver.get('https://cloud.bitbar.com/')
driver.maximize_window()
driver.implicitly_wait(10)
print(f'{driver.capabilities["browserVersion"]}')


wait = WebDriverWait(driver, 10)


# Challenge 1:
    # Open the preferred webdriver, for example Chromium for Google Chrome.
    # Enter this website: "https://cloud.bitbar.com/".
    # Login an already existing user.
    # Logout the user account.

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


    def login(self):
        email_field = driver.find_element(By.ID, 'login-email')
        email_field.send_keys(self.email)


        pass_field = driver.find_element(By.ID, 'login-password')
        pass_field.send_keys(self.password)


        sign_in_btn = driver.find_element(By.ID, 'login-submit')
        sign_in_btn.click()

    
    @staticmethod
    def logout():
        user_dropdown_button = driver.find_element(By.ID, 'header-menu-user')
        user_dropdown_button.click()

        time.sleep(2)

        logout_button = driver.find_element(By.ID, 'menu-user-logout')
        logout_button.click()


user_john = User('john.maruo100@gmail.com', 'UiopJklBnm,.')
User.login(user_john)
User.logout()
time.sleep(5)


# Challenge 2:
    # Login to an already existing user account.
    # Enter the "Projects" tab.
    # Create 3 new projects with random generated names containing 10 letters each.
    # Delete the created projects in reversed alphabetical order..
    # Exit the webdriver.

User.login(user_john)


def list_to_string(list):
    return "".join(str(item) for item in list)


all_letters = list(string.ascii_lowercase)
project_names = []
project_count = 3
random_letters_count = 10


def generate_project_names():
    for _ in range(project_count):
        randomized_letters = []

        for _ in range(random_letters_count):
            random_letter = random.choice(all_letters)
            randomized_letters.append(random_letter)

        project_name = list_to_string(randomized_letters)
        project_names.append(project_name)


def create_projects(project_names):
 
    for project in project_names:
        create_project_button = driver.find_element(By.XPATH, '//*[@id="testing_projects-Testing_Projects_0"]/div[1]/div[3]')
        create_project_button.click()

        name_project_field = driver.find_element(By.ID, 'form-name')
        name_project_field.send_keys(project)

        submit_project_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[title="Create"]')
            )
        )
        submit_project_button.click()
        time.sleep(2)


def remove_projects_reversed():
    project_names_reversed = sorted(project_names, reverse=True)
    print(project_names_reversed)

    for name in project_names_reversed:
        print(name)
        search_project = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')
        search_project.clear()
        search_project.send_keys(name)

        try:
            project_settings = driver.find_element(By.CLASS_NAME, 'dropdown-trigger')
            project_settings.click()

            remove_project = driver.find_element(By.CLASS_NAME, 'fa-trash')
            remove_project.click()

            delete_button = driver.find_element(By.CLASS_NAME, 'btn-danger')
            delete_button.click()
        except:
            print('something went wrong')

        time.sleep(2)


projects_site = driver.find_element(By.ID, 'menu-main-testing-projects')
projects_site.click()


generate_project_names()
create_projects(project_names)
remove_projects_reversed()


time.sleep(5)
driver.quit()