from app.tools.initalise import get_connection,initialize_db 

# CREATE
def add_task(title: str, scheduled_at: str | None = None):
    initialize_db()

    with get_connection() as conn:
        row = conn.execute("""
            INSERT INTO tasks (title, scheduled_at)
            VALUES (
                %s,
                %s::timestamptz
            )
            RETURNING *
        """, (title, scheduled_at)).fetchone()

        return dict(row)

if __name__ == "__main__":
    result = add_task(
        title="Learn MCP",
        scheduled_at="2026-10-10T10:00:00+05:30"
    )

    print("Task added successfully:")
    print(result)
