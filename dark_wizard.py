# Base Character class
import random


class Character:
    def __init__(self, name, health, attack_power, ability1, ability2):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability1_des = ""
        self.ability2_des = "" 
        self.player_class = ""
        self.status = ""
        self.stun_counter = 0
        self.min_damage = 5
        self.war_atk_cntr = 0
        self.rage = False
        self.stats_counter = 0
        self.burn_cntr = 0
    def health_check(self):
        self.heal()
        if self.health > self.max_health:            
            self.health = self.max_health
            print(f"{self.name}'s Current Health: {self.health}")
        else:
            print(f"{self.name}'s Current Health: {self.health}")
        
    
    def heal(self):
        heal = random.randint(10, 20)
        self.health += heal
        print(f"{self.name} regenerates {heal} points of health!")
    def status_check(self):
        #checks to see if character is frozen or if opponent has dodged
        #checked stats or blocked
        if self.status == "Burning":
            self.burn_cntr += 1
            self.health -= 15
            print(f"{self.name} was burnt for 15 damage!!")
            if self.burn_cntr == 3:
                self.status = ""
                self.burn_cntr = 0
        if self.status == "Dodged":
            
            self.stun_counter += 1
            if self.stun_counter == 2:
                self.status = ""
                self.stun_counter = 0
        if self.status == "Frozen":
                
                self.stun_counter += 1
                if self.stun_counter == 4:
                    self.status = ""
                    self.stun_counter = 0
        if self.status == "Blocked":
                
                self.stun_counter += 1
                if self.stun_counter == 2:
                    self.status = ""
                    self.stun_counter = 0
        if self.status == "stats":
            
            self.stats_counter += 1
            if self.stats_counter == 2:
                self.status = ""
                self.stats_counter = 0

    def attack(self, opponent):
        if self.rage == True:
            self.war_atk_cntr += 1
            if self.war_atk_cntr == 4:
                self.attack_power -= 10
                self.rage = False
        attack = self.attack_power
        attack = random.randint(self.min_damage,self.attack_power)
            
        opponent.health -= attack
        print(f"{self.name} attacks {opponent.name} for {attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def abilities(self, opponent):
               
        print("which ability would you like to use?" +
              f"\n1. {self.ability1}:\t\t\t\t\t{self.ability2}:\n" +
              f"{self.ability1_des}!\t\t" +
              f"{self.ability2_des}!!\n" +
              "----------------------------------")
        choice = input()
        if choice == '1':
            #for mages burning effect
            if self.player_class == "M":
                opponent.status = "Burning"
                opponent.burn_cntr = 0
                attack = self.attack_power
                attack = random.randint(self.min_damage,self.attack_power)
                attack += 30
                opponent.health -= attack
                print(f"{self.name} attacks {opponent.name} for {attack} damage!")
            #for warrior rage effect
            if self.rage == True:
                self.war_atk_cntr += 1
                if self.war_atk_cntr == 4:
                    self.attack_power -= 10
                    self.min_damage -= 10
            if self.player_class == "R":
                attack2 = random.randint(self.min_damage,self.attack_power)
                attack1 = random.randint(self.min_damage,self.attack_power)
                attack = attack1 + attack2
                opponent.health -= attack
                print(f"{self.name} attacks {opponent.name} for {attack} damage!")
            if self.player_class == "W":
                attack = self.attack_power
                attack = random.randint(self.min_damage,self.attack_power)
                attack += 20
                opponent.health -= attack
                print(f"{self.name} attacks {opponent.name} for {attack} damage!")
            if self.player_class == "P":
                attack = self.attack_power
                attack = random.randint(self.min_damage,self.attack_power)
                attack += 30
                opponent.health -= attack
                print(f"{self.name} attacks {opponent.name} for {attack} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
            
        elif choice == '2':
            #Warrior Rage ability
            if self.player_class == "W":
                self.rage = True
                self.war_atk_cntr = 0
                if self.war_atk_cntr < 4:
                    self.attack_power += 10
                    self.min_damage += 10

                
            #Mage Pillar of Ice ability
            if self.player_class == "M":
                
                opponent.status = "Frozen"
                opponent.stun_counter = 0
                print(f"{self.name} Froze {opponent.name} where they stand!!")
                
                
            #Rogue Tax Evasion ability
            if self.player_class == "R":
                opponent.status = "Dodged"
                opponent.stun_counter = 0
                print(f"{self.name} dodged {opponent.name}'s incoming attack!!")
                
                
            #Paladin Divine Shield ability
            if self.player_class == "P":
                opponent.status = "Blocked"
                opponent.stun_counter = 0
                print(f"{self.name} is shielded by the Light of the Goddess!!")
            
        else:
                print("Invalid choice. Try again.")
                opponent.status = "stats"
                opponent.stats_counter = 0
                
                
    

    def display_stats(self,):
        
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, ability1='Power Attack',
                         ability2='2. Rage')
        self.player_class = "W"
        self.ability1_des = "Attack your enemies with full force!!"
        self.ability2_des = "\tRAAAAAGGGGGEEEE!!!"
        self.min_damage = 10
    
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, ability1= 'Fireball',
                         ability2= "2. Pillar of Ice")
        self.player_class = "M"
        self.ability1_des = "Lob a Fireball at your foes!!"
        self.ability2_des = "\tStop your enemy in their tracks!!!"
        self.min_damage = 15
#Archer class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30, ability1= "Double Shot",
                         ability2= "2. Tax Evasion")
        self.player_class = "R"
        self.ability1_des = "Fire 2 arrows at your enemy!!"
        self.ability2_des = "\tNot even the Gov't can catch you!!!"
        self.min_damage = 12
    
#Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=35, ability1= "Divine Spear",
                         ability2= "\t\t2. Divine Shield")
        self.player_class = "P"
        self.ability1_des = "The Goddess lends you her spear to strike down your foe!!"
        self.ability2_des = "The Goddess protects you from harm!!!"
        self.min_damage = 20

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15,ability1='',ability2='')
        
    

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':        
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Rogue(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.abilities(wizard)
        elif choice == '3':
            player.health_check()
        elif choice == '4':
            player.display_stats()
            wizard.stats_counter = 0
            wizard.status = "stats"
        else:
            print("Invalid choice. Try again.")
            wizard.status = "stats"
            wizard.stats_counter = 0

        if wizard.health > 0:
            wizard.status_check()     
            
            if wizard.status == "" or wizard.status != "Frozen" and wizard.status != "stats":
                wizard.health_check()

            if wizard.status == "" or wizard.status == "Burning":
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard, {wizard.name}, has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
