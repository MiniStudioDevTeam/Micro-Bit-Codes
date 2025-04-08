let numberToCatch = 0
let presses = 0
let lives = 3

input.onButtonPressed(Button.A, function () {
    presses++
})

function newRound() {
    numberToCatch = randint(1, 9)
    presses = 0
    basic.showNumber(numberToCatch)
    basic.pause(3000)

    if (presses == numberToCatch) {
        basic.showIcon(IconNames.Yes)
    } else {
        lives--
        basic.showIcon(IconNames.No)
    }

    basic.pause(500)
    basic.clearScreen()
}

basic.showString("Catch!")

basic.forever(function () {
    if (lives <= 0) {
        basic.showString("Game Over")
        control.reset()
    }

    newRound()
})
