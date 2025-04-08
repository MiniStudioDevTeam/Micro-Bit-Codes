def on_button_pressed_a():
    global playerX
    if playerX > 0:
        led.unplot(playerX, 4)
        playerX += -1
        led.plot(playerX, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def spawnDot():
    global dotX, dotY
    dotX = randint(0, 4)
    dotY = 0

def on_button_pressed_b():
    global playerX
    if playerX < 4:
        led.unplot(playerX, 4)
        playerX += 1
        led.plot(playerX, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

dotY = 0
dotX = 0
playerX = 0
playerX = 2
lives = 3
basic.show_string("Dodge!")
led.plot(playerX, 4)

def on_forever():
    global dotY, lives
    spawnDot()
    for i in range(5):
        led.plot(dotX, dotY)
        basic.pause(300)
        led.unplot(dotX, dotY)
        dotY += 1
    if dotX == playerX:
        lives += -1
        basic.show_icon(IconNames.SKULL)
        basic.pause(500)
        basic.clear_screen()
        led.plot(playerX, 4)
    if lives <= 0:
        basic.show_string("Game Over")
        control.reset()
basic.forever(on_forever)
