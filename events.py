from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
from utils import scroll_to_text, update_input_value, click_button  # Import necessary functions from utils

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
    update_input_value(driver, "apiEventValue1", responseTime)
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
    update_input_value(driver, "appCrashEventDimensionValue1", pageCategory)
    update_input_value(driver, "appErrorEventDimensionValue2", page)
    update_input_value(driver, "appErrorEventDimensionValue3", errorName)
    update_input_value(driver, "appErrorEventDimensionValue4", errorDescription)
    update_input_value(driver, "appErrorEventDimensionValue5", errorMetadata)
    time.sleep(1)
    click_button(driver, config.BUTTON_ID_APP_ERROR)

# App Analytics Custom Event: logAppUIError
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

# App Analytics Custom Event: appLoginResult
def appLoginResult():
    return 0

# App Analytics Custom Event: appSignupResult
def appSignupResult():
    return 0

# App Analytics Custom Event: appTVPairResult
def appTVPairResult():
    return 0
