from sqlalchemy import *

from header_generator.changelog_header_generator import Changelog_header_generator


def create_table():
    metadata_obj = MetaData()
    user_preference = Table('customer', metadata_obj,
        Column('pref_id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
        Column('pref_name', String(40), nullable=False),
        Column('pref_value', String(100),
        Column('date_done', DateTime(timezone=True), server_default=func.now(), nullable=False, comment='Date of creation'))
    )

def read_confluence():
    confluence = Confluence(
        url='https://confluence.icellmobilsoft.hu',
        username='bertalan.pasztor',
        password='Tcg6276tcg')

    space = 'MLFF'
    title_parent = 'JBS - Customer service database'
    p_id = confluence.get_page_id(space, title_parent)
    a = confluence.get_page_by_id(p_id)
    print(a)
    exit(0)


def generate_changelog_header(command):
    pass



if __name__ == '__main__':
    #read_confluence()
    g = Changelog_header_generator(author='bertalan.pasztor',jira='a', version='0.3.0' )
    g.generate_header('ALTER TABLE exemption.exemption_vehicle ALTER COLUMN plate_number TYPE varchar(32) USING plate_number::varchar;')