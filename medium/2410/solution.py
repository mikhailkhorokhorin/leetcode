from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        res = 0
        playersIndex, trainersIndex = 0, 0

        while playersIndex < len(players) and trainersIndex < len(trainers):
            if players[playersIndex] <= trainers[trainersIndex]:
                res += 1
                playersIndex += 1
            trainersIndex += 1

        return res
