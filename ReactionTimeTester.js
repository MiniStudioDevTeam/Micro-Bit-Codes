let startTime = 0
let endTime = 0
let reactionTime = 0
let waitTime = 0
input.onButtonPressed(Button.A, function () {
    if (startTime > 0) {
        endTime = input.runningTime()
        reactionTime = endTime - startTime
        basic.showNumber(reactionTime)
        startTime = 0
    }
})
function countdownAndGo () {
    basic.showString("GO!")
    basic.pause(500)
    basic.clearScreen()
    waitTime = randint(2000, 5000)
    basic.pause(waitTime)
    basic.showIcon(IconNames.Happy)
    startTime = input.runningTime()
}
basic.forever(function () {
    countdownAndGo()
    while (startTime > 0) {
        // Waiting for user to press A
        basic.pause(100)
    }
    basic.pause(2000)
    basic.clearScreen()
})
