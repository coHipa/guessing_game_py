import random
import os


class Player:
    def __init__(self, name, health=100, damage=10, critChance=0.1):
        self.name = name
        self.health = health
        self.damage = damage
        self.correctGuesses = 0
        self.criticalDamage = 0
        self.critChance = critChance

    def isAlive(self):
        return self.health > 0

    def updateDamage(self):
        self.damage = 10 + self.criticalDamage

    def increaseCriticalDamage(self):
        self.criticalDamage = 1 * int(self.damage * (random.randint(20, 50) / 100) + 10)


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
        self.name = random.choice(
            ["Vergil", "Malenia", "C'Thun", "Baal", "Wizpig", "The Nameless"]
        )

    def isAlive(self):
        return self.health > 0


def main():
    playerName = input("Enter your name: ")
    player = Player(playerName)
    print("Guess through hell\n")
    print(f"{player.name} you wake up in hell and have to guess your way out.")

    while player.isAlive():
        enemyCount = random.randint(1, 5)
        bossEnemy = Enemy(health=100, damage=20)

        for i in range(enemyCount):
            minorEnemy = Enemy(health=15, damage=5)
            attackMinor(player, minorEnemy)

        attackBoss(player, bossEnemy)

        print("Nice fight, but you are not out yet.")
        input("Press any key")
        os.system("cls" if os.name == "nt" else "clear")


def attackMinor(player, enemy):
    secretNumber = random.randint(1, 10)
    print(f"{player.name}, attack this little enemy, fast (1-10)")

    if validGuess() == secretNumber:
        hitEnemy(player, enemy)
        print("You killed that guy.\n")
    else:
        player.health -= enemy.damage
        print(f"Your guess was wrong, you're hit {player.health} health left")


def attackBoss(player, enemy):
    secretNumber = random.randint(1, 50)
    print(f"You have to fight against {enemy.name} (1-50)\n")

    while enemy.isAlive() and player.isAlive():
        playerGuess = validGuess()
        if playerGuess > secretNumber:
            player.health -= enemy.damage
            print(f"Your guess was to high, your health: {player.health}\n")
        elif playerGuess < secretNumber:
            player.health -= enemy.damage
            print(f"Your guess was to low, your health: {player.health}\n")
        else:
            hitEnemy(player, enemy)
            print(
                f"You guessed right and hit the boss, remaining health: {enemy.health}"
            )
            secretNumber = random.randint(1, 50)


def hitEnemy(player, enemy):
    if random.random() < player.critChance:
        print("This was a critical hit")
        player.increaseCriticalDamage()
        enemy.health -= player.criticalDamage
    else:
        enemy.health -= player.damage


def validGuess():
    while True:
        userInput = input("Make your guess: ")
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Unvalid input.\n")


if __name__ == "__main__":
    main()
