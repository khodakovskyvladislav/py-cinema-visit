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
