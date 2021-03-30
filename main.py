def init_enemy():
    enemy.set(LedSpriteProperty.Y, 0)
    enemy.set(LedSpriteProperty.X, randint(0, 4))
    return enemy

def accelerate_enemy(game_round: number):
    sleep_time = 1000 / game_round ^ 1 / 4
    if sleep_time < 150:
        sleep_time = 150
    return sleep_time

def on_button_pressed_a():
    hero.change(LedSpriteProperty.X, -1)
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    hero.change(LedSpriteProperty.X, 1)
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

def initialize():
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    game.set_life(3)
    enemy = init_enemy()

def fall_enemy(sleep_time):
    global enemy, game_round
    sleep_time = accelerate_enemy(game_round)
    basic.pause(sleep_time)
    enemy.set(LedSpriteProperty.Y, enemy.get(LedSpriteProperty.Y) + 1)
    if enemy.get(LedSpriteProperty.Y) == 4:
        if enemy.get(LedSpriteProperty.X) == hero.get(LedSpriteProperty.X):
            game.remove_life(1)
            music.play_tone(196, music.beat(BeatFraction.EIGHTH))
        else:
            game.add_score(1)
            music.play_tone(784, music.beat(BeatFraction.EIGHTH))
        enemy = init_enemy()
        game_round = game_round + 1
        

hero: game.LedSprite = game.create_sprite(2, 4)
enemy: game.LedSprite = game.create_sprite(0, 0)
game_round = 1

def on_forever():
    initialize()
    sleep_time = 1000
    while True:
        fall_enemy(sleep_time)

basic.forever(on_forever)
