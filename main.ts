function init_enemy(): game.LedSprite {
    enemy.set(LedSpriteProperty.Y, 0)
    enemy.set(LedSpriteProperty.X, randint(0, 4))
    return enemy
}

function accelerate_enemy(game_round: number): number {
    let sleep_time = 1000 / game_round ^ 1 / 4
    if (sleep_time < 150) {
        sleep_time = 150
    }
    
    return sleep_time
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    hero.change(LedSpriteProperty.X, -1)
    music.playTone(523, music.beat(BeatFraction.Eighth))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    hero.change(LedSpriteProperty.X, 1)
    music.playTone(523, music.beat(BeatFraction.Eighth))
})
function initialize() {
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
    game.setLife(3)
    let enemy = init_enemy()
}

function fall_enemy(sleep_time: number) {
    
    sleep_time = accelerate_enemy(game_round)
    basic.pause(sleep_time)
    enemy.set(LedSpriteProperty.Y, enemy.get(LedSpriteProperty.Y) + 1)
    if (enemy.get(LedSpriteProperty.Y) == 4) {
        if (enemy.get(LedSpriteProperty.X) == hero.get(LedSpriteProperty.X)) {
            game.removeLife(1)
            music.playTone(196, music.beat(BeatFraction.Eighth))
        } else {
            game.addScore(1)
            music.playTone(784, music.beat(BeatFraction.Eighth))
        }
        
        enemy = init_enemy()
        game_round = game_round + 1
    }
    
}

let hero = game.createSprite(2, 4)
let enemy = game.createSprite(0, 0)
let game_round = 1
basic.forever(function on_forever() {
    initialize()
    let sleep_time = 1000
    while (true) {
        fall_enemy(sleep_time)
    }
})
