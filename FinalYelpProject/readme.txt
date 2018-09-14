The purpose of this application is to show the implementation of Yelp's Fusion API and to see if fast
food places are worth visiting or not based on the data we receive from the API.
We are specifically working with the businesses search endpoint that Yelp has provided us access to.



After running a query through Yelp's API in the APIsetup.py file with our desired default filters (such as location, restaurant type, etc.)
we retrieve the information into a JSON dictionary and then dump that information into a JSON file.

After traversing through the JSON dictionary we retrieve the name, review count, rating, price, location, and phone number of each restaurant.
Next that information gets stored into a relational database for better functionality for the main.py file.

The main.py file is where the GUI window
is created and the user can theoretically create 11 graphs using the filter options if enough data was retrieved by the API query.
However, filter options such as $$$ will not have enough data to show an informative graph of; therefore,a message box will show up instead.
The filter will still execute the appropriate results into a listbox and a selection can be made on each restaurant to see the attributes stored in the
database for that restaurant.



A clear filter button will return the original list of restaurants in the listbox. Analyze will allow the user to see the overall ratings for
fast food near De Anza and plot a pie graph that shows if the restaurants are mostly above 3 star rating or below. This will allow the user 
to know if it is even worthwhile to look at the restaurants near De Anza.
