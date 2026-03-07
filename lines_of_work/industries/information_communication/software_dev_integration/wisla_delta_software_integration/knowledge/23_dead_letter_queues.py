title = "Kolejki martwych wiadomości (DLQ)"

content = """
Dead Letter Queue przechowuje wiadomości, których nie udało się przetworzyć po wielokrotnych
próbach. Zapobiega blokowaniu głównej kolejki i umożliwia późniejszą analizę i ręczną interwencję.

**Kiedy używać:** Po wyczerpaniu retry, gdy wiadomość jest nieprawidłowa lub docelowy system
jest niedostępny przez dłuższy czas.

**Praktyki:** Loguj kontekst, zachowaj oryginalną wiadomość, ustaw alerty na wzrost DLQ.
"""  # noqa: E501

version = "0.0.1"
