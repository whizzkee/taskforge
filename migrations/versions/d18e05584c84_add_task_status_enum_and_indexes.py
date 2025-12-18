"""Add task status enum and indexes

Revision ID: d18e05584c84
Revises: 4b533c0268e1
Create Date: 2025-12-17 16:28:34.987619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd18e05584c84'
down_revision: Union[str, Sequence[str], None] = '4b533c0268e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    task_status_enum = sa.Enum(
        'todo',
        'in_progress',
        'done',
        name='task_status'
    )
    task_status_enum.create(op.get_bind(), checkfirst=True)

    op.execute(
        "ALTER TABLE tasks "
        "ALTER COLUMN status "
        "TYPE task_status "
        "USING status::task_status"
    )

    op.create_index('ix_tasks_assignee_id', 'tasks', ['assignee_id'], unique=False)
    op.create_index('ix_tasks_project_id', 'tasks', ['project_id'], unique=False)
    op.create_index('ix_tasks_status', 'tasks', ['status'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_index('ix_tasks_status', table_name='tasks')
    op.drop_index('ix_tasks_project_id', table_name='tasks')
    op.drop_index('ix_tasks_assignee_id', table_name='tasks')

    op.execute(
        "ALTER TABLE tasks "
        "ALTER COLUMN status "
        "TYPE VARCHAR(50)"
    )

    sa.Enum(
        'todo',
        'in_progress',
        'done',
        name='task_status'
    ).drop(op.get_bind(), checkfirst=True)

    # ### end Alembic commands ###
