from app.tools.initalise import get_connection,initialize_db 


# READ
def get_tasks(task_id: int | None = None):
    initialize_db()

    with get_connection() as conn:
        if task_id is not None:
            row = conn.execute(
                "SELECT * FROM tasks WHERE id = %s",
                (task_id,)
            ).fetchone()

            return dict(row) if row else {
                "error": "Task not found"
            }

        rows = conn.execute("""
            SELECT * FROM tasks
            ORDER BY scheduled_at NULLS LAST, id
        """).fetchall()

        return [dict(row) for row in rows]

