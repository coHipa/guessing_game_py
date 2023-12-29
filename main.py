import random
import os


class Player:
    def __init__(self, name, health=100, damage=10, critChance=0.1):
        self.name = name
        self.health = health
        self.damage = damage
        self.criticalDamage = 0
        self.critChance = critChance

    def isAlive(self):
        return self.health > 0

    def updateDamage(self):
        self.damage = 10 + self.criticalDamage

    def increaseCriticalDamage(self):
        self.criticalDamage = 1 * int(self.damage * (random.randint(20, 50) / 100) + 10)

    def buffWeapon(self):
        print("You defeated a boss. Now it's time to choose.")
        buffChoice = input("Do you want to buff your weapon? (y/n) ").lower()

        if buffChoice == "y":
            self.damage += random.randint(1, 5)
            self.critChance += random.uniform(0.05, 0.1)
            print(f"Base damage increased to {self.damage}.")
            print(f"Critical hit chance increased to {self.critChance * 100}%.")


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
    while True:
        gameLoop()
        userInput = input("Enter '666' to exit the game, press any key to return to battle.")
        if userInput == "666":
            break


def gameLoop():
    print("Guess through hell\n")
    playerName = input("Enter your name: ")
    player = Player(playerName)
    print(f"{player.name} you wake up in hell and have to guess your way out.")

    while player.isAlive():
        
        minorEnemy = Enemy(health=15, damage=5)
        attackMinor(player, minorEnemy)

        bossEnemy = Enemy(health=100, damage=20)
        attackBoss(player, bossEnemy)

        print("Nice fight, but you are not out yet.")
        input("Press any key")
        os.system("cls" if os.name == "nt" else "clear")


def attackMinor(player, enemy):
    enemyCount = random.randint(1, 5)

    for _ in range(enemyCount):
        secretNumber = random.randint(1, 10)
        print(f"{player.name}, attack this little enemy, fast (1-10)")

        while enemy.isAlive() and player.isAlive():
            playerGuess = validGuess()
            if playerGuess != secretNumber:
                player.health -= enemy.damage
                print(f"Your guess was wrong, you're hit {player.health} health left")
            else:
                attackEnemy(player, enemy)
                print("You killed that guy.\n")
                break


def attackBoss(player, enemy):
    secretNumber = random.randint(1, 50)
    print(f"A Boss apeared, you have to fight against {enemy.name} (1-50)\n")

    while enemy.isAlive() and player.isAlive():
        playerGuess = validGuess()
        if playerGuess != secretNumber:
            player.health -= enemy.damage
            print(f"Your guess {"was to high" if playerGuess > secretNumber else "to low"}, your health: {player.health}")
        else:
            attackEnemy(player, enemy)
            print(f"You guessed right and hit the boss, remaining health: {enemy.health}")
            secretNumber = random.randint(1, 50)

        if player.isAlive():
            player.buffWeapon()


def attackEnemy(player, enemy):
    if random.random() < player.critChance:
        print("This was a critical hit")
        player.increaseCriticalDamage()
        enemy.health -= player.criticalDamage
    else:
        enemy.health -= player.damage


def validGuess():
    while True:
        try:
            userInput = int(input("Make your guess: "))
            return userInput
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
