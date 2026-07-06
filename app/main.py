# In the module `main.py` you have to import all this classes. Classes
# should be imported by absolute path, that starts with 'app.' with 
# keyword 'from'. Write a
# function `cinema_visit` that takes `movie`, `customers` - a list 
# of customers, elements are dicts with 'name' and desired 'food' of a 
# customer, `hall_number` - number of the hall in cinema, 
# `cleaner` - name of the cleaner, that will clean the
# hall after movie session.

# This function should create instances of `Customer`, `CinemaHall`, and `Cleaner`.
# First, the cinema bar should sell food to customers. To do this, you can use the `CinemaBar`
# class without creating an instance. Then, the cinema hall should schedule a movie session,
# and finally, a cleaner should clean the cinema hall.  We expect each class to work with the provided data,
# accepting parameters in the correct order and having the necessary methods.
# No additional checks or error handling are needed!

def cinema_visit(movie: str, customers: list, hall_number: int, cleaner: str) -> None:
    from app.people.customer import Customer
    from app.cinema.bar import CinemaBar
    from app.cinema.hall import CinemaHall
    from app.people.cinema_staff import Cleaner

    # Create instances of Customer
    customer_instances = [Customer(name=cust["name"], food=cust["food"]) for cust in customers]

    # Sell food to customers using CinemaBar
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create instance of CinemaHall
    hall = CinemaHall(hall_number=hall_number)

    # Create instance of Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # Schedule movie session
    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)
