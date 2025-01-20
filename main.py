def on_button_pressed_a():
    global count, coin, Win_counter
    if count < 3:
        count += 1
        music.play(music.string_playable("B G E B C5 A G - ", 120),
            music.PlaybackMode.IN_BACKGROUND)
        coin = randint(0, 1)
        if coin == 0:
            basic.show_string("H")
            Win_counter += 1
            if Win_counter == 3:
                basic.show_string("WIN!!")
        else:
            basic.show_string("T")
            Win_counter = 0
    else:
        music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

Win_counter = 0
count = 0
coin = 0
coin = 0
count = 0
Win_counter = 0
basic.show_icon(IconNames.HEART)