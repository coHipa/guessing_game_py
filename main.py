import random


class Player:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def is_alive(self):
        return self.hp > 0


class Enemy:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg
        self.name = random.choice(["Vergil", "Malenia", "C'Thun", "Baal", "Wizpig", "The Nameless"])

    def is_alive(self):
        return self.hp > 0


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name, hp=100, dmg=10)
    print("Guess through hell\n")
    print("{player.name} you wake up in hell and have to guess your way out.")

    while player.is_alive():
        enemy_count = random.randint(1, 5)
        boss_enemy = Enemy(hp=100, dmg=20)

        for i in range(enemy_count):
            little_enemy = Enemy(hp=10, dmg=5)
            attack_little(player, little_enemy)

        attack_boss(player, boss_enemy)


def attack_little(player, enemy):
    secret_number = random.randint(1, 10)

    print("{player.name}, attack this little enemy, fast (1-10)")
    if valid_guess() == secret_number:
        enemy.hp -= player.dmg
        print("You killed that guy.\n")
    else:
        player.hp -= enemy.dmg
        print("Your guess was wrong, you're hit {player.hp} HP left")


def attack_boss(player, enemy):
    secret_number = random.randint(1, 50)

    while enemy.is_alive() and player.is_alive():
        print("You have to fight against {enemy.name} (1-50)\n")

        if valid_guess() > secret_number:
            player.hp -= enemy.dmg
            print("Your guess was to high, your HP: {player.hp}\n")
        elif valid_guess() < secret_number:
            player.hp -= enemy.dmg
            print("Your guess was to low, your HP: {player.hp}\n")
        else:
            enemy.hp -= player.dmg
            print("You guessed right and hit the boss, remaining HP: {enemy.hp}")
            secret_number = random.randint(1, 50)


def valid_guess():
    while True:
        user_input = input("Make your guess: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Unvalid input.\n")


if __name__ == "__main__":
    main()
