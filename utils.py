import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config

def setup_chrome_driver():
    """Sets up the Chrome WebDriver with necessary options and returns the driver."""
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={config.CHROME_PROFILE_PATH}")
    # chrome_options.add_argument("--headless")  # Run in headless mode
    # chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    # chrome_options.add_argument("--window-size=1920,1080")  # Set window size to avoid issues with headless mode
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

    # Set up the webdriver
    service = Service(executable_path=config.CHROMEDRIVER_PATH)
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

def select_custom_account_code(driver):
    """Selects the 'Custom' option from the account code dropdown."""
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, config.ACCOUNT_CODE_DROPDOWN_ID))
    )
    scroll_to_element(driver, dropdown)
    time.sleep(1)
    dropdown.click()

    custom_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, config.CUSTOM_OPTION_XPATH))
    )
    custom_option.click()

# def changeTextArea(driver, textarea_id, json_data):
#     # Wait until the textarea is present in the DOM and is visible
#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, textarea_id))
#     )
#     # Clear any existing text in the textarea
#     textarea.clear()

#     # Convert the JSON object to a string
#     json_string = json.dumps(json_data, indent=4)
    
#     # Update the textarea with the new value
#     textarea.send_keys(json_string)
#     # print(f"Textarea with ID '{textarea_id}' updated with JSON successfully.")

def changeTextArea(driver, textarea_id, json_data):
    # Wait until the textarea is present in the DOM and is visible
    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, textarea_id))
    )
    # Clear any existing text in the textarea
    textarea.clear()

    # Convert the JSON object to a string
    json_string = json.dumps(json_data, indent=4).strip()

    # Extract all except the last character
    text_to_paste = json_string[:-1]
    last_character = json_string[-1]

    # Use JavaScript to set the value of the textarea minus the last character
    driver.execute_script(f"document.getElementById('{textarea_id}').value = `{text_to_paste}`;")

    # Now append the last character using send_keys to simulate the final keypress
    textarea.send_keys(last_character)

def update_input_value(driver, input_id, value):
    """Updates the value of the input field with the given ID."""
    input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, input_id))
    )
    
    scroll_to_element(driver, input_field)
    time.sleep(1)
    
    # Clear any existing text in the input field
    input_field.clear()

    if value:
        # Extract all except the last character
        text_to_paste = value[:-1]
        last_character = value[-1]

        # Use JavaScript to set the value of the input field minus the last character
        driver.execute_script(f"document.getElementById('{input_id}').value = `{text_to_paste}`;")

        # Optionally, trigger the 'input' event if required by the application logic
        driver.execute_script(f"document.getElementById('{input_id}').dispatchEvent(new Event('input'));")

        # Now append the last character using send_keys to simulate the final keypress
        input_field.send_keys(last_character)
    else:
        # If the value is an empty string, just ensure the input is cleared
        driver.execute_script(f"document.getElementById('{input_id}').value = '';")
        # Optionally, trigger the 'input' event if required by the application logic
        driver.execute_script(f"document.getElementById('{input_id}').dispatchEvent(new Event('input'));")



# def update_input_value(driver, input_id, value):
#     """Updates the value of the input field with the given ID."""
#     input_field = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, input_id))
#     )
#     scroll_to_element(driver, input_field)
#     time.sleep(1)
#     input_field.clear()
#     input_field.send_keys(value)

# def update_input_value(driver, input_id, value):
#     """Updates the value of the input field with the given ID using JavaScript to avoid triggering events on each key press."""
#     input_field = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, input_id))
#     )
#     scroll_to_element(driver, input_field)
#     time.sleep(1)
#     input_field.clear()

#     # Use JavaScript to set the value of the input field
#     driver.execute_script(f"document.getElementById('{input_id}').value = '{value}';")

#     # Optionally, trigger any 'change' or 'input' event if required by the application logic
#     driver.execute_script(f"document.getElementById('{input_id}').dispatchEvent(new Event('input'));")


def toggle_auto_session(driver, should_enable=True):
    """Toggles the auto session switch based on the desired state."""
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, config.AUTO_SESSION_CHECKBOX_ID))
    )
    scroll_to_element(driver, checkbox)
    time.sleep(1)
    is_checked = checkbox.is_selected()

    if is_checked != should_enable:
        checkbox.click()
        # print(f"\tAuto session toggled to {'enabled' if should_enable else 'disabled'}.")
    # else:
        # print(f"\tAuto session already {'enabled' if should_enable else 'disabled'}.")

def play_and_pause_video(driver, video_id, play_time):
    """Scrolls to the video section, plays the video for a specified time, and then pauses it."""
    scroll_to_text(driver, config.TEXT_PLAYER_SETTINGS)
    time.sleep(1)
    video_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, video_id))
    )
    scroll_to_element(driver, video_element)
    time.sleep(1)
    driver.execute_script("arguments[0].play();", video_element)
    time.sleep(play_time)
    driver.execute_script("arguments[0].pause();", video_element)

def click_button(driver, button_id):
    """Scrolls to the 'Session Begin' button and clicks it."""
    button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, button_id))
    )
    driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
