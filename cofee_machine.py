class CoffeeMachine:

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        # Starting components machine has
        self.available = {'water': water, 'milk': milk, 'beans': beans, 'disposable_cups': cups, 'money': money}

        # Components and values of selected coffee
        self.coffee_menu_list = {'1': {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4},
                                 '2': {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7},
                                 '3': {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6},
                                 'back': 'back to main menu'}

        # Main menu items and them call functions
        self.main_menu_list = {'buy': self.buy, 'fill': self.fill, 'take': self.take,
                               'remaining': self.remaining, 'exit': self.exitnow}

        # "state" is necessary to select the correct input menu item
        # Also is a state of starting menu
        self.state = self.show_menu

    # Сhecking input for compliance with menu items
    def get_selected_menu_item(self, state):
        self.state = state
        menu_item = input()
        if (self.state == self.show_menu and menu_item in self.main_menu_list.keys())\
                or (self.state == self.buy and menu_item in self.coffee_menu_list.keys()):
            return menu_item  # Return menu_item if is in menu list (by state)
        else:
            print("Unknown command. Please try again\n")
            self.state()  # Else show menu again

    # Show available components
    def remaining(self):
        print()
        print(f"""The coffee machine has:
    {self.available['water']} of water
    {self.available['milk']} of milk
    {self.available['beans']} of coffee beans
    {self.available['disposable_cups']} of disposable cups
    {self.available['money']} of money\n""")

    # Show main menu and call selected operation
    def show_menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        operation = self.get_selected_menu_item(self.show_menu)
        self.main_menu_list[operation]()
        self.show_menu()

    def buy(self):

        # Func return True if all components available, else "not_enough_component"
        def can_make_coffee(coffee):
            if self.available['water'] < self.coffee_menu_list[coffee]['water']:
                return 'water'
            elif self.available['milk'] < self.coffee_menu_list[coffee]['milk']:
                return 'milk'
            elif self.available['beans'] < self.coffee_menu_list[coffee]['beans']:
                return 'beans'
            elif self.available['disposable_cups'] < 1:
                return 'disposable cups'
            else:
                return True

        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        selected_coffee = self.get_selected_menu_item(self.buy)
        if selected_coffee != 'back':
            if not isinstance(can_make_coffee(selected_coffee), bool):
                print(f'Sorry, not enough {can_make_coffee(selected_coffee)}!\n')  # Print "not_enough_component"
            else:
                print("I have enough resources, making you a coffee\n")
                self.available['water'] -= self.coffee_menu_list[selected_coffee]['water']
                self.available['milk'] -= self.coffee_menu_list[selected_coffee]['milk']
                self.available['beans'] -= self.coffee_menu_list[selected_coffee]['beans']
                self.available['disposable_cups'] -= 1
                self.available['money'] += self.coffee_menu_list[selected_coffee]['cost']
        self.show_menu()

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.available['water'] += int(input())
        print("Write how many ml of milk do you want to add:")
        self.available['milk'] += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.available['beans'] += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.available['disposable_cups'] += int(input())

    def take(self):
        print(f"I gave you ${self.available['money']}\n")
        self.available['money'] = 0
        self.state = self.show_menu

    # If "exit" was selected from main menu
    @staticmethod
    def exitnow():
        exit(0)


chef = CoffeeMachine()
chef.state()  # Show main menu from state
