import tst

MENU_PROMPT = """-- COFFEE BEAN APP --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection:"""


def menu():
    connection = tst.connect()
    tst.create_tables(connection)

    user_input = input(MENU_PROMPT)
    
#    while user_input != "5":
        
    if user_input == "1":
        name = input("Enter bean name: ")
        method = input("Enter how you've prepared it: ")
        rating = int(input("Enter your rating score(0-100): "))
        tst.add_bean(connection, name, method, rating)
    elif user_input == "2":
        beans = tst.get_all_beans(connection)
        for bean in beans:
            print(bean)
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    else:
        print('Invalid input, please try again!')


menu()