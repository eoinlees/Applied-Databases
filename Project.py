# Eoin Lees
# Applied Databases Project

#import pymysql as sql
#
#sql.connect()
#conn = sql.connect(user="root",cursorclass=sql.cursors.DictCursor,
#password="root",
#host="localhost",
#db="school",
#port=3306)



# Main function
def main():
	# Initialise array
	array = []

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			viewPeople()
			display_menu()
		elif (choice == "2"):
			viewCountriesByIndYear()
			display_menu()
		elif (choice == "3"):
			addNewPerson()
			display_menu()
		elif (choice == "4"):
			viewCountriesByName()
			display_menu()
		elif (choice == "5"):
			viewCountriesByPop()
			display_menu()
		elif (choice == "6"):
			FindStudentsByAddress()
			display_menu()
		elif (choice == "7"):
			addNewCourse()
			display_menu()
		elif (choice == "x"):
			break;
		else:
			display_menu()
			


def viewPeople():
	print("people")

def viewCountriesByIndYear():

	print("Countries by independence year")
def addNewPerson():
	print("New person added")

def viewCountriesByName():
	print("Countries by name")

def viewCountriesByPop():
	print("Countries by population")

def FindStudentsByAddress():
	print("Student Found")

def addNewCourse():
	print("new course added")

def display_menu():
	print("")
	print("MENU")
	print("=" * 4)
	print("1 - View People")
	print("2 - View Countries by Independence Year")
	print("3 - Add New Person")
	print("4 - View Countries by name")
	print("5 - View Countries by population")
	print("6 - Find students by Adress")
	print("7 - Add New Course")
	print("x - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()
