from microbit import *

steps = 0

while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(steps)
        sleep(100)  # Debounce to prevent multiple counts from a single shake

Explanation:
 * Import necessary library:
   * from microbit import *: This line imports all the necessary functions and classes from the MicroPython microbit library.
 * Initialize step counter:
   * steps = 0: This line creates a variable named steps and initializes it to 0. This variable will store the number of steps counted.
 * Main loop:
   * while True:: This creates an infinite loop that continuously checks for steps.
 * Check for shake gesture:
   * if accelerometer.was_gesture('shake'):: This line checks if the accelerometer has detected a shake gesture.
 * Increment step count and display:
   * steps += 1: If a shake is detected, this line increments the steps variable by 1.
   * display.show(steps): This line displays the current step count on the micro:bit's LED display.
 * Debounce:
   * sleep(100): This line introduces a short delay (100 milliseconds) to prevent multiple counts from a single shake.
To use this code:
 * Copy and paste: Copy the code into the MicroPython editor for the micro:bit.
 * Flash to micro:bit: Flash the code onto your micro:bit.
 * Run and count: Run the code and shake the micro:bit to count steps.
Note:
 * This is a basic step counter. For more accurate step counting, you might need to implement more sophisticated algorithms that consider factors like acceleration and gravity.
 * You can adjust the debounce time (sleep(100)) to fine-tune the sensitivity of the step counter.
I hope this helps!
