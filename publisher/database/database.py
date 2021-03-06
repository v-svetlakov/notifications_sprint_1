from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy import Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base


class Template(Base):
    """Модель шаблонов."""

    __tablename__ = "templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    name = Column(Text, nullable=False)
    template = Column(Text, nullable=False)

    __table_args__ = {"schema": "events"}


class Welcome(Base):
    """Модель шаблонов."""

    __tablename__ = "welcome"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    user_id = Column("user_id", UUID(as_uuid=True), ForeignKey("user.id"))
    template_id = Column("template_id", UUID(as_uuid=True), ForeignKey("templates.id"))

    __table_args__ = {"schema": "events"}


class Others(Base):
    """Модель шаблонов."""

    __tablename__ = "others"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    template_id = Column("template_id", UUID(as_uuid=True), ForeignKey("templates.id"))
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    __table_args__ = {"schema": "events"}


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    login = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    confirmed = Column(Boolean, nullable=False)
    mail_subscribe = Column(Boolean, nullable=False)

    __table_args__ = {"schema": "users"}
