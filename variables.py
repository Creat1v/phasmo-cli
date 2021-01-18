# Start Debug
Debug = 0

# Ghosts + Evidence Arrays
Evidences = ['EMF', 'Finger', 'Freeze', 'Writing', 'Box', 'Orb']

# bei dem Mapping ersparst du dir viel, da du die keys von dem dict dir rausholen kannst, somit hast du auch alle namen, und somit brauchst du keine extra Liste um dir die Namen vorzuhalten, und musst immer nur das Mapping und alle moeglichen Evidences pflegen
# stell dir das mapping so als key, value pair for wie in einer DB
mapping = {
  'Banshee' : ['EMF', 'Finger', 'Freeze'],
  'Demon' : ['Writing', 'Box', 'Freeze'],
  'Jinn' : ['EMF', 'Box', 'Orb'],
  'Mare' : ['Box', 'Orb', 'Freeze'],
  'Oni' : ['EMF', 'Writing', 'Box'],
  'Phantom' : ['EMF', 'Orb', 'Freeze'],
  'Poltergeist' : ['Box', 'Finger', 'Orb'],
  'Revenant' : ['EMF', 'Writing', 'Finger'],
  'Shade' : ['EMF', 'Writing', 'Orb'],
  'Spirit' : ['Writing', 'Box', 'Finger'],
  'Wraith' : ['Finger', 'Freeze', 'Box'],
  'Yurei' : ['Orb', 'Writing', 'Freeze']
}

Suspected_Type = []
Suspected_Type2 = []
Suspected_Type3 = []