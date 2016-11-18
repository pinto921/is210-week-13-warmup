#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" a program to be able to open and read a csv file found on the local filesystem"""

import json
import csv

GRADES = {'A': float(1.00),
          'B': float(0.90),
          'C': float(0.80),
          'D': float(0.70),
          'F': float(0.60)}

def get_score_summary(filename):
    """ a function that takes a filename as a string and returns a summarized version of the data

        Args:
            filename(names = strings): csv file read by function

        Return:
            average_cal: in charge of calculating average

        example:
            >>> get_score_summary('marcel.csv')
            {'NEW YORK': (1, 0.9), 'QUEENS': (4, 1.0)}
        """
    boro_count = {}
    dictionary = {}
    average_cal = {}

    try:
        with open(filename, 'r') as search:
            library = searcher.reader(search)

            for files in library

            camis, borough, grades = (items[0], items[1], items[10])

            if camis not in dictionary and grade in GRADES:
                dictionary[camis] = [grade, borough]
    except IOError as eror:
        print (error, 'Error: file not found')

    for files in dictionary.values()
    row_k = items[0]
    row_b = items[1]

    if row_b not in boro_count:
        boro_count[row_b] = [1, GRADES[1, Grades[row_k]]
    else:
        boro_count[row_b][0] +=1
        boro_count[row_b][1] += GRADES[row_k]

    for row_b, value in boro_count.iteritems():

        val = value[0]
        val2= value[1] / value[0]
        average_cal[row_b] = val, val2

    return average_cal

def get_market_density(val):
    """ market density function

        Args:
            json file for var

        Returns:
            dictionary for boroughs

        example:
            >>> get_market_density('green_markets.json')
            {u'Bronx': 32, u'brooklyn': 48, u'Staten Island': 2,
            u'MAnhattan': 39, u'Queens':16}
        """

        market = {}

        with open(val, 'r') as get_jason:
        json = json1(search_json)
        for files in json['data']:
        identi = files[8]
        identi = identi.upper().rstrip()

        if identi in market[identi] += 1

    return market

def correlate_data(csv_filename, json_filename, result_filename)
    """ extra data

        Args:
            csv_filename: scores

        Returns:
            json file

        Example:
        >>> {'BRONX': (0.9762820512820514, 0.1987179487179487)}
    """
    food_result = search_result(csv_filename)

    markets = search_market_densityresult(json_filename)

    payment= {}

    for score infood_result:
        density = {score: (food_result[score][1],
                           float(markets[score]) /
                           float(food_result[score][0]))}

        payment = dict(payment.items() + density.items())

    with open(result, 'w') as outfile:
        json(payment, files)

    return payment 
        
            

    
