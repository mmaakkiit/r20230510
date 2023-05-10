def on_button_pressed_a():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    for index in range(4):
        music.play_tone(262 + 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(294+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(330+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(349+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(330+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(294+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
        music.play_tone(330+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(349+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(392+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(440+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(392+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(349+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(330+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(262+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(294+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(294+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(330+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(330+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(349+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(349+ 音, music.beat(BeatFraction.HALF))
        music.play_tone(330+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(294+ 音, music.beat(BeatFraction.WHOLE))
        music.play_tone(262+ 音, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global 音
    音 += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

音 = 0
音 = 0

def on_forever():
    pass
basic.forever(on_forever)
