import sys

from data.config import REMOVE

sys.path.append('data')

from config import (
  ADDCAR,
  CHOOSEOPTION,
  ENTERCAR,
  GOODBYE,
  INVALIDINPUT,
  ISAUTHORIZED,
  MAINMENU,
  NOTAUTHORIZED,
  openDB,
  REMOVE,
  searchDB,
)

carIndexVal = 0
menuOption = 0
newCar = ""
searchFor = ""
yesOrNo = ""

def print_vehicle_list():
  with open(openDB(), 'r') as carDB:
    print("\n" + carDB.read())
    
def search_vehicles():
  searchFor = input(ENTERCAR).strip()
  if searchDB(searchFor):
    print("\n" + f"{searchFor}{ISAUTHORIZED}")
  else:
    print("\n" + f"{searchFor}{NOTAUTHORIZED}")
    
def add_vehicle():
  newCar = input(ADDCAR)
  with open(openDB(), 'a') as carDB:
    carDB.write(newCar + '\n')
  print(f"\nYou have added '{newCar}' as an authorized vehicle")
  
def delete_vehicle():
  searchFor = input(REMOVE).strip().lower()
  if searchDB(searchFor):
    with open(openDB(), 'r') as carDB:
      carIndexVal = [line.strip() for line in carDB]
    yesOrNo = input(
      '\nAre you sure you want to remove "' + searchFor +
      '" from the authorized vehicles list? '
      ).strip().lower()
    if yesOrNo == "yes":
      carIndexVal.remove(
        next(
          vehicle for vehicle in carIndexVal
          if vehicle.lower() == searchFor
        )
      )
      print(f'\nYou have REMOVED "{searchFor}" as an authorized vehicle')
      with open(openDB(), 'w') as carDB:
        for vehicle in carIndexVal:
          carDB.write(vehicle + '\n')
    elif yesOrNo == "no":
      print("\nAction cancelled.")
    else:
      print("\nInvalid input. Returning to main menu...")
  else:
    print("\nVehicle not found. Returning to Main Menu")

while True:
  print(MAINMENU)
  try:
    menuOption = int(input(f"{CHOOSEOPTION}"))
  except Exception:
    print(INVALIDINPUT)
    continue
    
  if menuOption == 1:
    print_vehicle_list()

  elif menuOption == 2:
    search_vehicles()

  elif menuOption == 3:
    add_vehicle()

  elif menuOption == 4:
    delete_vehicle()

  elif menuOption == 5:
   print(GOODBYE)
   break
  
  else:
    print(INVALIDINPUT)
