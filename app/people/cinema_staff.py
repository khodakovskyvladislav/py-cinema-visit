class Cleaner:
    # Конструктор: вызывается при создании объекта (например, Cleaner("Anna"))
    def __init__(self, name: str) -> None:
        # self.name — это "память" объекта. Мы сохраняем имя, чтобы помнить \
        # его позже.
        self.name = name

    # Метод действия: объект выполняет работу, используя свои данные (имя)
    def clean_hall(self, hall_number: int) -> None:
        # print выводит результат в консоль.
        # f-строка подставляет значения переменных прямо в текст.
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")
