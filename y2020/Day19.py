with open("Day19.in") as f:
    rules, strings = f.read().split("\n\n")

    ruleParsed = {}
    for rule in rules.split("\n"):
        number, requirements = rule.split(": ")
        if requirements[0] == '"':
            ruleParsed[number] = requirements[1:-1]
        else:
            ruleParsed[number] = [d.split(" ") for d in requirements.split(" | ")]

    strings = strings.split("\n")


# Part 1
import itertools
gotResult = {}
def getMatches(ruleNumber):
    data = ruleParsed[ruleNumber]
    if isinstance(data, str):
        return {data}

    if ruleNumber in gotResult:
        return gotResult[ruleNumber]

    result = set()
    for order in data:
        subParts = [getMatches(o) for o in order]
        result.update("".join(e) for e in itertools.product(*subParts))

    gotResult[ruleNumber] = result
    return result


validZero = getMatches("0")
print(sum(s in validZero for s in strings))


# Part 2
from pyformlang.cfg import Production, Variable, Terminal, CFG
vars = {k: Variable(k) for k in ruleParsed}
terminals = set()
prods = set()
ruleParsed["8"] = [["42"], ["42", "8"]]
ruleParsed["11"] = [["42", "31"], ["42", "11", "31"]]
for num, data in ruleParsed.items():
    if isinstance(data, str):
        ter = Terminal(data)
        terminals.add(ter)
        prods.add(Production(vars[num], [ter]))
    else:
        for order in data:
            prods.add(Production(vars[num], [vars[n] for n in order]))
cfg = CFG(set(), terminals, vars["0"], prods)
print(sum(cfg.contains(s) for s in strings))
