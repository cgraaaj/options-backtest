import csv
import datetime

trades2020 = [
    {'expiry': datetime.date(2020, 1, 2), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 37.15, 'pl': 37.05}, {'expiry': datetime.date(2020, 1, 2), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 40.05, 'pl': 39.849999999999994}, {'expiry': datetime.date(2020, 1, 9), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 33.35, 'pl': 33.25}, {'expiry': datetime.date(2020, 1, 9), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 47.35, 'pl': 47.25}, {'expiry': datetime.date(2020, 1, 16), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 45.0, 'pl': 44.95}, {'expiry': datetime.date(2020, 1, 16), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 40.75, 'pl': 40.65}, {'expiry': datetime.date(2020, 2, 6), 'type': 'ce', 'boughtAt': 113.0, 'soldAt': 35.0, 'pl': -78.0}, {'expiry': datetime.date(2020, 2, 6), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 46.8, 'pl': 46.65}, {'expiry': datetime.date(2020, 2, 13), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 47.95, 'pl': 47.85}, {'expiry': datetime.date(2020, 2, 13), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 35.6, 'pl': 35.550000000000004}, {'expiry': datetime.date(2020, 2, 20), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 46.9, 'pl': 46.85}, {'expiry': datetime.date(2020, 2, 20), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 43.25, 'pl': 43.2}, {'expiry': datetime.date(2020, 2, 27), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 40.85, 'pl': 40.75}, {'expiry': datetime.date(2020, 2, 27), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 43.45, 'pl': 43.25}, {'expiry': datetime.date(2020, 3, 5), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 47.95, 'pl': 47.85}, {'expiry': datetime.date(2020, 3, 5), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 40.25, 'pl': 40.2}, {'expiry': datetime.date(2020, 3, 19), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 43.85, 'pl': 43.75}, {'expiry': datetime.date(2020, 3, 19), 'type': 'pe', 'boughtAt': 5.95, 'soldAt': 40.25, 'pl': 34.3}, {'expiry': datetime.date(2020, 3, 26), 'type': 'ce', 'boughtAt': 0.25, 'soldAt': 40.0, 'pl': 39.75}, {'expiry': datetime.date(2020, 4, 9), 'type': 'ce', 'boughtAt': 1291.6, 'soldAt': 40.0, 'pl': -1251.6}, {'expiry': datetime.date(2020, 4, 9), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 32.6, 'pl': 32.5}, {'expiry': datetime.date(2020, 4, 23), 'type': 'ce', 'boughtAt': 0.2, 'soldAt': 35.0, 'pl': 34.8}, {'expiry': datetime.date(2020, 4, 23), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 40.5, 'pl': 40.45}, {'expiry': datetime.date(2020, 4, 30), 'type': 'ce', 'boughtAt': 0.7, 'soldAt': 48.35, 'pl': 47.65}, {'expiry': datetime.date(2020, 4, 30), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 42.4, 'pl': 42.3}, {'expiry': datetime.date(2020, 5, 7), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 31.35, 'pl': 31.25}, {'expiry': datetime.date(2020, 5, 7), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 36.65, 'pl': 36.55}, {'expiry': datetime.date(2020, 5, 14), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 41.75, 'pl': 41.65}, {'expiry': datetime.date(2020, 5, 14), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 37.45, 'pl': 37.400000000000006}, {'expiry': datetime.date(2020, 5, 21), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 50.0, 'pl': 49.95}, {'expiry': datetime.date(2020, 5, 21), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 50.0, 'pl': 49.9}, {'expiry': datetime.date(2020, 5, 28), 'type': 'ce', 'boughtAt': 1564.9, 'soldAt': 50.0, 'pl': -1514.9}, {'expiry': datetime.date(2020, 5, 28), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 50.0, 'pl': 49.9}, {'expiry': datetime.date(2020, 6, 4), 'type': 'ce', 'boughtAt': 0.45, 'soldAt': 45.4, 'pl': 44.949999999999996}, {'expiry': datetime.date(2020, 6, 4), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 48.8, 'pl': 48.65}, {'expiry': datetime.date(2020, 6, 11), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 43.95, 'pl': 43.85}, {'expiry': datetime.date(2020, 6, 11), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 46.35, 'pl': 46.25}, {'expiry': datetime.date(2020, 6, 18), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 44.0, 'pl': 43.9}, {'expiry': datetime.date(2020, 6, 18), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 48.0, 'pl': 47.8}, {'expiry': datetime.date(2020, 6, 25), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 46.7, 'pl': 46.550000000000004}, {'expiry': datetime.date(2020, 6, 25), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 38.45, 'pl': 38.300000000000004}, {'expiry': datetime.date(2020, 7, 2), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 30.8, 'pl': 30.7}, {'expiry': datetime.date(2020, 7, 2), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 45.25, 'pl': 45.15}, {'expiry': datetime.date(2020, 7, 9), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 34.8, 'pl': 34.699999999999996}, {'expiry': datetime.date(2020, 7, 9), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 36.6, 'pl': 36.5}, {'expiry': datetime.date(2020, 7, 16), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 45.05, 'pl': 44.949999999999996}, {'expiry': datetime.date(2020, 7, 16), 'type': 'pe', 'boughtAt': 0.3, 'soldAt': 47.5, 'pl': 47.2}, {'expiry': datetime.date(2020, 7, 23), 'type': 'ce', 'boughtAt': 0.2, 'soldAt': 45.75, 'pl': 45.55}, {'expiry': datetime.date(2020, 7, 23), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 46.55, 'pl': 46.4}, {'expiry': datetime.date(2020, 7, 30), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 43.25, 'pl': 43.15}, {'expiry': datetime.date(2020, 7, 30), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 40.25, 'pl': 40.05}, {'expiry': datetime.date(2020, 8, 6), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 40.0, 'pl': 39.95}, {'expiry': datetime.date(2020, 8, 6), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 41.15, 'pl': 41.05}, {'expiry': datetime.date(2020, 8, 13), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 48.55, 'pl': 48.4}, {'expiry': datetime.date(2020, 8, 13), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 41.35, 'pl': 41.25}, {'expiry': datetime.date(2020, 8, 20), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 44.0, 'pl': 43.85}, {'expiry': datetime.date(2020, 8, 20), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 44.9, 'pl': 44.8}, {'expiry': datetime.date(2020, 8, 27), 'type': 'ce', 'boughtAt': 413.25, 'soldAt': 42.7, 'pl': -370.55}, {'expiry': datetime.date(2020, 8, 27), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 49.75, 'pl': 49.6}, {'expiry': datetime.date(2020, 9, 3), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 41.75, 'pl': 41.65}, {'expiry': datetime.date(2020, 9, 3), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 40.0, 'pl': 39.9}, {'expiry': datetime.date(2020, 9, 10), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 40.0, 'pl': 39.85}, {'expiry': datetime.date(2020, 9, 10), 'type': 'pe', 'boughtAt': 0.25, 'soldAt': 45.85, 'pl': 45.6}, {'expiry': datetime.date(2020, 9, 17), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 48.35, 'pl': 48.25}, {'expiry': datetime.date(2020, 9, 17), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 43.05, 'pl': 42.949999999999996}, {'expiry': datetime.date(2020, 9, 24), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 45.2, 'pl': 45.050000000000004}, {'expiry': datetime.date(2020, 9, 24), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 44.05, 'pl': 43.849999999999994}, {'expiry': datetime.date(2020, 10, 1), 'type': 'ce', 'boughtAt': 51.35, 'soldAt': 38.65, 'pl': -12.700000000000003}, {'expiry': datetime.date(2020, 10, 1), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 50.0, 'pl': 49.8}, {'expiry': datetime.date(2020, 10, 8), 'type': 'ce', 'boughtAt': 0.3, 'soldAt': 48.0, 'pl': 47.7}, {'expiry': datetime.date(2020, 10, 8), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 49.6, 'pl': 49.45}, {'expiry': datetime.date(2020, 10, 15), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 44.15, 'pl': 44.0}, {'expiry': datetime.date(2020, 10, 15), 'type': 'pe', 'boughtAt': 0.3, 'soldAt': 50.0, 'pl': 49.7}, {'expiry': datetime.date(2020, 10, 22), 'type': 'ce', 'boughtAt': 0.25, 'soldAt': 46.55, 'pl': 46.3}, {'expiry': datetime.date(2020, 10, 22), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 46.65, 'pl': 46.5}, {'expiry': datetime.date(2020, 10, 29), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 50.0, 'pl': 49.85}, {'expiry': datetime.date(2020, 10, 29), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 34.25, 'pl': 34.1}, {'expiry': datetime.date(2020, 11, 5), 'type': 'ce', 'boughtAt': 289.4, 'soldAt': 30.0, 'pl': -259.4}, {'expiry': datetime.date(2020, 11, 5), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 38.45, 'pl': 38.400000000000006}, {'expiry': datetime.date(2020, 11, 12), 'type': 'ce', 'boughtAt': 0.35, 'soldAt': 41.3, 'pl': 40.949999999999996}, {'expiry': datetime.date(2020, 11, 12), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 41.8, 'pl': 41.699999999999996}, {'expiry': datetime.date(2020, 11, 19), 'type': 'ce', 'boughtAt': 17.45, 'soldAt': 41.3, 'pl': 23.849999999999998}, {'expiry': datetime.date(2020, 11, 19), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 48.35, 'pl': 48.25}, {'expiry': datetime.date(2020, 11, 26), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 49.0, 'pl': 48.85}, {'expiry': datetime.date(2020, 11, 26), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 40.4, 'pl': 40.25}, {'expiry': datetime.date(2020, 12, 3), 'type': 'ce', 'boughtAt': 0.4, 'soldAt': 49.0, 'pl': 48.6}, {'expiry': datetime.date(2020, 12, 3), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 45.5, 'pl': 45.3}, {'expiry': datetime.date(2020, 12, 10), 'type': 'ce', 'boughtAt': 0.3, 'soldAt': 49.95, 'pl': 49.650000000000006}, {'expiry': datetime.date(2020, 12, 10), 'type': 'pe', 'boughtAt': 0.25, 'soldAt': 44.25, 'pl': 44.0}, {'expiry': datetime.date(2020, 12, 17), 'type': 'ce', 'boughtAt': 0.2, 'soldAt': 44.2, 'pl': 44.0}, {'expiry': datetime.date(2020, 12, 17), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 44.95, 'pl': 44.75}, {'expiry': datetime.date(2020, 12, 24), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 30.2, 'pl': 30.05}, {'expiry': datetime.date(2020, 12, 24), 'type': 'pe', 'boughtAt': 0.2, 'soldAt': 40.0, 'pl': 39.8}, {'expiry': datetime.date(2020, 12, 31), 'type': 'ce', 'boughtAt': 0.3, 'soldAt': 41.15, 'pl': 40.85}, {'expiry': datetime.date(2020, 12, 31), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 50.0, 'pl': 49.85}
]
trades = [{'expiry': datetime.date(2018, 1, 4), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 50.0, 'pl': 49.95}, {'expiry': datetime.date(2018, 1, 4), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 31.8, 'pl': 31.75}, {'expiry': datetime.date(2018, 1, 11), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 34.8, 'pl': 34.75}, {'expiry': datetime.date(2018, 1, 11), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 42.55, 'pl': 42.449999999999996}, {'expiry': datetime.date(2018, 1, 18), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 34.8, 'pl': 34.75}, {'expiry': datetime.date(2018, 1, 18), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 35.95, 'pl': 35.900000000000006}, {'expiry': datetime.date(2018, 2, 1), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 45.0, 'pl': 44.95}, {'expiry': datetime.date(2018, 2, 1), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 45.0, 'pl': 44.9}, {'expiry': datetime.date(2018, 2, 22), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 40.6, 'pl': 40.5}, {'expiry': datetime.date(2018, 2, 22), 'type': 'pe', 'boughtAt': 0.15, 'soldAt': 35.2, 'pl': 35.050000000000004}, {'expiry': datetime.date(2018, 3, 1), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 35.0, 'pl': 34.95}, {'expiry': datetime.date(2018, 3, 1), 'type': 'pe', 'boughtAt': 259.35, 'soldAt': 43.95, 'pl': -215.40000000000003}, {'expiry': datetime.date(2018, 3, 8), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 44.95, 'pl': 44.900000000000006}, {'expiry': datetime.date(2018, 3, 8), 'type': 'pe', 'boughtAt': 0.85, 'soldAt': 43.0, 'pl': 42.15}, {'expiry': datetime.date(2018, 3, 15), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 39.9, 'pl': 39.8}, {'expiry': datetime.date(2018, 3, 15), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 38.7, 'pl': 38.650000000000006}, {'expiry': datetime.date(2018, 3, 28), 'type': 'ce', 'boughtAt': 463.05, 'soldAt': 39.9, 'pl': -423.15000000000003}, {'expiry': datetime.date(2018, 3, 28), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 48.8, 'pl': 48.699999999999996}, {'expiry': datetime.date(2018, 4, 12), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 33.0, 'pl': 32.95}, {'expiry': datetime.date(2018, 4, 12), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 31.55, 'pl': 31.5}, {'expiry': datetime.date(2018, 4, 19), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 38.0, 'pl': 37.95}, {'expiry': datetime.date(2018, 4, 19), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 50.0, 'pl': 49.9}, {'expiry': datetime.date(2018, 5, 10), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 38.0, 'pl': 37.95}, {'expiry': datetime.date(2018, 5, 10), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 42.6, 'pl': 42.550000000000004}, {'expiry': datetime.date(2018, 5, 24), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 38.4, 'pl': 38.35}, {'expiry': datetime.date(2018, 5, 24), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 33.1, 'pl': 33.050000000000004}, {'expiry': datetime.date(2018, 5, 31), 'type': 'ce', 'boughtAt': 158.0, 'soldAt': 43.4, 'pl': -114.6}, {'expiry': datetime.date(2018, 5, 31), 'type': 'pe', 'boughtAt': 0.3, 'soldAt': 35.0, 'pl': 34.7}, {'expiry': datetime.date(2018, 6, 7), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 39.95, 'pl': 39.900000000000006}, {'expiry': datetime.date(2018, 6, 7), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 30.0, 'pl': 29.95}, {'expiry': datetime.date(2018, 6, 14), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 44.9, 'pl': 44.85}, {'expiry': datetime.date(2018, 6, 14), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 39.7, 'pl': 39.650000000000006}, {'expiry': datetime.date(2018, 6, 28), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 33.4, 'pl': 33.25}, {'expiry': datetime.date(2018, 6, 28), 'type': 'pe', 'boughtAt': 0.85, 'soldAt': 49.95, 'pl': 49.1}, {'expiry': datetime.date(2018, 7, 5), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 35.4, 'pl': 35.3}, {'expiry': datetime.date(2018, 7, 5), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 42.75, 'pl': 42.7}, {'expiry': datetime.date(2018, 8, 2), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 34.65, 'pl': 34.6}, {'expiry': datetime.date(2018, 8, 2), 'type': 'pe', 'boughtAt': 39.5, 'soldAt': 35.35, 'pl': -4.149999999999999}, {'expiry': datetime.date(2018, 8, 9), 'type': 'ce', 'boughtAt': 100.7, 'soldAt': 36.8, 'pl': -63.900000000000006}, {'expiry': datetime.date(2018, 8, 9), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 47.55, 'pl': 47.449999999999996}, {'expiry': datetime.date(2018, 8, 16), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 30.45, 'pl': 30.4}, {'expiry': datetime.date(2018, 8, 16), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 35.6, 'pl': 35.5}, {'expiry': datetime.date(2018, 8, 23), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 32.3, 'pl': 32.25}, {'expiry': datetime.date(2018, 8, 23), 'type': 'pe', 'boughtAt': 2.15, 'soldAt': 44.85, 'pl': 42.7}, {'expiry': datetime.date(2018, 8, 30), 'type': 'ce', 'boughtAt': 0.15, 'soldAt': 40.0, 'pl': 39.85}, {'expiry': datetime.date(2018, 8, 30), 'type': 'pe', 'boughtAt': 10.7, 'soldAt': 48.75, 'pl': 38.05}, {'expiry': datetime.date(2018, 9, 19), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 40.0, 'pl': 39.9}, {'expiry': datetime.date(2018, 9, 19), 'type': 'pe', 'boughtAt': 202.25, 'soldAt': 44.65, 'pl': -157.6}, {'expiry': datetime.date(2018, 10, 11), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 41.7, 'pl': 41.6}, {'expiry': datetime.date(2018, 11, 1), 'type': 'ce', 'boughtAt': 13.2, 'soldAt': 49.9, 'pl': 36.7}, {'expiry': datetime.date(2018, 11, 1), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 42.0, 'pl': 41.95}, {'expiry': datetime.date(2018, 11, 22), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 42.9, 'pl': 42.85}, {'expiry': datetime.date(2018, 11, 22), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 42.05, 'pl': 41.949999999999996}, {'expiry': datetime.date(2018, 11, 29), 'type': 'ce', 'boughtAt': 305.85, 'soldAt': 47.4, 'pl': -258.45000000000005}, {'expiry': datetime.date(2018, 11, 29), 'type': 'pe', 'boughtAt': 0.1, 'soldAt': 38.95, 'pl': 38.85}, {'expiry': datetime.date(2018, 12, 6), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 39.0, 'pl': 38.95}, {'expiry': datetime.date(2018, 12, 6), 'type': 'pe', 'boughtAt': 98.05, 'soldAt': 42.0, 'pl': -56.05}, {'expiry': datetime.date(2018, 12, 13), 'type': 'ce', 'boughtAt': 0.1, 'soldAt': 50.0, 'pl': 49.9}, {'expiry': datetime.date(2018, 12, 13), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 44.85, 'pl': 44.800000000000004}, {'expiry': datetime.date(2018, 12, 20), 'type': 'ce', 'boughtAt': 0.05, 'soldAt': 48.25, 'pl': 48.2}, {'expiry': datetime.date(2018, 12, 20), 'type': 'pe', 'boughtAt': 0.05, 'soldAt': 49.85, 'pl': 49.800000000000004}]

profitTrades = [trade for trade in trades if trade['pl'] > 0]

lossTrades = [trade for trade in trades if trade['pl'] < 0]

print(profitTrades)
print(lossTrades)

pkeys = profitTrades[0].keys()
lkeys = lossTrades[0].keys()


with open('Profit2020.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, pkeys)
    dict_writer.writeheader()
    dict_writer.writerows(profitTrades)

with open('Loss2020.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, lkeys)
    dict_writer.writeheader()
    dict_writer.writerows(lossTrades)
