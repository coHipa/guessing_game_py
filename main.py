import random
import os


class Player:
    def __init__(self, name, hp=100, dmg=10, crit_chance=0.1):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.correct_guesses = 0
        self.critical_dmg = 0
        self.crit_chance = crit_chance

    def is_alive(self):
        return self.hp > 0

    def update_dmg(self):
        self.dmg = 10 + self.critical_dmg

    def increase_critical_dmg(self):
        self.critical_dmg = 1 * int(self.dmg * (random.randint(20, 50) / 100) + 10)


class Enemy:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg
        self.name = random.choice(
            ["Vergil", "Malenia", "C'Thun", "Baal", "Wizpig", "The Nameless"]
        )

    def is_alive(self):
        return self.hp > 0


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print("Guess through hell\n")
    print(f"{player.name} you wake up in hell and have to guess your way out.")

    while player.is_alive():
        enemy_count = random.randint(1, 5)
        boss_enemy = Enemy(hp=100, dmg=20)

        for i in range(enemy_count):
            minor_enemy = Enemy(hp=15, dmg=5)
            attack_minor(player, minor_enemy)

        attack_boss(player, boss_enemy)

        print("Nice fight, but you are not out yet.")
        input("Press any key")
        os.system("cls" if os.name == "nt" else "clear")


def attack_minor(player, enemy):
    secret_number = random.randint(1, 10)
    print(f"{player.name}, attack this little enemy, fast (1-10)")

    if valid_guess() == secret_number:
        hit_enemy(player, enemy)
        print("You killed that guy.\n")
    else:
        player.hp -= enemy.dmg
        print(f"Your guess was wrong, you're hit {player.hp} HP left")


def attack_boss(player, enemy):
    secret_number = random.randint(1, 50)
    print(f"You have to fight against {enemy.name} (1-50)\n")

    while enemy.is_alive() and player.is_alive():
        player_guess = valid_guess()
        if player_guess > secret_number:
            player.hp -= enemy.dmg
            print(f"Your guess was to high, your HP: {player.hp}\n")
        elif player_guess < secret_number:
            player.hp -= enemy.dmg
            print(f"Your guess was to low, your HP: {player.hp}\n")
        else:
            hit_enemy(player, enemy)
            print(f"You guessed right and hit the boss, remaining HP: {enemy.hp}")
            secret_number = random.randint(1, 50)


def hit_enemy(player, enemy):
    if random.random() < player.crit_chance:
        print("This was a critical hit")
        player.increase_critical_dmg()
        enemy.hp -= player.critical_dmg
    else:
        enemy.hp -= player.dmg


def valid_guess():
    while True:
        user_input = input("Make your guess: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Unvalid input.\n")


if __name__ == "__main__":
    main()
