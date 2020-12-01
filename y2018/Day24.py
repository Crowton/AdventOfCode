# Immune System:
# 337 units each with 6482 hit points (weak to radiation, fire; immune to cold, bludgeoning) with an attack that does 189 slashing damage at initiative 15
# 571 units each with 3178 hit points (weak to fire) with an attack that does 47 slashing damage at initiative 12
# 116 units each with 7940 hit points with an attack that does 638 fire damage at initiative 18
# 6017 units each with 9349 hit points (weak to cold) with an attack that does 14 cold damage at initiative 6
# 2246 units each with 4002 hit points (weak to radiation, slashing) with an attack that does 16 cold damage at initiative 3
# 3950 units each with 4493 hit points (weak to bludgeoning; immune to radiation, fire) with an attack that does 10 radiation damage at initiative 8
# 7494 units each with 1141 hit points (immune to bludgeoning) with an attack that does 1 cold damage at initiative 17
# 2501 units each with 9007 hit points with an attack that does 35 cold damage at initiative 7
# 844 units each with 3222 hit points (immune to bludgeoning, slashing) with an attack that does 37 radiation damage at initiative 9
# 1371 units each with 3695 hit points (immune to cold) with an attack that does 25 cold damage at initiative 10
#
# Infection:
# 2295 units each with 16577 hit points (immune to radiation) with an attack that does 12 fire damage at initiative 13
# 837 units each with 6736 hit points (weak to fire) with an attack that does 14 radiation damage at initiative 19
# 2841 units each with 9360 hit points (immune to bludgeoning; weak to radiation, cold) with an attack that does 6 fire damage at initiative 14
# 7374 units each with 51597 hit points (weak to cold; immune to bludgeoning, fire) with an attack that does 12 radiation damage at initiative 1
# 1544 units each with 29226 hit points (weak to fire, bludgeoning) with an attack that does 35 bludgeoning damage at initiative 5
# 293 units each with 13961 hit points (immune to slashing; weak to radiation) with an attack that does 79 radiation damage at initiative 2
# 1219 units each with 38142 hit points (immune to cold, fire) with an attack that does 53 bludgeoning damage at initiative 4
# 5233 units each with 30595 hit points (weak to bludgeoning, cold; immune to fire) with an attack that does 11 radiation damage at initiative 11
# 397 units each with 43710 hit points (weak to slashing, radiation; immune to cold, bludgeoning) with an attack that does 171 slashing damage at initiative 16
# 1316 units each with 36203 hit points (weak to slashing, bludgeoning) with an attack that does 50 cold damage at initiative 20


class Army:
    def __init__(self, t, units, hitspoints, weak, immune, attack, attacktype, initiative):
        self.t = t
        self.units = units
        self.hitspoints = hitspoints
        self.weak = weak
        self.immune = immune
        self.attack = attack
        self.attacktype = attacktype
        self.initiative = initiative

    def effect(self):
        return self.units * self.attack

    def damageDeltTo(self, other):
        if self.t == other.t:
            return -1

        if self.attacktype in other.immune:
            return 0
        if self.attacktype in other.weak:
            return 2 * self.effect()
        return self.effect()

    def takeDamage(self, d):
        self.units -= int(d / self.hitspoints)



imuneSystem = 0
infection = 1

# armies = [
#     Army(imuneSystem, 337, 6482, ['radiation', 'fire'], ['cold', 'bludgeoning'], 189, 'slashing', 15),
#     Army(imuneSystem, 571, 3178, ['fire'], [], 47, 'slashing', 12),
#     Army(imuneSystem, 116, 7940, [], [], 638, 'fire', 18),
#     Army(imuneSystem, 6017, 9349, ['cold'], [], 14, 'cold', 6),
#     Army(imuneSystem, 2246, 4002, ['radiation', 'slashing'], [], 16, 'cold', 3),
#     Army(imuneSystem, 3950, 4493, ['bludgeoning'], ['radiation', 'fire'], 10, 'radiation', 8),
#     Army(imuneSystem, 7494, 1141, [], ['bludgeoning'], 1, 'cold', 17),
#     Army(imuneSystem, 2501, 9007, [], [], 35, 'cold', 7),
#     Army(imuneSystem, 844, 3222, [], ['bludgeoning', 'slashing'],  37, 'radiation', 9),
#     Army(imuneSystem, 1371, 3695, [], ['cold'], 25, 'cold', 10),
#
#     Army(infection, 2295, 16577, [], ['radiation'], 12, 'fire', 13),
#     Army(infection, 837, 6736, ['fire'], [], 14, 'radiation', 19),
#     Army(infection, 2841, 9360, ['radiation', 'cold'], ['bludgeoning'], 6, 'fire', 14),
#     Army(infection, 7374, 51597, ['cold'], ['bludgeoning', 'fire'], 12, 'radiation', 1),
#     Army(infection, 1544, 29226, ['fire', 'bludgeoning'], [], 35, 'bludgeoning', 5),
#     Army(infection, 293, 13961, ['radiation'], ['slashing'], 79, 'radiation', 2),
#     Army(infection, 1219, 38142, [], ['cold', 'fire'], 53, 'bludgeoning', 4),
#     Army(infection, 5233, 30595, ['bludgeoning', 'cold'], ['fire'], 11, 'radiation', 11),
#     Army(infection, 397, 43710, ['cold', 'bludgeoning'], ['slashing', 'radiation'], 171, 'slashing', 16),
#     Army(infection, 1316, 36203, ['slashing', 'bludgeoning'], [], 50, 'cold', 20)
# ]

armies = [
    Army(imuneSystem, 17, 5390, ['radiation', 'bludgeoning'], [], 4507, 'fire', 2),
    Army(imuneSystem, 989, 1274, ['bludgeoning', 'slashing'], ['fire'], 25, 'slashing', 3),

    Army(infection, 801, 4706, ['radiation'], [], 116, 'bludgeoning', 1),
    Army(infection, 4485, 2961, ['fire', 'cold'], ['radiation'], 12, 'slashing', 4)
]

while True:
    types = [a.t for a in armies]
    typesSet = set()
    typesSet.update(types)
    if len(typesSet) <= 1:
        break

    for a in armies:
        print(a.t, a.units)
    print()

    attacks = {}
    beingAttacked = set()

    for a in sorted(armies, key=lambda a: (100/a.effect(), a.initiative)):
        considering = None
        damage = 1
        effect = -1
        initiative = -1
        for o in armies:
            if o not in beingAttacked:
                newdamage = a.damageDeltTo(o)
                neweffect = o.effect()
                if newdamage > damage or newdamage == damage and neweffect > effect or newdamage == damage and neweffect == effect and o.initiative > initiative:
                    damage = newdamage
                    effect = o.effect()
                    initiative = o.initiative
                    considering = o
        if considering is not None:
            beingAttacked.add(considering)
            attacks[a] = considering

    for a in sorted(attacks, key=lambda a: a.initiative):
        if a.units > 0:
            defender = attacks[a]
            damage = a.damageDeltTo(defender)
            defB = defender.units
            defender.takeDamage(damage)

            print(a.initiative, a.t, a.units, damage, 'Killing', defB - defender.units, 'units')
    print()

    armies2 = []
    for a in armies:
        if a.units > 0:
            armies2.append(a)
    armies = armies2

print(sum([a.units for a in armies]))

# 20936 too low
