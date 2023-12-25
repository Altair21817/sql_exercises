from send_sql_query import send_sql_query

SCRIPTS: list[str] = [
    'aero_pg_script.sql',
    'computer_pg_script.sql',
    # 'football_script.sql',
    'inc_out_pg_script.sql',
    'painting_pg_script.sql',
    'ships_pg_script.sql',
    # 'sql_ex_pg.sql',
]

for script in SCRIPTS:
    send_sql_query(script_path=f'test_data/{script}')
