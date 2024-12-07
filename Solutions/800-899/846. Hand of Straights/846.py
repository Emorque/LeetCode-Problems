from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        card = 0
        skipped = False
        skippedCard = 0
        currSize = 0
        currCard = hand[0] - 1

        while card < len(hand):
            if currSize == 0: #If the group is 0, start from with the current card
                currCard = hand[card]
                card += 1
                currSize = 1
                continue
            if currSize == groupSize: # if the group is filled, reset group to 0 and move card back to skipped if a card was skipped
                currSize = 0
                if skipped:
                    skipped = False
                    card = skippedCard   
            elif hand[card] == -1: # cards already in a group are converted to -1, so skip those if they are seen
                card += 1
            elif hand[card] == currCard + 1: # a consecutive card is found
                currCard = hand[card]
                hand[card] = -1
                currSize += 1
                card += 1
            elif hand[card] == currCard: # a duplicate card was found, skip it. For first skip in the current group, set skippedCard to the current card before skipping. For consecutive skips, just skip
                if not skipped:
                    skipped = True
                    skippedCard = card
                while hand[card] == currCard and card != len(hand) - 1: 
                    card += 1
                if card == len(hand) - 1: #if the card reaches in the end in the instance, then there is no consecutive card in the hand, return False
                    return False
            elif hand[card] > currCard + 1: # a non consecutive card was found, return False
                return False         
        return True #The entire hand was traversed with no falses, return True