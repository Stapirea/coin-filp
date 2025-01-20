input.onButtonPressed(Button.A, function () {
    if (count < 3) {
        count += 1
        music.play(music.stringPlayable("B G E B C5 A G - ", 120), music.PlaybackMode.InBackground)
        coin = randint(0, 1)
        if (coin == 0) {
            basic.showString("H")
            Win_counter += 1
            if (Win_counter == 3) {
                basic.showString("WIN!!")
            }
        } else {
            basic.showString("T")
            Win_counter = 0
        }
    } else {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(count)
})
let Win_counter = 0
let count = 0
let coin = 0
coin = 0
count = 0
Win_counter = 0
basic.showIcon(IconNames.Heart)
