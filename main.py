import time,os,random
from vars import *
def loop1(lake1_cords,moving_to):
  global current_location, current_surrounding,time,stanima
  fixed1=0
  fixed2=0
  fixed3=0
  time.sleep(1.5)#5
  if current_location[0]<lake1_cords[0]:
    fixed1=lake1_cords[0]-current_location[0]
  if current_location[0]>lake1_cords[0]:
    fixed1=current_location[0]-lake1_cords[0]
  if current_location[1]<lake1_cords[1]:
    fixed2=lake1_cords[1]-current_location[1]
  if current_location[1]>lake1_cords[1]:
    fixed2=current_location[1]-lake1_cords[1] #Up to this point is the same for all lakes
  if current_location[2]<lake1_cords[2]:
    fixed3=lake1_cords[2]-current_location[2]
  if current_location[2]>lake1_cords[2]:
    fixed3=current_location[2]-lake1_cords[2]
  total_distance=fixed1+fixed2+fixed3
  stanima1=total_distance/3.5
  stanima1=round(stanima1)
  if stanima1<stanima+1:
    print 'Moving to location...'
    print '\nTraveling cords:',fixed1,fixed2,fixed3
    current_surrounding=moving_to
    current_location=lake1_cords
    stanima-=stanima1
    print 'Total distance traveled:',total_distance,'(meters)'
    print 'Current area:',current_surrounding
    print 'Current cordinates:',current_location
    print 'Stanima:',stanima
  if stanima1+1>stanima:
    print 'You need to sleep. You are too tired to keep moving.'
  move_on=raw_input('Hit enter to exit change location:')
def loop2():
  global sides,choice
  if '(' in choice:
    choice = choice.replace('(','')
    sides=True
  if ')' in choice:
    choice = choice.replace(')','')
    sides=True
def loop3():
  #Use clear() before entering
  global storage_wood,wood,storage_water,water
  global storage_dirt,dirt,storage_rocks,rocks
  global storage_clay,clay,storage_bowl,bowl
  global storage_sticks,sticks,storage_pickaxe,pickaxe
  global storage_axe,axe,storage_shovel,shovel
  global home_storage
  choice1=''
  choice2=''
  storage_int=0
  storage_int+=storage_water+storage_wood+storage_dirt
  storage_int+=storage_rocks+storage_clay+storage_bowl
  storage_int+=storage_sticks+storage_pickaxe+storage_axe
  storage_int+=storage_shovel
  self_int=0
  self_int+=wood,water,dirt,rocks,clay,bowl,sticks
  self_int+=pickaxe,axe,shovel
  if storage_int+1>home_storage:
    if self_int+1>self_storage:
      print 'Both Your Home and inventory are full. In order to use this function, you must remove some items.'
      print '\nHint: Sell the things you don\'t need'
    if self_int<self_storage+1:
      print 'Your home storage is full. You can not add things to it. But, you may take things away.'
      print '(1)Withdraw\n(2)Leave'
      move_on=raw_input('1 or 2:').lower()
      choice1='hi'
      if move_on=="1":
        choice2="1"
      if move_on=="2":
        choice1="wefhgef"
    if choice1 is not 'hi':
      if choice1 is not "wefhgef":
        print '(1)Withdraw\n(2)Deposit\n(3)Leave'
        choice2=raw_input("Choose one of the options:")
        clear()
        if choice2 == "1":
          print 'Items stored:'
          print '(1)Wood:',storage_wood,'(logs)'
          print '(2)Water:',storage_water,'(oz)'
          print '(3)Dirt:',storage_dirt,'(lbs)'
          print '(4)Rocks:',storage_rocks,'(Qty)'
          print '(5)Clay:',storage_clay,'(lbs)'
          print '(6)Bowl:',storage_bowl,'(Qty)'
          print '(7)Sticks:',storage_sticks,'(Qty)'
          print '(8)Pickaxes:',storage_pickaxe,'(Qty)'
          print '(9)Shovels:',storage_shovel,'(Qty)'
          print '(10)Axes:',storage_axe,'(Qty)'
          choice = raw_input('What would you like to withdraw:')
          if choice == "1":
            if storage_wood<1:
              print 'You don\'t have enough.'
            if storage_wood>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_wood+1:
                  wood+=int(choice)
                  storage_wood-=int(choice)
                  print 'Current holding:'
                  print 'Wood in storage:',storage_wood
                  print 'Wood in inventory:',wood
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "2":
            if storage_water<1:
              print 'You don\'t have enough.'
            if storage_water>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_water+1:
                  water+=int(choice)
                  storage_water-=int(choice)
                  print 'Current holding:'
                  print 'Water in storage:',storage_water
                  print 'Water in inventory:',water
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "3":
            if storage_dirt<1:
              print 'You don\'t have enough.'
            if storage_dirt>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_dirt+1:
                  dirt+=int(choice)
                  storage_dirt-=int(choice)
                  print 'Current holding:'
                  print 'Dirt in storage:',storage_dirt
                  print 'Dirt in inventory:',dirt
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "4":
            if storage_rocks<1:
              print 'You don\'t have enough.'
            if storage_rocks>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_rocks+1:
                  rocks+=int(choice)
                  storage_rocks-=int(choice)
                  print 'Current holding:'
                  print 'Rocks in storage:',storage_rocks
                  print 'Rocks in inventory:',rocks
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "5":
            if storage_clay<1:
              print 'You don\'t have enough.'
            if storage_clay>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_clay+1:
                  clay+=int(choice)
                  storage_clay-=int(choice)
                  print 'Current holding:'
                  print 'Clay in storage:',storage_clay
                  print 'Clay in inventory:',clay
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "7":
            if storage_sticks<1:
              print 'You don\'t have enough.'
            if storage_sticks>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_clay+1:
                  clay+=int(choice)
                  storage_clay-=int(choice)
                  print 'Current holding:'
                  print 'Sticks in storage:',storage_clay
                  print 'Sticks in inventory:',clay
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "6":
            if storage_bowl<1:
              print 'You don\'t have enough.'
            if storage_bowl>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_bowl+1:
                  bowl+=int(choice)
                  storage_bowl-=int(choice)
                  print 'Current holding:'
                  print 'Bowl in storage:',storage_bowl
                  print 'Bowl in inventory:',bowl
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "8":
            if storage_pickaxe<1:
              print 'You don\'t have enough.'
            if storage_pickaxe>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_pickaxe+1:
                  pickaxe+=int(choice)
                  storage_pickaxe-=int(choice)
                  print 'Current holding:'
                  print 'Pickaxe(s) in storage:',storage_pickaxe
                  print 'Pickaxe(s) in inventory:',pickaxe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "9":
            if storage_shovel<1:
              print 'You don\'t have enough.'
            if storage_shovel>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_shovel+1:
                  shovel+=int(choice)
                  storage_shovel-=int(choice)
                  print 'Current holding:'
                  print 'Shovel(s) in storage:',storage_shovel
                  print 'Shovel(s) in inventory:',shovel
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "10":
            if storage_axe<1:
              print 'You don\'t have enough.'
            if storage_axe>0:
              choice=raw_input('How many to withdraw:')
              try:
                if int(choice)<storage_axe+1:
                  axe+=int(choice)
                  storage_axe-=int(choice)
                  print 'Current holding:'
                  print 'Axe(s) in storage:',storage_axe
                  print 'Axe(s) in inventory:',axe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          move_on=raw_input('Hit enter to exit crafting:')
          choice=''
        if choice2 == "2":
          print 'You have:'
          print '(1)Wood:',wood,'(logs)'
          print '(2)Water:',water,'(oz)'
          print '(3)Dirt:',dirt,'(lbs)'
          print '(4)Rocks:',rocks,'(Qty)'
          print '(5)Clay:',clay,'(lbs)'
          print '(6)Bowl:',bowl,'(Qty)'
          print '(7)Sticks:',sticks,'(Qty)'
          print '(8)Pickaxes:',pickaxe,'(Qty)'
          print '(9)Shovels:',shovel,'(Qty)'
          print '(10)Axes:',axe,'(Qty)'
          choice = raw_input('What would you like to withdraw:')
          if choice == "1":
            if wood<1:
              print 'You don\'t have enough.'
            if wood>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<wood+1:
                  wood-=int(choice)
                  storage_wood+=int(choice)
                  print 'Current holding:'
                  print 'Wood in storage:',storage_wood
                  print 'Wood in inventory:',wood
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "2":
            if water<1:
              print 'You don\'t have enough.'
            if water>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<water+1:
                  water-=int(choice)
                  storage_water+=int(choice)
                  print 'Current holding:'
                  print 'Water in storage:',storage_water
                  print 'Water in inventory:',water
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "3":
            if dirt<1:
              print 'You don\'t have enough.'
            if dirt>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<dirt+1:
                  dirt-=int(choice)
                  storage_dirt+=int(choice)
                  print 'Current holding:'
                  print 'Dirt in storage:',storage_dirt
                  print 'Dirt in inventory:',dirt
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "4":
            if rocks<1:
              print 'You don\'t have enough.'
            if rocks>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<rocks+1:
                  rocks-=int(choice)
                  storage_rocks+=int(choice)
                  print 'Current holding:'
                  print 'Rock(s) in storage:',storage_rocks
                  print 'Rock(s) in inventory:',rocks
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "5":
            if clay<1:
              print 'You don\'t have enough.'
            if clay>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<clay+1:
                  clay-=int(choice)
                  storage_clay+=int(choice)
                  print 'Current holding:'
                  print 'Clay in storage:',storage_clay
                  print 'Clay in inventory:',clay
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "6":
            if bowl<1:
              print 'You don\'t have enough.'
            if bowl>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<bowl+1:
                  bowl-=int(choice)
                  storage_bowl+=int(choice)
                  print 'Current holding:'
                  print 'Bowl(s) in storage:',storage_bowl
                  print 'Bowl(s) in inventory:',bowl
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "7":
            if sticks<1:
              print 'You don\'t have enough.'
            if sticks>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<sticks+1:
                  sticks-=int(choice)
                  storage_sticks+=int(choice)
                  print 'Current holding:'
                  print 'Stick(s) in storage:',storage_sticks
                  print 'Stick(s) in inventory:',sticks
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "8":
            if pickaxe<1:
              print 'You don\'t have enough.'
            if pickaxe>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<pickaxe+1:
                  pickaxe-=int(choice)
                  storage_pickaxe+=int(choice)
                  print 'Current holding:'
                  print 'Pickaxe(s) in storage:',storage_pickaxe
                  print 'Pickaxe(s) in inventory:',pickaxe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "9":
            if shovel<1:
              print 'You don\'t have enough.'
            if shovel>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<shovel+1:
                  shovel-=int(choice)
                  storage_shovel+=int(choice)
                  print 'Current holding:'
                  print 'Shovel(s) in storage:',storage_shovel
                  print 'Shovel(s) in inventory:',shovel
              except ValueError, TypeError:
                print 'You need to enter a number.'
          if choice == "10":
            if axe<1:
              print 'You don\'t have enough.'
            if axe>0:
              choice=raw_input('How many to deposit:')
              try:
                if int(choice)<axe+1:
                  axe-=int(choice)
                  storage_axe+=int(choice)
                  print 'Current holding:'
                  print 'Axe(s) in storage:',storage_axe
                  print 'Axe(s) in inventory:',axe
              except ValueError, TypeError:
                print 'You need to enter a number.'
          move_on=raw_input('Hit enter to exit crafting:')
          choice=''
def loop4(s,other,numbers):
  #s = (True)Shows other stuff and stats
  global dirt,wood,rocks,water,clay,bowl,sticks
  global self_storage,home_storage,stanima,max_stanima
  global current_surronding,current_location
  global pickaxe,axe,shovel,diamond,coal,iron,gold
  side='  ()'
  side1=1
  self_int=0
  self_int+=wood+water+dirt+rocks+clay+bowl+sticks
  self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
  print 'Minerals:'
  if numbers==True:
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Wood:',wood,'(logs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Dirt:',dirt,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Water:',water,'(oz)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Rocks:',rocks,'(Qty)'
    print 'Items:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Clay:',clay,'(lbs)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Bowls:',bowl,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Sticks:',sticks,'(Qty)'
    print 'Tools:'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Pickaxes:',pickaxe,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Shovels:',shovel,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Axes:',axe,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print 'Goodies:'
    print side2+'Coal:',coal,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Iron:',iron,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Gold:',gold,'(Qty)'
    side2=side[:3]+str(side1)+side[3:]
    side1+=1
    print side2+'Diamonds:',diamond,'(Qty)'
  if numbers==False:
    print '  Wood:',wood,'(logs)'
    print '  Dirt:',dirt,'(lbs)'
    print '  Water:',water,'(oz)'
    print '  Rocks:',rocks,'(Qty)'
    print 'Items:'
    print '  Clay:',clay,'(lbs)'
    print '  Bowls:',bowl,'(Qty)'
    print '  Sticks:',sticks,'(Qty)'
    print 'Tools:'
    print '  Pickaxes:',pickaxe,'(Qty)'
    print '  Shovels:',shovel,'(Qty)'
    print '  Axes:',axe,'(Qty)'
  if other==True:
    print 'Goodies:'
    print '  Coal:',coal,'(Qty)'
    print '  Iron:',iron,'(Qty)'
    print '  Gold:',gold,'(Qty)'
    print '  Diamonds:',diamond,'(Qty)'
  if s==True:
    print 'Storage:'
    print '  Inventory Storage:',self_storage,'(qty of items)'
    print '  Home storage:',home_storage,'(qty of items)'
    print '  Inventory capacity:',self_int,'out of',self_storage
    print 'Stats:'
    print '  Stanima:',stanima,'(%)'
    print '  Max_stanima',max_stanima,'(%)'
    print ''
    print 'Current money:',str(money)+' (cents)'
    print 'Current area:',current_surrounding
    print 'Current cordinates:',current_location
def clear():
  os.system('clear')
def dev_promt():
  print 'You must activate Dev_options to use this. This lock will be removed in future updates. Go to vars.py to see how to enable dev_options. It\'s at the bottom.'
#move_on=raw_input('Hit enter to exit crafting:')
p=True
dev=True#Default False
while p==True:
  clear()
  if dev==True:
    print 'Dev_options: Enabled\n'
  print 'Please read tips if this is the first time playing. Thank you!'
  print '(1)Gather resources'
  print '(2)Change location'
  print '(3)Go back home'
  print '(4)Crafting menu'
  print '(5)Sleep'
  print '(6)Tips'
  print '(7)Exersice'
  print '(8)Sell'
  print '(9)Mining'
  print '(*)Show inventory'
  print '(bye)Exit'
  if dev==True:
    print '\nDev_menu()\n'
  print '\nTo get help type (help)'
  choice=raw_input('Choose an option or enter code:')
  if choice==dev_options:
    use=False
    if dev==False:
      print 'Dev_options: Enabled'
      dev=True
      use=True
    if use==False:
      if dev==True:
        print 'Dev_options: Disabled'
        dev=False
    time.sleep(1)
  clear()
  loop2()
  if choice == "1":
    self_int=0
    self_int+=wood+water+dirt+rocks+clay+bowl+sticks
    self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
    #Water + Dirt = Clay
    #Wood = house, water holder, storage
    print '(1)Wood\n(2)Water\n(3)Dirt\n(4)Rocks\n(5)Sticks'
    choice=raw_input('What would you like to gather:')
    loop2()
    if choice == "1":
      if self_storage<self_int+3:
        print 'Your inventory is full.'
        choice='blah'
      if choice == "1":
        if axe>0:
          print 'Gathering wood...'
          time.sleep(3)
          wood+=3
          print 'Gathered wood'
          time.sleep(1)
        if axe<1:
          print 'You need more axe(s)'
    if choice == "2":
      if current_surrounding not in water_biomes:
        print 'You need to be near a lake or a river to gather water.'
      if current_surrounding in water_biomes:
        if self_storage<self_int+2:
          choice='blah'
        if choice == "2":
          print 'Gathering water...'
          time.sleep(3)
          water+=2
          print 'Gathered water'
          time.sleep(1)
    if choice == "3":
      if current_surrounding in dirt_biomes:
        if self_storage<self_int+2:
          choice='blah'
        if choice == "3":
          if shovel>0:
            print 'Gathering dirt...'
            time.sleep(3)
            dirt+=2
            print 'Gathered dirt'
            time.sleep(1)
          if shovel<1:
            print 'You need more shovel(s)'
      if current_surrounding not in dirt_biomes:
        print 'You must be in the forest to gather dirt.'
    if choice == "4":
      if current_surrounding in clay_biomes or current_surrounding in dirt_biomes:
        if self_storage<self_int+2:
          choice = 'blah'
        if choice == "4":
          print 'Gathering rocks...'
          time.sleep(3)
          rocks+=2
          print 'Gathered 2 rocks.'
          time.sleep(1)
      if current_surrounding not in clay_biomes or dirt_biomes:
        print 'You must at clay mountian or the forest to gather rocks.'
    if choice == "5":
      if current_surrounding in dirt_biomes:
        if self_storage<self_int+1:
          choice="blah"
        if choice == "5":
          print 'Gathering sticks...'
          time.sleep(3)
          sticks+=2
          print 'Gathered 2 sticks.'
          time.sleep(1)
      if current_surrounding not in dirt_biomes:
        print 'You must be in the forest to gather sticks.'
    choice=''
    move_on=raw_input('Hit enter to exit crafting:')
  if choice == "2":
    print 'Current location:',current_surrounding
    print '(1)Lake\n(2)River\n(3)Clay mountian\n(4)Exercise mountian\n(5)Desert\n(6)Abandoned city'
    choice = raw_input('Where would you like to go:')
    loop2(choice)
    if choice == "1":
      hi=random.randint(1,3)
      if hi==1:
        loop1(lake1_cords,'lake #1')
      if hi==2:
        loop1(lake2_cords,'lake #2')
      if hi==3:
        loop1(lake3_cords,'lake #3')
    if choice == "2":
      hi=random.randint(1,3)
      if hi==1:
        loop1(river1_cords,'river #1')
      if hi==2:
        loop1(river2_cords,'river #2')
      if hi==3:
        loop1(river3_cords,'river #3')
    if choice == "3":
      hi=random.randint(1,3)
      if hi==1:
        loop1(clay_mountian1_cords,'clay mountian #1')
      if hi==2:
        loop1(clay_mountian2_cords,'clay mountian #2')
      if hi==3:
        loop1(clay_mountian3_cords,'clay mountian #3')
    if choice == "4":
      loop1(exercise_mountian1_cords,'exercise mountian #1')
    if choice == "5":
      hi=random.randint(1,3)
      if hi==1:
        loop1(desert1_cords,'desert #1')
      if hi==2:
        loop1(desert2_cords,'desert #2')
      if hi==3:
        loop1(desert3_cords,'desert #3')
    if choice == "6":
      hi=random.randint(1,3)
      if hi==1:
        loop1(city1_cords,'city #1')
      if hi==2:
        loop1(city2_cords,'city #2')
      if hi==3:
        loop1(city3_cords,'city #3')
    choice = ''
  if choice == "3":
    loop1(home_location,'home')
    choice = ''
  if choice == "4":
    print '(1)Clay     Needs - Dirt:1 Water:1'
    print '(2)Bowl     Needs - Wood:2'
    print '(3)Sticks   Needs - Wood:1'
    if dev==True:
      print '(4)Pickaxe  Needs - Sticks:2 Rocks:3'
      print '(5)Shovel   Needs - Sticks:2 Rocks:1'
      print '(6)Axe      Needs - Sticks:2 Rocks:2'
    choice = raw_input('What would you like to make:')
    loop2(choice)
    if choice == "1":
      if dirt>0:
        if water>0:
          print 'Making clay...'
          time.sleep(2)
          print 'Made 1 clay'
          clay+=1
          dirt-=1
          water-=1
          print 'You have',clay,'clay'
      if dirt<1:
        print 'You need more dirt'
      if water<1:
        print 'You need more water'
        print 'You have',dirt,'dirt'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "2":
      if wood>1:
        print 'Making a bowl...'
        time.sleep(2)
        print 'Made 1 bowl'
        bowl+=1
        wood-=2
        print 'You have',bowl,'bowl(s)'
      if wood<2:
        print 'You need more wood'
        print 'You have',wood,'wood'
      move_on=raw_input('Hit enter to exit crafting:')
    if choice == "3":
      if wood>0:
        print 'Making sticks...'
        time.sleep(2)
        print 'Made 4 sticks.'
        sticks+=4
        wood-=1
        print 'You have',sticks,'stick(s)'
      if wood<1:
        print 'You need more wood'
        print 'You have',wood,'wood'
      move_on=raw_input('Hit enter to exit crafting:')
    if dev==True:
      if choice == "4":
        if sticks>1:
          if rocks>2:
            print 'Making a pickaxe...'
            time.sleep(2)
            print 'Made 1 pickaxe.'
            pickaxe+=1
            sticks-=2
            rocks-=3
            print 'You have',pickaxe,'pickaxe(s)'
        if sticks<2:
          print 'You need more sticks.'
        if rocks<3:
          print 'You need more rocks'
      if choice == "5":
        if sticks>1:
          if rocks>0:
            print 'Making a shovel...'
            time.sleep(2)
            print 'Made 1 shovel.'
            shovel+=1
            sticks-=2
            rocks-=1
            print 'You have',shovel,'shovel(s)'
        if sticks<2:
          print 'You need more sticks.'
        if rocks<1:
          print 'You need more rocks'
      if choice == "6":
        if sticks>1:
          if rocks>1:
            print 'Making a axe...'
            time.sleep(2)
            print 'Made 1 axe.'
            axe+=1
            sticks-=2
            rocks-=2
            print 'You have',axe,'axe(s)'
        if sticks<2:
          print 'You need more sticks.'
        if rocks<2:
          print 'You need more rocks'
    if dev==False:
      if choice == "4":
        dev_promt()
      if choice == "5":
        dev_promt()
      if choice == "6":
        dev_promt()
    choice = ''
  if choice == "5":
    if stanima==max_stanima:
      print 'You are not tired.'
    if stanima<max_stanima:
      print 'Sleeping...'
      stanima1=max_stanima-stanima
      sleep_time=stanima1/3
      sleep_time=round(sleep_time)
      if sleep_time>15:
        sleep_time=15
      if current_surrounding == "home":
        sleep_time/=2
      print 'Est:',sleep_time,'seconds'
      time.sleep(sleep_time)
      stanima=max_stanima
      move_on=raw_input('Hit enter to exit sleep:')
    choice = ''
  if choice == "6":
    print 'Things with (*) at the end are locked. At the end, not the beggining. Just making that clear.'
    print '\nYou can be anywhere when entering the mines. There is a mine in every location.'
    if dev==True:
      print '\nTo store store items at home. Do this. \n1. Make sure you are at home\n2. Open inventory\n3. Instead of hiting enter to exit type (storage) to store items.\nHint: You can also grab items back from doing this.'
    move_on=raw_input('\nHit enter to exit tips:')
    choice = ''
  if choice == "7":
    if current_surrounding=="exercise mountian #1":
      print 'Getting in the mood...'
      time.sleep(2.5)
      print 'Moving to the beat...'
      time.sleep(2.5)
      print 'Stanima increased by 15'
      max_stanima+=15
      print 'Recommended to go to sleep.'
    if current_surrounding is not "exercise mountian #1":
      print 'You need to travel to exersice mountian to use this function.'
    move_on=raw_input('Hit enter to exit exercise:')
  if choice == "8":
    clear()
    loop4(s=False,other=False,numbers=True)
    choice=raw_input('What would you like to sell:')
    if choice=="1":
      if wood>0:
        choice=raw_input('How many:')
        if wood==int(choice) or wood>int(choice):
          try:
            money+=int(choice)*price_wood
            wood-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Wood:',wood
          except ValueError:
            print 'You need to enter a number.'
      if wood<1:
        print 'You don\'t have any to sell'
    if choice=="2":
      if dirt>0:
        choice=raw_input('How many:')
        if dirt==int(choice) or dirt>int(choice):
          try:
            money+=int(choice)*price_dirt
            dirt-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Dirt:',dirt
          except ValueError:
            print 'You need to enter a number.'
      if dirt<1:
        print 'You don\'t have any to sell'
    if choice=="3":
      if water>0:
        choice=raw_input('How many:')
        if water==int(choice) or water>int(choice):
          try:
            money+=int(choice)*price_water
            water-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Water:',water
          except ValueError:
            print 'You need to enter a number.'
      if water<1:
        print 'You don\'t have any to sell'
    if choice=="4":
      if rocks>0:
        choice=raw_input('How many:')
        if rocks==int(choice) or rocks>int(choice):
          try:
            money+=int(choice)*price_rocks
            rocks-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Rock(s):',rocks
          except ValueError:
            print 'You need to enter a number.'
      if rocks<1:
        print 'You don\'t have any to sell'
    if choice=="5":
      if clay>0:
        choice=raw_input('How many:')
        if clay==int(choice) or clay>int(choice):
          try:
            money+=int(choice)*price_clay
            clay-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Clay:',clay
          except ValueError:
            print 'You need to enter a number.'
      if clay<1:
        print 'You don\'t have any to sell'
    if choice=="6":
      if bowls>0:
        choice=raw_input('How many:')
        if bowls==int(choice) or bowls>int(choice):
          try:
            money+=int(choice)*price_bowls
            bowls-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Bowl(s):',bowls
          except ValueError:
            print 'You need to enter a number.'
      if bowls<1:
        print 'You don\'t have any to sell'
    if choice=="7":
      if sticks>0:
        choice=raw_input('How many:')
        if sticks==int(choice) or sticks>int(choice):
          try:
            money+=int(choice)*price_sticks
            sticks-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Stick(s):',sticks
          except ValueError:
            print 'You need to enter a number.'
      if sticks<1:
        print 'You don\'t have any to sell'
    if choice=="8":
      if pickaxe>0:
        choice=raw_input('How many:')
        if pickaxe==int(choice) or pickaxe>int(choice):
          try:
            money+=int(choice)*price_pickaxe
            pickaxe-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Pickaxe(s):',pickaxe
          except ValueError:
            print 'You need to enter a number.'
      if pickaxe<1:
        print 'You don\'t have any to sell'
    if choice=="9":
      if shovel>0:
        choice=raw_input('How many:')
        if shovel==int(choice) or shovel>int(choice):
          try:
            money+=int(choice)*price_shovel
            shovel-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Shovel(s):',shovel
          except ValueError:
            print 'You need to enter a number.'
      if shovel<1:
        print 'You don\'t have any to sell'
    if choice=="10":
      if axe>0:
        choice=raw_input('How many:')
        if axe==int(choice) or axe>int(choice):
          try:
            money+=int(choice)*price_axe
            axe-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Axe(s):',axe
          except ValueError:
            print 'You need to enter a number.'
      if axe<1:
        print 'You don\'t have any to sell'
    if choice=="11":
      if coal>0:
        choice=raw_input('How many:')
        if coal==int(choice) or coal>int(choice):
          try:
            money+=int(choice)*price_coal
            coal-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Coal:',coal
          except ValueError:
            print 'You need to enter a number.'
      if coal<1:
        print 'You don\'t have any to sell'
    if choice=="12":
      if iron>0:
        choice=raw_input('How many:')
        if iron==int(choice) or iron>int(choice):
          try:
            money+=int(choice)*price_iron
            iron-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Iron:',iron
          except ValueError:
            print 'You need to enter a number.'
      if iron<1:
        print 'You don\'t have any to sell'
    if choice=="13":
      if gold>0:
        choice=raw_input('How many:')
        if gold==int(choice) or gold>int(choice):
          try:
            money+=int(choice)*price_gold
            gold-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Gold:',gold
          except ValueError:
            print 'You need to enter a number.'
      if gold<1:
        print 'You don\'t have any to sell'
    if choice=="14":
      if diamond>0:
        choice=raw_input('How many:')
        if diamond==int(choice) or diamond>int(choice):
          try:
            money+=int(choice)*price_diamond
            diamond-=int(choice)
            print 'Current holdings:'
            print 'Money:',money
            print 'Diamond:',diamond
          except ValueError:
            print 'You need to enter a number.'
      if diamond<1:
        print 'You don\'t have any to sell'
    choice=''
    move_on=raw_input('Hit enter to exit sell:')
  if choice == "9":
    self_int=0
    self_int+=wood+water+dirt+rocks+clay+bowl+sticks
    self_int+=pickaxe+axe+shovel+diamond+coal+iron+gold
    if pickaxe<1:
      print 'You need at least one pickaxe to mine.'
      time.sleep(1.5)
    if pickaxe>0:
      if self_storage<self_int+1:
        if stanima>60:
          print 'Going into the mines...'
          time.sleep(1.5)
          clear()
          print '(1)Coal       Est: 5 sec'
          print '(2)Iron       Est: 15 sec'
          print '(3)Gold       Est: 30 sec'
          print '(4)Diamond    Est: 1 min'
          choice = raw_input('What would you like to mine:')
          if choice == "1":
            print 'Going to find some coal...'
            time.sleep(1)
            print 'Found some coal. \nMining the coal...'
            time.sleep(5)
            coal+=1
            pickaxe-=1
          if choice == "2":
            print 'Going to find some iron...'
            time.sleep(1)
            print 'Found some iron. \nMining the iron...'
            time.sleep(15)
            iron+=1
            pickaxe-=1
          if choice == "3":
            print 'Going to find some gold...'
            time.sleep(1)
            print 'Found some gold. \nMining the gold...'
            time.sleep(30)
            gold+=1
            pickaxe-=1
          if choice == "4":
            print 'Going to find some diamonds...'
            time.sleep(1)
            print 'Found some diamonds. \nMining the diamonds...'
            time.sleep(60)
            diamond+=1
            pickaxe-=1
    choice = ''
  if choice in exit_pos:
    print 'Goodbye.'
    p=False
  if choice == "*":
    loop4(s=True,other=True,numbers=False)
    #clay,bowl,storage
    move_on=raw_input('Hit enter to exit bag:').lower()
    if move_on=="storage":
      if dev==True:
        clear()
        loop3()
      if dev==False:
        clear()
        dev_promt()
        move_on=raw_input('Hit enter to exit storage:')
    choice = ''
  if choice == "Dev_menu":
    if dev==True:
      if sides == True:
        print '(1)Give - Gives free stuff'
        print '(2)Remove - Removes stuff'
        choice = raw_input('Choose an option:')
        if choice == "1":
          clear()
          loop4(s=False,other=False,numbers=True)
          choice=raw_input('Choose an option:')
          if choice == "1":
            choice = raw_input('How many:')
            wood+=int(choice)
            choice = ''
          if choice == "2":
            choice = raw_input('How many:')
            dirt+=int(choice)
            choice = ''
          if choice == "3":
            choice = raw_input('How many:')
            water+=int(choice)
            choice = ''
          if choice == "4":
            choice = raw_input('How many:')
            rocks+=int(choice)
            choice = ''
          if choice == "5":
            choice = raw_input('How many:')
            clay+=int(choice)
            choice = ''
          if choice == "6":
            choice = raw_input('How many:')
            bowl+=int(choice)
            choice = ''
          if choice == "7":
            choice = raw_input('How many:')
            sticks+=int(choice)
            choice = ''
          if choice == "8":
            choice = raw_input('How many:')
            pickaxe+=int(choice)
            choice = ''
          if choice == "9":
            choice = raw_input('How many:')
            shovel+=int(choice)
            choice = ''
          if choice == "10":
            choice = raw_input('How many:')
            axe+=int(choice)
            choice = ''
          if choice == "11":
            choice = raw_input('How many:')
            coal+=int(choice)
            choice = ''
          if choice == "12":
            choice = raw_input('How many:')
            iron+=int(choice)
            choice = ''
          if choice == "13":
            choice = raw_input('How many:')
            gold+=int(choice)
            choice = ''
          if choice == "14":
            choice = raw_input('How many:')
            diamond+=int(choice)
            choice = ''
        if choice == "2":
          clear()
          loop4(s=False,other=False,numbers=True)
          choice=raw_input('Choose an option:')
          if choice == "1":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              wood=0
            if choice is not "*":
              if wood==int(choice) or wood>int(choice):
                wood-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "2":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              dirt=0
            if choice is not "*":
              if dirt==int(choice) or dirt>int(choice):
                dirt-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "3":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              water=0
            if choice is not "*":
              if water==int(choice) or water>int(choice):
                water-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "4":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              rocks=0
            if choice is not "*":
              if rocks==int(choice) or rocks>int(choice):
                rocks-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "5":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              clay=0
            if choice is not "*":
              if clay==int(choice) or clay>int(choice):
                clay-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "6":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              bowl=0
            if choice is not "*":
              if bowl==int(choice) or bowl>int(choice):
                bowl-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "7":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              sticks=0
            if choice is not "*":
              if sticks==int(choice) or sticks>int(choice):
                sticks-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "8":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              pickaxe=0
            if choice is not "*":
              if pickaxe==int(choice) or pickaxe>int(choice):
                pickaxe-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "9":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              shovel=0
            if choice is not "*":
              if shovel==int(choice) or shovel>int(choice):
                shovel-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "10":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              axe=0
            if choice is not "*":
              if axe==int(choice) or axe>int(choice):
                axe-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "11":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              coal=0
            if choice is not "*":
              if coal==int(choice) or coal>int(choice):
                coal-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "12":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              iron=0
            if choice is not "*":
              if iron==int(choice) or iron>int(choice):
                iron-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "13":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              gold=0
            if choice is not "*":
              if gold==int(choice) or gold>int(choice):
                gold-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
          if choice == "14":
            print '(*)Remove all'
            choice = raw_input('How many:')
            if choice == "*":
              diamond=0
            if choice is not "*":
              if diamond==int(choice) or diamond>int(choice):
                diamond-=int(choice)
              else:
                print 'You don\'t have enough. Sorry :('
                time.sleep(1.5)
            choice = ''
        choice = ''












