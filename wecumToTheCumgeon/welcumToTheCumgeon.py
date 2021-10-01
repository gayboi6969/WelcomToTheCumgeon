import time
import random
from random import randint
import json
with open('mapPrototype.json') as f:
    map_json = json.loads(f.read())

class roomPR():
    def __init__(self):
        self.PRvariable = 'cum'


def help():

    print('use move [direction] to move to a different room. use cont to continue the story if nothing is happening. use cum to cum, use map to check your map')

class Player:
    def __init__(self):
        self.health = 50
        self.damage = 10
        self.defense = 2
        self.havehpot = True

class CumGoblin:
    def __init__(self):
        self.health = 10
        self.damage = 5
        self.name = 'Cum Goblin'

class CumOrc:
    def __init__(self):
        self.health = 20
        self.damage = 10
        self.name = 'Cum Orc'

class CumOgre:
    def __init__(self):
        self.health = 50
        self.damage = 20
        self.name - 'THE MIGHTY CUM OGRE'

player = Player()
cumGoblin = CumGoblin()
cumOrc = CumOrc()

command = 'null'

def cumbat(cumGoblin):

    print('a wild', cumGoblin.name, 'approaches you! type help for cumbat commands')

    enemyStun = 0

    incumbat = True

    while incumbat:

        command = input()

        if command == 'fight':

            if enemyStun >= 0:

                cumGoblin.health = cumGoblin.health - player.damage

            elif enemyStun < 0:
                
                print('you hit the', cumGoblin.name, 'for', player.damage, 'damage')
                cumGoblin.health = cumGoblin.health - player.damage

                player.health = cumGoblin.damage - player.damage
                
            if cumGoblin.health <= 0:

                print('you beat them!')
                incumbat = False

        elif command == 'heal' and player.havehpot == True:

            player.health + 10
            havehpot = False

            player.health = player.health - (cumGoblin.damage - player.defense)
            print('you heal 10 health and the', cumGoblin.name, 'hits you for', cumGoblin.damage, 'damage')

            if player.health <= 0:

                print('you died')
                incumbat = False
        
        elif command == 'cum' and enemyStun == -1:

            willCum = random.int(1,5)
            
            if willCum == 1:

                print('You came on the ', cumGoblin.name, '! gross, there stunned for 3 turns.')

            elif willCum != 1:

                print('great job nerd, you missed, while you where jerking off he hit you for', cumGoblin.damage, 'damage')
                player.health = player.health - cumGoblin.damage

        print('you have', player.health, 'health and the enemy has', cumGoblin.health, 'health')

print('welcum to the cumgeon, would you you like to enter? (y/n)')
command = input()

if command == 'y' or 'Yes' or 'yes' or 'Y':
    print('you made a mistake')
    time.sleep(2)

    alive = True

    count = 0

    while count < 100:
        count = count + 1
        print('#####################################################################')
        time.sleep(.02)

    while alive:

        print('you wake up in your room like normal, exept your ass feels weird, but you dont think much of it. type help for command list.')
        command = input()

        if command == 'help':
            help()
        elif command == 'cont':
            print('you get out of your bed and you are naked, cum spills out of your ass. "must`ve been a wild night." suddenly, you start throwing up cum. "really wild" you say inbeetween coughs. Then cum comes out of your ears. "what the fuck??" you rush out of your room and your greeted to a giant room. a diembodied voice says')
            input()
            print('We'); time.sleep(.5); print('lc'); time.sleep; print('om'); time.sleep(.5); print('e '); time.sleep(.5); print('to'); time.sleep(.5); print(' t'); time.sleep(.5); print('he'); time.sleep(.5); print(' c'); time.sleep(.5); print('um'); time.sleep(.5); print('ge'); time.sleep(.5); print('on')

            roomStatus = 'b9'

            print('enter a command')
            command = input()

            if command == 'map':
                

        else:
            print('no')


elif command == 'n' or 'No' or 'no' or 'N':
    print('wow ok loser')
    quit()