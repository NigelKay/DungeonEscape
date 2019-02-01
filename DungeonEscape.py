#imports
from random import randint
import time

#classes
class Player:

	def __init__(self, name, chartype, health, player_lower_damage, player_upper_damage):
		self.name = name
		self.chartype = chartype
		self.health = health
		self.player_lower_damage = player_lower_damage
		self.player_upper_damage = player_upper_damage

	def attack(self):
		damage = randint(self.player_lower_damage,self.player_upper_damage)
		return damage

class Monster:

	def __init__(self, name, health, monster_lower_damage, monster_upper_damage):
		self.name = name
		self.health = health
		self.monster_lower_damage = monster_lower_damage
		self.monster_upper_damage = monster_upper_damage

	def attack(self):
		damage = randint(self.monster_lower_damage,self.monster_upper_damage)
		return damage

class Turn:

	def roll(self):
		roll_value = randint(1,100)
		return roll_value

#Intro
print("\n\n\nWelcome to DungeonEscape.\n")
time.sleep(1)
print("Your only goal is to escape alive.\n")
time.sleep(3)
print("You will be asked to choose a class: Paladin, Warrior or Berserker.\n")
time.sleep(3)
print("The Paladin has been blessed by the gods with high health.")
time.sleep(3)
print("The Berserker has trained his attack to umatched levels.")
time.sleep(3)
print("The Warrior is a well rounded individual with balanced stats.\n")
time.sleep(5)
print("Now, let's get you out of here...")
time.sleep(0.5)
print("\n")
time.sleep(0.5)
print("\n")
time.sleep(0.5)
print("\n")
time.sleep(0.5)

playerName = input("Enter your name: ")
playerClass = input("Choose a class: Paladin, Berserker or Warrior: (P/B/W)")

#Class stats
if playerClass[0].upper() == 'P':
	playerClassValid = 'Paladin'
elif playerClass[0].upper() == 'B':
	playerClassValid = 'Berserker'
else:
	playerClassValid = 'Warrior'

if playerClassValid == 'Paladin':
	playerHealth = 120
	pud = 24
	pld = 16
elif playerClassValid == 'Berserker':
	playerHealth = 80
	pud = 36
	pld = 24
else:
	playerHealth = 100
	pud = 30
	pld = 20

time.sleep(1)
print(f"\nAh, {playerName} the {playerClassValid}.. You may just survive..")
time.sleep(2)
print("\n\n\n\n\n")
gamePlayer = Player(playerName, playerClassValid, playerHealth, pld, pud)
#playerMaxHealth var for health potions
playerMaxHealth = gamePlayer.health

#monster instances
giantspider = Monster('Giant Spider',30,3,9) #8%
goblin = Monster('Goblin',15,2,5) #8%
troll = Monster('Troll',50,12,25) #8%
nympth = Monster('Nympth',38,4,8) #8%
bandit = Monster('Bandit',20,1,3) #8%
dragon = Monster('Dragon',100,10,45) #4%
dwarf = Monster('Dwarf',25,2,5) #8%
vampire = Monster('Vampire',35,9,12) #8%
firegolem = Monster('Fire Golem',70,15,28) #4%
siren = Monster('Siren',30,2,10) #8%
cyclops = Monster('Cyclops',40,10,18) #8%
demonlord = Monster('Demon Lord',70,18,32) #4%
slime = Monster('Slime',400,0,4) #4
skeleton = Monster('Skeleton',18,5,14) #8%
hydra = Monster('Hydra',90,8,30) #4%


#dice instance
game_dice = Turn()

#gameplay functions
def monsterCombat():
	monster_outcomes = {1:giantspider,2:goblin,3:skeleton,4:slime,5:demonlord,6:cyclops,7:siren,8:vampire,9:bandit,10:troll,
						11:dragon,12:skeleton,13:slime,14:skeleton,15:goblin,16:hydra,17:siren,18:firegolem,19:dwarf,20:giantspider,
						21:cyclops,22:skeleton,23:slime,24:vampire,25:skeleton,26:vampire,27:goblin,28:firegolem,29:vampire,30:troll,
						31:nympth,32:giantspider,33:dwarf,34:nympth,35:cyclops,36:vampire,37:bandit,38:dwarf,39:bandit,40:nympth,
						41:cyclops,42:hydra,43:vampire,44:troll,45:hydra,46:bandit,47:firegolem,48:nympth,49:dwarf,50:giantspider,
						51:firegolem,52:slime,53:nympth,54:siren,55:troll,56:cyclops,57:siren,58:goblin,59:dwarf,60:troll,
						61:cyclops,62:giantspider,63:hydra,64:skeleton,65:skeleton,66:bandit,67:siren,68:giantspider,69:nympth,70:troll,
						71:dragon,72:skeleton,73:demonlord,74:siren,75:bandit,76:giantspider,77:goblin,78:nympth,79:dragon,80:troll,
						81:demonlord,82:siren,83:goblin,84:giantspider,85:vampire,86:cyclops,87:troll,88:dwarf,89:bandit,90:nympth,
						91:vampire,92:demonlord,93:cyclops,94:goblin,95:dwarf,96:siren,97:goblin,98:bandit,99:dwarf,100:dragon}

	monster_roll = randint(1,100)
	scenarioMonster = monster_outcomes[monster_roll]
	print(f"\nYou ran into a {scenarioMonster.name}")
	time.sleep(1)
	print("Looks like it will attack!\n")
	time.sleep(1)
	monsterHealth = scenarioMonster.health

	while gamePlayer.health > 0 and monsterHealth > 0:
		m_turn_attack = scenarioMonster.attack()
		p_turn_attack = gamePlayer.attack()

		#if statement to make sure hit is not higher than player health
		if m_turn_attack >= gamePlayer.health:
			print(f"The {scenarioMonster.name} hit a {gamePlayer.health}.")
		else:

		#monster turn
			print(f"The {scenarioMonster.name} hit a {m_turn_attack}.")
		gamePlayer.health -= m_turn_attack
		time.sleep(0.5)
		if gamePlayer.health > 0:
			print(f"You have {gamePlayer.health} health points remaining.\n")
		else:
			print(f"Oh dear.. You have died.")
			quit()
		time.sleep(2)

		#Players turn
		#If statement for final hit
		if p_turn_attack >= monsterHealth and monsterHealth > 19:
			print(f"You have a burst of strength as you hit a {monsterHealth} on the {scenarioMonster.name}.")
		elif p_turn_attack >= monsterHealth and monsterHealth > 9:
			print(f"A swift move results in you hitting a {monsterHealth} on the {scenarioMonster.name}.")
		elif p_turn_attack >= monsterHealth:
			print(f"You calmly hit a {monsterHealth} on the {scenarioMonster.name}.")
		else:
			print(f"You hit a {p_turn_attack} on the {scenarioMonster.name}.")
		monsterHealth -= p_turn_attack

		#player turn
		time.sleep(0.5)
		if monsterHealth > 0:
			print(f"The {scenarioMonster.name} has {monsterHealth} health points remaining.\n")
		else:
			print(f"Congratulations, you have killed the {scenarioMonster.name}.")
		time.sleep(3)
	print("\n\n\n\n\n")

def mapMovement():
	mapMovementRoll = randint(1,30)
	mapMovementOutcomes = {1:'You walk down a corridor, bones lay scattered on the ground..',
							2:'You come to a narrow section of the tunnel, you are forced to walk sideways.',
							3:'You come to a low section of the tunnel, you are forced to crawl.',
							3:'There seems to be no torches on the wall ahead, its pitch black.',
							4:'You are forced to wade through knee high water..',
							5:'A steep incline to the tunnel is taking its toll on your stamina..',
							6:'The tunnel is poorly lit, you feel a rat brushing your leg.. At least you hope it was a rat.',
							7:'You are forced to be extra careful in this section of the tunnel due to low hanging stalactites.',
							8:'You walk past some strange markings on the wall..',
							9:".. You're sure you have walked down here before..",
							10:'You walk past a torture rack.',
							11:'..... This looks familiar..',
							12:"You walk into a wall, you're sure it wasn't there a minute ago?..",
							13:'Maybe you should have turned left back there?',
							14:'You keep walking for what feels like an hour.',
							15:'You walk up to find a dead end. You turn around and continue..',
							16:'You come to a forked path, you are compelled to go right..',
							17:"Your feet are really starting to hurt.",
							18:'You find that your current path has looped back on itself.',
							19:'You hear stone breaking up ahead.',
							20:'This section of tunnel seem familiar..',
							21:'You see a fresh corpse at the end of the tunnel..',
							22:'You walk past a large oak chair, decaying with the rest of this tunnel.',
							23:'You walk through an open section of cave, a meager supply of firewood lays nearby.',
							24:'You walk to the end of the coridor and find it continues to the left.',
							25:'You follow the tunnel to the right.',
							26:'The tunnel starts to slope downwards, surely this is the wrong way.',
							27:"You're close to the end, you can feel it..",
							28:"You walk past a bulky iron door.. but it's sealed shut.",
							29:'The tunnel widens a little as you walk.',
							30:'The tunnel seems to be sloping upwards'
	}

	print(mapMovementOutcomes[mapMovementRoll])
	time.sleep(3)
	print("\n\n\n\n")


def mapScenario():
	#randints - 10% chance to die
	deathChoice = randint(1,10)
	scenarioRoll = randint(1,3)

	#scenario dict
	scenarioOutcomes = {1:'a',2:'b',3:'c',4:'',5:'',6:'',7:'',8:'',9:'',10:'',
						11:'',12:'',13:'',14:'',15:'',16:'',17:'',18:'',19:'',20:''}

	#scenario matching
	if scenarioOutcomes[scenarioRoll] == 'a':
		print("You are walking down a corridor, there is a hole in the ground.\nDo you:\n1) Walk along the edge\n2) Jump over it\n3) Try a different route?")
	elif scenarioOutcomes[scenarioRoll] == 'b':
		print("You come to a cross-roads.\nDo you:\n1) Go straight.\n2) Go left.\n3) Go Right.\n4) Turn back.")
	elif scenarioOutcomes[scenarioRoll] == 'c':
		print("A goblin approaches you with some 'advice'.\nDo you:\n1) Follow his advice.\n2) Ignore the advice.")
		#etc etc

	time.sleep(1)
	player_choice = 0
	while player_choice not in range(1,11):
		player_choice = int(input("\nEnter your number choice: "))

	#Decide whether player dies.
	if deathChoice == player_choice:
		print("\nOh dear.. You have died.")
		quit()
	else:
		print("\nIt seems you live to see another roll of the die..")
	
	time.sleep(3)
	print("\n\n\n\n\n")

#Escape sequence
def escape():
	print("You are walking down a corridor, this looks familiar..")
	time.sleep(2)
	print("This time you notice a stone jutting out of the wall...")
	time.sleep(1)
	final_choice = input("Will you investigate? (Y/N)")
	if final_choice[0].lower() == 'y':
		time.sleep(2)
		print("\n")
		print("\n")
		time.sleep(0.5)
		print("You hear a rumble..\n\n\n")
		time.sleep(2.5)
		print("A panel of the cave wall slides back, the sunlight pours in..\n\n\n")
		time.sleep(3)
		print("Never return here adventurer..")
		time.sleep(3)
		print("\n")
		time.sleep(0.20)
		print("\n")
		time.sleep(0.20)
		print("\n")
		time.sleep(0.20)
		print("\n")
		time.sleep(0.20)
		print("\n")
		time.sleep(0.20)
		print("\n")
		time.sleep(0.20)
		print("─────────────────────────────────────────────────────────────────────")
		time.sleep(0.20)
		print("─██████████████─██████████████─██████──────────██████─██████████████─")
		time.sleep(0.20)
		print("─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░░░░░██─")
		time.sleep(0.20)
		print("─██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─██░░██████████─")
		time.sleep(0.20)
		print("─██░░██─────────██░░██──██░░██─██░░██████░░██████░░██─██░░██─────────")
		time.sleep(0.20)
		print("─██░░██─────────██░░██████░░██─██░░██──██░░██──██░░██─██░░██████████─")
		time.sleep(0.20)
		print("─██░░██──██████─██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░░░░░░░░░██─")
		time.sleep(0.20)
		print("─██░░██──██░░██─██░░██████░░██─██░░██──██████──██░░██─██░░██████████─")
		time.sleep(0.20)
		print("─██░░██──██░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██─────────")
		time.sleep(0.20)
		print("─██░░██████░░██─██░░██──██░░██─██░░██──────────██░░██─██░░██████████─")
		time.sleep(0.20)
		print("─██░░░░░░░░░░██─██░░██──██░░██─██░░██──────────██░░██─██░░░░░░░░░░██─")
		time.sleep(0.20)
		print("─██████████████─██████──██████─██████──────────██████─██████████████─")
		time.sleep(0.20)
		print("─────────────────────────────────────────────────────────────────────")
		time.sleep(0.20)
		print("─────────────────────────────────────────────────────────────────────")
		time.sleep(0.20)
		print("────██████████████─██████──██████─██████████████─████████████████────")
		time.sleep(0.20)
		print("────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██────")
		time.sleep(0.20)
		print("────██░░██████░░██─██░░██──██░░██─██░░██████████─██░░████████░░██────")
		time.sleep(0.20)
		print("────██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██────██░░██────")
		time.sleep(0.20)
		print("────██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░████████░░██────")
		time.sleep(0.20)
		print("────██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██────")
		time.sleep(0.20)
		print("────██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░██████░░████────")
		time.sleep(0.20)
		print("────██░░██──██░░██─██░░░░██░░░░██─██░░██─────────██░░██──██░░██──────")
		time.sleep(0.20)
		print("────██░░██████░░██─████░░░░░░████─██░░██████████─██░░██──██░░██████──")
		time.sleep(0.20)
		print("────██░░░░░░░░░░██───████░░████───██░░░░░░░░░░██─██░░██──██░░░░░░██──")
		time.sleep(0.20)
		print("────██████████████─────██████─────██████████████─██████──██████████──")
		time.sleep(0.20)
		print("─────────────────────────────────────────────────────────────────────")
		quit()
	else:
		print("You keep walking..\n\n\n\n\n")

def yesNoChoice():
	messageRoll = randint(1,10)
	effectRoll = randint(1,20)

	#message choice A-J
	message_dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j'}
	#{h:healthRestore,i:instaDeath,d:healthReduced,iu:upperAttack,il:lowerAttack}
	#{h:50%,i:5%,d:25%,u:10%,l:10%}
	effect_dict = {1:'il',2:'d',3:'h',4:'h',5:'h',6:'h',7:'d',8:'iu',9:'h',10:'d',
					11:'d',12:'h',13:'du',14:'h',15:'h',16:'h',17:'d',18:'dl',19:'h',20:'i'}

	#if block for message printing
	if message_dict[messageRoll] == 'a':
		print("You find a potion on the ground, do you drink it?")
	elif message_dict[messageRoll] == 'b':
		print("You discover a loose rock, do you wish to investigate?")
	elif message_dict[messageRoll] == 'c':
		print("You find an enchanted amulet, put it on?")
	elif message_dict[messageRoll] == 'd':
		print("You find an ancient well, take a drink?")
	elif message_dict[messageRoll] == 'e':
		print("You're walking down a corridor, you spot something interesting")
		print("It's a door! Would you like to enter?")
	elif message_dict[messageRoll] == 'f':
		print("You find a dusty chest, will you open it?")
	elif message_dict[messageRoll] == 'g':
		print("You stumble upon a ladder, will you see whats at the top?")
	elif message_dict[messageRoll] == 'h':
		print("You uncover an ancient tome, dare to look inside?")
	elif message_dict[messageRoll] == 'i':
		print("On your right is a dull ring upon a pedestal, would you like to take it?")
	elif message_dict[messageRoll] == 'j':
		print("You find a scroll with vague instructions on enchanting your weapon, would you like to try?")

	time.sleep(1)
	playerAnswer = input("Yes or No: ")
	time.sleep(1)
	print("\n")
	#if block for player decision | stat effect
	if playerAnswer[0].lower() == 'y':
		if effect_dict[effectRoll] == 'h':
			gamePlayer.health = playerMaxHealth
			print(f"You're health has been restored to {gamePlayer.health} health points.")

		elif effect_dict[effectRoll] == 'i':
			print("Oh dear.. You have died.")
			quit()

		elif effect_dict[effectRoll] == 'd':
			currentHealth = gamePlayer.health
			gamePlayer.health -= int((currentHealth / 2))
			print(f"Ouch! You have lost half of your remaining health. You now have {gamePlayer.health} health points remaining.")

		elif effect_dict[effectRoll] == 'iu':
			#round 20% increase to int
			increasedUpper = gamePlayer.player_upper_damage * 1.2
			gamePlayer.player_upper_damage = round(increasedUpper)
			print("Your maximum hit has been increased by 20%")

		elif effect_dict[effectRoll] == 'il':
			#make sure min hit cant go above max hit
			if (gamePlayer.player_lower_damage*1.2) >= gamePlayer.player_upper_damage:
				gamePlayer.player_lower_damage = gamePlayer.player_upper_damage
			else:
				#round 20% increase to int
				increasedLower = gamePlayer.player_lower_damage * 1.2
				gamePlayer.player_lower_damage = round(increasedLower)
			print("Your minimum hit has been increased by 20%")

		elif effect_dict[effectRoll] == 'du':
			#make sure max hit cant go below min hit
			if (gamePlayer.player_upper_damage*0.8) <= gamePlayer.player_lower_damage:
				gamePlayer.player_upper_damage = gamePlayer.player_lower_damage
			else:
				#round 20% decrease to int 
				decreasedUpper = gamePlayer.player_upper_damage * 0.8
				gamePlayer.player_upper_damage = round(decreasedUpper)
			print("Your maximum hit has been decreased by 20%")

		elif effect_dict[effectRoll] == 'dl':
			#round 20% decrease to int
			decreasedLower = gamePlayer.player_lower_damage * 0.8
			gamePlayer.player_lower_damage = round(decreasedLower)
			print("Your minimum hit has been decreased by 20%")

	time.sleep(1)
	print("You keep on walking..")
	time.sleep(3)
	print("\n\n\n\n\n")
#game function
def gameloop():
	while True:
		turn_roll = int(game_dice.roll())
		print(f'You roll the die, it lands on {turn_roll}.')
		time.sleep(2)
		print("\n\n\n\n\n")

		#{m:mapMovement,s:mapScenario,e:escape,c:monsterCombat,y:yesNoChoice}
		#{m:30%, s:25%, e:5%, c:25%, y:15%}
		turn_outcome = {1:'y',2:'s',3:'e',4:'c',5:'s',6:'m',7:'m',8:'m',9:'s',10:'s',
						11:'m',12:'c',13:'c',14:'m',15:'m',16:'m',17:'c',18:'m',19:'c',20:'y',
						21:'s',22:'y',23:'s',24:'m',25:'c',26:'m',27:'m',28:'s',29:'y',30:'y',
						31:'c',32:'c',33:'c',34:'m',35:'e',36:'c',37:'c',38:'m',39:'y',40:'c',
						41:'s',42:'m',43:'s',44:'c',45:'m',46:'s',47:'y',48:'s',49:'m',50:'y',
						51:'c',52:'c',53:'s',54:'m',55:'m',56:'m',57:'y',58:'y',59:'c',60:'y',
						61:'s',62:'m',63:'e',64:'c',65:'s',66:'c',67:'c',68:'s',69:'m',70:'y',
						71:'y',72:'s',73:'c',74:'s',75:'c',76:'s',77:'m',78:'m',79:'m',80:'s',
						81:'c',82:'c',83:'y',84:'s',85:'s',86:'m',87:'e',88:'s',89:'s',90:'m',
						91:'s',92:'m',93:'m',94:'y',95:'c',96:'c',97:'m',98:'s',99:'m',100:'e'}

		if turn_outcome[turn_roll] == 'm':
			mapMovement()
		elif turn_outcome[turn_roll] == 's':
			mapScenario()
		elif turn_outcome[turn_roll] == 'e':
			escape()
		elif turn_outcome[turn_roll] == 'c':
			monsterCombat()
		elif turn_outcome[turn_roll] == 'y':
			yesNoChoice()

gameloop()
