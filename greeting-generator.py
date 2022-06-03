from datetime import date


#current_year = date.today().year

#birthyear = int(input("Geburtsjahr:  "))
#name = str(input("Name: "))
#gender = str(input("Herr oder Frau ? : "))
#print("Hallo " + gender + " " + name + " du bist " + str(current_year - birthyear) + " Jahre alt.")

print("---Willkommen zum Geburtstag Generator---")
name = input("Name der Person eingeben: ")
age = input("Alter der zu grüßenden Person eingeben: ")
sender = input("Eignen Namen eingeben: ")

print("Hallo " + name + ",")
print("Ich wünche dir alles Gute zum " + age + "ten Geburtstag.")
print("Ich hoffe das du einen schönen Tag hast und mit deinen liebsten feierst.")
print("Zudem wunche ich die alles nur erdenklich Gute für das neue Lebensjahr und viel Gesundheit!")
print("Liebe Grüße")
print(sender)
