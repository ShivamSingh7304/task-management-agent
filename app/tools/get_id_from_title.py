from app.tools.initalise import get_connection,initialize_db 

def get_task_id_by_title(title: str):
    initialize_db()

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, title
            FROM tasks
            WHERE title ILIKE %s
            ORDER BY id
            """,
            (f"%{title}%",)
        ).fetchall()

        return [dict(row) for row in rows]
