def say_hello(frist_name, last_name):
    print("Hello " + frist_name + " " + last_name)
    print("Willkommen zurück")

kd_nummer = int(input("Kundennummer Eingeben: "))

if (kd_nummer > 0) and (kd_nummer <= 10):
    say_hello("Hussein", "Hussein")

elif (kd_nummer > 10) and (kd_nummer < 20) :
    say_hello("khadija", "Salameh")

else: print("Wrong User!")


