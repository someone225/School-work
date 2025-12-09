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




class player:
    hp = None
    defense = None
    regeneration = None
    movePriority = None

    def __init__(self):
        with open('difficulty.json', 'r') as file:
            difficultyData = json.load(file)

        print("Choose a difficulty:")
        for i in range(0, difficultyData['gameModeData']['dLength']):
            selector = 'difficulty' + str(i + 1)
            print("(%d) %s: %d starting HP, %d starting DEF, %d HP/turn life regeneration, +%d movement priority" %( (i + 1), difficultyData['gameModeData'][selector]['name'], difficultyData['gameModeData'][selector]['startingHealth'], difficultyData['gameModeData'][selector]['startingDefense'], difficultyData['gameModeData'][selector]['startingRegeneration'], difficultyData['gameModeData'][selector]['startingSpeed'] ) )
        difficultySelection = 0    
        difficultySelection = generalUtils.scanNumericalInput('range', difficultySelection, [1, difficultyData['gameModeData']['dLength']], "enter a choice: ")
        difficultySelection = 'difficulty' + str(difficultySelection)
        print("you have selected %s mode" %difficultyData['gameModeData'][difficultySelection]['name'])
        self.hp = difficultyData['gameModeData'][difficultySelection]['startingHealth']
        self.defense = difficultyData['gameModeData'][difficultySelection]['startingDefense']
        self.regeneration = difficultyData['gameModeData'][difficultySelection]['startingRegeneration']
        self.movePriority = difficultyData['gameModeData'][difficultySelection]['startingSpeed']



        

testPlayer = player()



