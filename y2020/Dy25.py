generator = 7
modulus = 20201227

cardKey = 17115212
doorKey = 3667832

cardTempKey = 1
doorTempKey = 1
theSecretKey = 0

while cardTempKey != cardKey and doorTempKey != doorKey:
    cardTempKey = (cardTempKey * generator) % modulus
    doorTempKey = (doorTempKey * generator) % modulus
    theSecretKey += 1

key = doorKey if cardTempKey == cardKey else cardKey
secretKey = pow(key, theSecretKey, modulus)
print(secretKey)
