from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_chrome_driver():
    """Sets up the Chrome WebDriver with necessary options and returns the driver."""
    chrome_options = Options()

    # Path to your Chrome profile directory
    profile_path = "/Users/ounrovali/Library/Application Support/Google/Chrome/Profile 1"  # Replace this with the actual path to your profile

    chrome_options.add_argument(f"user-data-dir={profile_path}")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")

    # Set up the webdriver
    service = Service(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scroll_to_element(driver, element):
    """Scrolls to a specific element on the page."""
    driver.execute_script("arguments[0].scrollIntoView();", element)

def scroll_to_text(driver, text):
    """Scrolls to an element containing the specified text."""
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
    )
    scroll_to_element(driver, element)

def update_input_value(driver, input_id, value):
    """Updates the value of the input field with the given ID."""
    input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, input_id))
    )
    input_field.clear()
    input_field.send_keys(value)

def session_begin(driver, text_session_begin, id_btn_session_begin):
    """Scrolls to the 'Session Begin' section and waits briefly."""
    scroll_to_text(driver, text_session_begin)

def play_and_pause_video(driver, video_id, play_time):
    """Plays the video for a specified time and then pauses it."""
    video_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, video_id))
    )
    scroll_to_element(driver, video_element)
    driver.execute_script("arguments[0].play();", video_element)
    time.sleep(play_time)
    driver.execute_script("arguments[0].pause();", video_element)

def main():
    """Main function to run the automated tasks."""
    driver = setup_chrome_driver()

    try:
        # Open the Vue.js application running on localhost
        driver.get("http://localhost:5173/")
        time.sleep(3)

        # Update the value of the input field with ID "input-account-code"
        update_input_value(driver, "input-account-code", "devyoubora")
        time.sleep(3)

        # Play the video for 3 seconds and then pause it
        play_and_pause_video(driver, "videohlsjs", 3)
        time.sleep(3)

        # Scroll to the session begin section
        session_begin(driver, "App Analytics Custom Events: Session Begin", "btn_session_begin")
        time.sleep(3)

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
