import rotatescreen
import time
# Accessing the main screen
rotate_screen = rotatescreen.get_primary_display()

for i in range(13):
    time.sleep(1)
    rotate_screen.rotate_to(i*90 % 360)