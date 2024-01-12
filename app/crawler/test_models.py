from sqlalchemy.orm import sessionmaker
import models

engine = models.connect_db()
models.create_tables(engine)
Session = sessionmaker(bind=engine)

session = Session()


try:
    creator = models.Creator(
        name="test",
    )
    session.add(creator)

    content = models.Content(
        creator=creator,
        name="test",
        url="test",
        price=100,
    )
    session.add(content)

    session.commit()

    # データが挿入されているか確認。
    obj = session.query(models.Content).first()
    print(obj.name)

    # データを更新
    # updated_content = session.query(models.Content).filter(models.Content.id == 1).first()
    # updated_content.price = 200
    # session.commit()

except:
    session.rollback()
    raise
finally:
    session.close()
