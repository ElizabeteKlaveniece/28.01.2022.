text = input("Ievadiet tekstu!")
def deleteCombo(text): #deklarējam funkciju, arguments - text
  if text.count("abc")>0: #pārbaudām, vai ir kaut viena kombo "abc"
    text = text.replace("abc","") #aizvietojam "abc" ar ""
    print(text) #izvadām tekstu uz ekrāna
  else: #pretējā gadījumā
    text = "Meklējamā kombinācija netika atrasta!" #aizvietojam tekstu ar paziņojumu
    print(text) #izvadām tekstu uz ekrāna
  return text #atgriežam vērtību text
deleteCombo(text)