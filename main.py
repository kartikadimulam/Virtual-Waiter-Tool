from functions import *

if __name__ == "__main__":

  the_menu = { "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "H" : "Display restaurant expense rating",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"}

spicy_scale_map = {
        1: "Not spicy",
        2: "Low-key spicy",
        3: "Hot",
        4: "Diabolical",
}

restaurant_menu_list = [
  {
    "name": "burrito",
    "calories": 500,
    "price": 12.90,
    "is_vegetarian": "yes",
    "spicy_level": 2
  },
  {
    "name": "rice bowl",
    "calories": 400,
    "price": 14.90,
    "is_vegetarian": "no",
    "spicy_level": 3
  },
  {
    "name": "margherita",
    "calories": 800,
    "price": 18.90,
    "is_vegetarian": "no",
    "spicy_level": 2
  }
]

list_menu = {
        "A": "complete menu",
        "V": "vegetarian dishes only",
    }

opt = None

while True:
      print_main_menu(the_menu) 
      print("::: Enter an option")
      opt = input("> ")

      if opt.upper() == 'Q' :
          print("Goodbye!\n")
          break 
        
      elif opt.upper() == 'L':
        list_helper(list_menu, restaurant_menu_list, spicy_scale_map)

      elif opt.upper() == 'A':
        add_helper(restaurant_menu_list, spicy_scale_map)

      elif opt.upper() == 'D':
        restaurant_menu_list = delete_helper(restaurant_menu_list, spicy_scale_map)

      elif opt.upper() == 'S':
        save_helper(restaurant_menu_list)
        
      elif opt.upper() == 'R':
        load_helper(restaurant_menu_list, spicy_scale_map)

      elif opt.upper() == 'U':
        update_helper(restaurant_menu_list, spicy_scale_map)

      elif opt.upper()=='H':
        get_restaurant_expense_rating(restaurant_menu_list)
        
        
        
      else:
          if opt in the_menu: 
              print(f"You selected option {opt} to > {the_menu[opt]}.")
          else:
              print(f"WARNING: {opt} is an invalid option.\n")

      print("Have a delicious day!")



 
