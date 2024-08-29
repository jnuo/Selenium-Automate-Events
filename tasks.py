import time
import random
from utils import setup_chrome_driver
from events import (
    update_analytics_options,
    session_begin,
    appApiResult,
    appCrash,
    appError,
    appUIError,
    appLoginResult,
    appSignupResult,
    appTVPairResult,
    click_fire_navigation,
    click_end_session
)
from utils import(
    toggle_auto_session,
    select_custom_account_code,
    update_input_value
)
from config import LOCALHOST_URL, ANALYTICS_OPTIONS_TEXTAREA_ID, INPUT_ACCOUNT_CODE_ID, CUSTOM_ACCOUNT, VIDEO_ELEMENT_ID

def select_random_user_name():
    """Generate a pool of user names and select one randomly."""
    user_names = [f"User {i}" for i in range(1, 94)]
    selected_user_name = random.choice(user_names)
    return selected_user_name

def select_random_device():
    """Select a random device type and device code based on the play distribution."""
    device_play_distribution = [
        ("SmartPhone", "Android", 35000),
        ("PC", "PCWindows", 30234),
        ("SmartPhone", "iPhone", 30000),
        ("STB", "AndroidTV", 25000),
        ("Tablet", "AndroidTablet", 21961),
        ("PC", "PCMac", 8215),
        ("TV", "LG", 3135),
        ("Tablet", "iPad", 2759),
        ("SmartPhone", "Android", 2653),
        ("TV", "SamsungTizen", 2502),
        ("Fire TV", "FireTV", 1239),
        ("TV", "Hisense", 1028),
        ("TV", "Roku3", 769),
        ("PC", "PCLinux", 722),
        ("Android TV", "SonyBravia", 427),
        ("Android TV", "Chromecast", 422),
        ("PC", "ChromeOS", 325),
        ("STB", "Android", 279),
        ("Tablet", "AndroidTablet", 154),
        ("TV", "Chromecast", 85),
        ("Fire TV", "Toshiba_STV", 25),
        ("STB", "Xiaomi", 24),
        ("Android TV", "Xiaomi", 19),
        ("STB", "PCLinux", 7),
        ("Tablet", "Hisense", 5),
        ("Fire TV", "Android", 4)
    ]

    # Create a weighted list of device type and device code pairs
    weighted_device_list = []
    for device_type, device_code, plays in device_play_distribution:
        weighted_device_list.extend([(device_type, device_code)] * plays)

    # Randomly select a device type and code pair from the weighted list
    selected_device_type, selected_device_code = random.choice(weighted_device_list)
    return selected_device_type, selected_device_code

def update_analytics_options_with_random_user(driver, textarea_id):
    """Update analytics options with a randomly selected user name."""
    selected_user_name = select_random_user_name()
    selected_device_type, selected_device_code = select_random_device()
  
    json_data = {
        "app.name": "Web Testing Tool - Multiplayer App",
        "device.code": selected_device_code,
        "device.type": selected_device_type,
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
    print(f'{selected_user_name} starts new session on {selected_device_type} & {selected_device_code}')

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
        ('Fail', 'Google', '403', 'Account disabled due to suspicious activity'),
        ('Fail', 'Google', '500', 'Internal server error during Google authentication'),
        ('Fail', 'Google', '404', 'Google account not found'),
        ('Fail', 'Google', '401', 'Google OAuth consent screen not completed'),
        ('Fail', 'Google', '503', 'Google service unavailable, try again later'),
        ('Fail', 'Google', '429', 'Too many login attempts on Google, please wait'),
        ('Fail', 'Google', '502', 'Bad gateway error during Google login'),
        ('Fail', 'Google', '403', 'Google login denied, account under review'),
        ('Fail', 'Google', '400', 'Malformed request to Google login API'),
        ('Fail', 'Google', '408', 'Request timeout during Google login'),
        ('Fail', 'Apple', '401', 'Invalid Apple ID credentials'),
        ('Fail', 'Apple', '403', 'User denied permission to Apple login'),
        ('Fail', 'Apple', '500', 'Apple authentication server error'),
        ('Fail', 'Apple', '404', 'Apple ID not found'),
        ('Fail', 'Apple', '409', 'Apple ID already in use in another session'),
        ('Fail', 'Apple', '403', 'Apple login restricted, account flagged for security'),
        ('Fail', 'Facebook', '403', 'User denied permission to Facebook login'),
        ('Fail', 'Facebook', '500', 'Error retrieving user profile from Facebook'),
        ('Fail', 'Facebook', '401', 'Invalid Facebook OAuth token'),
        ('Fail', 'Facebook', '403', 'Facebook login denied, app not authorized'),
        ('Fail', 'Facebook', '404', 'Facebook account not found'),
        ('Fail', 'Facebook', '409', 'Conflict during Facebook login, try again'),
        ('Fail', 'Email', '401', 'Invalid email or password'),
        ('Fail', 'Email', '403', 'User account is locked due to too many failed attempts'),
        ('Fail', 'Email', '500', 'Internal server error during email login'),
        ('Fail', 'Email', '404', 'Email account not found'),
        ('Fail', 'Email', '429', 'Too many requests, email login rate limited'),
        ('Fail', 'Email', '403', 'Email login restricted, account flagged for review'),
        ('Fail', 'Email', '408', 'Request timeout during email login'),
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
    if result[0] == 'Fail':
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
        ('Fail', 'Google', '400', 'Invalid Google account information provided'),
        ('Fail', 'Google', '409', 'Google account already registered'),
        ('Fail', 'Google', '422', 'Google account does not meet age requirements'),
        ('Fail', 'Google', '500', 'Google server error during signup'),
        ('Fail', 'Google', '403', 'Google account creation denied'),
        ('Fail', 'Apple', '400', 'Invalid Apple ID details'),
        ('Fail', 'Apple', '409', 'Apple ID already in use'),
        ('Fail', 'Apple', '422', 'Apple ID does not meet age requirements'),
        ('Fail', 'Apple', '500', 'Apple server error during signup'),
        ('Fail', 'Apple', '403', 'Apple account creation restricted'),
        ('Fail', 'Facebook', '400', 'Invalid Facebook account details'),
        ('Fail', 'Facebook', '409', 'Facebook account already exists'),
        ('Fail', 'Facebook', '422', 'Facebook account does not meet age requirements'),
        ('Fail', 'Facebook', '500', 'Facebook server error during signup'),
        ('Fail', 'Facebook', '403', 'Facebook account creation denied'),
        ('Fail', 'Email', '400', 'Invalid email address or details'),
        ('Fail', 'Email', '409', 'Email already registered'),
        ('Fail', 'Email', '422', 'Email does not meet age requirements'),
        ('Fail', 'Email', '500', 'Server error during email signup'),
        ('Fail', 'Email', '403', 'Email account creation restricted'),
        ('Fail', 'Email', '400', 'Password does not meet complexity requirements'),
        ('Fail', 'Email', '422', 'Email domain not supported'),
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
    if result[0] == 'Fail':
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

def generate_api_result(driver):
    """Randomly generate an API result for various video streaming actions, ensuring up to 25% error rate."""
    
    # Define success scenarios for different API methods with realistic app_page and appApiMethod values
    success_scenarios = {
        'browseGenre': [
            ('/genre/action', 'Success', 'loginGenre', '200', ''),
            ('/genre/comedy', 'Success', 'loginGenre', '200', ''),
        ],
        'browseRecommendations': [
            ('/recommendations/home', 'Success', 'fetchRecommendations', '200', ''),
            ('/recommendations/trending', 'Success', 'fetchRecommendations', '200', ''),
        ],
        'pagination': [
            ('/search/results', 'Success', 'pagination', '200', ''),
            ('/genre/action/page2', 'Success', 'pagination', '200', ''),
        ],
        'addToFavorites': [
            ('/favorites', 'Success', 'addFavorite', '200', ''),
            ('/favorites', 'Success', 'addFavorite', '200', ''),
        ],
        'removeFromFavorites': [
            ('/favorites', 'Success', 'removeFavorite', '200', ''),
            ('/favorites', 'Success', 'removeFavorite', '200', ''),
        ],
        'downloadToMobile': [
            ('/downloads', 'Success', 'downloadToMobile', '200', ''),
            ('/downloads', 'Success', 'downloadToMobile', '200', ''),
        ],
        'changeProfile': [
            ('/profile/change', 'Success', 'changeUserProfile', '200', ''),
            ('/profile/change', 'Success', 'changeUserProfile', '200', ''),
        ],
        'updateSettings': [
            ('/settings/video', 'Success', 'updateVideoSettings', '200', ''),
            ('/settings/audio', 'Success', 'updateAudioSettings', '200', ''),
        ]
    }
    
    # Define failure scenarios for different API methods with realistic app_page and appApiMethod values
    failure_scenarios = {
        'browseGenre': [
            ('/genre/action', 'Fail', 'loginGenre', '404', 'Genre not found'),
            ('/genre/comedy', 'Fail', 'loginGenre', '500', 'Server error while browsing genre'),
        ],
        'browseRecommendations': [
            ('/recommendations/home', 'Fail', 'fetchRecommendations', '500', 'Server error while fetching recommendations'),
            ('/recommendations/trending', 'Fail', 'fetchRecommendations', '503', 'Service unavailable for recommendations'),
        ],
        'pagination': [
            ('/search/results', 'Fail', 'pagination', '400', 'Bad request for pagination'),
            ('/genre/action/page2', 'Fail', 'pagination', '500', 'Server error during pagination'),
        ],
        'addToFavorites': [
            ('/favorites', 'Fail', 'addFavorite', '400', 'Bad request while adding to favorites'),
            ('/favorites', 'Fail', 'addFavorite', '500', 'Server error while adding to favorites'),
        ],
        'removeFromFavorites': [
            ('/favorites', 'Fail', 'removeFavorite', '400', 'Bad request while removing from favorites'),
            ('/favorites', 'Fail', 'removeFavorite', '500', 'Server error while removing from favorites'),
        ],
        'downloadToMobile': [
            ('/downloads', 'Fail', 'downloadToMobile', '403', 'Forbidden to start download'),
            ('/downloads', 'Fail', 'downloadToMobile', '500', 'Server error during download initiation'),
        ],
        'changeProfile': [
            ('/profile/change', 'Fail', 'changeUserProfile', '400', 'Bad request while changing profile'),
            ('/profile/change', 'Fail', 'changeUserProfile', '500', 'Server error while changing profile'),
        ],
        'updateSettings': [
            ('/settings/video', 'Fail', 'updateVideoSettings', '400', 'Bad request while updating video settings'),
            ('/settings/audio', 'Fail', 'updateAudioSettings', '500', 'Server error while updating audio settings'),
        ]
    }
    
    # Randomly select an API method
    api_method = random.choice(list(success_scenarios.keys()))

    # Randomly decide success or failure with a 75% success rate
    if random.random() <= 0.75:  # 75% chance to select a success scenario
        result = random.choice(success_scenarios[api_method])
    else:  # 25% chance to select a failure scenario
        result = random.choice(failure_scenarios[api_method])
    
    response_time = random.randint(10, 1250)  # Generate a random response time
    
    # Map the correct parameters
    app_page = result[0]  # This is the URL path or screen name
    response_status = result[1]  # Either "Success" or "Fail"
    api_method_value = result[2]  # Contextual action instead of HTTP method
    status_code = result[3]  # Status code, typically 200, 404, etc.
    error_description = result[4]  # Error description or empty string if successful
    
    print(f'\tAPI Method: {api_method}, App Page: {app_page}, API Action: {api_method_value}, Status: {response_status}, Status Code: {status_code}, Error Description: {error_description}, Response Time: {response_time}ms')
    
    # Call the appApiResult function with the correct mapping
    appApiResult(driver, response_time, api_method, app_page, api_method_value, response_status, status_code, error_description)

def run_scenario(driver):
    """Run a scenario based on random selection."""
    scenario_type = random.choice(['login_only', 'login_only', 'login_only', 'login_only', 'signup_only', 'signup_then_login'])

    if scenario_type == 'login_only':
        print("\tScenario: Login Only")
        generate_login_result(driver)
        # Generate a few API call results after login
        for _ in range(random.randint(1, 3)):  # Send 1 to 3 API calls
            generate_api_result(driver)

    elif scenario_type == 'signup_only':
        print("\tScenario: Signup Only")
        generate_signup_result(driver)
        # Generate a few API call results after signup
        for _ in range(random.randint(1, 3)):  # Send 1 to 3 API calls
            generate_api_result(driver)

    elif scenario_type == 'signup_then_login':
        print("\tScenario: Signup then Login")
        generate_signup_result(driver)
        time.sleep(1)
        generate_login_result(driver)
        # Generate a few API call results after signup and login
        for _ in range(random.randint(1, 5)):  # Send 1 to 5 API calls
            generate_api_result(driver)

    elif scenario_type == 'login_then_signup':
        print("\tScenario: Login then Signup")
        generate_login_result(driver)
        time.sleep(1)
        generate_signup_result(driver)
        # Generate a few API call results after login and signup
        for _ in range(random.randint(1, 5)):  # Send 1 to 5 API calls
            generate_api_result(driver)

def setup_new_session(driver):
    # Open the Vue.js application running on localhost
    driver.get(LOCALHOST_URL)
    time.sleep(1)

    # Update analytics options with a random user name
    update_analytics_options_with_random_user(driver, ANALYTICS_OPTIONS_TEXTAREA_ID)
    time.sleep(1)

    # Ensure the auto session start toggle is turned on
    toggle_auto_session(driver)
    time.sleep(1)

    # Choose Account Code: Custom
    select_custom_account_code(driver)
    time.sleep(1)
        
    # Input devyoubora as the Account Code
    update_input_value(driver, INPUT_ACCOUNT_CODE_ID, CUSTOM_ACCOUNT)
    time.sleep(1)
        
    # Click Fire Navigation button to start a session
    click_fire_navigation(driver)
    time.sleep(1)
    
    return driver

def run_automation_task():
    driver = setup_chrome_driver()
    try:
        setup_new_session(driver)
        run_scenario(driver)
        time.sleep(1)

    except Exception as e:
        # Print the error to the console
        print(f"An error occurred: {e}")

    finally:
        # Click End Session button to end the session
        click_end_session(driver)
        
        # Close the driver
        driver.quit()



 # Trigger other events

        # appCrash(driver, 'signup', '/app/signup.aspx', 'java.lang.NullPointerException', 'Object not set to an instance of an object', '''
        #             Exception in thread "main" java.lang.NullPointerException
        #                 at com.example.myproject.Book.getTitle(Book.java:16)        
        #                 at com.example.myproject.Author.getBookTitles(Author.java:25)        
        #                 at com.example.myproject.Bootstrap.main(Bootstrap.java:14)
        #             '''
        # )
        # time.sleep(1)

        # appError(driver,
        #             'signup',
        #             '/app/signup.aspx',
        #             'java.lang.NullPointerException',
        #             'Object not set to an instance of an object',
        #             '''
        #             Exception in thread "main" java.lang.NullPointerException
        #                 at com.example.myproject.Book.getTitle(Book.java:16)       
        #                 at com.example.myproject.Author.getBookTitles(Author.java:25)
        #                 at com.example.myproject.Bootstrap.main(Bootstrap.java:14)
        #             '''
        # )
        # time.sleep(1)

        # appUIError(driver,
        #            'signup',
        #            '/app/login.aspx',
        #            'password-incorrect',
        #            'the password not match the username',
        #            'Incorrect Password',
        #            'The password you have entered does not match with the email address. Please check your password and try again.'
        # )
        # time.sleep(1)

        # appTVPairResult(driver, 'Success', '200', '')
        # time.sleep(1)