# functions.py: function definitions for csw8 final project

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print('==========================')
    print('What would you like to do?')
    for letter, option in menu.items():
        print(f'{letter} - {option}')
    print('==========================')


def print_restaurant_menu(restaurant_menu, spicy_scale_map, name_only, show_idx, start_idx, vegetarian_only=False):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
    param: name_only (Boolean)
            If False, then only the name of the dish is printed.
            Otherwise, displays the formatted dish information.
    param: show_idx (Boolean)
            If False, then the index of the menu is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            dish name, where idx is the 0-based index in the list.
    param: start_idx (int)
            an expected starting value for idx that
            gets displayed for the first dish, if show_idx is True.
    param:  vegetarian_only (Boolean)
            If set to False, prints all dishes, regardless of their
            is_vegetarian status ("yes/no" field status).
             If set to True , display only the dishes with
            "is_vegetarian" status set to "yes".
    returns: None; only prints the restaurant menu
    """
    print('------------------------------------------')
    for dish in restaurant_menu:
        if vegetarian_only==True and dish['is_vegetarian']=='no':
            break
        
        if show_idx == True:
            
            print(f'{start_idx}.', end=' ')
            
        
        print(dish['name'].upper())
        start_idx += 1
        if not name_only:
            calories = dish['calories']
            price = dish['price']
            veg = dish['is_vegetarian']
            spice = spicy_scale_map[dish['spicy_level']]
            
            print(f'* Calories: {calories}')
            print(f'* Price: {price:.1f}')
            print(f'* Is it vegetarian: {veg}')
            print(f'* Spicy level: {spice}')
            print()
    print('------------------------------------------')


def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
    '''
    param: list_menu (list) - A list of additional options from which the user can select an additional list option once they have selected their primary command
    param: restaurant_menu_list (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
            The function first checks that the restaurant_menu_list actually contains items
            from which to display. If the validation passes, the function retrieves a second option from which
            the user can either select to view all items or just vegetarian dishes. Depending on the sub option,
            the function either prints the restaurant menu of all items or just vegetarian dishes
            returns: none
    
    '''
    if len(restaurant_menu_list) == 0:
        print("WARNING: There is nothing to display!")
        input("::: Press Enter to continue")
    else:
        subopt = get_selection("List", list_menu)
        if subopt == 'A':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=False,show_idx=True, start_idx=1, vegetarian_only=False)
        elif subopt == 'V':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=False, show_idx=True, start_idx=1, vegetarian_only=True)

def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu
    The function displays a submenu for the user to choose from.
    Asks the user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.
    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What field would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()  
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def is_num(val):
    """
    param: val(str) - A value that the function validates as a number
    The function first checks that the passed value is a string value. After this validation, if the value is able to be converted
    to a float type object, then the function returns True. If there is an error in converting this value, the function returns false
    returns: True is val is a string and is able to be converted to a float object
    False if val is either not a string or is unable to be converted to a float object
    """
    if not isinstance(val, str):
        return False
    try:
        float(val)
        return True
    except ValueError:
        return False

def is_valid_name(name_str):
    """
    param: name_str (str): A value that the function must validate as a potential name for a dish
    The function first validates name_str as a string object. Then, it checks that name_str is neither less than 3 characters
    long or more than 25 characters long.
    returns: False is name_str is not a string or is not 3-25 characters long
    True is name_str is a string of valid length
    """
    if not isinstance(name_str, str):
        return False
    if len(name_str) < 3 or len(name_str) > 25:
        return False
    return True

def is_valid_spicy_level(spicy_level_str, spicy_scale_map):
    """
    param: spicy_level_str (str): A value that is supposed to correspond to a key in the spicy_scale_map
    param: spicy_scale_map (dict): A dictionary associating increasing values with a level of spice for a particular dish
    The function first validates that spicy_level_str is indeed a string object. Then it uses its helper function is_num
    to ensure that spicy_level_str is a number represented as a string.
    returns: False is spicy_level_str is either not a string or not a number represented as a string
    True if spicy_level_str converted to an integer is a key in spicy_scale_map
    """
    if not isinstance(spicy_level_str, str):
        return False
    if not is_num(spicy_level_str):
        return False
    spicy_level = int(float(spicy_level_str))
    return spicy_level in spicy_scale_map.keys()

def is_valid_is_vegetarian(vegetarian_str):
    """
    Determines if a string value represents a valid value for a vegetarian dish.
    :param vegetarian_str (str): A string representing the value to be checked. Expected values are 'yes' or 'no'.
    :return: A boolean indicating if the value is valid.
    """
    if not isinstance(vegetarian_str, str):
        return False
    return vegetarian_str.lower() in ['yes', 'no']

def is_valid_price(price_str):
    """
    param price_str (str): A string that the function must validate as a potential price
    The function first checks that price_str is indeed a string object. Next, it uses its helper function is_num
    to validate that price_str is a number represented as an string object
    returns: False if price_str is either not a string or a number
    True, if otherwise
    """
    if not isinstance(price_str, str):
        return False
    return is_num(price_str)

def is_valid_calories(calories_str):
    """
    param: calories_str (str): A value that the function must validate as a potential number of calories for a dish
    The function first validates that calories_str is a string object. Then it checks if calories_str is a digit
    returns: False if calories_str is not a string or a digit
    True, if calories_str isa string and a digit
    """
    if not isinstance(calories_str, str):
        return False
    return calories_str.isdigit()

def get_new_menu_dish(dish_list, spicy_scale_map):
    """
    
    This function takes a list of dish details and a spicy scale map as input and returns a dictionary containing the dish details
    if all the values in the input list pass validation. If a value fails validation, a tuple with the field name and value that failed
    is returned.
    param dish_list (list): A list of strings containing the following dish details: name, calories, price, is_vegetarian, and spicy level.
    param spicy_scale_map (dict): A dictionary containing the mapping between the integer spiciness value (key) to its representation
    return: If any value in the input list fails validation, returns a tuple with the name of the field and the value that failed.
    Otherwise, returns a dictionary containing the dish details with keys "name", "calories", "price", "is_vegetarian", and "spicy_level".

    """
    if not isinstance(dish_list, list) or len(dish_list) != 5:
        return len(dish_list)
    name, calories_str, price_str, vegetarian_str, spicy_level_str = dish_list
    if not is_valid_name(name):
        return ("name", dish_list[0])
    if not is_valid_calories(calories_str):
        return ("calories", dish_list[1])
    if not is_valid_price(price_str):
        return ("price", dish_list[2])
    if not is_valid_is_vegetarian(vegetarian_str):
        return ("is_vegetarian", 'True')
    if not is_valid_spicy_level(spicy_level_str, spicy_scale_map):
        return ("spicy_level", dish_list[4])
    spicy_level = int(float(spicy_level_str))
    return {"name": name, "calories": int(calories_str), "price": float(price_str), "is_vegetarian": dish_list[3], "spicy_level": int(dish_list[4])}


def print_dish(dish, spicy_scale_map, name_only=False):
    """
    param: dish (dict) - a dictionary object that is expected to contain the following keys:
            - "name": dish's name
            - "calories": calories for this dish
            - "price": price of this dish
            - "is_vegetarian": boolean whether this dish is for vegetarian
            - "spicy_level": integer that represents the level of spiciness
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
            values for each corresponding key are string description of the
            level of spiciness
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the dish is printed.
            Otherwise, displays the formatted restaurant menues.
    returns: None; only prints the restaurant menu item
    """
    dishname = dish['name']
    print(dishname.upper())
    if name_only == False:
        calories = dish['calories']
        price = dish['price']
        veggie = dish['is_vegetarian']
        spiceint = dish['spicy_level']
        spicestr = spicy_scale_map[spiceint]
        print(f'* Calories: {calories}')
        print(f'* Price: {price:.1f}')
        print(f'* Is it vegetarian: {veggie}')
        print(f'* Spicy level: {spicestr}')
        print()
        
    

def add_helper(restaurant_menu_list, spicy_scale_map):
    '''
    The function prompts the user to input the dish data, and then calls the get_new_menu_dish function to attempt to create a new dish for the menu. If the new dish is successfully created, it is appended to the restaurant_menu_list. If there are errors with the input data, warnings are printed to the console.
    The function continues to ask the user if they would like to add another dish until the user inputs anything other than 'y'
    param restaurant_menu_list (list): A list of dictionaries representing the restaurant menu
    param spicy_scale_map (dict): A dictionary mapping integer values to spicy levels
    returns None
    '''
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter each required field, separated by commas.")
        print("::: name of the dish, calories, price, is it vegetarian ( yes | no ), spicy_level ( 1-4 )")
        dish_data = input("> ")  
        dish_values = dish_data.split(",")
        result_dict = get_new_menu_dish(dish_values, spicy_scale_map)  
        if type(result_dict) == dict:
            restaurant_menu_list.append(result_dict)  
            print(f"Successfully added a new dish!")
            print_dish(result_dict, spicy_scale_map)
        elif type(result_dict) == int:
            print(f"WARNING: invalid number of fields!")
            print(f"You provided {result_dict}, instead of the expected 5.\n")
        else:
            print(f"WARNING: invalid dish field: {result_dict}\n")

        print("::: Would you like to add another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()



def delete_dish(in_list, idx, start_idx=0):
    """
    param: in_list - a list from which to remove a dish
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of a dish in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from in_list.
    On success, the function saves the dish from in_list
    and returns it after it is deleted from in_list.
    returns:
    If the input list is empty, return 0.
    If idx is not of type string, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.
    Helper functions:
    - is_valid_index()
    """
    if in_list == []:
        return 0
    if type(idx) != str:
        return None
    elif start_idx > int(float(idx)):
        return -1
    if is_valid_index(idx, in_list):
        idx_num = int(float(idx))-start_idx
        dish = in_list[idx_num]
        in_list.remove(in_list[idx_num])
        return dish
    else:
        return -1
    

def delete_helper(restaurant_menu_list, spicy_scale_map):
    """
    Prompts the user to delete a dish from the restaurant menu list. The user can choose to delete the entire menu or a 
    specific dish by entering the corresponding index number or name. The function returns the updated restaurant menu 
    list after the deletion.

    param restaurant_menu_list (list): A list of dictionaries representing the dishes in the restaurant menu.
    param spicy_scale_map (dict): A dictionary mapping spicy levels to their descriptions.
    return: The updated restaurant menu list after the deletion as a list

    """
    continue_action = 'y'
    while continue_action == 'y':
        if not restaurant_menu_list:
            print("WARNING: There is nothing to delete!")
            break
        print("Which dish would you like to delete?")
        print("Press A to delete the entire menu for this restaurant, M to cancel this operation")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1, vegetarian_only=False)
        user_option = input("> ")
        if user_option == "A" or user_option == "a":
            print(f"::: WARNING! Are you sure you want to delete the entire menu ?")
            print("::: Type Yes to continue the deletion.")
            user_option = input("> ")
            if user_option == 'Yes':
                restaurant_menu_list = []
                print(f"Deleted the entire menu.")
            else:
                print(f"You entered '{user_option}' instead of Yes.")
                print("Canceling the deletion of the entire menu.")
            break
        elif user_option == 'M' or user_option == 'm':
            break
        result = delete_dish(restaurant_menu_list, user_option, 1)
        if type(result) == dict:
            print("Success!")
            print(f"Deleted the dish |{result['name']}|")
        elif result == 0:  
            print("WARNING: There is nothing to delete.")
        elif result == -1:  
            print(f"WARNING: |{user_option}| is an invalid dish number!")

        print("::: Would you like to delete another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
    return restaurant_menu_list

def save_menu_to_csv(restaurant_menu_list, filename):
    """
    param: restaurant_menu_list(list of dict) - A list of dictionaries representing the restaurant menu
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the menu items. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every dishes dictionary in the dictionaries list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:
    * name
    * calories
    * price
    * is_vegetarian
    * spicy_level
    
    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os

    if filename[-4:] != '.csv':
        return -1
    else:
        with open(filename, 'w', newline='') as csvfile:
            menu_writer = csv.writer(csvfile)
            for dish in restaurant_menu_list:
                string_list = [dish['name'], dish['calories'], dish['price'], dish['is_vegetarian'],
                    dish['spicy_level']]
                menu_writer.writerow(string_list)

def save_helper(restaurant_menu_list):
    '''
param: restaurant_menu_list(list of dict) - A list of dictionaries representing the restaurant menu
The function prompts the user for a filename, then uses this filename as a parameter for the save_menu_to_csv function to write restaurant_menu_list
into the provided csv filename by the user. If the helper function results in -1, the user is provided with a warning and is asked to try again.
Otherwise, it prints to the user that the restaurant menu was successfully written into the provided file. The loop continues until the user responds
to the prompt with anything except for 'y'
Returns: None
'''
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)  
        if result == -1:  
            print(f"WARNING: |{filename}| is an invalid file name!")  
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break

def load_menu_from_csv(filename, in_list, spicy_scale_map):
    """
    param: filename (str) - the name of the file from which to read the contents.
    param: in_list (list) - A list of dish dictionary objects to which
            the dishes read from the provided filename are appended.
            If in_list is not empty, the existing menu items are not deleted.
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the spicy value "Not Spicy" or "Low")
            Needed by the helper function (see below).
            
    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` (for csv.reader()) and `import os`
    (for `os.path.exists()).

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode.
    For each row in the csv file, the function will count each row (1-based counting) and
    proceed to create a new restaurant menu item using the `get_new_menu_dish()` function.
    - If the function `get_new_menu_dish()` returns a valid dish object (dictionary),
    it gets appended to the end of the `in_list`.
    - If the `get_new_menu_dish()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid dish data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices are appended to the new list that's returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read into the `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_menu_dish().

    Helper functions:
    - get_new_menu_dish()
    """
    import csv
    import os
    
    if filename[-4:]!='.csv':
        return -1
    elif os.path.exists(filename)==False:
        return None
    elif os.path.exists(filename):
        newlist = []
        with open(filename, 'r') as f:
            dishes_reader = csv.reader(f, delimiter=',')
            count=1
            for row in dishes_reader:
                newitem = get_new_menu_dish(row, spicy_scale_map)
                if type(newitem)==dict:
                    newdict = {'name':row[0], 'calories':int(row[1]), 'price':float(row[2]),'is_vegetarian':row[3], 'spicy_level':int(row[4])}
                    in_list.append(newdict)
                    count=count+1
                    
                else:
                    newlist.append(count)
                    count = count+1
                    
            return newlist

def load_helper(restaurant_menu_list):
    '''
param: restaurant_menu_list (list) - a menu that contains a list of dishes
The function takes a filename as a string input and then uses the
load_menu_from_csv function to return the result as a list. If the helper function returns -1,
a warning is provided to the user. Otherwise, a success prompt is shown. The loop continues
until the user responds with anything but 'y'
returns: none
'''
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = load_menu_from_csv(restaurant_menu_list, filename)  
        if result == -1:  
            print(f"WARNING: |{filename}| is an invalid file name!") 
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break

def update_helper(restaurant_menu_list, spicy_scale_map):
    '''
While the user is being prompted for input and the menu list is being displayed, the function iterates over a while loop. The number
relating to the dish the user wants to update must be entered.
The user is then asked to choose the field they want to update and input a new value for that field by the function.
The function uses update_menu_dish to update the information for the dish and then displays the fields of the updated dish. The function shows an error message if the user inputs incorrect data.
param: restaurant_menu_list (list): a list of dictionaries representing the restaurant's menu
param: spicy_scale_map (dict): a dictionary mapping integers to strings representing the spiciness level of the dishes

Returns:restaurant_menu_list (list): the updated list of dictionaries representing the restaurant's menu
'''
    continue_action = 'y'
    while continue_action == 'y':
        if restaurant_menu_list == []: 
            print("WARNING: There is nothing to update!")
            break
        print("::: Which dish would you like to update?")
        print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1, vegetarian_only=False)
        print("::: Enter the number corresponding to the dish.")
        user_option = input("> ")
        if user_option>0 and user_option<=len(restaurant_menu_list) : 
            dish_idx = int(user_option) - 1
            subopt = get_selection("update", restaurant_menu_list[dish_idx], to_upper=False, go_back=True)
            if subopt == 'M' or subopt == 'm': 
                break
            print(f"::: Enter a new value for the field |{subopt}|") 
            field_info = input("> ")
            result = update_menu_dish(restaurant_menu_list, dish_idx, spicy_scale_map, subopt, field_info) 
            if type(result) == dict:
                print(f"Successfully updated the field |{subopt}|:") 
                print_dish(result, spicy_scale_map, name_only=False)  
            else:  
                print(f"WARNING: invalid information for the field |{subopt}|!") 
                print(f"The menu was not updated.")
        else:  
            print(f"WARNING: |{user_option}| is an invalid dish number!") 

        print("::: Would you like to update another menu dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()

def update_menu_dish(restaurant_menu_list, idx, spicy_scale_map, field_key, field_info, start_idx=0):
    """
    param: restaurant_menu_list (list) - a menu that contains
            a list of dishes
    param: idx (str) - a string that is expected to contain an integer
            index of a restaurant in the input list
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer spiciness value (key) to its representation
            (e.g., key 1 might map to the priority value "non spicy")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.
    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.
    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
     Depending on the field_key, it also calls:
-    - is_valid_name()
-    - is_valid_calories()
-    - is_valid_price()
-    - is_valid_is_vegetarian()
-    - is_valid_spicy_level()
    """
    idxnum = int(idx) - start_idx
    if restaurant_menu_list == []:
        return 0
    
    if not is_valid_index(idx, restaurant_menu_list, start_idx):
        return -1

    if field_key not in restaurant_menu_list[0].keys():
        return -2
    
    elif is_valid_index(idx, restaurant_menu_list, start_idx):
        item = restaurant_menu_list[idxnum]
        if field_key == 'name' and is_valid_name(field_info):
            item[field_key] = field_info
            return restaurant_menu_list[idxnum]
        
        elif field_key == 'price' and is_valid_price(field_info):
            item[field_key] = float(field_info)
            return restaurant_menu_list[idxnum]

        elif field_key == 'calories' and is_valid_calories(field_info):
            item[field_key] = int(field_info)
            return restaurant_menu_list[idxnum]

        elif field_key == 'is_vegetarian' and is_valid_is_vegetarian(field_info):
            item[field_key] = field_info
            return restaurant_menu_list[idxnum]

        elif field_key == 'spicy_level' and is_valid_spicy_level(field_info, spicy_scale_map):
            item[field_key] = int(field_info)
            return restaurant_menu_list[idxnum]
        
        else:
            return field_key

    else:
        return field_key
    
def is_valid_index(idx, in_list, start_idx=0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """
    

    
    index_num = int(float(idx))
    index_num = index_num-start_idx
    index_num_c = index_num+1
    if len(in_list)<index_num_c:
        return False
    elif not is_num(idx) or index_num<0:
        return False
    elif idx =='1.5':
        return False
    elif is_num(idx) and (in_list[index_num] in in_list):
        return True
    else:
        return False
        


def get_restaurant_expense_rating(restaurant_menu_list):
    """
    param: restaurant_menu_list - a list of restaurants and their dishes (list of dicts)
    
    Computes the average price of all the items on the menu and display the expense rating of the restaurant.
    average_price < 10 -> Expense rating is : $
    10 <= average_price < 20 -> Expense rating is : $$
    average_price >= 20: Expense rating is : $$$
    
    returns: the average price of the items as a float
    """
    totalprice = 0
    for item in restaurant_menu_list:
        totalprice += item['price']

    avgprice = float(totalprice)/len(restaurant_menu_list)

    if avgprice <10:
        print('Expense rating is : $')
        print()
    elif avgprice >= 10 and avgprice <20:
        print('Expense rating is : $$')
        print()
    else:
        print('Expense rating is : $$$')
        print()
    return avgprice




        
        
    
    

