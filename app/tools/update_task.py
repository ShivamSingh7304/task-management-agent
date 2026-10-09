from app.tools.initalise import get_connection,initialize_db 

# UPDATE
def update_task(
    task_id: int,
    title: str | None = None,
    scheduled_at: str | None = None,
    status: str | None = None
):
    fields = []
    values = []

    if title is not None:
        fields.append("title = %s")
        values.append(title)

    if scheduled_at is not None:
        fields.append("scheduled_at = %s::timestamptz")
        values.append(scheduled_at)

    if status is not None:
        if status not in ("pending", "completed"):
            return {"error": "Invalid status"}

        fields.append("status = %s")
        values.append(status)

    if not fields:
        return {"error": "No fields to update"}

    initialize_db()
    values.append(task_id)

    with get_connection() as conn:
        row = conn.execute(
            f"""
            UPDATE tasks
            SET {', '.join(fields)}
            WHERE id = %s
            RETURNING *
            """,
            values
        ).fetchone()

        return dict(row) if row else {
            "error": "Task not found"
        }
