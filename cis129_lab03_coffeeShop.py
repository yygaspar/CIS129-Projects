# Yessenia Gaspar
# Module 3: Lab
# 30746 CIS129

#Create an interactive text-based Coffee Shop simulator that calculates and produces a receipt.
#Must allow user to input integers via keyboard input

#create coffee, muffin, and tax variables

coffeePrice = 5
muffinPrice = 4
taxPercent = 0.06

#entry input introduction - for customer raport
print('******************************************************')
print('Thank you for visiting Three Thrones Coffee and Pasteries Shop! ')

#requests and opbtain customer input
coffeeOrders = int(input('How many coffees did you purchase?\n'))
muffinOrders = int(input('How many muffins did you purchase?\n'))

print('Thanks! You ordered ', coffeeOrders, ' coffee(s) and ', muffinOrders, ' muffin(s).',)
print('******************************************************')
print('\n******************************************************')

#Complete the receipt portion of the code.
#Add the coffee amounts and muffin total amount, then charge tax
#Coffee is $5.00 each
#Muffin is $4.00 each
#Tax is 6%

print('Three Thrones Coffee and Pasteries Shop Receipt') 
print('Coffee at $5 each: $', coffeeOrders*coffeePrice, '\nMuffins at $4 each: $', muffinOrders*muffinPrice)

foodOrder = (coffeeOrders*coffeePrice)+(muffinOrders*muffinPrice)
foodOrder = int(foodOrder)

print('6% tax: $', round(taxPercent * foodOrder, 2) )
taxTotal = taxPercent * foodOrder
taxTotal = float(taxTotal)


#Calculate complete total
#add the foodOrder with taxes
print('-----------')
print('Total: $', foodOrder + taxTotal )
print('******************************************************')

#End of receipt lab
