from pprint import pprint

with open('recipes.txt', 'r') as f:
    cook_book = {}
    for name_food in f:
        name_food = name_food.strip()
        count_ingridiets = f.readline().strip()
        cook_book[name_food] = []
        for i in range(1, (int(count_ingridiets) + 1)):
            dict_ing = {}
            i = f.readline().strip()
            i_list = i.split('|')
            dict_ing['ingridient_name'] = i_list[0]
            dict_ing['quantity'] = i_list[1]
            dict_ing['measure'] = i_list[2]
            cook_book[name_food].append(dict_ing)
        none_line = f.readline().strip()


def get_shop_list_by_dishes(dishes, person_count):
    count_food = {}

    for inp_food in dishes:
        ingridients = cook_book[inp_food]
        for ing_value in ingridients:
            ingridient_name = ing_value['ingridient_name']
            if ingridient_name not in count_food:
                count_ing = {}
                quantity = ing_value['quantity']
                measure = ing_value['measure']
                count_ing['quantity'] = int(quantity) * person_count
                count_ing['measure'] = measure
                count_food[ingridient_name] = count_ing
            else:
                count_food[ingridient_name] = {'measure': measure, 'quantity': int(quantity) * person_count}
    pprint(count_food)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)