# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from crawler.models import connect_db, create_tables, Content, Creator
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


class PcollePipeline:
    def __init__(self):
        engine = connect_db()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        # sql common
        session = self.Session()

        if "product" in item["url"]:
            # Content
            creator_stmt = select(Creator).filter_by(name=item["creator"])
            creator = session.scalars(creator_stmt).first()
            # print(creator)
            if creator is None:
                creator = Creator(name=item["creator"])
                session.add(creator)
                # session.commit()

            # priceを整数にする
            item["price"] = int(item["price"].replace(",", "").split("円")[0])

            content_stmt = select(Content).filter_by(url=item["url"])
            content = session.scalars(content_stmt).first()

            if content is None:
                content = Content(
                    name=item["name"], url=item["url"], price=item["price"], creator=creator
                )
                session.add(content)

            try:
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

        else:
            # Creator
            creator_stmt = select(Creator).filter_by(name=item["name"])
            creator = session.scalars(creator_stmt).first()
            # print(creator)

            if creator is None:
                creator = Creator(name=item["creator"], url=item["url"])
                session.add(creator)

            if creator.url is None:
                creator.url = item["url"]

            try:
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

        return item


# class CrawlerPipeline:
#     def process_item(self, item, spider):
#         return item
