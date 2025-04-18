
menu = ["Hamburger", "Pizza", "Fried chicken", "Hot dog", "Tacos", 
        "Mac and cheese", "Turkey sandwich", "French fries", 
        "Chicken wings", "Caesar salad"] 

def greet():
    mesera = "Laura"
    user_name = input(f"Hi i'm {mesera} what's your name? ")
    return user_name 


def show_menu():
    print("\t||Menu||")
    number = 1 
    for food in menu:
        print(f"{number}, {food.upper()}") 
        number = number + 1


def take_order():
    option = input("What would you like to order (1-10)")
    if option == "1":
        return menu[0]
    if option == "2":
        return menu[1]
    if option == "3":
        return menu[2]
    if option == "4":
        return menu[3]
    if option == "5":
        return menu[4]
    if option == "6":
        return menu[5]
    if option == "7":
        return menu[6]
    if option == "8":
        return menu[7]
    if option == "9":
        return menu[8]
    if option == "10":
        return menu[9]
    else:
        print("Sorry that's not a valid order") 




greet()
show_menu()
take_order()


    

    
        
    
    
    


