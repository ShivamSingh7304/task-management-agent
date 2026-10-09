from app.tools.initalise import get_connection,initialize_db 

# DELETE
def delete_task(task_id: int):
    initialize_db()

    with get_connection() as conn:
        row = conn.execute("""
            DELETE FROM tasks
            WHERE id = %s
            RETURNING id
        """, (task_id,)).fetchone()

        return (
            {"id": row["id"], "message": "Task deleted"}
            if row
            else {"error": "Task not found"}
        )
