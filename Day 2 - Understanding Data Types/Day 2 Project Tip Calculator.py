print('Welcome to the tip calculator!')
total = input('What was the total bill? $')
tipPercent = input('What percentage tip would you like to give? 10, 12 or 15?')
peopleCount = input('How many people to split the bill?')

totalWithTip = float(total) + (float(total) * (int(tipPercent) / 100))
totalPerPerson = totalWithTip / int(peopleCount)
finalAmount = "{:.2f}".format(totalPerPerson)
print(f'Each person should pay: ${finalAmount}')


