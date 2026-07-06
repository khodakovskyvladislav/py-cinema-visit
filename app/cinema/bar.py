# Импорт через TYPE_CHECKING, чтобы избежать циклической зависимости,
# если Customer тоже когда-то захочет импортировать Bar.
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.people.customer import Customer


class CinemaBar:
    # @staticmethod означает, что методу не нужен объект класса (self).
    # Мы можем вызвать его как CinemaBar.sell_product(...)
    @staticmethod
    def sell_product(product: str, customer: "Customer") -> None:
        # Используем данные из объекта customer (его имя),
        # чтобы сформировать сообщение.
        print(f"Cinema bar sold {product} to {customer.name}.")
