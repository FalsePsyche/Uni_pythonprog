"""Data Abstractions"""

from utils import mean

#############################
# Phase 1: Data Abstraction #
#############################


# Reviews

def make_review(restaurant_name, rating):
    """Return a review data abstraction."""
    return [restaurant_name, rating]

def review_restaurant_name(review):
    """Return the restaurant name of the review, which is a string."""
    return review[0]

def review_rating(review):
    """Return the number of stars given by the review, which is a
    floating point number between 1 and 5."""
    return review[1]


# Users

def make_user(name, reviews):
    """Return a user data abstraction."""
    return [name, {review_restaurant_name(r): r for r in reviews}]

def user_name(user):
    """Return the name of the user, which is a string."""
    return user[0]

def user_reviews(user):
    """Return a dictionary from restaurant names to reviews by the user."""
    return user[1]


### === +++ USER ABSTRACTION BARRIER +++ === ###

def user_reviewed_restaurants(user, restaurants):
    """Return the subset of restaurants reviewed by user.

    Arguments:
    user -- a user
    restaurants -- a list of restaurant data abstractions
    """
    names = list(user_reviews(user))
    return [r for r in restaurants if restaurant_name(r) in names]

def user_rating(user, restaurant_name):
    """Return the rating given for restaurant_name by user."""
    reviewed_by_user = user_reviews(user)
    user_review = reviewed_by_user[restaurant_name]
    return review_rating(user_review)


# Restaurants

def make_restaurant(name, location, categories, price, reviews):
    """Return a restaurant data abstraction."""
    # You may change this starter implementation however you wish, including
    # adding more items to the dictionary below.
    # BEGIN Question 1
    "*** REPLACE THIS LINE ***"
    # END Question 1
    return {
        'name': name,
        'location': location,
        'categories': categories,
        'price': price,
        'reviews': reviews,
    }

def restaurant_name(restaurant):
    """Return the name of the restaurant, which is a string."""
    return restaurant['name']

def restaurant_location(restaurant):
    """Return the location of the restaurant, which is a list containing
    latitude and longitude."""
    return restaurant['location']

def restaurant_categories(restaurant):
    """Return the categories of the restaurant, which is a list of strings."""
    return restaurant['categories']

def restaurant_price(restaurant):
    """Return the price of the restaurant, which is a number."""
    return restaurant['price']

def restaurant_ratings(restaurant):
    """Return a list of ratings, which are numbers from 1 to 5, of the
    restaurant based on the reviews of the restaurant.
    
    >>> soda_reviews = [make_review('Soda', 4.5), make_review('Soda', 4)]
    >>> soda = make_restaurant('Soda', [127.0, 0.1], ['Restaurants', 'Breakfast & Brunch'], 1, soda_reviews)
    >>> restaurant_ratings(soda)
    [4.5, 4]
"""
    # BEGIN Question 1
    return [item[1] for item in restaurant['reviews']]
    # END Question 1


### === +++ RESTAURANT ABSTRACTION BARRIER +++ === ###

def restaurant_num_ratings(restaurant):
    """Return the number of ratings for restaurant.
    >>> woz_reviews = [make_review('Wozniak Lounge', 4), make_review('Wozniak Lounge', 3),
    ...                make_review('Wozniak Lounge', 5)]
    >>> woz = make_restaurant('Wozniak Lounge', [127.0, 0.1], ['Restaurants', 'Pizza'], 1, woz_reviews)
    >>> restaurant_num_ratings(woz)
    3
    """
    # BEGIN Question 2
    return len(restaurant['reviews'])
    # END Question 2

def restaurant_mean_rating(restaurant):
    """Return the average rating for restaurant.
    >>> woz_reviews = [make_review('Wozniak Lounge', 4), make_review('Wozniak Lounge', 3),
    ...                make_review('Wozniak Lounge', 5)]
    >>> woz = make_restaurant('Wozniak Lounge', [127.0, 0.1], ['Restaurants', 'Pizza'], 1, woz_reviews)
    >>> restaurant_mean_rating(woz) # decimal value
    4.0
    """
    # BEGIN Question 2
    return mean(restaurant_ratings(restaurant))
    # END Question 2