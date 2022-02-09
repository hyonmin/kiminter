'''
there is a report which should be done once a week.
It should be printed like below.

- x weeks Report -
Dep:
Name:
Task Summary:

make a code to produce 1~50 weeks report

condition: the names of files should be '1weeks.txt', '2weeks.txt', ...
'''


for x in range(1,51):
	files = open(str(x) + "weeks.txt", 'w', encoding = "utf8")
	print('- {} weeks Report -' .format(x), file = files)
	print("Dep: ", file = files)
	print("Name: ", file = files)
	print("Task Summary: ", file = files)
	files.close()

for x in range(1,51):
	with open(str(x)+'weeks.txt', 'w', encoding = 'utf8') as reports:
		reports.write("- {0} weeks Report -" .format(x))
		reports.write("\nDep: ")
		reports.write("\nName: ")
		reports.write("\nTask Summary: ")
	    
