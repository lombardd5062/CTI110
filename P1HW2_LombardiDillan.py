print('This program calculates and displays travel expense')
#October 3, 2023
#CSI-110 P1HW2-Travel Expense
#Dillan Lombardi
#Display "Program goals"
#Diplay "Enter Budget:"
#input budget
#Display "Enter travel destination:"
#input destination/travel
#Display "How much they'll spend on gas"
#input gas
#Display "How much for accomodation"
#input accomodation
#Display "How much for food?"
#input food
#Display "title for travel expense"
#Display "Location", location/travel
#Display "Original budget", budget
#Display "Fuel", gas
#Display "Accomodation", accomodation
#Display "Food", food
#set total = gas + accomodation + food
#set remaining = budget - total
#Display "Remaining Balance:", remaining
print('Enter Budget:', end=' ')
budget=int(input())
print('Enter your travel destination:', end=' ')
travel=input()
print('How much do you think you will spend on gas?', end=' ')
gas=int(input())
print('Approximately, how much will you need for accomodation/hotel?', end=' ')
accomodation=int(input())
print('Last, how much do you need for food?', end=' ')
food=int(input())
print('----Travel Expense----')
print('Location:', travel)
print('Initial Budget', budget)
print('Fuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food)
total = int(gas) + int(accomodation) + int(food)
remaining = int(budget) - int(total)
print('Remaining Balance:', remaining)

