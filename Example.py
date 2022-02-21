# SYSEN5160 Homework #2 
# Source Code: https://github.com/PhilipGriffith/AHPy/blob/master/ahpy/ahpy.py
import itertools

from AHPy import ahpy

# Example from https://en.wikipedia.org/wiki/Analytic_hierarchy_process_%E2%80%93_car_example
def m(elements, judgments):
   return dict(zip(elements, judgments))

cri = ('Calories', 'Proteins', 'Carbs', 'Fats')
c_cri = list(itertools.combinations(cri, 2))
criteria = ahpy.Compare('Criteria', m(c_cri, (1, 5, 5, 9, 7, 1 / 5)), 3)

alt = ('Large Egg', 'Large Banana', '2oz Lentil Pasta', '5oz Greek Yogurt', '3oz Chicken', '2oz Mixed Nuts')
pairs = list(itertools.combinations(alt, 2))

calories_m = (9, 9, 1, 0.5, 5, 1, 1 / 9, 1 / 9, 1 / 7, 1 / 9, 1 / 9, 1 / 7, 1 / 2, 5, 6)
calories = ahpy.Compare('Calories', m(pairs, calories_m), 3)

proteins_m = (1, 5, 7, 9, 1 / 3, 5, 7, 9, 1 / 3, 2, 9, 1 / 8, 2, 1 / 8, 1 / 9)
proteins = ahpy.Compare('Proteins', m(pairs, proteins_m), 3)

carbs_m = (1, 7, 5, 9, 6, 7, 5, 9, 6, 1 / 6, 3, 1 / 3, 7, 5, 1 / 5)
carbs = ahpy.Compare('Carbs', m(pairs, carbs_m), 3)

fats_m = (1, 7, 5, 9, 6, 7, 5, 9, 6, 1 / 6, 3, 1 / 3, 7, 5, 1 / 5)
fats = ahpy.Compare('Fats', m(pairs, fats_m), 3)

criteria.add_children([calories, proteins, carbs, fats])

compose = ahpy.Compose()
compose.add_comparisons('Criteria', m(c_cri, (1, 5, 5, 9, 7, 1 / 5)), 3)
h = {'Criteria': ['Calories', 'Proteins', 'Carbs', 'Fats']}
compose.add_hierarchy(h)
