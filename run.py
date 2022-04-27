from game import (
    NoughtsAndCrossesGame,
    NoughtsAndCrossesRandomPlayer,
)

if __name__ == "__main__":
    instance = NoughtsAndCrossesGame(
        NoughtsAndCrossesRandomPlayer(), NoughtsAndCrossesRandomPlayer()
    )
    results = [0, 0, 0]
    for i in range(10000):
        outcome = instance.play()
        results[outcome] += 1
    print(results)
