#!/usr/bin/env python
import pickle
import textwrap
import os, sys
import re

path = os.path.split(os.path.abspath(__file__))[0]

c = open(path + '/classes.db', 'rb')
r = open(path + '/races.db', 'rb')
p = open(path + '/class_powers.db', 'rb')

classes = pickle.load(c)
races = pickle.load(r)
powers = pickle.load(p)

def main(): 
# Dictionary to hold your character
    mychara = {}
    width = 60

# Classes
    confirm = False
    while not confirm:
        os.system('clear')
        count = 1
        class_temp = {}
        print '%-3s   %-20s %s' % ('', 'Classes', 'Role')
        print '-'*width
        for c in sorted(classes):
            class_temp[count] = c
            role = re.compile('^([A-Za-z]*)\. ').findall(classes[c]['Role'][0])[0]
            print '%-3s : %-20s %s' % (count, c, role)
            count += 1
        print '-'*width
        print '\n'

        myclass = input('View Class: ')

        # Give Stats
        os.system('clear')
        for c in sorted(classes[class_temp[myclass]]):
            try:
                stat = classes[class_temp[myclass]][c][0]
            except IndexError:
                stat = ''
            stat = stat.encode('ascii', 'ignore')
            stat = textwrap.wrap(stat, width=50)
            print c, ':'
            for s in stat:
                print '%-10s %s' % ('', s)
            print ' '

        q = raw_input('Pick this Class (Y/n): ')
        if q.upper() == 'Y':
            confirm = True

    mychara['class'] = class_temp[myclass]

# Races
    confirm = False
    while not confirm:
        os.system('clear')
        count = 1
        race_temp = {}
        print '%-3s   %-20s %s' % ('', 'Races', 'Ability Scores')
        print '-'*width
        for r in sorted(races):
            race_temp[count] = r
            print '%-3s : %-20s %s' % (count, r, races[r]['Ability Scores'][0])
            count += 1
        print '-'*width
        print '\n'

        myrace = input('View Race: ')

        # Give Stats
        os.system('clear')
        for c in sorted(races[race_temp[myrace]]):
            try:
                stat = races[race_temp[myrace]][c][0]
            except IndexError:
                stat = ''
            stat = stat.encode('ascii', 'ignore')
            stat = textwrap.wrap(stat, width=50)
            print c, ':'
            for s in stat:
                print '%-10s %s' % ('', s)
            print ' '

        q = raw_input('Pick this Race (Y/n): ')
        if q.upper() == 'Y':
            confirm = True

    mychara['race'] = race_temp[myrace]

# Spells
# At-Will
    confirm = False
    while not confirm:
        os.system('clear')
        count = 1
        atwill_temp = {}
        print 'At-Will Powers'
        print '-'*width
        for s in sorted(powers):
            atwill_temp[count] = s
            if powers[s]['Class'][0] == mychara['class']:
                try:
                    level = powers[s]['Level'][0]
                except IndexError:
                    level = ''
                except KeyError:
                    level = ''
                if level == '1':
                    if powers[s]['Power Usage'][0] == 'At-Will':
                        print '%-3s : %s' % (count, s)
                        count += 1
        print '-'*width
        print '\n'

        myatwill = input('View Power: ')

        # Give Stats
        os.system('clear')
        for c in sorted(powers[atwill_temp[myatwill]]):
            try:
                stat = powers[atwill_temp[myatwill]][c][0]
            except IndexError:
                stat = ''
            stat = stat.encode('ascii', 'ignore')
            stat = textwrap.wrap(stat, width=50)
            print c, ':'
            for s in stat:
                print '%-10s %s' % ('', s)
            print ' '

        q = raw_input('Pick this Power (Y/n): ')
        if q.upper() == 'Y':
            confirm = True 

    mychara['atwill1'] = atwill_temp[myatwill]

# Spells
# At-Will2
    confirm = False
    while not confirm:
        os.system('clear')
        count = 1
        atwill_temp = {}
        print 'At-Will Powers'
        print '-'*width
        for s in sorted(powers):
            if s == mychara['atwill1']:
                continue
            atwill_temp[count] = s
            if powers[s]['Class'][0] == mychara['class']:
                try:
                    level = powers[s]['Level'][0]
                except IndexError:
                    level = ''
                except KeyError:
                    level = ''
                if level == '1':
                    if powers[s]['Power Usage'][0] == 'At-Will':
                        print '%-3s : %s' % (count, s)
                        count += 1
        print '-'*width
        print '\n'

        myatwill2 = input('View Power: ')

        # Give Stats
        os.system('clear')
        for c in sorted(powers[atwill_temp[myatwill]]):
            try:
                stat = powers[atwill_temp[myatwill]][c][0]
            except IndexError:
                stat = ''
            stat = stat.encode('ascii', 'ignore')
            stat = textwrap.wrap(stat, width=50)
            print c, ':'
            for s in stat:
                print '%-10s %s' % ('', s)
            print ' '

        q = raw_input('Pick this Power (Y/n): ')
        if q.upper() == 'Y':
            confirm = True

    mychara['atwill2'] = atwill_temp[myatwill2]

# Spells
# Daily
    confirm = False
    while not confirm:
        os.system('clear')
        count = 1
        daily_temp = {}
        print 'Daily Powers'
        print '-'*width
        for s in sorted(powers):
            daily_temp[count] = s
            if powers[s]['Class'][0] == mychara['class']:
                try:
                    level = powers[s]['Level'][0]
                except IndexError:
                    level = ''
                except KeyError:
                    level = ''
                if level == '1':
                    if powers[s]['Power Usage'][0] == 'Daily':
                        print '%-3s : %s' % (count, s)
                        count += 1

        print '-'*width
        print '\n'

        mydaily = input('Pick your Daily Power: ')

        # Give Stats
        os.system('clear')
        for c in sorted(powers[daily_temp[mydaily]]):
            try:
                stat = powers[daily_temp[mydaily]][c][0]
            except IndexError:
                stat = ''
            stat = stat.encode('ascii', 'ignore')
            stat = textwrap.wrap(stat, width=50)
            print c, ':'
            for s in stat:
                print '%-10s %s' % ('', s)
            print ' '

        q = raw_input('Pick this Power (Y/n): ')
        if q.upper() == 'Y':
            confirm = True

    mychara['daily'] = daily_temp[mydaily]

    os.system('clear')
    for me in mychara:
        print '%-10s %s' % (me, mychara[me])

if __name__ == '__main__':
    main()
