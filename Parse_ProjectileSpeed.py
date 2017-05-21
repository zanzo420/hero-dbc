# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=C0301

"""
@author: Aethys256
"""

import sys
import os
import csv

generatedDir = os.path.join('DBC', 'generated')
parsedDir = os.path.join('DBC', 'parsed')

Spells = {}

os.chdir(os.path.join(os.path.dirname(sys.path[0]), 'AethysDBC'))

# Since Blizzard only gives us an id and not the spell id, we have to parse Spell.db to retrieve the Spell ID.
with open(os.path.join(generatedDir, 'Spell.csv')) as csvfile:
    reader = csv.DictReader(csvfile, escapechar='\\')
    for row in reader:
        Spells[row['id_misc']] = row['id']


PrjSpeedRawValue = 0
PrjSpeedNbValue = 0

with open(os.path.join(generatedDir, 'SpellMisc.csv')) as csvfile:
    reader = csv.DictReader(csvfile, escapechar='\\')
    with open(os.path.join(parsedDir, 'ProjectileSpeed.lua'), 'w', encoding='utf-8') as file:
        file.write('AethysCore.Enum.ProjectileSpeed = {\n')
        for row in reader:
            prj_speed_f = float(row['proj_speed'])
            if prj_speed_f > 0 and row['id'] in Spells:
                prj_speed_int = int(prj_speed_f)
                PrjSpeedRawValue += prj_speed_int
                PrjSpeedNbValue += 1
                file.write('  [' + Spells[row['id']] + '] = ' + str(prj_speed_int) + ',\n')
        file.write('}\n')

print('Projectile Speed Mean : ' + str(PrjSpeedRawValue/PrjSpeedNbValue))