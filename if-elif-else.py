user_code = int(input("Dein usercode eingeben: "))
name = str(input("Name Eingeben: "))


if (user_code > 0) and (user_code <= 5):
    print("Willkommen Herr " + name + " du gehörst zu Gruppe (A)")




elif ((user_code >= 6) and (user_code <= 10)) or ((user_code == 7) or (user_code == 8)):
    print("Willkommen Herr " + name + " du gehörst zu Gruppe (B)")
    print("Welcome back!")


elif (user_code >= 11) and (user_code <= 15):
    print("Willkommen Herr " + name + " du gehörst zu Gruppe (C)")


elif (user_code >= 16) and (user_code <= 20):
    print("Willkommen Herr " + name + " du gehörst zu Gruppe (D)")



else:
    print("User nicht gefunden")