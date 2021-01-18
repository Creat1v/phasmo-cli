#!/usr/bin/python
# Helps finding the ghost type in Phasmophobia

import sys
import argparse
import variables

def get_evidence_by_ghosttype(ghosttype):
    if (ghosttype == "Banshee"):
        return variables.Banshee
    if (ghosttype == "Demon"):
        return variables.Demon
    if (ghosttype == "Jinn"):
        return variables.Jinn
    if (ghosttype == "Mare"):
        return variables.Mare
    if (ghosttype == "Oni"):
        return variables.Oni
    if (ghosttype == "Phantom"):
        return variables.Phantom
    if (ghosttype == "Poltergeist"):
        return variables.Poltergeist
    if (ghosttype == "Revenant"):
        return variables.Revenant
    if (ghosttype == "Shade"):
        return variables.Shade
    if (ghosttype == "Spirit"):
        return variables.Spirit
    if (ghosttype == "Wraith"):
        return variables.Wraith
    if (ghosttype == "Yurei"):
        return variables.Yurei

# Parsing optional arguments (nargs)
parser = argparse.ArgumentParser(description='Shows ghost type depending on given evidences. \
    Available evidences: EMF Finger Freeze Writing Box Orb')
parser.add_argument('evi1', type=str, help='1. Evidence', nargs='?')
parser.add_argument('evi2', type=str, help='2. Evidence', nargs='?')
parser.add_argument('evi3', type=str, help='3. Evidence', nargs='?')
args = parser.parse_args()

# Phase 1
print ("-----------")
if args.evi1 is not None:
    print ("Possible evidences: " + str(variables.Evidences))
    print ("1st Evidence: " + args.evi1)
    Evidence1 = str(args.evi1)
else:
    print ("Possible evidences: " + str(variables.Evidences))
    print ("Enter 1. evidence:")
    Evidence1 = input()

for i in variables.Ghosts:
    if (Evidence1 in get_evidence_by_ghosttype(i)): # If the evidence matches the ghost's ones
        variables.Suspected_Type.append(i)
        print (i + " - " + str(get_evidence_by_ghosttype(i))) # Print the ghosttype + evidences of the ghost

# Phase 2
print ("-----------")
if args.evi2 is not None:
    print ("2nd Evidence: " + args.evi2)
    Evidence2 = str(args.evi2)
else:
    print ("Enter 2. evidence:")
    Evidence2 = input()

for i in variables.Suspected_Type:
    if (Evidence2 in get_evidence_by_ghosttype(i)): # If the evidence matches the ghost's ones
        variables.Suspected_Type2.append(i)
        print (i + " - " + str(get_evidence_by_ghosttype(i))) # Print the ghosttype + evidences of the ghost

# Phase 3
print ("-----------")
if args.evi3 is not None:
    print ("3rd Evidence: " + args.evi3)
    Evidence3 = str(args.evi3)
else:
    print ("Enter 3. evidence:")
    Evidence3 = input()

for i in variables.Suspected_Type2:
    if (Evidence3 in get_evidence_by_ghosttype(i)): # If the evidence matches the ghost's ones
        variables.Suspected_Type3.append(i)
        print (i + " - " + str(get_evidence_by_ghosttype(i))) # Print the ghosttype + evidences of the ghost
