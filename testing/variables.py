#This file contains the variables and their function

#This function defines the base values for the player/monsters
def defBaseValues(failsafe, health, damage, resistance):
    #The failsafe value determines if the program runs.
    #The value defaults to 0 (the program does not run) in the event the program runs in game
    #If the value is 2, then the program runs but the input messages will not play.
    #This is intended to be used by the game for the player values or developer monsters
    if failsafe == 1:
        #The baseValue list goes down the base statistic in this order, [health, damage, resistance]
        baseValues = []
        #The base health determines how many points of damage the enemy can take before being defeated
        placeholder = int(input("How much base health does the enemy have? "))
        baseValues.append(placeholder)
        #The base damage determines how many raw points of damage the enemy deals per attack
        placeholder = int(input("How much base damage does the enemy deal?"))
        baseValues.append(placeholder)
        #The base resistance determines how amount of reduced damage the enemy takes
        #The base resistance value is maximized at 80% reduced damage
        placeholder = int(input("how much base resistance does the enemy deal?"))
        if placeholder > 80:
            placeholder = 80
        baseValues.append(placeholder)
        return baseValues
    elif failsafe == 2:
        baseValues = []
        baseValues.append(health)
        baseValues.append(damage)
        if resistance > 80:
            resistance = 80
        baseValues.append(resistance)
        return baseValues
def defModifier():
    #healthMod determines how much the health is increased or decreased
    #damageMod determines how much the damage is increased or decreased
    #resistanceMod determines how much the resistance is increased or decreased
    #lifestealMod determines how much the entity is healed per damage point dealt (negative value heals the opposing entity instead of the attacking entity)
    #bleedMod determines how much damage the entity takes over time per round (negative value heals the attacked entity per round instead of harming it)
    #healMod determines how much health is restored upon consuming the item
    #healingMod determines the magnitude of healing, positive values increase the magnitude while negative decrease the magnitude
    valueIndex = []
    placeholder = int(input('What is the passive magnitude of health?'))
    valueIndex.append(placeholder)
    placeholder = int(input('What is the passive magnitude of damage?'))
    valueIndex.append(placeholder)
    placeholder = int(input('What is the passive integer of resistance?'))
    valueIndex.append(placeholder)
    placeholder = int(input('What is the active percentage of lifesteal?'))
    valueIndex.append(placeholder)
    placeholder = int(input('What is the active amount of bleed?'))
    valueIndex.append(placeholder)
    placeholder = int(input('What is the active amount of health restored?'))
    valueIndex.append(placeholder)
    placeholder = int(input('What is the active magnitude of healing dealt?'))
    valueIndex.append(placeholder)
    return valueIndex
testValue1 = defModifier()
testValue2 = defModifier()
def modifierAdding(variable1, variable2):
    totalHealthMod = variable1[0]+variable2[0]
    print('The maximum value of healthMod is', totalHealthMod)
    totalDamageMod = variable1[1]+variable2[1]
    print('The maximum value of damageMod is', totalDamageMod)
    totalResistanceMod = variable1[2]+variable2[2]
    print('The maximum value of resistanceMod is', totalResistanceMod)
    totalLifeStealMod = variable1[3]+variable2[3]
    print('The maximum value of lifestealMod is', totalLifeStealMod)
    totalBleedMod = variable1[4]+variable2[4]
    print('The maximum value of bleedMod is', totalBleedMod)
    totalHealMod = variable1[5]+variable2[5]
    print('The maximum value of healMod is', totalHealMod)
    totalHealingMod = variable1[6]+variable2[6]
    print('The maximum value of healingMod is', totalHealingMod)
print(modifierAdding(testValue1,testValue2))