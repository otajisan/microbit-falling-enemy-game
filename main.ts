function init_enemy (enemy: game.LedSprite) {
    enemy.set(LedSpriteProperty.Y, 0)
    enemy.set(LedSpriteProperty.X, randint(0, 4))
    return enemy
}
function accelerate_enemy (game_round: number) {
    let sleep_time2 = 1000 / game_round ^ 1 / 4
if (sleep_time2 < 150) {
        sleep_time2 = 150
    }
    return sleep_time2
}
input.onButtonPressed(Button.A, function () {
    hero.change(LedSpriteProperty.X, -1)
    music.playTone(523, music.beat(BeatFraction.Eighth))
})
function initialize () {
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
    game.setLife(3)
    sleep_time = 1000
    game_round = 1
    enemy = game.createSprite(0, 0)
    enemy = init_enemy(enemy)
}
input.onButtonPressed(Button.B, function () {
    hero.change(LedSpriteProperty.X, 1)
    music.playTone(523, music.beat(BeatFraction.Eighth))
})
function fall_enemy () {
    while (game.isGameOver() == false) {
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
            basic.pause(sleep_time)
            enemy = init_enemy(enemy)
            game_round = game_round + 1
        }
    }
}
let enemy: game.LedSprite = null
let sleep_time = 0
let hero: game.LedSprite = null
let game_round = 0
hero = game.createSprite(2, 4)
initialize()
basic.forever(function () {
    fall_enemy()
})
