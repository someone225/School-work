"""
Course Number: ENGR 13300
Semester: fall 2025

Description:
    personal project containing very liberal use of free will

Assignment Information:
    Assignment:     personal project - team 19
    Team ID:        007 - 19 
    Author:         Mark, sheng65@purdue.edu
    Date:           09/12/2025

Contributors:
    Mark, sheng65@purdue [repeat for each]
    numpy API referance: https://numpy.org/doc/stable/reference/index.html#reference
    python JSON API referance: https://docs.python.org/3/library/json.html

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.

    *this program does import a custom library built for the purpose of this course
    which contains functions intended for general use. I am the author of the afformentioned
    library but other team members have access to it for ease of use in group projects. 
"""


import json #<- external modules
import numpy as np
from Team19CustomUtils import generalUtils, proceduralTree #<- modules I made but its also on pypi so its not a private library per se
#run "python3 -m pip install Team_19_Custom_Utils_Lib" or "pip install --upgrade Team-19-Custom-Utils-Lib" before use


#yoink those yummy yummy json files in my tummy
with open('Enemies.json', 'r') as file:
    enemyData = json.load(file)

with open('Weapons.json', 'r') as file:
    weaponData = json.load(file)

with open('reforges.json', 'r') as file:
    reforgeData = json.load(file)


rng = np.random.default_rng()




#for all that talk about not using too  many classes I end up creating a player class
#well this is still more optimal than a bunch of unencapsualted memory lying around everywhere I guess
class player:
    hp = None
    defense = None
    regeneration = None
    damage = None
    apRatio =  None
    weapon = None
    weaponReforge = None
    debug = 0
    # a lot of these variables arent used in debug mode because I pretty much gave the player hacks in debug mode

    def __init__(self):
        with open('difficulty.json', 'r') as file:
            difficultyData = json.load(file)

        #this looks like a lot of code but its just pulling the data already there in the json files and printing it out
        print("Choose a difficulty:")
        for i in range(0, difficultyData['gameModeData']['dLength']):
            selector = 'difficulty' + str(i + 1)
            print("(%d) %s: %d starting HP, %d starting DEF, %d HP/turn life regeneration - \033[93m%s\033[0m" %( (i + 1), difficultyData['gameModeData'][selector]['name'], difficultyData['gameModeData'][selector]['startingHealth'], difficultyData['gameModeData'][selector]['startingDefense'], difficultyData['gameModeData'][selector]['startingRegeneration'], difficultyData['gameModeData'][selector]['description'] ) )
        difficultySelection = 0    
        difficultySelection = generalUtils.scanNumericalInput('range', difficultySelection, [0, difficultyData['gameModeData']['dLength']], "enter a choice: ")
        if difficultySelection == 0:
            print("\033[92mDebug mode selected!\033[0m")
            self.debug = 1
        else:
            difficultySelection = 'difficulty' + str(difficultySelection)
            print("you have selected %s mode" %difficultyData['gameModeData'][difficultySelection]['name'])
            self.hp = difficultyData['gameModeData'][difficultySelection]['startingHealth']
            self.defense = difficultyData['gameModeData'][difficultySelection]['startingDefense']
            self.regeneration = difficultyData['gameModeData'][difficultySelection]['startingRegeneration']
            #its probaby not too hard from here to just finish non-debug mode i mean all i need now is the combat system since stage selection is done as well
            #but this already served its purpose as a tech demo of procedural optimization and json file integration
            #so like as my role model's catchphrase goes: "Take it easy!" - yukkuri reimu



        
#all the code under this is just basic checks and arithmetic all the complicated bits are handled by the libraries

Player = player()
Tree = proceduralTree.tree()
populator = [0] * enemyData['enemyData']['dLength']
for i in range(0, len(populator)):
    populator[i] = i + 1
Tree.setSeed(3, 5, 3, populator, True)
Tree.populateBuffers()
divergenceOptions = [0] * Tree.seed[2]
for i in range(0, Tree.seed[2]):
    divergenceOptions[i] = i + 1


print("The seed this run is ", end='')
for i in range(0, len(Tree.seed)):
    print(Tree.seed[i], sep = '', end = '')
for i in range(0, len(populator)):
    print(populator[i], sep = '', end = '')


def combat(Player: player, enemy: int, devMode: int):
    #function to begin a combat encounter
    enemyName = enemyData['enemyData']['enemy' + str(enemy)]['name']
    enemyHP = enemyData['enemyData']['enemy' + str(enemy)]['baseHealth']
    enemyDEF = enemyData['enemyData']['enemy' + str(enemy)]['baseDefense']
    enemyATK = enemyData['enemyData']['enemy' + str(enemy)]['baseDamage']

    print("Combat initiated against %s - %d HP / %d DEF / %d ATK" % (enemyName, enemyHP, enemyDEF, enemyATK ) ) 
    if devMode == 1:
        print("\033[91mL BOZO!\033[0m %s died to elite hacker skills" % enemyName)
        temp = input("enter any key to proceed: ")
        dropLoot(Player)
        return 1
    else:
        while enemyHP > 0:
            moveSelection = 0
            for turnCount in range(1, 2):
                match turnCount:
                    case 1:
                        #player turn
                        print("Your turn! What will you do?")
                        print("(1) Attack")
                        print("(2) Defend")
                        userInput = 0
                        userInput = generalUtils.scanNumericalInput('range', userInput, [1,2], 'Make your choice: ')
                        match userInput:
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

def dropLoot(Player: player):
    #returns weaponID of dropped weapon, if any, otherwise return 0
    roll = rng.random()
    out = 0
    #this rng mechanism is very very evil will be incredibly infuriating
    #"WHERE IS OMNI MAN, WHERE IS HE!?"
    for i in range(weaponData['weaponData']['dLength'], 0, -1):
        if(roll <= weaponData['weaponData']['weapon' + str(i)]['obtainRate']):
            out = i
            break
   
    if not(out == 0):
        reforgeID = np.random.randint(1, weaponData['weaponData']['dLength'])
        reforgeIndex = 'reforge' + str(reforgeID)
        weaponIndex = 'weapon' + str(out)

        reforgeName = str(reforgeData['reforgeData'][reforgeIndex]['name'])
        baseName = str(weaponData['weaponData'][weaponIndex]['name'])
        

        weaponName = reforgeName + baseName
        weaponDamage = weaponData['weaponData'][weaponIndex]['baseDamage'] * reforgeData['reforgeData'][reforgeIndex]['baseDamageModifier']
        weaponPierce = weaponData['weaponData'][weaponIndex]['apRatio'] * reforgeData['reforgeData'][reforgeIndex]['apModifier']
        weaponBonus = weaponData['weaponData'][weaponIndex]['extraMoves']
        print("you got %s! %d ATK / %d%% AP / %d extra moves" %(weaponName, weaponDamage, weaponPierce * 100, weaponBonus))
        userInput = 0
        userInput = generalUtils.scanNumericalInput('match', userInput, [0, 1], ("Would you like to equip this weapon? (0) - N / (1) - Y: "))
        if(userInput == 1):
            Player.damage = weaponDamage
            Player.apRatio = weaponPierce
            print("you equipped %s" %weaponName)
        else:
            print("you discarded %s" %weaponName)
        #using a class as a function input bypasses the usual containment of a UDF so we can just fuck around with the values however we want
        #not public variables however those are evil and will likely blow up any code
    
    else:
        print("\033[91mUNLUCKY!\033[0m L'il bro didn't even drop anything sucks to suck")
        temp = input("enter any key to proceed: ")

    
    

#the current buffer will indicate which enemies are to be fought on the current depth
#the future buffer will indicate which enemies are to be fought on the next depth

if(Player.debug == 1):

    while Tree.currentDepth <= Tree.seed[0]:
    
        #basically all this big mess does is display the current combat and enemy encounter status
        #thats all
        #it looks like a lot but it really isn't
        print("\ndebug: enemies encountered on current depth: ", end = '')
        for i in range(0, len(Tree.presentBuffer)):
            selector = 'enemy' + str(Tree.presentBuffer[i])
            print(enemyData['enemyData'][selector]['name'], sep = '', end = '')
            if i < len(Tree.presentBuffer) - 1:
                print(", ", sep = '', end = '')
        print("\n")

        for i in range(0, len(Tree.presentBuffer)):
            combat(Player, Tree.presentBuffer[i], 1)
        print("You have completed floor %d" %Tree.currentDepth)
        if(Tree.currentDepth == Tree.seed[0]):
            print("Congrats, you cleared this stupid game")
            break      
        print(" You like gambling, don't you? \n Choose a random set of enemies to fight for floor %d" %(Tree.currentDepth + 1))
        for i in range(0, len(Tree.lookAheadBuffer)):
            print("(%d) " %(i + 1), sep = '', end = '')
            for j in range(0, len(Tree.lookAheadBuffer[0])):
                selector = 'enemy' + str(Tree.lookAheadBuffer[i][j])
                print("???", sep = '', end = '')
                if j < len(Tree.lookAheadBuffer[0]) - 1:
                    print(", ", sep = '', end = '')
            print('\n', sep = '', end = '')
        userInput = 0
        userInput = generalUtils.scanNumericalInput('range', userInput, divergenceOptions, "Make Your Choice: ")
        print("Good Luck")
        Tree.advanceDepths(userInput)
            
    
else:
    print("\nNon debug mode hasn't been finished yet lol")
    #ture
    







