with open("Day22.in") as f:
    players = f.read().split("\n\n")
    player1 = list(map(int, players[0].split("\n")[1:]))
    player2 = list(map(int, players[1].split("\n")[1:]))

player1Copy = player1.copy()
player2Copy = player2.copy()

# Part 1
while player1 and player2:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)

winner = max(player1, player2, key=lambda t: len(t))
print(sum((len(winner) - i) * c for i, c in enumerate(winner)))


# Part 2
def playRec(player1, player2, isSub=True):
    if isSub and max(player1 + player2) in player1:
        return 1, []

    seen = set()

    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if state in seen:
            return 1, player1
        seen.add(state)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            winner, _ = playRec(player1[:card1], player2[:card2])
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    return (1, player1) if player1 else (2, player2)


_, winnerDeck = playRec(player1Copy, player2Copy, isSub=False)
print(sum((len(winnerDeck) - i) * c for i, c in enumerate(winnerDeck)))
