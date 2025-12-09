import json
import numpy as np
from Team19CustomUtils import generalUtils, proceduralTree
#run "python3 -m pip install Team_19_Custom_Utils_Lib" or "pip install --upgrade Team-19-Custom-Utils-Lib" before use


with open('Enemies.json', 'r') as file:
    enemyData = json.load(file)

with open('Weapons.json', 'r') as file:
    weaponData = json.load(file)

with open('reforges.json', 'r') as file:
    reforgeData = json.load(file)

debugMode = 0
rng = np.random.default_rng()




class player:
    hp = None
    defense = None
    regeneration = None
    damage = None
    weapon = None

    def __init__(self):
        with open('difficulty.json', 'r') as file:
            difficultyData = json.load(file)

        print("Choose a difficulty:")
        for i in range(0, difficultyData['gameModeData']['dLength']):
            selector = 'difficulty' + str(i + 1)
            print("(%d) %s: %d starting HP, %d starting DEF, %d HP/turn life regeneration - \033[93m%s\033[0m" %( (i + 1), difficultyData['gameModeData'][selector]['name'], difficultyData['gameModeData'][selector]['startingHealth'], difficultyData['gameModeData'][selector]['startingDefense'], difficultyData['gameModeData'][selector]['startingRegeneration'], difficultyData['gameModeData'][selector]['description'] ) )
        difficultySelection = 0    
        difficultySelection = generalUtils.scanNumericalInput('range', difficultySelection, [0, difficultyData['gameModeData']['dLength']], "enter a choice: ")
        if difficultySelection == 0:
            print("Debug mode selected!")
            debugMode = 1
        else:
            difficultySelection = 'difficulty' + str(difficultySelection)
            print("you have selected %s mode" %difficultyData['gameModeData'][difficultySelection]['name'])
            self.hp = difficultyData['gameModeData'][difficultySelection]['startingHealth']
            self.defense = difficultyData['gameModeData'][difficultySelection]['startingDefense']
            self.regeneration = difficultyData['gameModeData'][difficultySelection]['startingRegeneration']



        

Player = player()
Tree = proceduralTree.tree()
populator = [0] * enemyData['enemyData']['dLength']
for i in range(0, len(populator)):
    populator[i] = i + 1
Tree.setSeed(3, 2, 2, populator, False)
Tree.populateBuffers()

print("The seed this run is ", end='')
for i in range(0, len(Tree.seed)):
    print(Tree.seed[i], sep = '', end = '')
for i in range(0, len(populator)):
    print(populator[i], sep = '', end = '')


def combat(Player: player, enemy: int):
    #function to begin a combat encounter
    enemyName = enemyData['enemyData']['enemy' + str(enemy)]['name']
    enemyHP = enemyData['enemyData']['enemy' + str(enemy)]['baseHealth']
    enemyDEF = enemyData['enemyData']['enemy' + str(enemy)]['baseDefense']
    enemyATK = enemyData['enemyData']['enemy' + str(enemy)]['baseDamage']

    print("Combat initiated against %s - %d HP / %d DEF / %d ATK" % (enemyName, enemyHP, enemyDEF, enemyATK ) ) 

    while enemyHP > 0:
        moveSelection = 0
        for turnCount in range(1, 2):
            match turnCount:
                case 1:
                    #player turn
                    print("Your turn! What will you do?")
                    print("(1) Attack")
                    print("(2) Defend")
                    input = 0
                    input = generalUtils.scanNumericalInput('range', input, [1,2], 'Make your choice: ')
                    match input:
                        case 1:
                            #attack
                            moveSelection = 1
                            print("You dealt %d damage!" %Player.damage)
                            enemyHP -= Player.damage
                            print("%s is now on %d HP" % (enemyName, enemyHP) )
                        case 2:
                            #defend
                            moveSelection = 2
                            print("")
                case 2:
                    #enemy turn
                    print("")

    return 0

def dropLoot():
    #returns weaponID of dropped weapon, if any, otherwise return 0
    roll = rng.random()
    for i in range(weaponData['weaponData']['dLength'], 0, -1):
        if(roll <= weaponData['weaponData']['weapon' + str(i)]['obtainRate']):
            return i
    return 0
    

#the current buffer will indicate which enemies are to be fought on the current depth
#the future buffer will indicate which enemies are to be fought on the next depth

if(debugMode == 1):
    print("\ndebug: enemies encountered on current depth: ", end = '')
    for i in range(0, len(Tree.presentBuffer)):
        selector = 'enemy' + str(Tree.presentBuffer[i])
        print(enemyData['enemyData'][selector]['name'], sep = '', end = '')
        if i < len(Tree.presentBuffer) - 1:
            print(", ", sep = '', end = '')
    print("\n")






