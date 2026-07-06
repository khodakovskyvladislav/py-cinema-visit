# - `hall.py` - inside this module create `CinemaHall`
#    class that describes actions during the movie session. Its
#    `__init__` method takes and stores ONLY the `number `of the hall in the cinema.
#    This class should have only one method `movie_session`, that
#    takes `movie_name`, `customers` - list of a customers
#    (`Customer` instances), `cleaning_staff` - cleaner (`Cleaner` 
#    instance). This method prints about movie start, calls 
#    customers method `watch_movie`, prints about movie end,
#    calls cleaner method `clean_hall`. So, we are expecting
#    that everything listed above will be performed in `movie_session` function.

# ```python
# hall = CinemaHall(hall_number=5)
# movie_name = "Madagascar"
# customers = [
#     Customer(name="Bob", food="Coca-cola"),
#     Customer(name="Alex", food="popcorn")
# ]
# cleaning_staff = Cleaner(name="Anna")

# hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)

class CinemaHall:
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(self, movie_name: str, customers: list, cleaning_staff) -> None:
        print(f"Movie '{movie_name}' is starting in hall number {self.hall_number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f"Movie '{movie_name}' has ended in hall number {self.hall_number}.")
        cleaning_staff.clean_hall(self.hall_number)

hall = CinemaHall(hall_number=5)
movie_name = "Madagascar"
customers = [
    Customer(name="Bob", food="Coca-cola"),
    Customer(name="Alex", food="popcorn")
]
cleaning_staff = Cleaner(name="Anna")

hall.movie_session(movie_name=movie_name, customers=customers, cleaning_staff=cleaning_staff)