"""
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""

# description:
"""
no. of cards can be represtented as list of numbers, in decreasing order  
bob needs to find the pos of the card containing a given num( target)

assuming :
cards = [7,6,5,4,3,2,1]
target_num = 4
pos = 3   --> o/p
"""
# Signature
# def locate_card(cards, target_num):
#     # lets introduce 2 more variable hi and lo 
#     lo, hi = 0, len(cards) -1

#     while lo <= hi:
#         mid = (lo+hi) //2

#         mid_number = cards[mid]

#         print("lo: ", lo, "hi: ", hi, "mid: ", mid_number)
#         if mid_number == target_num:
#             return mid
        
#         elif mid_number < target_num:
#             hi = mid-1
        
#         elif mid_number > target_num:
#             lo = mid+1
#     return -1        

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1



# lets come up with inputs and outputs to cover edge cases 
"""
test cases: for target 4
list containing non repeating numbers [7,6,5,4,3,2,1]
list containing repeating numbers 'cards': [7,7,6,6,6,5,5,4,4,3,2,1,1,1,1,1,1]
list containing no target num in cards [7,6,5,3,2,1], return -1
list is empty with elements 'cards': [] 

"""
test = [
    {'input': { 
        'cards':  [], 
        'target': 4
    },
    'output': -1 } ,

    {'input': { 
        'cards':  [7,6,5,4,3,2,1], 
        'target': 4
    },
    'output': 3
},
    {'input': { 
        'cards':  [7,7,6,6,6,5,5,4,4,3,2,1,1,1,1,1,1], 
        'target': 4
    },
    'output': 7 },

    {'input': { 
        'cards':  [7,6,5,3,2,1], 
        'target': 4
    },
    'output': -1 }

]


import unittest


class SimpleTest(unittest.TestCase):
    def test1(self):
      self.assertEqual( locate_card(test[0]['input']['cards'], 4 ), test[0]['output'] )
    def test2(self):
      self.assertEqual( locate_card(test[1]['input']['cards'], 4 ), test[1]['output'] )
    def test3(self):
      self.assertEqual( locate_card(test[2]['input']['cards'], 4 ), test[2]['output'] )
    def test4(self):
      self.assertEqual( locate_card(test[3]['input']['cards'], 4 ), test[3]['output'] )

if __name__ == '__main__':
   unittest.main()