from functions import *

#get_selection
action = 'select'
suboptions = {'1': 'Option 1', '2': 'Option 2', '3': 'Option 3'}
go_back = True

assert get_selection(action, suboptions, go_back=go_back) == None
action = 'select'
suboptions = {'A': 'Option A', 'B': 'Option B', 'C': 'Option C'}
to_upper = True

assert get_selection(action, suboptions, to_upper=to_upper) == 'A'
assert get_selection(action, suboptions, to_upper=to_upper) == 'a'
assert get_selection(action, suboptions, go_back=go_back) == 'M'



#is_valid_name
assert is_valid_name("a") == False
assert is_valid_name("bo") == False
assert is_valid_name(42) == False
assert is_valid_name(["soup"]) == False
assert is_valid_name("soup") == True

#is_num
assert is_num("3.14159")
assert not is_num("hello world")
assert not is_num(None)

#is_valid_spicy_level
spicy_scale_map = {1: "Mild", 2: "Medium", 3: "Spicy", 4: "Extra Spicy"}
assert is_valid_spicy_level("2", spicy_scale_map)
spicy_scale_map = {1: "Mild", 2: "Medium", 3: "Spicy", 4: "Extra Spicy"}
assert not is_valid_spicy_level("5", spicy_scale_map)
spicy_scale_map = {1: "Mild", 2: "Medium", 3: "Spicy", 4: "Extra Spicy"}
assert not is_valid_spicy_level(None, spicy_scale_map)

#is_valid_is_vegetarian
assert is_valid_is_vegetarian('yes') == True
assert is_valid_is_vegetarian('NO') == True
assert is_valid_is_vegetarian(123) == False

#is_valid_price
assert is_valid_price('10.99') == True
assert is_valid_price(10.99) == False
assert is_valid_price('10.9.9') == False

#is_valid_calories
assert is_valid_calories('500') == True
assert is_valid_calories(500) == False
assert is_valid_calories('500a') == False

#get_new_menu_dish
assert type(get_new_menu_dish(['Pasta', '800', '15.99', 'yes', '4'], {
        1: "Not spicy",
        2: "Low-key spicy",
        3: "Hot",
        4: "Diabolical",
})) == dict
assert get_new_menu_dish(['', '800', '15.99', 'yes', '4'], {
        1: "Not spicy",
        2: "Low-key spicy",
        3: "Hot",
        4: "Diabolical",
}) == ('name', '')
assert get_new_menu_dish(['Pasta', '800', '15.a9', 'yes', '4'], {
        1: "Not spicy",
        2: "Low-key spicy",
        3: "Hot",
        4: "Diabolical",
}) == ('price', '15.a9')

#is_valid_index
assert is_valid_index('2', ['apple', 'banana', 'orange'], 0) == True
assert is_valid_index('-1', ['apple', 'banana', 'orange'], 0) == False
assert is_valid_index('not_a_number', ['apple', 'banana', 'orange'], 0) == False

#delete_dish
assert delete_dish(['apple', 'banana', 'orange'], '1', 0) == 'banana'
assert delete_dish([], '1', 0) == 0
assert delete_dish(['apple', 'banana', 'orange'], 1, 0) == None


#save_menu_to_csv

menu_list = [{'name': 'spaghetti', 'calories': 500, 'price': 12.99, 'is_vegetarian': False, 'spicy_level': 1}]
filename = 'menu.csv'
assert save_menu_to_csv(menu_list, 'menu.txt') == -1
assert save_menu_to_csv(menu_list, filename) == None


# load_menu_from_csv
in_list = []
spicy_scale_map = {1: 'Not Spicy', 2: 'Low', 3: 'Medium', 4: 'High', 5: 'Very High'}
filename = 'menu.csv'
assert load_menu_from_csv('menu.txt', in_list, spicy_scale_map) == -1
assert load_menu_from_csv('nonexistent.csv', in_list, spicy_scale_map) == None
assert load_menu_from_csv(filename, in_list, spicy_scale_map) == []

#delete_helper
assert delete_helper([], {}) == []
menu = [{"name": "Spaghetti Carbonara", "price": 15.99, "spicy": 1, "vegetarian": False}]
assert delete_helper(menu, {1: "Mild", 2: "Medium", 3: "Hot"}) == []
menu = [
    {"name": "Margherita Pizza", "price": 12.99, "spicy": 1, "vegetarian": True},
    {"name": "Spaghetti Carbonara", "price": 15.99, "spicy": 1, "vegetarian": False},
    {"name": "Chicken Alfredo", "price": 16.99, "spicy": 1, "vegetarian": False}
]
expected = [
    {"name": "Margherita Pizza", "price": 12.99, "spicy": 1, "vegetarian": True},
    {"name": "Chicken Alfredo", "price": 16.99, "spicy": 1, "vegetarian": False}
]
assert delete_helper(menu, {1: "Mild", 2: "Medium", 3: "Hot"}) == expected


#update_menu_dish
menu_list = [{'name': 'spaghetti', 'calories': 500, 'price': 12.99, 'is_vegetarian': False, 'spicy_level': 1}]
idx = '0'
spicy_scale_map = {1: 'Not Spicy', 2: 'Low', 3: 'Medium', 4: 'High', 5: 'Very High'}
field_key = 'price'
field_info = '15.99'
start_idx = 0
assert update_menu_dish(menu_list, idx, spicy_scale_map, field_key, field_info, start_idx) == None
menu = [{'name': 'pizza', 'price': 10.99, 'is_vegetarian': False}]
assert update_menu_dish(menu, 'abc', {}, 'name', 'cheese pizza') == -1
menu = [{'name': 'pizza', 'price': 10.99, 'is_vegetarian': False}]
assert update_menu_dish(menu, '0', {}, 'invalid_field', 'some value') == -2
menu = [{'name': 'pizza', 'price': 10.99, 'is_vegetarian': False}]
updated_item = update_menu_dish(menu, '0', {}, 'name', 'cheese pizza')
assert updated_item == {'name': 'cheese pizza', 'price': 10.99, 'is_vegetarian': False}
assert menu_list[0]['price'] == 15.99

#update_helper
assert update_helper(42, {}) == TypeError
assert update_helper([], "spicy_scale_map") == TypeError
assert type(update_helper([{'name': 'pizza', 'price': 10}], {1: 'mild', 2: 'medium', 3: 'hot'})) == list

#get_restaurant_expense_rating
restaurant_menu_list = [{'name': 'burger', 'price': 8}, {'name': 'pizza', 'price': 12}, {'name': 'salad', 'price': 7}]
assert get_restaurant_expense_rating(restaurant_menu_list) == 9.0
restaurant_menu_list = [{'name': 'burger', 'price': 25}, {'name': 'pizza', 'price': 30}, {'name': 'salad', 'price': 20}]
assert get_restaurant_expense_rating(restaurant_menu_list) == 25.0
restaurant_menu_list = [{'name': 'burger', 'price': 0}, {'name': 'pizza', 'price': 10}, {'name': 'salad', 'price': 20}]
assert get_restaurant_expense_rating(restaurant_menu_list) == 10.0







