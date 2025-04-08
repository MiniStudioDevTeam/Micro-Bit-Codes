Number2 = 0

def on_gesture_shake():
    global Number2
    basic.clear_screen()
    Number2 = randint(1, 6)
    if Number2 == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif Number2 == 2:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            """)
    elif Number2 == 3:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . .
            """)
    elif Number2 == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif Number2 == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
