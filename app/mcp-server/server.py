from fastmcp import FastMCP

from app.tools.add_task import add_task
from app.tools.delete_task import delete_task
from app.tools.get_id_from_title import get_task_id_by_title
from app.tools.get_task import get_tasks
from app.tools.update_task import update_task

mcp = FastMCP("task_manager")


@mcp.tool()
def create_task(title: str, description: str = ""):
    """Create a new task."""
    return add_task(title, description)


@mcp.tool()
def list_tasks():
    """Get all tasks."""
    return get_tasks()


@mcp.tool()
def delete_task_by_id(task_id: int):
    """Delete a task using its ID."""
    return delete_task(task_id)


@mcp.tool()
def find_task_id(title: str):
    """Find a task ID using its title."""
    return get_task_id_by_title(title)


@mcp.tool()
def edit_task(task_id: int, title: str, description: str = ""):
    """Update an existing task."""
    return update_task(task_id, title, description)


if __name__ == "__main__":
    mcp.run(transport='streamable-http')
