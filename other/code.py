import time
import board
import digitalio
import neopixel

try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

# Enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True


# LED setup.
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# BUTTON_A is an reference to the 2 buttons on the Circuit Python Express
switch = digitalio.DigitalInOut(board.BUTTON_A)
switch.direction = digitalio.Direction.INPUT

# pull controls the electrical behavoir of the pin
# The standard Pull.DOWN as electricity flows through the pin, switch.value = False(LOW), When the button is pressed, switch.value = True(HIGH)
switch.pull = digitalio.Pull.DOWN


wave_file = open("cow.wav", "rb")
wave_file2 = open("cow2.wav", "rb")
wave_file3= open("cow3.wav", "rb")
wave = WaveFile(wave_file)
wave2 = WaveFile(wave_file2)
wave3 = WaveFile(wave_file3)
audio = AudioOut(board.SPEAKER)

flipflop = False
startTime = time.monotonic() # Starts counting when the program runs

fadeValue = 0
fadeToggle = False
increase = 5

pixelsF = neopixel.NeoPixel(board.A7,5, brightness=1, auto_write=False)

pixelsR = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1, auto_write=False)

ani_on = False
#ani_wa = False
flipflop = False
startTime = time.monotonic() # Starts counting when the program runs
interval = 0.5 #increase or decrease to speed up or slow down blink


#def animationWa():
    #global startTime, interval, flipflop, pixels
    #if time.monotonic() - startTime > interval:
    #    startTime = time.monotonic()

        #pixelsF.fill((255,100,0))
        #pixelsR.fill((255,0,0))
        #pixelsF.show()
        #pixelsR.show()
        #time.sleep(0.5)

        #pixelsF.fill((0,0,0))
        #pixelsR.fill((0,0,0))
        #pixelsF.show()
        #pixelsR.show()
        #time.sleep(0.5)

        #pixelsF.fill((255,100,0))
        #pixelsR.fill((255,0,0))
        #pixelsF.show()
        #pixelsR.show()
        #time.sleep(0.5)

        #pixelsF.fill((0,0,0))
        #pixelsR.fill((0,0,0))
        #pixelsF.show()
        #pixelsR.show()
        #time.sleep(0.5)



def animationOn():
    #global startTime, interval, pixels
    #if time.monotonic() - startTime > interval:
    #    startTime = time.monotonic()

    pixelsF.fill((0,0,0))
    pixelsR.fill((0,0,0))
    pixelsF.show()
    pixelsR.show()
    time.sleep(20)

    pixelsF.fill((255,255,255))
    pixelsR.fill((255,0,0))
    pixelsF.show()
    pixelsR.show()
    time.sleep(0.1)

    pixelsF.fill((0,0,0))
    pixelsR.fill((0,0,0))
    pixelsF.show()
    pixelsR.show()
    time.sleep(0.1)

    pixelsF.fill((255,255,255))
    pixelsR.fill((255,0,0))
    pixelsF.show()
    pixelsR.show()
    time.sleep(0.1)

    pixelsF.fill((0,0,0))
    pixelsR.fill((0,0,0))
    pixelsF.show()
    pixelsR.show()
    time.sleep(0.8)


wasPressed = False # Keeps track of the last time button was pressed
mode = 0


while True:
    print("Current Mode: " + str(mode))
    # print("Current switch value: " + str(switch.value))
    if switch.value == True:
        wasPressed = True # Keeps track that the button is pressed
    else:
        # This is the state when the button is de-pressed
        # Check if the button was pressed in the past
        if wasPressed == True:
            wasPressed = False # Resets the variable for next time the button is pressed
            mode = mode + 1 # Change the mode

    if mode == 0:
        pixelsF.fill((0,0,0))
        pixelsR.fill((0,0,0))
        flipflop = False
        print("You are in mode 0")
    elif mode == 1:
        audio.play(wave2)
        if ani_on == False:
            ani_on = True
            animationOn()

        else:
            pixelsF.fill((255,255,255))
            pixelsR.fill((255,0,0))
            pixelsF.show()
            pixelsR.show()


        print("You are in mode 1")
    elif mode == 2:
        if time.monotonic() - startTime > interval:
    	 startTime = time.monotonic()
         audio.play(wave3)
    	 if flipflop == False:
                pixelsF.fill((255,100,0))
                pixelsR.fill((255,0,0))
                flipflop = True
    	 else:
                pixelsF.fill((0,0,0))
                pixelsR.fill((0,0,0))
                flipflop = False
    	 pixelsF.show()
         pixelsR.show()


        print("You are in mode 2")
    else:
        print("Back to mode 0")
        mode = 0
        ani_on = False
        #ani_wa = False

    time.sleep(0.01)


  # debounce delay
