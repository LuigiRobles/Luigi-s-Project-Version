#!/usr/bin/env python3
# Project 01 Unit Test
# Do not modify this file, for testing your functions

import unittest as unittest
import exSolution as exs

class TestReturnMethods(unittest.TestCase):

    # Unit Test: playerScore()
    def test_playerScore(self):

        # Get Point Dictionary from Function initPoints()
        points = exs.initPoints()

        # Validate Scores
        self.assertEqual(exs.playerScore('Hello',points), 8)
        self.assertEqual(exs.playerScore('World',points), 9)
        self.assertEqual(exs.playerScore('Zebra',points), 16)
        self.assertEqual(exs.playerScore('Hello World',points), 17)


    # Unit Test: validWord()
    def test_validWord(self):

        # Get Players Dictionary from Function initPlayers()
        players = exs.initPlayers()

        # Invalid Entry: No Entry Made
        self.assertFalse(exs.validWord('','',players), True)

        # Valid Entry: Initial Value Entered
        self.assertTrue(exs.validWord('Hello','',players), True)

        # Valid Entry
        self.assertTrue(exs.validWord('Hello','World',players), True)
        players['player1'].append("Hello")
        players['player2'].append("World")

        # Invalid Entry: Same Word Repeated
        self.assertTrue(exs.validWord('Hello','hello',players), False)

        # Invalid Entry: No Characters in Common
        self.assertFalse(exs.validWord('Bad','Wolf',players), True)

        # Valid Entry
        self.assertTrue(exs.validWord('Dictionary','Picture',players), True)
        players['player1'].append("Dictionary")
        players['player2'].append("Picture")

        # Valid Player Lists
        self.assertEqual(players['player1'], ['Hello','Dictionary'], True)
        self.assertEqual(players['player2'], ['World','Picture'], True)


    # Unit Test: Dictionary Replacement
    def test_dictReplace(self):
        # Get Players Dictionary
        messages = exs.initMessages()

        # Message 0
        self.assertEqual(messages[0] % {'nbr':1,'scr':20}, 'Player 1 Wins with a score of 20!', True)
        # Message 1
        self.assertEqual(messages[1], 'Tie Game, no winners.', True)
        # Message 2
        self.assertEqual(messages[2] % {'nbr':2}, 'Invalid word! Player 2 Wins!', True)
        # Message 3
        self.assertEqual(messages[3], 'Invalid word! You must enter a valid word to start.', True)
        # Message 4
        self.assertEqual(messages[4] % {'nbr':1}, 'Player 1 Entered the Words:', True)


if __name__ == '__main__':
    unittest.main() 
