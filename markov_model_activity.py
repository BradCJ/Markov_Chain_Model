import numpy as np


# The statespace
states = ["Sleep","Run","Icecream"]

# Possible sequences of events
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.05,0.9,0.05],[0.05,0.05,0.9],[0.9,0.05,0.05]]

activity_Today = input('Activity Today is? ')

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activityToday = activity_Today
    activityList = [activityToday]
    i = 0
    prob = 1

    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            
            if change == "SS":
                prob = prob * transitionMatrix[0][0]
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * transitionMatrix[0][1]
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * transitionMatrix[0][2]
                activityToday = "Icecream"
                activityList.append("Icecream")

        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            
            if change == "RS":
                prob = prob * transitionMatrix[1][0]
                activityToday = "Sleep"
                activityList.append("Sleep")
                pass
            elif change == "RR":
                prob = prob * transitionMatrix[1][1]
                activityList.append("Run")
            else:
                prob = prob * transitionMatrix[1][2]
                activityToday = "Icecream"
                activityList.append("Icecream")

        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            
            if change == "IS":
                prob = prob * transitionMatrix[2][0]
                activityToday = "Sleep"
                activityList.append("Sleep")
                pass
            elif change == "IR":
                prob = prob * transitionMatrix[2][1]
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * transitionMatrix[2][2]
                activityList.append("Icecream")
        
        i += 1    
    
    return activityList

# To save every activityList
list_activity = []
count0 = 0
count1 = 0
count2 = 0
times = int(input('How many time steps? '))
sequences = int(input('How many sequences? '))

# `Range` starts from the first count up until but excluding the last count
for iterations in range(1,sequences):
        list_activity.append(activity_forecast(times))

# Iterate through the list to get a count of all activities ending in state:'Run'
for smaller_list in list_activity:
    if(smaller_list[times] == states[0]):
        count0 += 1

    elif(smaller_list[times] == states[1]):
        count1 += 1

    elif(smaller_list[times] == states[2]):
        count2 += 1

count = [count0, count1, count2]

# Calculate the probability of starting from state:'Sleep' and ending at state:'Run'
percentage = []
for c in count:
    percentage.append(c/sequences*100)

percentages = np.amax(percentage)

activity_Tomorrow = states[np.argmax(percentage)]

print(f'The probability of starting at state:"{activity_Today}" and ending at state:"{activity_Tomorrow}" = {str(percentages)}%')
