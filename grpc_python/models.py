from __future__ import annotations
from typing import List

"""SQLAlchemy Data Models."""

from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import Integer, Text, String
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    projects = relationship("Project", back_populates="user")
    folders = relationship("Folder", back_populates="user")
    files = relationship("File", back_populates="user")


    def __repr__(self):
        return f"<User {self.username}>"


class Project(Base):
    __tablename__ = "project"

    id = mapped_column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="projects")
    folders = relationship("Folder", back_populates="project")

    def __repr__(self):
        return f"<Project {self.name}>"


class Folder(Base):
    """Folder."""

    __tablename__ = "folder"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="folders")
    project_id = mapped_column(ForeignKey("project.id"))
    project = relationship("Project", back_populates="folders")
    files = relationship("File", back_populates="folder")
    parent_folder_id = mapped_column(ForeignKey("folder.id"))
    parent_folder = relationship('Folder, remote_side=[id]')

    def __repr__(self):
        return f"<Folder {self.name}>"


class File(Base):
    """File."""

    __tablename__ = "file"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="files")
    folder_id = mapped_column(ForeignKey("folder.id"))
    folder = relationship("Folder", back_populates="files")
    content = Column(Text)

    def __repr__(self):
        return f"<File {self.name}>"


if __name__ == "__main__":
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/workspace') 
    Base.metadata.create_all(engine)