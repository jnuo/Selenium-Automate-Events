# config.py

# Paths and URLs
CHROME_PROFILE_PATH = "/Users/ounrovali/Library/Application\ Support/Google/Chrome/Default" # work computer
# CHROME_PROFILE_PATH = "/Users/jnuo/Library/Application Support/Google/Chrome/Default" # home computer

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
LOCALHOST_URL = "http://localhost:5173/" # work computer
# LOCALHOST_URL = "https://www.google.com/" # home computer

# Element IDs and XPaths
ACCOUNT_CODE_DROPDOWN_ID = "account-code-dropdown"
CUSTOM_OPTION_XPATH = "//ul[contains(@class, 'dropdown-menu show')]//button[text()='Custom']"
AUTO_SESSION_CHECKBOX_ID = "autoSessionCheckbox"
INPUT_ACCOUNT_CODE_ID = "input-account-code"
CUSTOM_ACCOUNT = "devyoubora"
ANALYTICS_OPTIONS_TEXTAREA_ID = "textarea"

# CUSTOM_ACCOUNT = "root"
BUTTON_ID_SESSION_BEGIN = "btn_session_begin"
BUTTON_ID_API_RESULT = "btn_api_result"
BUTTON_ID_APP_CRASH = "btn_app_crash"
BUTTON_ID_APP_ERROR = "btn_app_error"
BUTTON_ID_APP_UI_ERROR = "btn_app_ui_error"
BUTTON_ID_APP_LOGIN_RESULT = "btn_app_login_result"
BUTTON_ID_APP_SIGNUP_RESULT = "btn_app_signup_result"
BUTTON_ID_APP_TVPAIR_RESULT = "btn_app_tvpair_result"
VIDEO_ELEMENT_ID = "videohlsjs"

# Text to scroll to
TEXT_SESSION_BEGIN = "App Analytics Custom Events: Session Begin"
TEXT_APP_API_RESULT = "App Analytics Custom Event: appApiResult"
TEXT_APP_CRASH = "App Analytics Custom Event: logAppCrash"
TEXT_APP_ERROR = "App Analytics Custom Event: logAppError"
TEXT_APP_UI_ERROR = "App Analytics Custom Event: logAppUIError"
TEXT_LOGIN_RESULT = "App Analytics Custom Event: appLoginResult"
TEXT_SIGNUP_RESULT = "App Analytics Custom Event: appSignupResult"
TEXT_TVPAIR_RESULT = "App Analytics Custom Event: appTVPairResult"
TEXT_PLAYER_SETTINGS = "Player Settings"
