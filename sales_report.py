"""Generate sales report showing total melons each salesperson sold."""


salespeople = []    #create list of salespersons' names
melons_sold = []    #create list of melons sold

f = open('sales-report.txt')    #opens text file "sales-report.txt" for data
for line in f:  #for each line in the text file "sales-report.txt", do the following:
    line = line.rstrip()    #remove the extra white space in said line
    entries = line.split('|')   #create list of all data

    salesperson = entries[0]    #add each salesperson's name to empty list above to fill list
    melons = int(entries[2])    #add melons sold (in same order) to empty list above to fill list, convert all numbers to integers

    if salesperson in salespeople:  #if salesperson is already in above salespeople list, do the following:
        position = salespeople.index(salesperson)   #finds said salesperson
        melons_sold[position] += melons #add melons sold from above to existing number of melons quantity
    else:   
        salespeople.append(salesperson) #if salesperson is not in list, add name and melons sold
        melons_sold.append(melons)


for i in range(len(salespeople)):   #loop over indices of salespeople and melons sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') 

#suggestions include using functions and unpacking of list
