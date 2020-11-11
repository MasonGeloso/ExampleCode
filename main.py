from random import randint


def playGameOfDice(playerName):
    """Plays a game of dice which the first to 5 wins

    Args:
        playerName (str): The name of the player

    Returns:
        str: The winner of the game
    """

    winner = False
    playerScore = 0
    computerScore = 0


    while not winner:
        continued = input('Press Enter to Roll:')

        playerRoll = randint(1, 6)
        computerRole = randint(1, 6)

        if playerRoll > computerRole:
            playerScore += 1
            print(f'{playerName} won!\n{playerName}: {playerScore}\nComputer: {computerScore}')
        elif playerRoll == computerRole:
            computerScore += 1
            print(f'Computer won!\n{playerName}: {playerScore}\nComputer: {computerScore}')
        else:
            computerScore += 1
            print(f'It\'s a draw! But the computer wins!\n{playerName}: {playerScore}\nComputer: {computerScore}')


        if playerScore == 5:
            winner = playerName
        elif computerScore == 5:
            winner = 'Computer'
        else:
            continue

    return winner


print(
    f"{playGameOfDice(input('What is your name: '))} won the game!"
    )



