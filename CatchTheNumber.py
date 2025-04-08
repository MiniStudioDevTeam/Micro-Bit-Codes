def on_button_pressed_a():
    global presses
    presses += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def newRound():
    global numberToCatch, presses, lives
    numberToCatch = randint(1, 9)
    presses = 0
    basic.show_number(numberToCatch)
    basic.pause(3000)
    if presses == numberToCatch:
        basic.show_icon(IconNames.YES)
    else:
        lives += -1
        basic.show_icon(IconNames.NO)
    basic.pause(500)
    basic.clear_screen()
numberToCatch = 0
presses = 0
lives = 3
basic.show_string("Catch!")

def on_forever():
    if lives <= 0:
        basic.show_string("Game Over")
        control.reset()
    newRound()
basic.forever(on_forever)
