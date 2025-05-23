import logging

# Configuration du fichier de log
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)


def get_number(prompt):
    """Demande un nombre entier à l'utilisateur avec validation (non vide)."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            return int(user_input)
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

def get_string(prompt):
    """Demande une chaîne alphabétique à l'utilisateur avec validation."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            if not user_input.isalpha():
                raise ValueError("Input must contain only letters.")
            return user_input
        except ValueError as e:
            print("Invalid input! Please enter letters only (no numbers or symbols).")
            logging.error(f"ValueError occurred: {e}")

def get_binary_choice(prompt):
    """Demande à l'utilisateur d'entrer 1 ou 0 uniquement, avec validation complète."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            value = int(user_input)
            if value not in (0, 1):
                raise ValueError("Input must be 0 or 1.")
            return value
        except ValueError as e:
            print("Invalid input! Please enter 1 or 0.")
            logging.error(f"ValueError occurred: {e}")

def get_menu_choice(prompt):
    """Demande à l'utilisateur d'entrer 1 ou 0 uniquement, avec validation complète."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty.")
            value = int(user_input)
            if value not in (1,2,3,4):
                raise ValueError("Input must be between 1 or 4.")
            return value
        except ValueError as e:
            print("Invalid input! Please enter 1 or 4.")
            logging.error(f"ValueError occurred: {e}")

def view_summary(data):
    if not data:
        print("nothing here.")
        return  # on sort de la fonction
    for key, value in data.items():
        #print(f"Categorie: {key}")
        if not value:
            print("  There is nothing here.")
        else:
            print(f"Categorie: {key} \n  {' '.join(f'- {group[0]} : {group[1]}' for group in value)} ")

def view_expenses_by_categorie(data):
    if not data:
        print("nothing here .")
        return  # on sort de la fonction
    for key, value in data.items():
        #print(f"Categorie: {key}")
        if not value:
            print("  There is nothing here.")
        else:
            print(f"Categorie: {key} \n  Total: {sum(group[1] for group in value)}")




def personnal_tracker():
    expenses = dict()
    boucle = True
    while boucle:
        print("Welcome to the Personal Finance Tracker! \n")
        choice = get_menu_choice("1 - Add an expense with a description, category, and amount. \n"
                           "2 - View all expenses. \n"
                           "3 - View a summary of expenses by category. \n"
                           "4 - leave \n")
        if choice == 1:
            while True:
                categorie = get_string("Enter expense category > ")
                categorie_exists = False

                # Vérifie si la catégorie existe déjà
                reuse = 0
                for key in expenses:
                    if key.strip().lower() == categorie.strip().lower():
                        print("This category already exists.")
                        reuse = get_binary_choice("Do you want to reuse it? (1 = Yes, 0 = No) > ")
                        if reuse == 0:
                            # Demande une nouvelle catégorie
                            categorie_exists = True
                        else:
                            # On garde cette catégorie existante
                            categorie = key  # récupère la forme exacte déjà dans le dict
                            categorie_exists = False
                        break

                if categorie_exists:
                    continue  # recommencer le while pour ressaisir la catégorie

                expense_description = get_string("Enter expense description > ")
                amount = get_number("Enter amount > ")

                if reuse == 1:
                    for key,value in expenses.items():
                        if key == categorie:
                            value.append((expense_description,amount))
                else:
                    expenses.update({categorie:[(expense_description,amount)]})

                # Proposer à l'utilisateur de continuer ou pas
                new = get_binary_choice("If you are finished, press 0. Otherwise, press 1 > ")
                if new == 0:
                    break

        if choice == 2:
            view_summary(expenses)

        if choice == 3:
            view_expenses_by_categorie(expenses)

        if choice == 4:
            print("Goodbye!")
            break



personnal_tracker()





