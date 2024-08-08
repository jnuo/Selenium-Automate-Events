from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
# Comment out or remove this line to run in non-headless mode
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Disable the first run and default browser check
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--no-default-browser-check")

# Add preferences to disable the search engine prompt
prefs = {
    "search.suggest_enabled": False,
    "browser.default_search_provider_enabled": True,
    "browser.default_search_provider_name": "Google",
    "browser.default_search_provider.search_url": "https://www.google.com/search?q={searchTerms}",
    "browser.default_search_provider_id": "google",
    "browser.default_search_provider_icon_url": "https://www.google.com/favicon.ico"
}
chrome_options.add_experimental_option("prefs", prefs)

# Set up the webdriver
service = Service(executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

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
    # Wait for the input field to be present
    wait = WebDriverWait(driver, 20)
    input_field = wait.until(
        EC.presence_of_element_located((By.ID, input_id))
    )
    # Clear the input field and set the new value
    input_field.clear()
    input_field.send_keys(value)

def session_begin(driver, text_session_begin, id_btn_session_begin):

    scroll_to_text(driver, text_session_begin)
    time.sleep(3)
    return 0

def play_and_pause_video(driver, video_id, play_time):
    """Plays the video for a specified time and then pauses it."""
    # Wait for the video element to be present
    wait = WebDriverWait(driver, 20)
    video_element = wait.until(
        EC.presence_of_element_located((By.ID, video_id))
    )
    scroll_to_element(driver, video_element)
    
    # Play the video
    driver.execute_script("arguments[0].play();", video_element)
    time.sleep(play_time)  # Play for the specified time

    # Pause the video
    driver.execute_script("arguments[0].pause();", video_element)

id_input_account_code = "input-account-code"
account_name = "devyoubora"
id_video = "videohlsjs"
id_btn_session_begin = "btn_session_begin"
text_session_begin = "App Analytics Custom Events: Session Begin"

try:
    # Open the Vue.js application running on localhost
    driver.get("http://localhost:5173/")

    # Update the value of the input field with ID "input-account-code" to "devyoubora"
    update_input_value(driver, id_input_account_code, account_name)

    # Play the video for 10 seconds and then pause it
    play_and_pause_video(driver, id_video, 3)

    # scroll to session begin
    session_begin(driver, text_session_begin, id_btn_session_begin)

finally:
    # Close the driver
    driver.quit()
