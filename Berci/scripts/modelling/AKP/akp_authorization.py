from typing import Optional
import datetime

from sqlalchemy import BigInteger, Boolean, CheckConstraint, DateTime, ForeignKeyConstraint, Index, LargeBinary, PrimaryKeyConstraint, String, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class AuthorizationRole(Base):
    __tablename__ = 'authorization_role'
    __table_args__ = (
        PrimaryKeyConstraint('x__id', name='pk_authorization_role'),
        UniqueConstraint('authorization_role_id', name='uq_authorization_role_authorization_role_id'),
        {'comment': 'A tábla az AKP-ban használt szerepköröket tartalmazza, melyek a '
                'keycloakkal szinkronban kell legyenek. Amennyiben egy AKP-ban '
                'használt szerepkör a keycloakban törlésre került, úgy itt az '
                'ACTIVE státusza hamisra vált és nem használható a rendszerben.',
     'schema': 'akp_authorization'}
    )

    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Elsődleges kulcs')
    x__insdate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='A beszúrás időpontja')
    x__insuser: Mapped[str] = mapped_column(String(255), nullable=False, comment='A beszúrást végző felhasználó neve')
    x__version: Mapped[int] = mapped_column(BigInteger, nullable=False, server_default=text('0'), comment='Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[str] = mapped_column(String(255), nullable=False, comment='A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[str] = mapped_column(String(50), nullable=False, comment='A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, comment='Jelzi, hogy a szerepkör létezik-e keycloakban')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='A módosítást végző felhasználó neve')

    authorization_role_to_function: Mapped[list['AuthorizationRoleToFunction']] = relationship('AuthorizationRoleToFunction', back_populates='authorization_role')


class AuthorizationRoleHist(Base):
    __tablename__ = 'authorization_role$hist'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='pk_authorization_role$hist'),
        {'comment': 'History table, source description: A tábla az AKP-ban használt '
                'szerepköröket tartalmazza, melyek a keycloakkal szinkronban kell '
                'legyenek. Amennyiben egy AKP-ban használt szerepkör a keycloakban '
                'törlésre került, úgy itt az ACTIVE státusza hamisra vált és nem '
                'használható a rendszerben. ',
     'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistDefault(Base):
    __tablename__ = 'authorization_role$hist_default'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_default_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202603(Base):
    __tablename__ = 'authorization_role$hist_p2026_03'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_03_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202604(Base):
    __tablename__ = 'authorization_role$hist_p2026_04'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_04_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202605(Base):
    __tablename__ = 'authorization_role$hist_p2026_05'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_05_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202606(Base):
    __tablename__ = 'authorization_role$hist_p2026_06'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_06_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202607(Base):
    __tablename__ = 'authorization_role$hist_p2026_07'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_07_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202608(Base):
    __tablename__ = 'authorization_role$hist_p2026_08'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_08_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleHistP202609(Base):
    __tablename__ = 'authorization_role$hist_p2026_09'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role$hist_p2026_09_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_name: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A szerepkör neve (keycloakból szinkronizált)')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A szerepkör egyedi azonosítója (keycloakból szinkronizált UUID)')
    active: Mapped[Optional[bool]] = mapped_column(Boolean, comment='Logged field: Jelzi, hogy a szerepkör létezik-e keycloakban')


class AuthorizationRoleToFunctionHist(Base):
    __tablename__ = 'authorization_role_to_function$hist'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='pk_authorization_role_to_function$hist'),
        {'comment': 'History table, source description: A tábla mappeli össze, hogy '
                'mely funkciókat mely szerepkörrel veheti igénybe a felhasználó. ',
     'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistDefault(Base):
    __tablename__ = 'authorization_role_to_function$hist_default'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_default_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202603(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_03'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_03_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202604(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_04'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_04_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202605(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_05'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_05_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202606(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_06'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_06_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202607(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_07'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_07_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202608(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_08'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_08_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationRoleToFunctionHistP202609(Base):
    __tablename__ = 'authorization_role_to_function$hist_p2026_09'
    __table_args__ = (
        CheckConstraint("x__hist_state::text = ANY (ARRAY['I'::character varying, 'U'::character varying, 'D'::character varying]::text[])", name='ck_authorization_role_to_function$hist_op'),
        PrimaryKeyConstraint('x__id', 'x__hist_ts', name='authorization_role_to_function$hist_p2026_09_pkey'),
        {'schema': 'akp_authorization'}
    )

    x__hist_ts: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(True, 6), primary_key=True, server_default=text('clock_timestamp()'), comment='History timestamp, the moment of the DML operation.')
    x__hist_state: Mapped[str] = mapped_column(String(1), nullable=False, comment='History DML Operations:  ("I"-Insert record; "U"-Update record; "D"-Delete record, physical deletion).')
    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Logged field: Elsődleges kulcs')
    x__insdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: A beszúrás időpontja')
    x__insuser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A beszúrást végző felhasználó neve')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Logged field: Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='Logged field: A módosítást végző felhasználó neve')
    x__version: Mapped[Optional[int]] = mapped_column(BigInteger, comment='Logged field: Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[Optional[str]] = mapped_column(String(30), comment='Logged field: FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[Optional[str]] = mapped_column(String(50), comment='Logged field: A funkció neve.')


class AuthorizationSync(Base):
    __tablename__ = 'authorization_sync'
    __table_args__ = (
        CheckConstraint("authorization_sync_type::text = 'ROLE'::text", name='ck_authorization_sync_authorization_sync_type'),
        PrimaryKeyConstraint('x__id', name='pk_authorization_sync'),
        UniqueConstraint('authorization_sync_type', name='uq_authorization_sync_authorization_sync_type'),
        {'comment': 'A tábla tartalmazza a DBbe való adatszinkronizálások utolsó '
                'idejét.',
     'schema': 'akp_authorization'}
    )

    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Elsődleges kulcs')
    x__insdate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='A beszúrás időpontja')
    x__insuser: Mapped[str] = mapped_column(String(255), nullable=False, comment='A beszúrást végző felhasználó neve')
    x__version: Mapped[int] = mapped_column(BigInteger, nullable=False, server_default=text('0'), comment='Az aktuális verziója a rekordnak')
    authorization_sync_type: Mapped[str] = mapped_column(String(100), nullable=False, comment='A szinkronizáció típusa')
    authorization_sync_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, comment='A szinkronizáció utolsó ideje')
    authorization_sync_hash: Mapped[str] = mapped_column(String(128), nullable=False, comment='A szinkronizáció válaszából képzett hash')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='A módosítást végző felhasználó neve')


class LogEntry(Base):
    __tablename__ = 'log_entry'
    __table_args__ = (
        PrimaryKeyConstraint('x__id', name='pk_log_entry'),
        {'comment': 'A táblában a rest végpontok hívásával kapcsolatos adatok kerülnek '
                'ideiglenesen letárolásra.',
     'schema': 'akp_authorization'}
    )

    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Elsődleges kulcs')
    log_message: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, comment='Az eredeti log bejegyzés mentve JSON formában')
    entry_timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, comment='Bejegyzés keletkezésének ideje')
    x__insdate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='A beszúrás időpontja')
    x__insuser: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'0'::character varying"), comment='A beszúrást végző felhasználó neve')
    x__version: Mapped[int] = mapped_column(BigInteger, nullable=False, server_default=text('0'), comment='Az aktuális verziója a rekordnak')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='A módosítást végző felhasználó neve')


class OrganizationMapping(Base):
    __tablename__ = 'organization_mapping'
    __table_args__ = (
        PrimaryKeyConstraint('x__id', name='pk_organization_mapping'),
        UniqueConstraint('organization_code', name='uq_organization_mapping_organization_code'),
        {'comment': 'A tábla a lakehouse-ból lekérdezett szervezetek adatait, valamint '
                'az abból képzett szervezet kódot tartalmazza.',
     'schema': 'akp_authorization'}
    )

    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Elsődleges kulcs')
    x__insdate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='A beszúrás időpontja')
    x__insuser: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("'0'::character varying"), comment='A beszúrást végző felhasználó neve')
    x__version: Mapped[int] = mapped_column(BigInteger, nullable=False, server_default=text('0'), comment='Az aktuális verziója a rekordnak')
    organization_name: Mapped[str] = mapped_column(String(100), nullable=False, comment='A szervezet neve.')
    organization_code: Mapped[str] = mapped_column(String(200), nullable=False, comment='A szervezet kódja (keycloak csoport név).')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='A módosítást végző felhasználó neve')


class AuthorizationRoleToFunction(Base):
    __tablename__ = 'authorization_role_to_function'
    __table_args__ = (
        CheckConstraint("authorization_function_name::text = ANY (ARRAY['CHANGE_PASSWORD'::character varying::text, 'EDIT_ROLE_TO_FUNCTION_MAP'::character varying::text, 'VEHICLE_OPERATIONAL_LOG_VIEW'::character varying::text, 'VEHICLE_SECURITY_LOG_VIEW'::character varying::text, 'VEHICLE_BUSINESS_LOG_VIEW'::character varying::text, 'BICYCLE_OPERATIONAL_LOG_VIEW'::character varying::text, 'BICYCLE_SECURITY_LOG_VIEW'::character varying::text, 'BICYCLE_BUSINESS_LOG_VIEW'::character varying::text, 'VEHICLE_NOTIFICATION_VIEW'::character varying::text, 'VEHICLE_MANUAL_RAW_DATA_CHECK'::character varying::text, 'VEHICLE_MANUAL_DATA_CHECK'::character varying::text, 'VEHICLE_DATA_PACKAGE_APPROVE'::character varying::text, 'VEHICLE_MANUAL_DATA_UPLOAD'::character varying::text, 'VEHICLE_MANUAL_DATA_CORRECTION'::character varying::text, 'VEHICLE_MANUAL_CALCULATION_START'::character varying::text, 'VEHICLE_MANUAL_PUBLICATION_STRAT'::character varying::text, 'VEHICLE_MANUAL_AUTOMATIC_VALIDATION_START'::character varying::text, 'BICYCLE_NOTIFICATION_VIEW'::character varying::text, 'BICYCLE_MANUAL_RAW_DATA_CHECK'::character varying::text, 'BICYCLE_MANUAL_DATA_CHECK'::character varying::text, 'BICYCLE_DATA_PACKAGE_APPROVE'::character varying::text, 'BICYCLE_MANUAL_DATA_UPLOAD'::character varying::text, 'BICYCLE_MANUAL_DATA_CORRECTION'::character varying::text, 'BICYCLE_MANUAL_CALCULATION_START'::character varying::text, 'BICYCLE_MANUAL_PUBLICATION_STRAT'::character varying::text, 'BICYCLE_MANUAL_AUTOMATIC_VALIDATION_START'::character varying::text, 'FILE_DATA_UPLOAD'::character varying::text, 'API_DATA_UPLOAD'::character varying::text, 'VEHICLE_TRAFFIC_DATA_QUERY'::character varying::text, 'BICYCLE_TRAFFIC_DATA_QUERY'::character varying::text, 'REPORT_VIEW'::character varying::text, 'TRAFFIC_CALENDAR_CLOSE'::character varying::text, 'TRAFFIC_CALENDAR_OPEN'::character varying::text, 'MASTER_DATA_VIEW'::character varying::text, 'MASTER_DATA_EDIT'::character varying::text, 'BICYCLE_VALIDATION_DATA_EDIT'::character varying::text, 'TRAFFIC_CALENDAR_APPROVE'::character varying::text, 'ALERT_MANAGEMENT'::character varying::text, 'VEHICLE_VALIDATION_DATA_EDIT'::character varying::text, 'PERIODICITY_FACTOR_FILE_MANAGE'::character varying::text])", name='ck_authorization_role_to_function_authorization_function_name'),
        ForeignKeyConstraint(['authorization_role_id'], ['akp_authorization.authorization_role.x__id'], name='fk_authorization_role_to_function_authorization_role_id'),
        PrimaryKeyConstraint('x__id', name='pk_authorization_role_to_function'),
        UniqueConstraint('authorization_role_id', 'authorization_function_name', name='uq_authorization_role_to_function_role_id_function_name'),
        Index('ix_authorization_role_to_function_authorization_role_id', 'authorization_role_id'),
        {'comment': 'A tábla mappeli össze, hogy mely funkciókat mely szerepkörrel '
                'veheti igénybe a felhasználó.',
     'schema': 'akp_authorization'}
    )

    x__id: Mapped[str] = mapped_column(String(30), primary_key=True, comment='Elsődleges kulcs')
    x__insdate: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='A beszúrás időpontja')
    x__insuser: Mapped[str] = mapped_column(String(255), nullable=False, comment='A beszúrást végző felhasználó neve')
    x__version: Mapped[int] = mapped_column(BigInteger, nullable=False, server_default=text('0'), comment='Az aktuális verziója a rekordnak')
    authorization_role_id: Mapped[str] = mapped_column(String(30), nullable=False, comment='FK(AUTHORIZATION_ROLE.X_ID)')
    authorization_function_name: Mapped[str] = mapped_column(String(50), nullable=False, comment='A funkció neve.')
    x__moddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='Az utolsó módosítás időpontja')
    x__moduser: Mapped[Optional[str]] = mapped_column(String(255), comment='A módosítást végző felhasználó neve')

    authorization_role: Mapped['AuthorizationRole'] = relationship('AuthorizationRole', back_populates='authorization_role_to_function')
