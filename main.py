from tasks import run_automation_task
import time

def main():
    """Main function to run the automated tasks repeatedly."""
    number_of_runs = 10  # Set the number of times you want to run the script

    for _ in range(number_of_runs):
        run_automation_task()
        print("\tCompleted one run of the automation task.")
        time.sleep(2)  # Optional: Add a delay between runs if needed

if __name__ == "__main__":
    main()
