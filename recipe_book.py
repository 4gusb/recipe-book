#program that assign a dish, according desired type of meal and difficulty
import time 
import json
import random

dict = json.load(open('data.json'))

def inputMeal():
    print("What meal are u craving for?")
    meal = input("B (breakfast) | L (lunch) | D (dinner): ").upper()
    while(meal!= 'B' and meal!='L' and meal!= 'D'):
        print("Input Error. Choose again:")
        meal = input("B (breakfast) | L (lunch) | D (dinner): ").upper()
    return meal
             
def inputLevel():
    level = 0
    while level<1 or level>5:   
        try:
            level = int(input("On a scale from 1 to 5, tell us how gourmet do you want the dish to be: "))
        except ValueError:
            print("ValueError. Please, choose wisely!")
            level = int(input("On a scale from 1 to 5, how gourmet do you want the dish to be?: "))
    return level


def choosing(m, d):
   list_of_keys = [key for key in dict if dict[key]['Meal']==m and dict[key]['Level']==str(d)]
   choose = random.choice(list(list_of_keys))
   print("Your choosen meal is: {}".format(choose))
   time.sleep(3)

   while True:
         condition = input("\nAre u happy with your meal? Y (yes) | N (if you want us to pick other): ").upper()
         if condition=="Y":
            while True:
                     condition = input("\nDo you want the full recipe? Y (yes) | N (no):").upper()
                     if condition=="Y":
                        print("\n")
                        print(dict[choose]['Directions'])
                        print("\n\nSee u!")
                        break
                     elif condition=="N":
                        print("\nGreat! See u!")
                        break
                     else:
                        print("Please, choose a valid option!")
            break
         elif condition=="N":
            choosing(m, d)
            break   
         else:
            print("Please, choose a valid option!")  

   

def main():
    print("\nWelcome, we are here to choose the perfect meal 4 u!")
    meal = inputMeal()
    difficulty = inputLevel()
    print(meal)
    print(difficulty)
    print("According to your wishes.....")
    time.sleep(3)
    choosing(meal, difficulty)
    


main()
