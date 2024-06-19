print("გამარჯობათ რაც გინდათ აირჩიეტ და კონსულტანტი დაგეხმარებათ")

price = int(input("რა ფასის ნითი გჭირდებათ:  "))
discount = input("რა ფასდაკლება გინდათ:  ")

final = ((int(price) * int(discount)) / 100 )

print (price - final)