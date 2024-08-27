import time
import random
import config
from utils import (
    setup_chrome_driver,
    select_custom_account_code,
    update_input_value,
    toggle_auto_session,
    play_and_pause_video,
)
from events import (
    update_analytics_options,
    session_begin,
    appApiResult,
    appCrash,
    appError,
    appUIError,
    appLoginResult,
    appSignupResult,
    appTVPairResult
)

def select_random_user_name():
    """Generate a pool of user names and select one randomly."""
    user_names = [f"User {i}" for i in range(1, 94)]
    selected_user_name = random.choice(user_names)
    return selected_user_name

def update_analytics_options_with_random_user(driver, textarea_id):
    """Update analytics options with a randomly selected user name."""
    selected_user_name = select_random_user_name()
    
    # JSON data with the randomly selected user name
    json_data = {
        "app.name": "Web Testing Tool - Multiplayer App",
        "app.releaseVersion": "1.1.2",
        "user.name": selected_user_name,
        "content.title": "Custom Title - Analytics Options",
        "content.customDimensions": {
            "qa-custom-1": "mlucas",
            "qa-custom-2": "coiso",
            "qa-custom-3": "cenas"
        }
    }
    
    # Update analytics options with the generated JSON data
    update_analytics_options(driver, textarea_id, json_data)

def run_automation_task():
    """Run the automation task once."""
    driver = setup_chrome_driver()

    try:
        # Open the Vue.js application running on localhost
        driver.get(config.LOCALHOST_URL)
        time.sleep(1)

        # Update analytics options with a random user name
        update_analytics_options_with_random_user(driver, config.ANALYTICS_OPTIONS_TEXTAREA_ID)
        time.sleep(1)

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

        # Trigger other events
        appApiResult(driver, 32, 'signup', '/app/signup.aspx', '/signupEmail', 'Success', '200', '')
        time.sleep(1)

        appCrash(driver, 'signup', '/app/signup.aspx', 'java.lang.NullPointerException', 'Object not set to an instance of an object', '''
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

def main():
    """Main function to run the automated tasks repeatedly."""
    number_of_runs = 10  # Set the number of times you want to run the script

    for _ in range(number_of_runs):
        run_automation_task()
        print("Completed one run of the automation task.")
        time.sleep(2)  # Optional: Add a delay between runs if needed

if __name__ == "__main__":
    main()
