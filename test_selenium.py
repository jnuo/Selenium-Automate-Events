import time
import config
from utils import (
    setup_chrome_driver,
    scroll_to_element,
    scroll_to_text,
    select_custom_account_code,
    update_input_value,
    toggle_auto_session,
    play_and_pause_video,
    click_button,
)
from events import (
    session_begin,
    appApiResult,
    appCrash,
    appError,
    appUIError,
    appLoginResult,
    appSignupResult,
    appTVPairResult
)

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
        # time.sleep(1)

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

        appLoginResult(driver, 'Success', 'Google', '200', '')
        time.sleep(1)

        appSignupResult(driver, 'Success', 'Email', '200', '')
        time.sleep(1)
        
        appTVPairResult(driver, 'Success', '200', '')
        time.sleep(1)

    except Exception as e:
        # Print the error to the console
        print(f"An error occurred: {e}")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
