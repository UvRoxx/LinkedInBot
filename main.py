from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os

linked_in_email = os.environ("EMAIL")
linked_in_pass = os.environ("PASSWORD")

driver_path = "/Users/utkarshvarma/Dropbox/My Mac (UTKARSHs-MacBook-Pro.local)/Documents/Development/chromedriver"
url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
job_url = "https://www.linkedin.com/jobs/search/?currentJobId=2294483366&f_LF=f_AL&geoId=101174742&keywords=python%20developer&location=Canada"

driver = webdriver.Chrome(driver_path)

driver.get(url)

email = driver.find_element_by_id("username")
email.send_keys(linked_in_email)
password = driver.find_element_by_id("password")
password.send_keys(linked_in_pass)
button = driver.find_element_by_tag_name("button")
button.click()

driver.get(job_url)
i = 4
sleep(2)
while i < 10:
    try:
        card = driver.find_elements_by_class_name("job-card-container")[i]
        card.click()
        sleep(2)
        buttons = driver.find_element_by_class_name(
            "jobs-details-top-card__container, flex-grow-1, jobs-details-top-card__actions-container, jobs-s-apply, "
            "jobs-apply-button--top-card").find_elements_by_tag_name("button")
        for button in buttons:
            if button.text == "Easy Apply":
                button.click()
        form = driver.find_element_by_class_name("jobs-easy-apply-content").find_element_by_tag_name(
            "form")
        number_content = form.find_element_by_tag_name("input")
        number_content.send_keys("5146064170")
        number_button = form.find_element_by_tag_name("button")
        number_button.click()

        final_button = form = driver.find_element_by_class_name("jobs-easy-apply-content").find_element_by_tag_name(
            "form").find_elements_by_tag_name("button")[3]
        final_button.click()

        # final_button = driver.find_element_by_class_name("ph5").find_element_by_tag_name("button")
        final_button = driver.find_elements_by_class_name('artdeco-button')[2]
        final_button.click()
        final_button.send_keys(Keys.ESCAPE)
    except NoSuchElementException:
        print("Skipped")
    except ElementClickInterceptedException:
        i += 1
        driver.refresh()
    except:
        print("bare error")
    finally:
        i += 1
