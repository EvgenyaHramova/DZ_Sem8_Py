

coffee_beans = int(input('Количество порций кофейных зерен: '))
milk = int(input('Количество порций молока: '))
cream = int(input('Количество порций сливок: '))
ingredients = [coffee_beans, milk, cream]
print(ingredients)  # [1, 2, 3]


coffee_recipe = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0], 'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2], 'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}

preference = input(
    'Какие рецепты кофе предпочитаете? Назовите в порядке убывания предпочтений:  ').split(', ')
print(preference)  # ['Кон Пана', 'Капучинно', 'Эспрессо']


for i in preference:
    for key in coffee_recipe:
        if key == i:
            x = coffee_recipe.get(key)
            if x <= ingredients:
                ing = []
                for k in range(0, len(ingredients)):
                    ing.append(ingredients[k] - x[k])
                    k += 1
                ingredients = ing
                print(ingredients)
                print(i)    

print('Извините, нет достаточного количества ингредиентов для приготовления', i)





# for key in coffee_recipe:
#     if key == preference:
#         x = coffee_recipe.get(preference)
#         print(x)
#         if x > ingredients:
#             print("Извините, достаточного количества ингредиентов для приготовления данного рецепта нет.")
#         else:
#             print('Пожалуйста, ваш кофе!')
    

         

# ingredients = [2,4,3]
# def choose_coffee (*args):
#   for coffee in args:
#     if coffee == 'Эспрессо' and ingredients[0] >= 1:
#       ingredients[0] -= 1
#       return 'Эспрессо'
#     elif coffee == 'Капучино' and ingredients[0] >= 1 and ingredients[1] >= 3:
#       ingredients[0] -= 1
#       ingredients[1] -= 3
#       return 'Капучино'
#     elif coffee == 'Маккиато' and ingredients[0] >= 2 and ingredients[1] >= 1:
#       ingredients[0] -= 2
#       ingredients[1] -= 1
#       return 'Маккиато'
#     elif coffee == 'Кофе по-венски' and ingredients[0] >= 1 and ingredients[2] >= 2:
#       ingredients[0] -= 1
#       ingredients[2] -= 2
#       return 'Кофе по-венски'
#     elif coffee == 'Латте Маккиато' and ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
#       ingredients[0] -= 1
#       ingredients[1] -= 2
#       ingredients[2] -= 1
#       return 'Латте Маккиато'
#     elif coffee == 'Кон Панна' and ingredients[0] >= 1 and ingredients[2] >= 1:
#       ingredients[0] -= 1
#       ingredients[2] -= 1
#       return 'Кон Панна'
#   return 'К сожалению, не можем предложить Вам напиток'

# print(choose_coffee('Кон Панна', 'Эспрессо'))
# print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))
# print(choose_coffee('Капучино', 'Маккиато', 'Эспрессо'))




# ingredient = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
#               'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
#               'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}
 
 
# def choose_coffee(preferences):
#     for i in preferences:
#         if ingredient[i][0] <= ingredients[0] and ingredient[i][1] <= ingredients[1] and ingredient[i][2] <= ingredients[2]:
#             ingredients[0] -= ingredient[i][0]
#             ingredients[1] -= ingredient[i][1]
#             ingredients[2] -= ingredient[i][2]
#             return i
#     return 'К сожалению, не можем предложить Вам напиток'
 
 
# ingredients = [10, 10, 10]
# print(choose_coffee('Кон Панна, Эспрессо, Капучино, Маккиато, Кофе по-венски, Латте Маккиато '.split(', ')))
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
# print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))

