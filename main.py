import random


class Player:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg


class Enemy:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg


def main():
    print("Guess through hell\n")
    print("You wake up in hell and have to guess your way out.")

    player = Player(hp=100, dmg=10)
    while player.hp > 0:
        enemy_count = random.randint(1, 5)
        boss_enemy = Enemy(hp=100, dmg=20)

        for i in range(enemy_count):
            little_enemy = Enemy(hp=10, dmg=5)
            attack_little(player, little_enemy)

        attack_boss(player, boss_enemy)


def attack_little(player, enemy):
    secret_number = random.randint(1, 10)

    player_guess = int(input("Attack that little enemy (1-10) "))
    if player_guess == secret_number:
        enemy.hp -= player.dmg
        print("You killed that guy.\n")
    else:
        player.hp -= enemy.dmg
        print("Your guess was wrong, you're hit {0} HP left".format(player.hp))


def attack_boss(player, enemy):
    secret_number = random.randint(1, 50)

    while enemy.hp > 0 and player.hp > 0:
        player_guess = int(input("You have to fight a boss (1-50) "))

        if player_guess > secret_number:
            player.hp -= enemy.dmg
            print("Your guess was to high, your HP: {0}\n".format(player.hp))
        elif player_guess < secret_number:
            player.hp -= enemy.dmg
            print("Your guess was to low, your HP: {0}\n".format(player.hp))
        else:
            enemy.hp -= player.dmg
            print("You guessed right and hit the boss, remaining HP: {0}".format(enemy.hp))
            secret_number = random.randint(1, 50)


if __name__ == "__main__":
    main()
