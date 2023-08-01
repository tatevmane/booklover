#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:06:32 2023

@author: tatevgomtsyan
"""

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        person = BookLover('Tatev','tmg6jda@virginia.edu','Novel')
        person.add_book('The Alchemist', 5)
        self.assertTrue(person.has_read('The Alchemist'))
    def test_2_add_book(self):
        person = BookLover('Tatev','tmg6jda@virginia.edu','Novel')
        person.add_book('The Alchemist', 5)  
        person.add_book('The Alchemist', 5)                
        book_count = len(person.book_list['book_name'])  
        self.assertEqual(book_count, 1)            
    def test_3_has_read(self): 
        person = BookLover('Tatev','tmg6jda@virginia.edu','Novel')
        person.add_book('Kite Runner', 3)
        self.assertTrue(person.has_read('Kite Runner'))
    def test_4_has_read(self): 
        person = BookLover('Tatev','tmg6jda@virginia.edu','Novel')
        self.assertFalse(person.has_read(''))
    def test_5_num_books_read(self): 
        person = BookLover('Tatev','tmg6jda@virginia.edu','Novel')
        person.add_book('1984', 3)
        person.add_book('The Great Gatsby', 4)
        person.add_book('Pride and Prejudice', 5)
        self.assertEqual(person.num_books_read(), 3)
    def test_6_fav_books(self):
        person = BookLover('Tatev','tmg6jda@virginia.edu','Novel')
        person.add_book('1984', 3)
        person.add_book('The Great Gatsby', 4)
        person.add_book('Pride and Prejudice', 5)
        person.add_book('The Scarlet Letter', 1) 
        fav_books = person.fav_books()
        self.assertTrue((fav_books['book_rating'] > 3).all())
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(BookLoverTestSuite))

    with open('booklover_results.txt', 'w') as file:
        runner = unittest.TextTestRunner(stream=file, verbosity=2)
        test_results = runner.run(test_suite)
    