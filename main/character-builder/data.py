races = ['elf', 'dwarf', 'human', 'halfing']
classes = ['fighter', 'rogue', 'wizard', 'ranger']

stats = ['str', 'dex', 'con', 'cha', 'int', 'wis']

starting_kits = {
  'fighter': [{'weapon': 'short sword', 'armor': 'chain mail'}, {'weapon': 'bow', 'armor': 'leather'}],
  'rogue': [{'weapon': 'dagger', 'armor': 'leather'}, {'weapon': 'crossbow', 'armor': 'padded'}],
  'wizard': [{'weapon': 'staff', 'armor': 'none'}, {'weapon': 'darts', 'armor': 'none'}],
  'ranger': [{'weapon': 'spear', 'armor': 'scale mail'}, {'weapon': 'bow', 'armor': 'leather'}],
}

armor_class = {'leather': '2', 'chain mail': '6', 'padded': '4', 'scale mail': '5', 'none': '0' }
weapon_damage = {'short sword': '1d8', 'bow': '1d6', 'dagger': '1d4', 'crossbow': '1d6', 'staff': '1d4', 'darts': '1d4', 'spear': '1d6'}