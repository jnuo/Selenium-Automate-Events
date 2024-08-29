from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
from utils import scroll_to_text, update_input_value, click_button, changeTextArea, scroll_to_element

# Change the textarea value
def update_analytics_options(driver, textarea_id, new_text):
    changeTextArea(driver, textarea_id, new_text)

def click_fire_navigation(driver):
    """Clicks the 'Fire Navigation' button by its ID after scrolling into view."""
    fire_navigation_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, config.BUTTON_FIRE_NAVIGATION))
    )
    # Scroll to the button before clicking it
    scroll_to_element(driver, fire_navigation_button)
    time.sleep(1)
    fire_navigation_button.click()
    print("\tClicked the 'Fire Navigation' button.")

def click_end_session(driver):
    """Clicks the 'End Session' button by its ID after scrolling into view."""
    scroll_to_text(driver, "App Analytics Session Events")
    time.sleep(1)
    end_session_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, config.BUTTON_END_SESSION))
    )
    # Scroll to the button before clicking it
    scroll_to_element(driver, end_session_button)
    end_session_button.click()
    print("\tClicked the 'End Session' button.")

# App Analytics Custom Events: Session Begin
def session_begin(driver):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_SESSION_BEGIN)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_SESSION_BEGIN)

# App Analytics Custom Event: appApiResult
def appApiResult(driver, responseTime, pageCategory, page, apiMethod, responseStatus, errorName, errorDescription):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_APP_API_RESULT)
    time.sleep(1)
    update_input_value(driver, "apiEventValue1", str(responseTime))
    update_input_value(driver, "apiEventDimensionValue1", pageCategory)
    update_input_value(driver, "apiEventDimensionValue2", page)
    update_input_value(driver, "apiEventDimensionValue3", apiMethod)
    update_input_value(driver, "apiEventDimensionValue4", responseStatus)
    update_input_value(driver, "apiEventDimensionValue5", errorName)
    update_input_value(driver, "apiEventDimensionValue6", errorDescription)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_API_RESULT)

# App Analytics Custom Event: logAppCrash
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

# App Analytics Custom Event: logAppError
def appError(driver, pageCategory, page, errorName, errorDescription, errorMetadata):
    """Scrolls to the 'Session Begin' section."""
    scroll_to_text(driver, config.TEXT_APP_ERROR)
    time.sleep(1)
    update_input_value(driver, "appErrorEventDimensionValue1", pageCategory)
    update_input_value(driver, "appErrorEventDimensionValue2", page)
    update_input_value(driver, "appErrorEventDimensionValue3", errorName)
    update_input_value(driver, "appErrorEventDimensionValue4", errorDescription)
    update_input_value(driver, "appErrorEventDimensionValue5", errorMetadata)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_ERROR)

# App Analytics Custom Event: logAppUIError
def appUIError(driver, pageCategory, page, errorName, errorDescription, uiErrorHeader, uiErrorBody):
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

# App Analytics Custom Event: appLoginResult
def appLoginResult(driver, loginStatus, loginType, errorName, errorDescription):
    scroll_to_text(driver, config.TEXT_LOGIN_RESULT)
    time.sleep(1)
    update_input_value(driver, "appLoginResultEventDimensionValue1", loginStatus)
    update_input_value(driver, "appLoginResultEventDimensionValue2", loginType)
    update_input_value(driver, "appLoginResultEventDimensionValue3", errorName)
    update_input_value(driver, "appLoginResultEventDimensionValue4", errorDescription)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_LOGIN_RESULT)

# App Analytics Custom Event: appSignupResult
def appSignupResult(driver, signupStatus, signupType, errorName, errorDescription):
    scroll_to_text(driver, config.TEXT_SIGNUP_RESULT)
    time.sleep(1)
    update_input_value(driver, "appSignupResultEventDimensionValue1", signupStatus)
    update_input_value(driver, "appSignupResultEventDimensionValue2", signupType)
    update_input_value(driver, "appSignupResultEventDimensionValue3", errorName)
    update_input_value(driver, "appSignupResultEventDimensionValue4", errorDescription)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_SIGNUP_RESULT)

# App Analytics Custom Event: appTVPairResult
def appTVPairResult(driver, tvPairStatus, errorName, errorDescription):
    scroll_to_text(driver, config.TEXT_TVPAIR_RESULT)
    time.sleep(1)
    update_input_value(driver, "appTVPairResultEventDimensionValue1", tvPairStatus)
    update_input_value(driver, "appTVPairResultEventDimensionValue2", errorName)
    update_input_value(driver, "appTVPairResultEventDimensionValue3", errorDescription)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_TVPAIR_RESULT)
