input.onButtonPressed(Button.A, function () {
    if (playerX > 0) {
        led.unplot(playerX, 4)
        playerX += -1
        led.plot(playerX, 4)
    }
})
function spawnDot () {
    dotX = randint(0, 4)
    dotY = 0
}
input.onButtonPressed(Button.B, function () {
    if (playerX < 4) {
        led.unplot(playerX, 4)
        playerX += 1
        led.plot(playerX, 4)
    }
})
let dotY = 0
let dotX = 0
let playerX = 0
playerX = 2
let lives = 3
basic.showString("Dodge!")
led.plot(playerX, 4)
basic.forever(function () {
    spawnDot()
    for (let i = 0; i <= 4; i++) {
        led.plot(dotX, dotY)
        basic.pause(300)
        led.unplot(dotX, dotY)
        dotY += 1
    }
    if (dotX == playerX) {
        lives += -1
        basic.showIcon(IconNames.Skull)
        basic.pause(500)
        basic.clearScreen()
        led.plot(playerX, 4)
    }
    if (lives <= 0) {
        basic.showString("Game Over")
        control.reset()
    }
})
