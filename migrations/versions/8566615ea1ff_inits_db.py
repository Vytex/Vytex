"""inits db

Revision ID: 8566615ea1ff
Revises: 
Create Date: 2021-03-19 18:42:57.815077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8566615ea1ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lines',
    sa.Column('venueID', sa.Integer(), nullable=False),
    sa.Column('date', sa.VARCHAR(length=8), nullable=False),
    sa.Column('x00000030', sa.Integer(), nullable=True),
    sa.Column('x00300100', sa.Integer(), nullable=True),
    sa.Column('x01000130', sa.Integer(), nullable=True),
    sa.Column('x01300200', sa.Integer(), nullable=True),
    sa.Column('x02000230', sa.Integer(), nullable=True),
    sa.Column('x02300300', sa.Integer(), nullable=True),
    sa.Column('x03000330', sa.Integer(), nullable=True),
    sa.Column('x03300400', sa.Integer(), nullable=True),
    sa.Column('x04000430', sa.Integer(), nullable=True),
    sa.Column('x04300500', sa.Integer(), nullable=True),
    sa.Column('x05000530', sa.Integer(), nullable=True),
    sa.Column('x05300600', sa.Integer(), nullable=True),
    sa.Column('x06000630', sa.Integer(), nullable=True),
    sa.Column('x06300700', sa.Integer(), nullable=True),
    sa.Column('x07000730', sa.Integer(), nullable=True),
    sa.Column('x07300800', sa.Integer(), nullable=True),
    sa.Column('x08000830', sa.Integer(), nullable=True),
    sa.Column('x08300900', sa.Integer(), nullable=True),
    sa.Column('x09000930', sa.Integer(), nullable=True),
    sa.Column('x09301000', sa.Integer(), nullable=True),
    sa.Column('x10001030', sa.Integer(), nullable=True),
    sa.Column('x10301100', sa.Integer(), nullable=True),
    sa.Column('x11001130', sa.Integer(), nullable=True),
    sa.Column('x11301200', sa.Integer(), nullable=True),
    sa.Column('x12001230', sa.Integer(), nullable=True),
    sa.Column('x12301300', sa.Integer(), nullable=True),
    sa.Column('x13001330', sa.Integer(), nullable=True),
    sa.Column('x13301400', sa.Integer(), nullable=True),
    sa.Column('x14001430', sa.Integer(), nullable=True),
    sa.Column('x14301500', sa.Integer(), nullable=True),
    sa.Column('x15001530', sa.Integer(), nullable=True),
    sa.Column('x15301600', sa.Integer(), nullable=True),
    sa.Column('x16001630', sa.Integer(), nullable=True),
    sa.Column('x16301700', sa.Integer(), nullable=True),
    sa.Column('x17001730', sa.Integer(), nullable=True),
    sa.Column('x17301800', sa.Integer(), nullable=True),
    sa.Column('x18001830', sa.Integer(), nullable=True),
    sa.Column('x18301900', sa.Integer(), nullable=True),
    sa.Column('x19001930', sa.Integer(), nullable=True),
    sa.Column('x19302000', sa.Integer(), nullable=True),
    sa.Column('x20002030', sa.Integer(), nullable=True),
    sa.Column('x20302100', sa.Integer(), nullable=True),
    sa.Column('x21002130', sa.Integer(), nullable=True),
    sa.Column('x21302200', sa.Integer(), nullable=True),
    sa.Column('x22002230', sa.Integer(), nullable=True),
    sa.Column('x22302300', sa.Integer(), nullable=True),
    sa.Column('x23002330', sa.Integer(), nullable=True),
    sa.Column('x23300000', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('venueID', 'date')
    )
    op.create_table('venue',
    sa.Column('venueID', sa.Integer(), nullable=False),
    sa.Column('venue', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('description', sa.NVARCHAR(length=500), nullable=True),
    sa.Column('venueURL', sa.VARCHAR(length=2083), nullable=True),
    sa.Column('venueCity', sa.NVARCHAR(length=500), nullable=True),
    sa.Column('venueIcon', sa.VARCHAR(length=500), nullable=True),
    sa.Column('monOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('monClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('tueOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('tueClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('wedOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('wedClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('thuOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('thuClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('friOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('friClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('satOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('satClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('sunOpen', sa.TIME(timezone=4), nullable=True),
    sa.Column('sunClose', sa.TIME(timezone=4), nullable=True),
    sa.Column('lineCapacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('venueID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue')
    op.drop_table('lines')
    # ### end Alembic commands ###
