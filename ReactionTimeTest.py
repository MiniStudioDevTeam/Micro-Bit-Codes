startTime = 0
endTime = 0
reactionTime = 0
waitTime = 0

def on_button_pressed_a():
    global endTime, reactionTime, startTime
    if startTime > 0:
        endTime = input.running_time()
        reactionTime = endTime - startTime
        basic.show_number(reactionTime)
        startTime = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def countdownAndGo():
    global waitTime, startTime
    basic.show_string("GO!")
    basic.pause(500)
    basic.clear_screen()
    waitTime = randint(2000, 5000)
    basic.pause(waitTime)
    basic.show_icon(IconNames.HAPPY)
    startTime = input.running_time()

def on_forever():
    countdownAndGo()
    while startTime > 0:
        # Waiting for user to press A
        basic.pause(100)
    basic.pause(2000)
    basic.clear_screen()
basic.forever(on_forever)
