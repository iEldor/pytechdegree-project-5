from peewee import *

db = SqliteDatabase('journal.db')

class BaseModel(Model):
    class Meta:
        database = db

class Entry(BaseModel):
    
    title = CharField(max_length=255, unique=True)
    date = DateField()
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()

    # @classmethod
    # def create_entry(cls, title, date, time_spent, learned, resources):
    #     with DATABASE.transaction():
    #         cls.create(
    #             title=title,
    #             date=date,
    #             time_spent=time_spent,
    #             learned=learned,
    #             resources=resources
    #         )


def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)
    db.close()