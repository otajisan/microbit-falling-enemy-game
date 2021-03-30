def init_enemy(enemy: game.LedSprite):
    enemy.set(LedSpriteProperty.Y, 0)
    enemy.set(LedSpriteProperty.X, randint(0, 4))
    return enemy
def accelerate_enemy(game_round: number):
    sleep_time2 = 1000 / game_round ^ 1 / 4
    if sleep_time2 < 150:
        sleep_time2 = 150
    return sleep_time2

def on_button_pressed_a():
    hero.change(LedSpriteProperty.X, -1)
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
input.on_button_pressed(Button.A, on_button_pressed_a)

def initialize():
    global sleep_time, game_round, enemy
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    game.set_life(3)
    sleep_time = 1000
    game_round = 1
    enemy = game.create_sprite(0, 0)
    enemy = init_enemy(enemy)

def on_button_pressed_b():
    hero.change(LedSpriteProperty.X, 1)
    music.play_tone(523, music.beat(BeatFraction.EIGHTH))
input.on_button_pressed(Button.B, on_button_pressed_b)

def fall_enemy():
    global sleep_time, enemy, game_round
    while game.is_game_over() == False:
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
            basic.pause(sleep_time)
            enemy = init_enemy(enemy)
            game_round = game_round + 1
enemy: game.LedSprite = None
sleep_time = 0
hero: game.LedSprite = None
game_round = 0
hero = game.create_sprite(2, 4)
initialize()

def on_forever():
    fall_enemy()
basic.forever(on_forever)
