from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Date, Text
from sqlalchemy import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from crawler import config

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqldb://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}"
    f"@{config.MYSQL_HOST}/{config.MYSQL_DATABASE}"
)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def connect_db():
    return create_engine(SQLALCHEMY_DATABASE_URL)


def create_tables(engine):
    return Base.metadata.create_all(bind=engine)


class Content(Base):
    __tablename__ = "contents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("creator.id"), nullable=False)
    creator: Mapped["Creator"] = relationship("Creator", back_populates="contents")
    # genres: Mapped[list["Genre"]] = relationship(
    #     "Genre", back_populates="contents", secondary="content_genre"
    # )
    # product_id: Mapped[str] = mapped_column(String(255))
    # release_date: Mapped[date] = mapped_column(Date)
    # rating: Mapped[int] = mapped_column(Integer)
    # views: Mapped[int] = mapped_column(Integer)
    # image_urls =
    # description = mapped_column(Text)
    # tags =
    # file_name: Mapped[str] = mapped_column(String(255))
    # file_size: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(Timestamp, server_default=current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        Timestamp, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )


# class ContentImage(Base):
#     __tablename__ = "content_image"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
#     content_id: Mapped[int] = mapped_column(Integer, ForeignKey("content.id", nullable=False))
#     url: Mapped[str] = mapped_column(String(255))
#     created_at: Mapped[datetime] = mapped_column(Timestamp, server_default=current_timestamp())
#     updated_at: Mapped[datetime] = mapped_column(
#         Timestamp, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
#     )


class Creator(Base):
    __tablename__ = "creators"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255), nullable=True)
    # profile =
    # hp_url =
    contents: Mapped[list["Content"]] = relationship("Content", back_populates="creator")
    # created_at: Mapped[datetime] = mapped_column(Timestamp, server_default=current_timestamp())
    # updated_at: Mapped[datetime] = mapped_column(
    #     Timestamp, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    # )


# class Genre(Base):
#     __tablename__ = "genre"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(255))
#     contents: Mapped[list["Content"]] = relationship("Content", back_populates="genres")
#     # description =
#     # image_urls =
#     # created_at =
#     # updated_at =


# class Tag(Base):
#     __tablename__ = "tag"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(String(255))
#     url: Mapped[str] = mapped_column(String(255))
#     # description =
#     # image_urls =
#     # created_at =
#     # updated_at =
