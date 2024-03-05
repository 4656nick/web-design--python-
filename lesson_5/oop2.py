class Human:
    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.happiness = 100

    def eat(self, food_amount):
        if self.hunger >= food_amount:
            self.hunger -= food_amount
            return True
        return False

    def play(self):
        self.hunger -= 10
        self.happiness += 20

    def work(self):
        self.hunger -= 10
        return 150

    def pet_cat(self, cat):
        self.happiness += 5
        cat.happiness += 5


class Wife(Human):
    def __init__(self, name):
        super().__init__(name)

    def buy_food(self, money, food_amount):
        if money >= food_amount * 10:
            money -= food_amount * 10
            return money, food_amount
        return money, 0

    def buy_shoes(self, money):
        if money >= 350:
            money -= 350
            return money, True
        return money, False

    def clean_house(self, dirtiness):
        cleaned_dirt = min(dirtiness, 100)
        dirtiness -= cleaned_dirt
        return dirtiness


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.happiness = 100

    def eat(self, food_amount):
        if self.hunger >= food_amount:
            self.hunger -= food_amount
            return True
        return False

    def sleep(self):
        self.hunger -= 10
        self.happiness += 10

    def scratch_wallpaper(self, dirtiness):
        dirtiness += 5
        return dirtiness


class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirtiness = 0
        self.shub_count = 0


house = House()
husband = Human('Артем')
wife = Wife('Анна')
cat = Cat('Васька')

for day in range(365):
    print('================== День {} =================='.format(day))
    house.money += husband.work()
    house.money, food_bought = wife.buy_food(house.money, house.food)
    house.food += food_bought
    house.dirtiness = wife.clean_house(house.dirtiness)

    if house.dirtiness > 90:
        husband.happiness -= 10
        wife.happiness -= 10

    if husband.eat(30) and wife.eat(30) and cat.eat(10):
        husband.play()
        bought_shoes = wife.buy_shoes(house.money)
        if bought_shoes:
            house.shub_count += 1
        cat.sleep()
        husband.pet_cat(cat)
    print(house.money)
    print(house.food)
    print(house.shub_count)

print('Деньги в тумбочке:', house.money)
print('Съедено еды:', house.food)
print('Куплено шуб:', house.shub_count)