from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon Name",["Pik","Charm","Squa"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)