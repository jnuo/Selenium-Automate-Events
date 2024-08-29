import time
import random
from utils import setup_chrome_driver
from events import (
    update_analytics_options,
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
from config import LOCALHOST_URL, ANALYTICS_OPTIONS_TEXTAREA_ID, INPUT_ACCOUNT_CODE_ID, CUSTOM_ACCOUNT

def setup_new_session(driver):
    # Open the Vue.js application running on localhost
    driver.get(LOCALHOST_URL)
    time.sleep(1)

    # Update analytics options with a random user name
    update_analytics_options_with_random_user_random_device(driver)
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

def update_analytics_options_with_random_user_random_device(driver):
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
    update_analytics_options(driver, ANALYTICS_OPTIONS_TEXTAREA_ID, json_data)
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
            wait_time = random.randint(1, 1)  # Wait between 2 and 10 seconds before retrying
            print(f"\tLogin failed. Waiting {wait_time} seconds before retrying...")
            time.sleep(1)

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
            wait_time = random.randint(1, 1)  # Wait between 2 and 10 seconds before retrying
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
    error_code = result[3]  # Status code, typically 200, 404, etc.
    error_description = result[4]  # Error description or empty string if successful
    
    print(f'\tAPI Method: {api_method}, App Page: {app_page}, API Action: {api_method_value}, API Response Status: {response_status}, Error Code: {error_code}, Response Time: {response_time}ms')
    
    # Call the appApiResult function with the correct mapping
    appApiResult(driver, response_time, api_method, app_page, api_method_value, response_status, error_code, error_description)

def generate_app_crash(driver):
    """Randomly generate an app crash event with realistic error details."""
    
    crash_scenarios = [
        # (pageCategory, page, errorName, errorDescription, errorMetadata)
        ('loginGenre', '/genre/action', 'NullPointerException', 'Attempt to invoke a method on a null object reference', 
         'Exception in thread "main" java.lang.NullPointerException\n    at com.example.myproject.Book.getTitle(Book.java:16)\n    at com.example.myproject.Author.getBookTitles(Author.java:25)\n    at com.example.myproject.Bootstrap.main(Bootstrap.java:14)'),
        
        ('loginGenre', '/genre/action', 'IndexOutOfBoundsException', 'Index 5 out of bounds for length 3', 
         'java.lang.IndexOutOfBoundsException: Index 5 out of bounds for length 3\n    at java.base/java.util.ArrayList.rangeCheck(ArrayList.java:659)\n    at java.base/java.util.ArrayList.get(ArrayList.java:435)\n    at com.example.myproject.Library.getBook(Library.java:47)\n    at com.example.myproject.Reader.readBook(Reader.java:22)'),
        
        ('fetchRecommendations', '/recommendations/home', 'IllegalArgumentException', 'Invalid argument passed to method', 
         'java.lang.IllegalArgumentException: Invalid argument passed to method\n    at com.example.myproject.Calculator.addNumbers(Calculator.java:11)\n    at com.example.myproject.Main.main(Main.java:6)'),
        
        ('pagination', '/search/results', 'ArrayIndexOutOfBoundsException', 'Array index is out of range', 
         'java.lang.ArrayIndexOutOfBoundsException: Index 10 out of bounds for length 5\n    at com.example.myproject.ArrayProcessor.processArray(ArrayProcessor.java:29)\n    at com.example.myproject.Main.main(Main.java:14)'),
        
        ('addFavorite', '/favorites', 'FileNotFoundException', 'File not found in the specified directory', 
         'java.io.FileNotFoundException: /user/home/document.txt (No such file or directory)\n    at java.base/java.io.FileInputStream.open0(Native Method)\n    at java.base/java.io.FileInputStream.open(FileInputStream.java:213)\n    at com.example.myproject.FileReader.readFile(FileReader.java:19)'),
        
        ('removeFavorite', '/favorites', 'SocketTimeoutException', 'Connection timed out after 30000 milliseconds', 
         'java.net.SocketTimeoutException: connect timed out\n    at java.base/java.net.PlainSocketImpl.waitForConnect(Native Method)\n    at java.base/java.net.PlainSocketImpl.socketConnect(PlainSocketImpl.java:107)\n    at java.base/java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:206)\n    at com.example.myproject.NetworkManager.connect(NetworkManager.java:42)'),
        
        ('downloadToMobile', '/downloads', 'ClassNotFoundException', 'Specified class not found in classpath', 
         'java.lang.ClassNotFoundException: com.example.myproject.MissingClass\n    at java.base/java.net.URLClassLoader.findClass(URLClassLoader.java:471)\n    at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:589)\n    at com.example.myproject.Main.main(Main.java:18)'),
        
        ('changeUserProfile', '/profile/change', 'OutOfMemoryError', 'Java heap space exceeded', 
         'java.lang.OutOfMemoryError: Java heap space\n    at java.base/java.util.Arrays.copyOf(Arrays.java:3721)\n    at com.example.myproject.LargeObject.allocate(LargeObject.java:56)\n    at com.example.myproject.Main.main(Main.java:20)'),
        
        ('updateVideoSettings', '/settings/video', 'IllegalStateException', 'Method has been invoked at an illegal or inappropriate time', 
         'java.lang.IllegalStateException: Cannot call method after it has been closed\n    at com.example.myproject.Resource.close(Resource.java:33)\n    at com.example.myproject.Manager.manage(Manager.java:14)\n    at com.example.myproject.Main.main(Main.java:17)'),
        
        ('updateAudioSettings', '/settings/audio', 'NumberFormatException', 'Invalid number format during parsing', 
         'java.lang.NumberFormatException: For input string: "abc123"\n    at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)\n    at com.example.myproject.Parser.parseNumber(Parser.java:11)\n    at com.example.myproject.Main.main(Main.java:9)'),
        
        ('fetchRecommendations', '/recommendations/trending', 'SecurityException', 'Access denied due to security policy', 
         'java.lang.SecurityException: Permission denied\n    at java.base/java.lang.SecurityManager.checkPermission(SecurityManager.java:608)\n    at com.example.myproject.AccessControl.checkAccess(AccessControl.java:22)\n    at com.example.myproject.Main.main(Main.java:15)'),
        
        ('loginGenre', '/genre/comedy', 'SQLSyntaxErrorException', 'Syntax error in SQL query', 
         'java.sql.SQLSyntaxErrorException: You have an error in your SQL syntax\n    at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:118)\n    at com.example.myproject.Database.executeQuery(Database.java:29)\n    at com.example.myproject.Main.main(Main.java:18)'),
        
        ('pagination', '/genre/action/page2', 'ClassCastException', 'Cannot cast object of type \'String\' to \'Integer\'', 
         'java.lang.ClassCastException: java.lang.String cannot be cast to java.lang.Integer\n    at com.example.myproject.Converter.convert(Converter.java:14)\n    at com.example.myproject.Main.main(Main.java:11)'),
        
        ('addFavorite', '/favorites', 'IOException', 'I/O operation failed or was interrupted', 
         'java.io.IOException: Stream closed\n    at java.base/java.io.BufferedInputStream.getBufIfOpen(BufferedInputStream.java:168)\n    at com.example.myproject.StreamProcessor.process(StreamProcessor.java:33)\n    at com.example.myproject.Main.main(Main.java:20)'),
        
        ('removeFavorite', '/favorites', 'UnsupportedOperationException', 'Operation is not supported', 
         'java.lang.UnsupportedOperationException: Operation is not supported\n    at com.example.myproject.Feature.execute(Feature.java:21)\n    at com.example.myproject.Main.main(Main.java:16)'),
        
        ('downloadToMobile', '/downloads', 'ConcurrentModificationException', 'Concurrent modification detected during iteration', 
         'java.util.ConcurrentModificationException\n    at java.base/java.util.ArrayList$Itr.checkForComodification(ArrayList.java:1013)\n    at java.base/java.util.ArrayList$Itr.next(ArrayList.java:967)\n    at com.example.myproject.IteratorExample.iterate(IteratorExample.java:28)\n    at com.example.myproject.Main.main(Main.java:22)'),
        
        ('changeUserProfile', '/profile/change', 'StackOverflowError', 'Stack overflow due to recursive method calls', 
         'java.lang.StackOverflowError\n    at com.example.myproject.RecursionExample.recursiveMethod(RecursionExample.java:10)\n    at com.example.myproject.RecursionExample.recursiveMethod(RecursionExample.java:11)\n    at com.example.myproject.Main.main(Main.java:13)'),
        
        ('updateVideoSettings', '/settings/video', 'FileAlreadyExistsException', 'File already exists and cannot be overwritten', 
         'java.nio.file.FileAlreadyExistsException: /user/home/document.txt\n    at java.base/sun.nio.fs.UnixException.translateToIOException(UnixException.java:94)\n    at com.example.myproject.FileManager.createFile(FileManager.java:22)\n    at com.example.myproject.Main.main(Main.java:10)'),
        
        ('updateAudioSettings', '/settings/audio', 'ArithmeticException', 'Division by zero', 
         'java.lang.ArithmeticException: / by zero\n    at com.example.myproject.Calculator.divide(Calculator.java:13)\n    at com.example.myproject.Main.main(Main.java:15)'),
        
        ('loginGenre', '/genre/action', 'TimeoutException', 'Operation timed out after waiting for 60 seconds', 
         'java.util.concurrent.TimeoutException: Operation timed out\n    at com.example.myproject.Operation.execute(Operation.java:34)\n    at com.example.myproject.Main.main(Main.java:11)'),
        
        ('fetchRecommendations', '/recommendations/home', 'FileSystemException', 'File system error during file operation', 
         'java.nio.file.FileSystemException: /user/home/document.txt: No space left on device\n    at java.base/sun.nio.fs.UnixException.translateToIOException(UnixException.java:92)\n    at com.example.myproject.FileManager.saveFile(FileManager.java:18)\n    at com.example.myproject.Main.main(Main.java:9)'),
        
        ('pagination', '/search/results', 'BufferOverflowException', 'Attempt to write beyond buffer\'s limit', 
         'java.nio.BufferOverflowException\n    at java.base/java.nio.Buffer.checkOverflow(Buffer.java:145)\n    at com.example.myproject.BufferHandler.write(BufferHandler.java:32)\n    at com.example.myproject.Main.main(Main.java:14)'),
        
        ('addFavorite', '/favorites', 'MalformedURLException', 'Invalid URL format', 
         'java.net.MalformedURLException: no protocol: example.com\n    at java.base/java.net.URL.<init>(URL.java:620)\n    at com.example.myproject.UrlProcessor.processUrl(UrlProcessor.java:11)\n    at com.example.myproject.Main.main(Main.java:9)'),
        
        ('removeFavorite', '/favorites', 'InterruptedException', 'Thread interrupted while waiting', 
         'java.lang.InterruptedException: sleep interrupted\n    at java.base/java.lang.Thread.sleep(Native Method)\n    at com.example.myproject.ThreadManager.waitForCompletion(ThreadManager.java:25)\n    at com.example.myproject.Main.main(Main.java:12)'),
        
        ('downloadToMobile', '/downloads', 'BrokenBarrierException', 'Broken barrier detected in multithreaded operation', 
         'java.util.concurrent.BrokenBarrierException\n    at java.base/java.util.concurrent.CyclicBarrier.dowait(CyclicBarrier.java:257)\n    at com.example.myproject.ConcurrencyExample.await(ConcurrencyExample.java:33)\n    at com.example.myproject.Main.main(Main.java:11)')
    ]
    
    # Randomly select a crash scenario
    crash_scenario = random.choice(crash_scenarios)
    
    page_category, page, error_name, error_description, error_metadata = crash_scenario
    
    print(f'\tApp Crash Event: {error_name}, Description: {error_description}')
    
    # Call the appCrash function with the selected scenario
    appCrash(driver, page_category, page, error_name, error_description, error_metadata)

def generate_app_error(driver):
    """Randomly generate an app error event with realistic error details."""
    
    error_scenarios = [
        # (pageCategory, page, errorName, errorDescription, errorMetadata)
        ('fetchData', '/data/fetch', 'NetworkError', 'Failed to fetch data from server', 
         'java.net.ConnectException: Connection refused\n    at java.base/java.net.PlainSocketImpl.socketConnect(PlainSocketImpl.java:107)\n    at java.base/java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:206)\n    at com.example.myproject.DataFetcher.fetchData(DataFetcher.java:45)\n    at com.example.myproject.MainActivity.loadData(MainActivity.java:88)'),
        
        ('loginAttempt', '/login', 'AuthenticationError', 'Invalid credentials provided', 
         'java.lang.SecurityException: Invalid credentials\n    at com.example.myproject.AuthenticationManager.authenticate(AuthenticationManager.java:54)\n    at com.example.myproject.LoginActivity.attemptLogin(LoginActivity.java:112)'),
        
        ('saveSettings', '/settings/save', 'DatabaseError', 'Failed to save settings to the database', 
         'java.sql.SQLException: Unable to insert record into settings table\n    at com.example.myproject.DatabaseManager.saveSettings(DatabaseManager.java:67)\n    at com.example.myproject.SettingsActivity.save(SettingsActivity.java:53)'),
        
        ('syncData', '/data/sync', 'TimeoutError', 'Data synchronization timed out', 
         'java.util.concurrent.TimeoutException: Synchronization operation timed out\n    at com.example.myproject.SyncManager.syncData(SyncManager.java:98)\n    at com.example.myproject.SyncService.startSync(SyncService.java:45)'),
        
        ('loadProfile', '/profile/load', 'ParsingError', 'Failed to parse user profile data', 
         'java.lang.NumberFormatException: For input string: "abc123"\n    at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)\n    at com.example.myproject.ProfileParser.parse(ProfileParser.java:32)\n    at com.example.myproject.ProfileActivity.loadProfile(ProfileActivity.java:77)'),
        
        ('fetchRecommendations', '/recommendations/fetch', 'APILimitExceededError', 'API rate limit exceeded', 
         'java.lang.Exception: API rate limit exceeded\n    at com.example.myproject.ApiClient.handleResponse(ApiClient.java:122)\n    at com.example.myproject.RecommendationService.fetchRecommendations(RecommendationService.java:66)'),
        
        ('backgroundTask', '/task/execute', 'TaskExecutionError', 'Background task failed to complete', 
         'java.lang.Exception: Task execution failed\n    at com.example.myproject.TaskExecutor.execute(TaskExecutor.java:89)\n    at com.example.myproject.BackgroundService.runTask(BackgroundService.java:39)'),
        
        ('uploadData', '/data/upload', 'FileUploadError', 'Error occurred while uploading file', 
         'java.io.IOException: Failed to upload file due to network issues\n    at com.example.myproject.UploadManager.uploadFile(UploadManager.java:57)\n    at com.example.myproject.FileUploadActivity.upload(FileUploadActivity.java:46)'),
        
        ('loadData', '/data/load', 'DataProcessingError', 'Error while processing loaded data', 
         'java.lang.IllegalArgumentException: Invalid data format received\n    at com.example.myproject.DataProcessor.process(DataProcessor.java:29)\n    at com.example.myproject.DataLoader.load(DataLoader.java:42)'),
        
        ('initService', '/service/init', 'ServiceInitializationError', 'Failed to initialize the required service', 
         'java.lang.IllegalStateException: Service initialization failed due to missing dependencies\n    at com.example.myproject.ServiceManager.initService(ServiceManager.java:36)\n    at com.example.myproject.MainActivity.startService(MainActivity.java:52)'),
        
        ('apiCall', '/api/call', 'ResponseParsingError', 'Failed to parse response from API call', 
         'java.lang.Exception: Unexpected response format\n    at com.example.myproject.ApiClient.parseResponse(ApiClient.java:78)\n    at com.example.myproject.ApiService.makeCall(ApiService.java:41)'),
        
        ('dataBackup', '/backup/data', 'BackupError', 'Error during data backup operation', 
         'java.io.IOException: Data backup failed due to insufficient storage\n    at com.example.myproject.BackupManager.performBackup(BackupManager.java:34)\n    at com.example.myproject.BackupService.startBackup(BackupService.java:22)'),
        
        ('fileProcessing', '/file/process', 'FileProcessingError', 'Error processing the file', 
         'java.nio.file.FileSystemException: Failed to process file: access denied\n    at com.example.myproject.FileProcessor.process(FileProcessor.java:58)\n    at com.example.myproject.FileService.run(FileService.java:27)'),
        
        ('updateProfile', '/profile/update', 'ValidationError', 'User profile validation failed', 
         'java.lang.IllegalArgumentException: Invalid user profile details\n    at com.example.myproject.ProfileValidator.validate(ProfileValidator.java:44)\n    at com.example.myproject.ProfileService.updateProfile(ProfileService.java:19)'),
        
        ('refreshToken', '/auth/refresh', 'TokenRefreshError', 'Failed to refresh authentication token', 
         'java.lang.SecurityException: Token refresh failed due to invalid session\n    at com.example.myproject.AuthManager.refreshToken(AuthManager.java:62)\n    at com.example.myproject.TokenService.refresh(TokenService.java:34)'),
        
        ('initializeComponent', '/component/init', 'ComponentLoadError', 'Failed to load required component', 
         'java.lang.NoClassDefFoundError: Component class not found\n    at com.example.myproject.ComponentLoader.load(ComponentLoader.java:51)\n    at com.example.myproject.ComponentService.init(ComponentService.java:23)'),
        
        ('uploadImage', '/image/upload', 'ImageUploadError', 'Error occurred while uploading image', 
         'java.io.IOException: Failed to upload image due to server error\n    at com.example.myproject.ImageUploadManager.uploadImage(ImageUploadManager.java:46)\n    at com.example.myproject.ImageService.upload(ImageService.java:32)'),
        
        ('syncSettings', '/settings/sync', 'SettingsSyncError', 'Error during settings synchronization', 
         'java.lang.Exception: Settings synchronization failed\n    at com.example.myproject.SettingsManager.sync(SettingsManager.java:64)\n    at com.example.myproject.SyncService.performSync(SyncService.java:28)'),
        
        ('downloadContent', '/content/download', 'ContentDownloadError', 'Error downloading content', 
         'java.io.IOException: Content download failed due to interrupted connection\n    at com.example.myproject.DownloadManager.download(DownloadManager.java:79)\n    at com.example.myproject.ContentService.download(ContentService.java:45)'),
        
        ('loadDashboard', '/dashboard/load', 'DashboardLoadError', 'Error occurred while loading dashboard', 
         'java.lang.Exception: Dashboard data is incomplete\n    at com.example.myproject.DashboardLoader.load(DashboardLoader.java:22)\n    at com.example.myproject.DashboardActivity.display(DashboardActivity.java:31)'),
        
        ('processOrder', '/order/process', 'OrderProcessingError', 'Error occurred while processing order', 
         'java.lang.IllegalArgumentException: Invalid order details provided\n    at com.example.myproject.OrderProcessor.process(OrderProcessor.java:37)\n    at com.example.myproject.OrderService.execute(OrderService.java:24)'),
        
        ('generateReport', '/report/generate', 'ReportGenerationError', 'Error occurred during report generation', 
         'java.io.IOException: Report generation failed due to file write error\n    at com.example.myproject.ReportGenerator.generate(ReportGenerator.java:54)\n    at com.example.myproject.ReportService.create(ReportService.java:41)'),
        
        ('saveDraft', '/draft/save', 'DraftSaveError', 'Failed to save draft', 
         'java.io.IOException: Draft save failed due to disk space issues\n    at com.example.myproject.DraftManager.save(DraftManager.java:18)\n    at com.example.myproject.DraftService.save(DraftService.java:29)'),
        
        ('syncContacts', '/contacts/sync', 'ContactsSyncError', 'Error during contacts synchronization', 
         'java.lang.Exception: Contacts synchronization failed\n    at com.example.myproject.ContactsManager.sync(ContactsManager.java:38)\n    at com.example.myproject.ContactsService.performSync(ContactsService.java:47)'),
        
        ('initializeSession', '/session/init', 'SessionInitializationError', 'Failed to initialize user session', 
         'java.lang.IllegalStateException: Session initialization failed due to invalid state\n    at com.example.myproject.SessionManager.initialize(SessionManager.java:26)\n    at com.example.myproject.SessionService.start(SessionService.java:32)'),
        
        ('loadPreferences', '/preferences/load', 'PreferencesLoadError', 'Error occurred while loading user preferences', 
         'java.lang.Exception: Failed to load user preferences from storage\n    at com.example.myproject.PreferencesLoader.load(PreferencesLoader.java:21)\n    at com.example.myproject.PreferencesService.load(PreferencesService.java:14)')
    ]
    
    # Randomly select an error scenario
    error_scenario = random.choice(error_scenarios)
    
    page_category, page, error_name, error_description, error_metadata = error_scenario
    
    print(f'\tApp Error Event: {error_name}, Description: {error_description}')
    
    # Call the appError function with the selected scenario
    appError(driver, page_category, page, error_name, error_description, error_metadata)

def generate_app_ui_error(driver):
    """Randomly generate a UI error event with realistic error details."""
    
    ui_error_scenarios = [
        # (pageCategory, page, errorName, errorDescription, uiErrorHeader, uiErrorBody)
        ("loginPage", "/login", "InvalidCredentials", "User provided invalid login credentials", 
         "Login Failed", "The email or password you entered is incorrect. Please try again."),
        
        ("loginPage", "/login", "AccountLocked", "User account is locked due to multiple failed login attempts", 
         "Account Locked", "Your account has been locked due to too many failed login attempts. Please reset your password."),
        
        ("checkout", "/checkout", "PaymentDeclined", "User payment method was declined by the bank", 
         "Payment Error", "Your payment was declined. Please use a different payment method."),
        
        ("settings", "/settings/profile", "ProfileUpdateFailed", "Failed to update user profile information", 
         "Profile Update Error", "There was an error updating your profile. Please check your details and try again."),
        
        ("registration", "/signup", "EmailAlreadyUsed", "User attempted to register with an already used email address", 
         "Registration Error", "This email address is already associated with another account. Please use a different email."),
        
        ("forgotPassword", "/password/reset", "EmailNotFound", "User attempted to reset password for an email that does not exist", 
         "Reset Password Error", "The email address you entered does not match our records. Please check and try again."),
        
        ("checkout", "/checkout", "InsufficientFunds", "User has insufficient funds for the transaction", 
         "Payment Declined", "Your card was declined due to insufficient funds. Please use a different payment method."),
        
        ("checkout", "/checkout", "InvalidCardNumber", "User provided an invalid card number", 
         "Invalid Card Number", "The card number you entered is invalid. Please check the number and try again."),
        
        ("settings", "/settings/preferences", "PreferenceUpdateFailed", "Failed to save user preferences", 
         "Update Failed", "We could not save your preferences. Please try again later."),
        
        ("content", "/content/view", "ContentNotAvailable", "Requested content is not available in the user’s region", 
         "Content Unavailable", "This content is not available in your region. Please choose another title."),
        
        ("streaming", "/stream/start", "StreamTimeout", "Streaming failed to start due to a timeout", 
         "Streaming Error", "We couldn’t start the stream. Please check your connection and try again."),
        
        ("streaming", "/stream/start", "UnsupportedFormat", "User attempted to stream content in an unsupported format", 
         "Format Not Supported", "The content you are trying to view is not supported on your device."),
        
        ("loginPage", "/login", "CaptchaRequired", "Captcha verification is required for login", 
         "Captcha Required", "Please complete the captcha verification to proceed with login."),
        
        ("checkout", "/checkout", "AddressInvalid", "Shipping address provided by user is invalid", 
         "Invalid Address", "The shipping address you provided is invalid. Please check and enter a valid address."),
        
        ("registration", "/signup", "WeakPassword", "User provided a password that does not meet the required strength", 
         "Weak Password", "Your password is too weak. Please use a stronger password with a mix of letters, numbers, and symbols."),
        
        ("forgotPassword", "/password/reset", "TokenExpired", "Password reset token has expired", 
         "Token Expired", "Your password reset link has expired. Please request a new one."),
        
        ("streaming", "/stream/start", "RegionRestriction", "User attempted to access content restricted in their region", 
         "Restricted Content", "This content is restricted in your region. Please choose another title."),
        
        ("checkout", "/checkout", "CardExpired", "User’s card has expired", 
         "Card Expired", "The card you entered has expired. Please use a valid card."),
        
        ("registration", "/signup", "InvalidEmailFormat", "User provided an email address with an invalid format", 
         "Invalid Email", "The email address you entered is not valid. Please enter a valid email address."),
        
        ("settings", "/settings/account", "AccountDeletionFailed", "Failed to delete user account", 
         "Deletion Failed", "We could not delete your account at this time. Please try again later."),
        
        ("content", "/content/view", "SubscriptionRequired", "User attempted to access content that requires a subscription", 
         "Subscription Required", "This content requires a subscription. Please subscribe to access."),
        
        ("checkout", "/checkout", "CVVIncorrect", "User entered an incorrect CVV number", 
         "Incorrect CVV", "The CVV number you entered is incorrect. Please check and try again."),
        
        ("registration", "/signup", "AgeRestriction", "User attempted to register but did not meet the age requirement", 
         "Age Restriction", "You do not meet the age requirement to create an account."),
        
        ("streaming", "/stream/start", "BandwidthLow", "User’s internet connection is too slow to start streaming", 
         "Low Bandwidth", "Your internet connection is too slow to stream this content. Please try again later."),
        
        ("content", "/content/download", "StorageFull", "User’s device has insufficient storage to download content", 
         "Insufficient Storage", "Your device does not have enough storage to download this content. Please free up space and try again.")
    ]
    
    # Randomly select a UI error scenario
    ui_error_scenario = random.choice(ui_error_scenarios)
    
    page_category, page, error_name, error_description, ui_error_header, ui_error_body = ui_error_scenario
    
    print(f'\tApp UI Error Event: {error_name}, Description: {error_description}, UI Header: {ui_error_header}, UI Body: {ui_error_body}')
    
    # Call the appUIError function with the selected scenario
    appUIError(driver, page_category, page, error_name, error_description, ui_error_header, ui_error_body)

def generate_tv_pair_result(driver):
    """Randomly generate a TV Pairing result with a 60% success rate and 40% failure rate."""
    
    success_scenarios = [
        # (tvPairStatus, errorName, errorDescription)
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
        ('Success', '', ''),
    ]
    
    failure_scenarios = [
        # (tvPairStatus, errorName, errorDescription)
        ('Fail', 'TVPairingTimeout', 'The TV pairing process timed out. Please try again.'),
        ('Fail', 'InvalidTVCode', 'The TV pairing code entered is invalid.'),
        ('Fail', 'NetworkError', 'A network error occurred during TV pairing.'),
        ('Fail', 'TVNotResponding', 'The TV is not responding. Please ensure it is powered on and connected.'),
        ('Fail', 'PairingRejected', 'The TV rejected the pairing request.'),
        ('Fail', 'TVPairingFailed', 'The TV pairing process failed due to an unknown error.'),
        ('Fail', 'IncorrectPIN', 'The PIN entered is incorrect. Please check and try again.'),
        ('Fail', 'PairingTimeout', 'The pairing session has expired. Please initiate pairing again.'),
        ('Fail', 'TVNotFound', 'The TV could not be found on the network.'),
        ('Fail', 'TVPairingCancelled', 'The TV pairing process was cancelled.'),
    ]
    
    # Randomly decide if the result should be a success (60%) or failure (40%)
    if random.random() < 0.60:
        result = random.choice(success_scenarios)
    else:
        result = random.choice(failure_scenarios)
    
    tv_pair_status, error_name, error_description = result
    
    print(f'TV Pair Result: {tv_pair_status}, Error: {error_name}, Description: {error_description}')
    
    # Call the appTVPairResult function with the selected scenario
    appTVPairResult(driver, tv_pair_status, error_name, error_description)

def run_scenario(driver):
    """Run a scenario based on random selection."""
    scenario_type = random.choice(['login_only', 'login_only', 'login_only', 'login_only', 'signup_only', 'signup_then_login'])

    if scenario_type == 'login_only':
        print("\tScenario: Login Only")
        generate_login_result(driver)

    elif scenario_type == 'signup_only':
        print("\tScenario: Signup Only")
        generate_signup_result(driver)

    elif scenario_type == 'signup_then_login':
        print("\tScenario: Signup then Login")
        generate_signup_result(driver)
        time.sleep(1)
        generate_login_result(driver)

    # Generate a few API call results after scenario execution
    for _ in range(random.randint(1, 5)):  # Send 1 to 5 API calls
        generate_api_result(driver)

    # Randomly decide if an app crash should happen (10% chance)
    if random.random() < 0.85:
        generate_app_crash(driver)

    # Randomly decide if an app error should happen (30% chance)
    for _ in range(random.randint(1, 2)):  # Send 1 to 5 API calls
        generate_app_error(driver)

    # Randomly decide if a UI error should happen (70% chance)
    for _ in range(random.randint(1, 4)):  # Send 1 to 5 API calls
        generate_app_ui_error(driver)

    # Randomly decide if a TV Pair error should happen (60% chance)
    if random.random() < 0.40:
        generate_tv_pair_result(driver)

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
