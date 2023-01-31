coffee_recipe = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0], 'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2], 'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}
# coffee_beans = int(input('Количество порций кофейных зерен: '))
# milk = int(input('Количество порций молока: '))
# cream = int(input('Количество порций сливок: '))
# ingredients = [coffee_beans, milk, cream]
# print(ingredients)  # [2, 2, 3]

# preference = input('Какие рецепты кофе предпочитаете? Назовите в порядке убывания предпочтений:  ').split(',')
# for i in preference:
#     for key in coffee_recipe:
#         if key == i:
#             x = coffee_recipe.get(key)
#             ing = []
#             if x[0] <= ingredients[0] and x[1] <= ingredients[1] and x[2] <= ingredients[2]:
#                 print(i)
                
#                 for k in range(len(ingredients)):  
#                     ing.append(ingredients[k] - x[k])
                
#                 ingredients = ing
#                 #print(ingredients)
#             else:
#                 print('Извините, нет достаточного количества ингредиентов для приготовления', i)



def choose_coffee(preference):
    for i in preference:
        for key in coffee_recipe:
            if key == i:
                x = coffee_recipe.get(key)
                ing = []
                if x[0] <= ingredients[0] and x[1] <= ingredients[1] and x[2] <= ingredients[2]:
                    print(i)
                
                    for k in range(len(ingredients)):  
                        ing.append(ingredients[k] - x[k])
                
                    ingredients = ing
                    #print(ingredients)
                else:
                    print('Извините, нет достаточного количества ингредиентов для приготовления', i)
                

coffee_beans = int(input('Количество порций кофейных зерен: '))
milk = int(input('Количество порций молока: '))
cream = int(input('Количество порций сливок: '))
ingredients = [coffee_beans, milk, cream]
print(ingredients)  # [2, 2, 3]

preference = input('Какие рецепты кофе предпочитаете? Назовите в порядке убывания предпочтений:  ').split(',')

choose_coffee(preference)   # [Латте Маккиато, Маккиато, Капучино]
