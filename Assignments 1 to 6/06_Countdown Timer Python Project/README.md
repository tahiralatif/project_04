# Countdown Timer in Python 🕒

This is a simple countdown timer script written in Python. The timer takes input in seconds and counts down to zero, updating the display every second.

## 📋 Features

- Takes user input in seconds
- Converts seconds into MM:SS format
- Displays countdown in real-time
- Shows a "Time's up!" message at the end

## 🚀 How to Run

1. Make sure you have Python installed on your system.
2. Save the script in a file, for example: `countdown_timer.py`
3. Open terminal or command prompt.
4. Navigate to the script's directory.
5. Run the script using:

```bash
python countdown_timer.py
Enter the time in seconds when prompted.

🧠 Example
makefile
Copy
Edit
Enter the time in seconds: 10
00:10
00:09
...
00:01
Time's up!
🛠️ Code Explanation
python
Copy
Edit
import time
This imports Python’s time module to use the sleep() function.

python
Copy
Edit
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
This function takes seconds as input.

It uses divmod() to get minutes and seconds.

The formatted time is printed on the same line using end='\r'.

The timer waits for one second in each loop using time.sleep(1).

python
Copy
Edit
countdown = int(input("Enter the time in seconds: "))
countdown_timer(countdown)
This part asks the user for input and runs the timer.

📎 Requirements
Python 3.x

❤️ Author
Created with 💻 by Tahira

