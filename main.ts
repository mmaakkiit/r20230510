input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    for (let index = 0; index < 4; index++) {
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.playTone(294 + 音, music.beat(BeatFraction.Whole))
        music.playTone(330 + 音, music.beat(BeatFraction.Whole))
        music.playTone(349 + 音, music.beat(BeatFraction.Whole))
        music.playTone(330 + 音, music.beat(BeatFraction.Whole))
        music.playTone(294 + 音, music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(330 + 音, music.beat(BeatFraction.Whole))
        music.playTone(349 + 音, music.beat(BeatFraction.Whole))
        music.playTone(392 + 音, music.beat(BeatFraction.Whole))
        music.playTone(440 + 音, music.beat(BeatFraction.Whole))
        music.playTone(392 + 音, music.beat(BeatFraction.Whole))
        music.playTone(349 + 音, music.beat(BeatFraction.Whole))
        music.playTone(330 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Half))
        music.playTone(262 + 音, music.beat(BeatFraction.Half))
        music.playTone(294 + 音, music.beat(BeatFraction.Half))
        music.playTone(294 + 音, music.beat(BeatFraction.Half))
        music.playTone(330 + 音, music.beat(BeatFraction.Half))
        music.playTone(330 + 音, music.beat(BeatFraction.Half))
        music.playTone(349 + 音, music.beat(BeatFraction.Half))
        music.playTone(349 + 音, music.beat(BeatFraction.Half))
        music.playTone(330 + 音, music.beat(BeatFraction.Whole))
        music.playTone(294 + 音, music.beat(BeatFraction.Whole))
        music.playTone(262 + 音, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
    }
})
input.onButtonPressed(Button.AB, function () {
    音 += -1
    basic.showNumber(音)
})
input.onButtonPressed(Button.B, function () {
    音 += 1
    basic.showNumber(音)
})
let 音 = 0
音 = 0
basic.forever(function () {
	
})
