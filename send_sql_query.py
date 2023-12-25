"""
Файл, который отправляет скрипт в базу данных PostgreSQL.
"""

import psycopg2

db_params: dict[str, str] = {
    'database': 'db_pg',
    'user': 'user_pg',
    'password': 'pass_pg',
    'host': 'localhost',
    'port': '5432',
}


def send_sql_query(script_path: str, db_driver: any = psycopg2) -> None:
    """
    Получает путь SQL-script для отправки в базу данных.
    Тип драйвера по-умолчанию: PostgreSQL.
    Печатает в консоль результаты выполнения.
    Ничего не возвращает.
    По выполнении команд закрывает соединение с базой данных.
    """

    if not db_driver in (psycopg2,):
        raise RuntimeError(
            f'Тип драйвера БД {db_driver} не поддерживается! '
            f'Пожалуйста, используйте следующие типы: "psycopg2".'
        )

    connection = db_driver.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute(open(script_path, "r").read())
    connection.commit()

    if cursor.description:
        results = cursor.fetchall()
        for row in results:
            print(row)

    cursor.close()
    connection.close()

    return
