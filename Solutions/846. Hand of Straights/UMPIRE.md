1. Share questions you would ask to help understand the question:
- Do the numbers in each group have to increase by exactly one?
- Is the list sorted?
- Can groupSize be greater than the len of hand?
- If groupSize is equal to 1, is the answer always True?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Sorting

3. Write out in plain English what you want to do: 
- One check that can be done right away, is if the length of hand is not evenly divisible by groupSize
- So what I am thinking of, is since we need the groups to have consecutive cards, instead of using something like a hashmap or heap, what if the list was sorted?
- This way, the groups can be formed from left to right, and if there is a card that is not consecutive while building a group, then False can be returned right away
- After sorting, I will use a pointer that will loop through the list
- I will also use ints to hold the currGroupSize, an int to hold the first number skipped (if a number is equal to the previous, it can be used for the next group), and a boolean if it was skipped
- And to ensure that cards are not considered multiple times, they can be turned into -1 (inplace editing)
- If at any point the group cannot be build, return False

4. Translate each sub-problem into pseudocode:
- if the len of handsizes is not a multiple of groupsize, return False

- sort the hand array

- Initialize a card pointer to 1
- Initialize a skipped boolean to False
- Initialize a skippedCard int to 0 and currCardSize to 1 
- set currCand to hand[0]

- while card < len(hand) - 1:
  - if skipped: 
    - skipped = false
    - card = skippedCard
  - while currCardSize != groupSize:
    - if hand[card] == -1:
      - card += 1 
      - continue
    - if hand[card] == currCard =+ 1:
      - currCard = hand[card]
      - currCardSize += 1
      - card += 1
    - else if hand[card] == currCard:
      - skipped = True
      - skippedCard = card
      - while hand[card] != currCard:
        - card += 1
    - else if hand[card] > currCard + 1:
      - return False
  - currCardSize = 0

5. Translate the pseudocode into Python and share your final answer:
  <!--  class Solution:
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
          return True #The entire hand was traversed with no falses, return True  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that there are no additional data structures, with the most time complex part being the sorting. There are conditionals that can end the algorithm early once one group cannot be created
- One weak area is that I put this constraint that I did not want to introduce multiple data strucutres. I knew a heap would be very useful, but to iterate through it requires another data structure to hold duplicate numbers, since those don't want to be removed
  - In the goal of using no extra data strucutres and performing inplace edits on the hand to ignore used cards, the conditionals themselves make sense, but the logic within each one may be hard to follow without comments or me explaining the reasoning