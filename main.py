menu = [
    "Hamburger with fries",
    "Hot Dog",
    "BBQ Ribs",
    "Buffalo Wings",
    "Apple Pie",
    "Mac and Cheese",
    "Pancakes with maple syrup",
    "Peanut Butter and Jelly Sandwich",
    "Clam Chowder",
    "Fried Chicken"
]

See_the_menu = menu 
waiter = "Laura"

print("\nWelcome to Mamma mia che buono!\n")

greet = input(f"Hi I'm {waiter}, what's your name? ")
print(f"Thank you for choosing us, {greet.title()}!") 

see = input("Do you want to see the menu? (yes/no) ").lower()

if see == 'yes':
    print("\n || Here is the menu ↓ ||\n") 
    print(f"1. {See_the_menu[0]}\t $10")
    print(f"2. {See_the_menu[1]}\t $11")
    print(f"3. {See_the_menu[2]}\t $12")
    print(f"4. {See_the_menu[3]}\t $13") 
    print(f"5. {See_the_menu[4]}\t $14") 
    print(f"6. {See_the_menu[5]}\t $15") 
    print(f"7. {See_the_menu[6]}\t $16") 
    print(f"8. {See_the_menu[7]}\t $17") 
    print(f"9. {See_the_menu[8]}\t $18") 
    print(f"10. {See_the_menu[9]}\t $19") 

    take_order = input("\nAre you ready to place an order? (yes/no) ").lower()
    
    if take_order == 'yes':
        while True:
            elegir = input("Choose a dish by number [1-10]: ")
            if elegir == '1':
                print(f"Your {See_the_menu[0]} will be ready in a minute.")
            elif elegir == '2':
                print(f"Your {See_the_menu[1]} will be ready in a minute.")
            elif elegir == '3':
                print(f"Your {See_the_menu[2]} will be ready in a minute.")
            elif elegir == '4':
                print(f"Your {See_the_menu[3]} will be ready in a minute.")
            elif elegir == '5':
                print(f"Your {See_the_menu[4]} will be ready in a minute.")
            elif elegir == '6':
                print(f"Your {See_the_menu[5]} will be ready in a minute.")
            elif elegir == '7':
                print(f"Your {See_the_menu[6]} will be ready in a minute.")
            elif elegir == '8':
                print(f"Your {See_the_menu[7]} will be ready in a minute.")
            elif elegir == '9':
                print(f"Your {See_the_menu[8]} will be ready in a minute.")
            elif elegir == '10':
                print(f"Your {See_the_menu[9]} will be ready in a minute.")
            else:
                print("Sorry, that option is not available.")

            need_more = input("\nDo you want to order something else? (yes/no) ").lower()
            if need_more != 'yes':
                print("\nThanks for your order. Enjoy your meal!")
                break
