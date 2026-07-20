from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    hall_number: int,
    cleaner: str,
    movie: str,
    customers: list,
) -> None:
    # 1. Создаем объекты покупателей
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]

    # 2. Создаем объекты персонала
    cleaner_obj = Cleaner(cleaner)
    hall_obj = CinemaHall(hall_number)

    # 3. Продаем еду каждому
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    # 4. Проводим сеанс
    hall_obj.movie_session(movie, customer_objects, cleaner_obj)


customers = [
    {"name": "Bob", "food": "Coca-cola"},
    {"name": "Alex", "food": "popcorn"}
]
hall_number = 5
cleaner_name = "Anna"
movie = "Madagascar"
cinema_visit(customers=customers, hall_number=hall_number,
             cleaner=cleaner_name, movie=movie)
