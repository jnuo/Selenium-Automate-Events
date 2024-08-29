from tasks import run_automation_task
import time

def main():
    """Main function to run the automated tasks repeatedly."""
    number_of_runs = 5  # Set the number of times you want to run the script

    for i in range(number_of_runs):
        run_automation_task()
        print(f"\tCompleted {i}th run of the automation task.")
        time.sleep(1)  # Optional: Add a delay between runs if needed

if __name__ == "__main__":
    main()
