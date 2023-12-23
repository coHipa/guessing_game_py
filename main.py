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


def attack_little(player, enemy):
    secret_number = random.randint(1, 10)

    player_guess = int(input("Attack that little enemy (1-10) "))
    if player_guess == secret_number:
        enemy.hp -= player.dmg
        print("You killed that guy.\n")
    else:
        player.hp -= enemy.dmg
        print("Your guess was wrong, you're hit {0} HP left".format(player.hp))


if __name__ == "__main__":
    main()
