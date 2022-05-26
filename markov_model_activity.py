import numpy as np


def actual_state():
    # The statespace
    states = np.array(["Sleep","Run","Eat"])

    # Possible sequences of events
    transitionName = np.array([["SS","SR","SE"],["RS","RR","RE"],["ES","ER","EE"]])

    # Probabilities matrix (transition matrix)
    transitionMatrix = np.array([[0.3,0.5,0.2],[0.6,0.2,0.2],[0.1,0.1,0.8]])

    return states, transitionName, transitionMatrix

states, transitionName, transitionMatrix = actual_state()

# Set inputs
activity_Today = input('Activity Today is? ')

times = int(input('How many time steps? '))

sequences = int(input('How many sequences? '))

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    activityToday = activity_Today
    activityList = [activityToday]
    i = 0
    prob = 1

    while i != days:
        if activityToday == states[0]:
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            
            if change == transitionName[0][0]:
                prob = prob * transitionMatrix[0][0]
                activityList.append(states[0])
                pass
            elif change == transitionName[0][1]:
                prob = prob * transitionMatrix[0][1]
                activityToday = states[1]
                activityList.append(states[1])
            else:
                prob = prob * transitionMatrix[0][2]
                activityToday = states[2]
                activityList.append(states[2])

        elif activityToday == states[1]:
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            
            if change == transitionName[1][0]:
                prob = prob * transitionMatrix[1][0]
                activityToday = states[0]
                activityList.append(states[0])
                pass
            elif change == transitionName[1][1]:
                prob = prob * transitionMatrix[1][1]
                activityList.append(states[1])
            else:
                prob = prob * transitionMatrix[1][2]
                activityToday = states[2]
                activityList.append(states[2])

        elif activityToday == states[2]:
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            
            if change == transitionName[2][0]:
                prob = prob * transitionMatrix[2][0]
                activityToday = states[0]
                activityList.append(states[0])
                pass
            elif change == transitionName[2][1]:
                prob = prob * transitionMatrix[2][1]
                activityToday = states[1]
                activityList.append(states[1])
            else:
                prob = prob * transitionMatrix[2][2]
                activityList.append(states[2])
        
        i += 1    
    
    return activityList

# To save every activityList
list_activity = []
count0 = 0
count1 = 0
count2 = 0

# `Range` starts from the first count up until but excluding the last count
for iterations in range(1,sequences):
        list_activity.append(activity_forecast(times))

# Iterate through the list to get a count of all activities ending in each state
for smaller_list in list_activity:
    if(smaller_list[times] == states[0]):
        count0 += 1

    elif(smaller_list[times] == states[1]):
        count1 += 1

    elif(smaller_list[times] == states[2]):
        count2 += 1

count = [count0, count1, count2]

# Calculate the probability of starting from state and ending at state
percentage = []
for c in count:
    percentage.append(c/sequences*100)

percentages = np.amax(percentage)

activity_Tomorrow = states[np.argmax(percentage)]

print(f'The probability of starting at state:"{activity_Today}" and ending at state:"{activity_Tomorrow}" = {str(percentages)}%')
