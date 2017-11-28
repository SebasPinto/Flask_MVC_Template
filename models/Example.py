import peewee

DB = MySQLDatabase("bot_guarumo", 
						host="apps.ccsmckgi9ggi.us-east-1.rds.amazonaws.com", 
						port=3306, 
						user="dgualdron", 
						passwd="91532004ab")


#This class represent a Table in your database, it must be with the same name, but in lower case. In this case 'example'
class Example(Model):
	id          = IntegerField(null=False)
    name	    = CharField(max_length=800, null=False)

    class Meta:
        database = DB


DB.connect()