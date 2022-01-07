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
def locate_card(cards, target_num):
    # implementaion 1: Linear Search 
    for idx, val in enumerate(cards):
        # reached end of the array did not find the element
        if idx == len(cards):
            return -1
        if val == target_num:
            return idx
        
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
    # def test3(self):
    #   self.assertTrue( 4 + 5 == 9)

if __name__ == '__main__':
   unittest.main()