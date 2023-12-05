import sys
total = 0
for line in sys.stdin:
    gamenumber = ""
    game = line.split(':')

    #Determine Game Number
    for char in game[0]:
        if char.isdigit():
            gamenumber+= char
    
    #Manmade horrors beyond our comprehension (declare dictionary, split/clean data and match to existing keys)
    game = game[1].split(';')
    highestCounts = {'red': 0, 'green': 0, 'blue': 0}
    for roll in game:
        colorcounts = {'red': 0, 'green': 0, 'blue': 0}
        turn = roll.split(',')

        for info in turn:
            parts = info.strip().split()
            if len(parts) == 2 and parts[0].isdigit():
                colorcounts[parts[1]] = int(parts[0])

        if(colorcounts['red'] > highestCounts['red']):
            highestCounts['red'] = colorcounts['red']        
        if(colorcounts['blue'] > highestCounts['blue']):
            highestCounts['blue'] = colorcounts['blue']
        if(colorcounts['green'] > highestCounts['green']):
            highestCounts['green'] = colorcounts['green']
        
    print(highestCounts)
    total += highestCounts['red'] * highestCounts['blue'] * highestCounts['green']

        

print(total)