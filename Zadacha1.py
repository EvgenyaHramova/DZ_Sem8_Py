
coffee_beans = int(input('Количество порций кофейных зерен: '))
milk = int(input('Количество порций молока: '))
cream = int(input('Количество порций сливок: '))
ingredients = [coffee_beans, milk, cream]
print(ingredients)  # [2, 2, 3]

coffee_recipe = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0], 'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2], 'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}

preference = input('Какие рецепты кофе предпочитаете? Назовите в порядке убывания предпочтений:  ').split(', ')
print(preference)   # [Латте Маккиато, Маккиато, Капучино]
                    #    

for i in preference:
    for key in coffee_recipe:
        if key == i:
            x = coffee_recipe.get(key)
            if ingredients < x:
                print('Извините, нет достаточного количества ингредиентов для приготовления', key)
            if ingredients >= x:    
                ing = []
                for k in range(0, len(ingredients)):
                
                    if ingredients[k] < x[k]:
                        ing.append(ingredients[k])
                        k += 1
                    else:
                        ing.append(ingredients[k] - x[k])
                        k += 1
                ingredients = ing
            print(i)
            print(ingredients)
            
            

            
# print(choose_coffee)

# def choose_coffee(preference):
# for i in preference:
    # for key in coffee_recipe:
    #     if key == i:
    #         x = coffee_recipe.get(key)
    #         if ingredients < x:
    #             print('Извините, нет достаточного количества ингредиентов для приготовления', key)
    #         if ingredients >= x:    
    #             ing = []
    #             for k in range(0, len(ingredients)):
    #                 if ingredients[k] >= x[k]:
    #                     ing.append(ingredients[k] - x[k])
                    
    #                 else:
    #                     ing.append(ingredients[k])
    #                     k += 1
    #             print(i)
    #         ingredients = ing
    #         print(ingredients)

# def choose_coffee(preference):
#     for i in preference:
#         if coffee_recipe[i][0] <= ingredients[0] and coffee_recipe[i][1] <= ingredients[1] and coffee_recipe[i][2] <= ingredients[2]:
#             ingredients[0] -= coffee_recipe[i][0]
#             ingredients[1] -= coffee_recipe[i][1]
#             ingredients[2] -= coffee_recipe[i][2]
#             return i
#     return 'К сожалению, не можем предложить Вам напиток'