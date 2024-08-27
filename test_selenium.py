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
    print(f'user.name is {selected_user_name}')
    
    # Update analytics options with the generated JSON data
    update_analytics_options(driver, textarea_id, json_data)

def generate_login_result(driver):
    """Randomly generate a login result ensuring at least 85% success rate."""
    # Define success scenarios
    success_scenarios = [
        ('Success', 'Google', '200', ''),
        ('Success', 'Google', '200', ''),
        ('Success', 'Google', '200', ''),
        ('Success', 'Apple', '200', ''),
        ('Success', 'Facebook', '200', ''),
        ('Success', 'Email', '200', ''),
        ('Success', 'Email', '200', ''),
    ]
    
    # Define failure scenarios
    failure_scenarios = [
        ('Failure', 'Google', '403', 'Account disabled due to suspicious activity'),
        ('Failure', 'Google', '500', 'Internal server error during Google authentication'),
        ('Failure', 'Google', '404', 'Google account not found'),
        ('Failure', 'Google', '401', 'Google OAuth consent screen not completed'),
        ('Failure', 'Google', '503', 'Google service unavailable, try again later'),
        ('Failure', 'Google', '429', 'Too many login attempts on Google, please wait'),
        ('Failure', 'Google', '502', 'Bad gateway error during Google login'),
        ('Failure', 'Google', '403', 'Google login denied, account under review'),
        ('Failure', 'Google', '400', 'Malformed request to Google login API'),
        ('Failure', 'Google', '408', 'Request timeout during Google login'),
        ('Failure', 'Apple', '401', 'Invalid Apple ID credentials'),
        ('Failure', 'Apple', '403', 'User denied permission to Apple login'),
        ('Failure', 'Apple', '500', 'Apple authentication server error'),
        ('Failure', 'Apple', '404', 'Apple ID not found'),
        ('Failure', 'Apple', '409', 'Apple ID already in use in another session'),
        ('Failure', 'Apple', '403', 'Apple login restricted, account flagged for security'),
        ('Failure', 'Facebook', '403', 'User denied permission to Facebook login'),
        ('Failure', 'Facebook', '500', 'Error retrieving user profile from Facebook'),
        ('Failure', 'Facebook', '401', 'Invalid Facebook OAuth token'),
        ('Failure', 'Facebook', '403', 'Facebook login denied, app not authorized'),
        ('Failure', 'Facebook', '404', 'Facebook account not found'),
        ('Failure', 'Facebook', '409', 'Conflict during Facebook login, try again'),
        ('Failure', 'Email', '401', 'Invalid email or password'),
        ('Failure', 'Email', '403', 'User account is locked due to too many failed attempts'),
        ('Failure', 'Email', '500', 'Internal server error during email login'),
        ('Failure', 'Email', '404', 'Email account not found'),
        ('Failure', 'Email', '429', 'Too many requests, email login rate limited'),
        ('Failure', 'Email', '403', 'Email login restricted, account flagged for review'),
        ('Failure', 'Email', '408', 'Request timeout during email login'),
    ]
    
    # Weighted selection to ensure at least 85% success rate
    if random.random() <= 0.85:  # 85% chance to select a success scenario
        result = random.choice(success_scenarios)
    else:  # 15% chance to select a failure scenario
        result = random.choice(failure_scenarios)
    print(f'\tlogin result for this user is {str(result)}')
    
    # Call the appLoginResult function with the selected scenario
    appLoginResult(driver, *result)

    # If failure, decide whether to retry
    if result[0] == 'Failure':
        retry_chance = random.random()
        if retry_chance <= 0.5:  # 50% chance to retry
            wait_time = random.randint(2, 10)  # Wait between 2 and 10 seconds before retrying
            print(f"\tLogin failed. Waiting {wait_time} seconds before retrying...")
            time.sleep(wait_time)

            # 50% chance to succeed on retry
            if random.random() <= 0.5:
                success_result = random.choice(success_scenarios)
                print(f"\tRetrying login  result is {str(success_result)}.")
                appLoginResult(driver, *success_result)
            else:
                failed_result = random.choice(failure_scenarios)
                print(f"\tRetrying login  result is {str(failed_result)}.")
                appLoginResult(driver, *failed_result)

def generate_signup_result(driver):
    """Randomly generate a signup result ensuring up to 25% error rate, with different methods and scenarios."""
    # Define success scenarios
    success_scenarios = [
        ('Success', 'Google', '200', ''),
        ('Success', 'Google', '200', ''),
        ('Success', 'Google', '200', ''),
        ('Success', 'Apple', '200', ''),
        ('Success', 'Facebook', '200', ''),
        ('Success', 'Email', '200', ''),
        ('Success', 'Email', '200', ''),
    ]
    
    # Define failure scenarios
    failure_scenarios = [
        ('Failure', 'Google', '400', 'Invalid Google account information provided'),
        ('Failure', 'Google', '409', 'Google account already registered'),
        ('Failure', 'Google', '422', 'Google account does not meet age requirements'),
        ('Failure', 'Google', '500', 'Google server error during signup'),
        ('Failure', 'Google', '403', 'Google account creation denied'),
        ('Failure', 'Apple', '400', 'Invalid Apple ID details'),
        ('Failure', 'Apple', '409', 'Apple ID already in use'),
        ('Failure', 'Apple', '422', 'Apple ID does not meet age requirements'),
        ('Failure', 'Apple', '500', 'Apple server error during signup'),
        ('Failure', 'Apple', '403', 'Apple account creation restricted'),
        ('Failure', 'Facebook', '400', 'Invalid Facebook account details'),
        ('Failure', 'Facebook', '409', 'Facebook account already exists'),
        ('Failure', 'Facebook', '422', 'Facebook account does not meet age requirements'),
        ('Failure', 'Facebook', '500', 'Facebook server error during signup'),
        ('Failure', 'Facebook', '403', 'Facebook account creation denied'),
        ('Failure', 'Email', '400', 'Invalid email address or details'),
        ('Failure', 'Email', '409', 'Email already registered'),
        ('Failure', 'Email', '422', 'Email does not meet age requirements'),
        ('Failure', 'Email', '500', 'Server error during email signup'),
        ('Failure', 'Email', '403', 'Email account creation restricted'),
        ('Failure', 'Email', '400', 'Password does not meet complexity requirements'),
        ('Failure', 'Email', '422', 'Email domain not supported'),
    ]
    
    # Weighted selection to ensure up to 75% success rate and 25% failure rate
    if random.random() <= 0.75:  # 75% chance to select a success scenario
        result = random.choice(success_scenarios)
    else:  # 25% chance to select a failure scenario
        result = random.choice(failure_scenarios)
    print(f'\tsignup result for this user is {str(result)}')

    # Call the appSignupResult function with the selected scenario
    appSignupResult(driver, *result)

    # If failure, decide whether to retry
    if result[0] == 'Failure':
        retry_chance = random.random()
        if retry_chance <= 0.5:  # 50% chance to retry
            wait_time = random.randint(2, 10)  # Wait between 2 and 10 seconds before retrying
            print(f"\tSignup failed. Waiting {wait_time} seconds before retrying...")
            time.sleep(wait_time)

            # 50% chance to succeed on retry
            if random.random() <= 0.5:
                success_result = random.choice(success_scenarios)
                print(f"\tRetrying signup result is {str(success_result)}.")
                appSignupResult(driver, *success_result)
            else:
                failed_result = random.choice(failure_scenarios)
                print(f"\tRetrying signup result is {str(failed_result)}.")
                appSignupResult(driver, *failed_result)

def run_scenario(driver):
    """Run a scenario based on random selection."""
    scenario_type = random.choice(['login_only', 'signup_only', 'signup_then_login', 'login_then_signup'])

    if scenario_type == 'login_only':
        print("\tScenario: Login Only")
        generate_login_result(driver)

    elif scenario_type == 'signup_only':
        print("\tScenario: Signup Only")
        generate_signup_result(driver)

    elif scenario_type == 'signup_then_login':
        print("\tScenario: Signup then Login")
        generate_signup_result(driver)
        time.sleep(2)
        generate_login_result(driver)

    elif scenario_type == 'login_then_signup':
        print("\tScenario: Login then Signup")
        generate_login_result(driver)
        time.sleep(2)
        generate_signup_result(driver)

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

        # Run a scenario (login, signup, or both)
        run_scenario(driver)

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
        print("\tCompleted one run of the automation task.")
        time.sleep(2)  # Optional: Add a delay between runs if needed

if __name__ == "__main__":
    main()
