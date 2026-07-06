from typing import TYPE_CHECKING

# Блок TYPE_CHECKING выполняется только анализатором (Pylance), 
# но игнорируется при реальном запуске программы. 
# Это решает проблему циклических импортов и ошибок UndefinedVariable.
if TYPE_CHECKING:
    from app.people.cinema_staff import Cleaner


class CinemaHall:
    # Конструктор: сохраняем номер зала, чтобы метод movie_session 
    # знал, где именно проходит сеанс.
    def __init__(self, hall_number: int) -> None:
        self.hall_number = hall_number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: "Cleaner"  # Аннотация (Forward Reference)
    ) -> None:
        # 1. Информируем о начале сеанса, используя номер зала из\
        # атрибутов класса
        print(f"Movie '{movie_name}' is starting in hall number"
              f"{self.hall_number}.")
        
        # 2. Перебираем каждого клиента из переданного списка
        for customer in customers:
            # 3. Вызываем у объекта 'customer' его собственный\
            #  метод 'watch_movie'
            customer.watch_movie(movie_name)
            
        # 4. Сообщаем об окончании сеанса
        print(f"Movie '{movie_name}' has ended in hall number"
              f"{self.hall_number}.")
        
        # 5. Делегируем уборку: вызываем метод 'clean_hall' у объекта\
        # 'cleaning_staff',
        # передавая ему номер текущего зала.
        cleaning_staff.clean_hall(self.hall_number)
