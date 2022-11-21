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

