def on_gesture_shake():
    global steps
    steps += 1
    basic.show_number(steps)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
steps = 0
