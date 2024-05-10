import requests
import bs4
#requests1 = requests.get("https://flipkart.com/poco-c31-royal-blue-64-gb-/p/itm19effae969b86")
requests1 = requests.get("https://www.amazon.in/Apple-MacBook-Chip-13-inch256GB/dp/B08N5W4NNB/ref=sr_1_1?crid=1J2JI0HJBX9JV&keywords=macbook+air+m1&qid=1
680253105&sprefix=macbook+air+m%2Caps%2C229&sr=8-1")
print("REQUEST 1 = \n", requests1 , "\n")
print("CONTENTS OF REQUEST 1 = \n", requests1.content , "\n")
soup = bs4.BeautifulSoup(requests1.text)
print(soup)
#reviews = soup.find_all( 'div' , { 'class' : 't-ZTKy'}); # or findAll
reviews = soup.find_all( 'div' , { 'class' : 'a-expander-content reviewText review-text-content aexpander-partial-collapse-content'}); # or findAll
print(reviews)
# lets extract on by one a review from the above reviews
# the avove is list of reviews as we have used find_all()
count = 1
for review in reviews :
 print("\nFETCHING REVIEW" , str(count), "\n")
 print(review.get_text() , "\n\n")
 count = count + 1
# lets make it more redable
#Next try to fetch customer ratings
#ratings = soup.find ( 'span' , {'class' : 'a-size-base a-color-secondary' }).get_text()
ratings = soup.find ( 'div' , {'class' : 'a-row a-spacing-medium averageStarRatingNumerical'
}).get_text()
print(ratings)
# Fetch individual Rating
individual_ratings = soup.find_all( 'i' , { 'class' : 'a-icon a-icon-star a-star-4 review-rating' });
#print(individual_ratings)
for ind_r in individual_ratings:
 print ( ind_r.get_text())
# Fetching customer names
customer_name_list = soup.find_all( 'div' , { 'class' : 'a-profile-content' });
#print(individual_ratings)
for cust in customer_name_list:
 print ( cust.get_text())