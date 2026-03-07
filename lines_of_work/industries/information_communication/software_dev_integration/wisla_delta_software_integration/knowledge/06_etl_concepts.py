title = "Koncepcje ETL"

content = """
ETL (Extract, Transform, Load) to wzorzec przenoszenia danych między systemami:
wyciąganie ze źródeł, przekształcanie do docelowego formatu, ładowanie do celu.

**Extract:** Odczyt z baz danych, plików, API. Uwzględnij incremental load (tylko zmiany)
zamiast full load przy dużych wolumenach. Używaj watermarków lub CDC (Change Data Capture).

**Transform:** Mapowanie pól, walidacja, agregacja, deduplikacja, wzbogacanie.
Przetwarzaj w pamięci lub w pipeline (Spark, dbt, custom). Obsługuj błędy — loguj
i kieruj do kwarantanny zamiast zatrzymywać cały batch.

**Load:** Zapisywanie do hurtowni, data lake lub systemu docelowego. Upsert zamiast
insert+delete przy aktualizacjach. Rozważ load w transakcjach dla spójności.

**Orchestracja:** Narzędzia jak Apache Airflow, Prefect lub Azure Data Factory
koordynują zależności między krokami ETL i harmonogramują uruchomienia.
"""  # noqa: E501

version = "0.0.1"
