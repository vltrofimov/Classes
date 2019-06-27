#Class defenition

class farm_member:
    weight = 0
    feed_status = "non-feeded"
    name = ''
    def to_feed(self):
        self.feed_status = 'feeded'

class animal(farm_member):
    pass

class bird(farm_member):
    egg_collection_status = 'eggs non-collected'
    def egg_collection(self):
        self.egg_collection_status='eggs collected'

class goose(bird):
    voice='ga-ga'

class cow(animal):
    milk_coolection_status ='milk non-collected'
    voice = 'mu-mu'
    def milk_collection(self):
        self.milk_coolection_status = 'milk collected'

class ship(animal):
    wool_collection_status = 'wool non-collected'
    def wool_collection(self):
        self.wool_collection_status= 'wool collected'
    voice = 'be-be'

class chicken(bird):
    voice = 'ko-ko'

class goat(animal):
    voice = 'me-me'
    milk_coolection_status = 'milk non-collected'
    def milk_collection(self):
        self.milk_coolection_status = 'milk collected'

class duck(bird):
    voice = 'krya-krya'

#Objects creation

goose_1 = goose()
goose_1.name = 'Серый'
goose_1.weight=5
goose_1.to_feed()
goose_1.egg_collection()

goose_2 = goose()
goose_2.name = 'Белый'
goose_2.weight=4
goose_2.to_feed()
goose_2.egg_collection()

cow_1 = cow()
cow_1.name = 'Манька'
cow_1.weight = 500
cow_1.to_feed()
cow_1.milk_collection()

ship_1 = ship()
ship_1.name = 'Барашек'
ship_1.weight = 50
ship_1.to_feed()
ship_1.wool_collection()

ship_2 = ship()
ship_2.name = 'Кудрявый'
ship_2.weight = 70
ship_2.to_feed()
ship_2.wool_collection()

chicken_1 = chicken()
chicken_1.name = 'Коко'
chicken_1.weight = 3
chicken_1.to_feed()
chicken_1.egg_collection()

chicken_2 = chicken()
chicken_2.name = 'Кукареку'
chicken_2.weight=2
chicken_2.to_feed()
chicken_2.egg_collection()

goat_1 = goat()
goat_1.name = 'Рога'
goat_1.weight = 35
goat_1.to_feed()
goat_1.milk_collection()

goat_2 = goat()
goat_2.name = 'Копыта'
goat_2.weight = 40
goat_2.to_feed()
goat_2.milk_collection()

duck_1 = duck()
duck_1.name = 'Кряква'
duck_1.weight = 6
duck_1.to_feed()
duck_1.egg_collection()


animals = [goose_1, goose_2, cow_1, ship_1, ship_2, chicken_1, chicken_2,goat_1,goat_2,duck_1]
weights = [a.weight for a in animals]
print('Общий вес животных = {} килограмм'.format(sum(weights)))

max_weight = max(weights)
for animal in animals:
    if animal.weight == max_weight:
        print('самое тяжелое животное',animal.name,'его вес = {} килограмм'.format(max_weight))