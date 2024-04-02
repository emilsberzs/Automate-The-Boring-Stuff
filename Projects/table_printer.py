#Program for organizing lists of string into a neatly formatted table output

table_data = [['apples', 'oranges', 'cherries', 'bananas'],
              ['Alice', 'Bob','Carol','David'],
              ['dogs','cats','moose','goose']]

def print_table(table):
    for list in table:

        #Find the longest word in each list, add 1 (to accomodate spacing between columns), and save it as width of column:
        column_width = 0
        for item in list:
            if len(item) + 1 > column_width:
                column_width = len(item) + 1
        
        list.append(column_width)

        #Stuck here, need to format rows and print out. ATBS page 154.
    
            

print_table(table_data)