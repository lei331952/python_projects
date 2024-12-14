import winsound
import time


def play_sound():
    winsound.Beep(440, 1000)
    time.sleep(1)
    winsound.Beep(440, 1000)


def play_sound_after(duration_in_seconds):
    print(f"Waiting for {duration_in_seconds} seconds...")
    time.sleep(duration_in_seconds)
    print("Time's up!")
    play_sound()


while True:
    duration = int(input('Duration in seconds to sound alarm(or 0 to quit):'))
    if duration == 0:
        break
    play_sound_after(duration)
