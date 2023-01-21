from collections import namedtuple
from collections import defaultdict
import functools

recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20, 'Укроп': 0}

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

def collect_statistics(statistics):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(arg1, arg2, **kwargs):
            result = func(arg1, arg2, **kwargs)
            if result[0] == 0:
                order_tuple = Order(result[0], int(arg2) - result[1])
            if result[0] == 1:
                order_tuple = Order(result[0], result[1])
            statistics[arg1].append(order_tuple)
            return result
        return wrapped
    return decorator

@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    portions = []
    if food not in recipes.keys():
        return 0, 0

    if food in recipes.keys():
        for recipe_key, recipe_value in recipes.items():
            if food in recipe_key:
                ingredients = recipes[recipe_key]
                for ingredient_key, ingredient_value in ingredients.items():
                    if ingredient_key in store.keys():
                        portions.append(store[ingredient_key] / ingredients[ingredient_key])
                    else:
                        return 0, 0
        if min(portions) - count >= 0:
            return 1, count
        else:
            return 0, int(min(portions))

print(check_portions('Бутерброд с ветчиной', 2))
print(check_portions('Бутерброд с ветчиной', 20))
print(check_portions('Салат Витаминный', 1))
print(statistics)
