from tasks import run_automation_task
import time

def main():
    """Main function to run the automated tasks indefinitely."""
    run_count = 0  # Initialize a run counter
    sleep_time = 2  # Initial sleep time after an exception
    max_sleep_time = 300  # Maximum sleep time (5 minutes)

    while True:
        try:
            run_automation_task()
            run_count += 1
            print(f"\tCompleted {run_count}th run of the automation task.")
            time.sleep(1)  # Optional: Add a delay between runs if needed

            # Reset sleep time after a successful run
            sleep_time = 2

        except Exception as e:
            # Log the exception
            print(f"An error occurred during run {run_count}: {e}")
            print(f"\tSleeping for {sleep_time} seconds before retrying...")

            # Wait before retrying
            time.sleep(sleep_time)

            # Increase the sleep time for the next retry, up to the maximum
            sleep_time = min(sleep_time * 2, max_sleep_time)

if __name__ == "__main__":
    main()
