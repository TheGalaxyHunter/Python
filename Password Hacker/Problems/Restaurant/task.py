import itertools

# main_courses, desserts and drinks are pre-defined list
# price_main_courses, price_desserts and price_drinks are pre-defined list

main_course = zip(main_courses, price_main_courses)
desert = zip(desserts, price_desserts)
drink = zip(drinks, price_drinks)
for mc, des, dri in itertools.product(main_course, desert, drink):
    price = mc[1] + des[1] + dri[1]
    if price > 30:
        continue
    print(mc[0], des[0], dri[0], price)

# another solution--->
# dishes = itertools.product(main_courses, desserts, drinks)
# prices = itertools.product(price_main_courses, price_desserts, price_drinks)
# for dish, price in zip(dishes, prices):
#     if sum(price) > 30:
#         continue
#     print(*dish, sum(price))
