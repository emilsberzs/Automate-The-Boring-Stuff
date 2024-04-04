#Program for organizing lists of string into a neatly formatted table output

table_data = [['apples', 'oranges', 'cherries', 'bananas'],
              ['Alice', 'Bob','Carol','David'],
              ['dogs','cats','moose','goose']]
column_widths = []

def print_table(table):
    for list in table
        #Find the longest word in each list, add 1 (to accomodate spacing between columns), and save it as width of column:
        column_width = 0
        for item in list:
            if len(item) + 2 > column_width:
                column_width = len(item) + 2
        column_widths.append(column_width)

    for i in range(0,len(table[0])): #For each row, corresponding to number of elements in each inner list
        row = ''                     #Initialise row as an empty string
        for j in range(0,len(table)): #For each inner list
            row += table[j][i].rjust(column_widths[j]) #Add 
        print(row)
            
#Better code, taken from Stack Over Flow
def print_table_2(tab):
    for j in range(len(tab[0])):
        for i in range(len(tab)):
            m = max([len(s) for s in tab[i]])
            print(tab[i][j].rjust(m), end=' ')
        print('')

print_table_2(table_data)