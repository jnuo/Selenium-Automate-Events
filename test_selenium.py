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

def update_input_value(driver, input_id, value):
    """Updates the value of the input field with the given ID."""
    input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, input_id))
    )
    # scroll_to_element(driver, input_field)
    time.sleep(1)
    input_field.clear()
    input_field.send_keys(value)

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
        print(f"Auto session toggled to {'enabled' if should_enable else 'disabled'}.")
    else:
        print(f"Auto session already {'enabled' if should_enable else 'disabled'}.")

def session_begin(driver):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_SESSION_BEGIN)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_SESSION_BEGIN)

def appApiResult(driver, responseTime, pageCategory, page, apiMethod, responseStatus, errorName, errorDescription):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_APP_API_RESULT)
    time.sleep(1)
    update_input_value(driver, "apiEventValue1", responseTime)
    update_input_value(driver, "apiEventDimensionValue1", pageCategory)
    update_input_value(driver, "apiEventDimensionValue2", page)
    update_input_value(driver, "apiEventDimensionValue3", apiMethod)
    update_input_value(driver, "apiEventDimensionValue4", responseStatus)
    update_input_value(driver, "apiEventDimensionValue5", errorName)
    update_input_value(driver, "apiEventDimensionValue6", errorDescription)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_API_RESULT)

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
    button = driver.find_element(By.ID, config.BUTTON_ID_SESSION_BEGIN)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(10)

def appCrash(driver, pageCategory, page, errorName, errorDescription, errorMetadata):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_APP_CRASH)
    time.sleep(1)
    update_input_value(driver, "appCrashEventDimensionValue1", pageCategory)
    update_input_value(driver, "appCrashEventDimensionValue2", page)
    update_input_value(driver, "appCrashEventDimensionValue3", errorName)
    update_input_value(driver, "appCrashEventDimensionValue4", errorDescription)
    update_input_value(driver, "appCrashEventDimensionValue5", errorMetadata)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_CRASH)

def appError(driver, pageCategory, page, errorName, errorDescription, errorMetadata):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_APP_ERROR)
    time.sleep(1)
    update_input_value(driver, "appCrashEventDimensionValue1", pageCategory)
    update_input_value(driver, "appErrorEventDimensionValue2", page)
    update_input_value(driver, "appErrorEventDimensionValue3", errorName)
    update_input_value(driver, "appErrorEventDimensionValue4", errorDescription)
    update_input_value(driver, "appErrorEventDimensionValue5", errorMetadata)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_ERROR)

def appUIError(driver, pageCategory, page, errorName, errorDescription, uiErrorHeader, uiErrorBody):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_APP_UI_ERROR)
    time.sleep(1)
    update_input_value(driver, "appUIErrorEventDimensionValue1", pageCategory)
    update_input_value(driver, "appUIErrorEventDimensionValue2", page)
    update_input_value(driver, "appUIErrorEventDimensionValue3", errorName)
    update_input_value(driver, "appUIErrorEventDimensionValue4", errorDescription)
    update_input_value(driver, "appUIErrorEventDimensionValue5", uiErrorHeader)
    update_input_value(driver, "appUIErrorEventDimensionValue6", uiErrorBody)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_UI_ERROR)

def main():
    """Main function to run the automated tasks."""
    driver = setup_chrome_driver()

    try:
        # Open the Vue.js application running on localhost
        driver.get(config.LOCALHOST_URL)
        time.sleep(3)

        # Ensure the auto session start toggle is turned on
        toggle_auto_session(driver)
        time.sleep(1)

        # Choose Account Code: Custom
        select_custom_account_code(driver)
        time.sleep(1)
        
        # Input devyoubora as the Account Code
        update_input_value(driver, config.INPUT_ACCOUNT_CODE_ID, config.CUSTOM_ACCOUNT)
        time.sleep(1)

        # Play the video for 3 seconds and then pause it
        play_and_pause_video(driver, config.VIDEO_ELEMENT_ID, 3)
        time.sleep(1)

        # Session Begin Event
        session_begin(driver)
        time.sleep(1)

        # Scroll to the session begin section
        appApiResult(driver, 32, 'signup', '/app/signup.aspx', '/signupEmail', 'Success', '200', '')
        time.sleep(1)

        appCrash(driver, 
                    'signup', 
                    '/app/signup.aspx', 
                    'java.lang.NullPointerException', 
                    'Object not set to an instance of an object', 
                    '''
                    Exception in thread "main" java.lang.NullPointerException
                        at com.example.myproject.Book.getTitle(Book.java:16)        
                        at com.example.myproject.Author.getBookTitles(Author.java:25)        
                        at com.example.myproject.Bootstrap.main(Bootstrap.java:14)
                    '''
        )
        time.sleep(1)

        appError(driver,
                    'signup', 
                    '/app/signup.aspx', 
                    'java.lang.NullPointerException', 
                    'Object not set to an instance of an object', 
                    '''
                    Exception in thread "main" java.lang.NullPointerException
                        at com.example.myproject.Book.getTitle(Book.java:16)        
                        at com.example.myproject.Author.getBookTitles(Author.java:25)        
                        at com.example.myproject.Bootstrap.main(Bootstrap.java:14)
                    '''
        )
        time.sleep(1)

        appUIError(driver,
                   'signup',
                   '/app/login.aspx',
                   'password-incorrect',
                   'the password not match the username',
                   'Incorrect Password',
                   'The password you have entered does not match with the email address. Please check your password and try again.'
        )
        time.sleep(1)

    except Exception as e:
        # Print the error to the console
        print(f"An error occurred: {e}")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
