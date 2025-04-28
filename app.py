import sys
from datetime import datetime
import pytz



def main():

    now_sf = datetime.now(pytz.timezone('America/New_York')).strftime("%-I:%M %p")
    now_wh = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%-I:%M %p")

    message = f"Hello world, the time is now {now_sf} in San Francisco and {now_wh} in Woods Hole."



    # print output to the github actions console for this step
    if sys.argv[1] == '--print':
        print(message)

    # append the time to a txt file s
    if sys.argv[1] == '--txt':
        with open("output.txt", "a") as f:
            f.write(message + "\n")



if __name__ == "__main__":
    main()