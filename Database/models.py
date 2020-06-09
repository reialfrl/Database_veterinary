import peewee
import datetime

HOST = 'localhost'
USER = 'root'
PASSWORD = '123456'
DATABASE = 'store'

database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, password=PASSWORD)

class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50)
    status = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

    def __str__(self):
        return self.username

class Store(peewee.Model):
    user = peewee.ForeignKeyField(User, related_name='stores')
    name = peewee.CharField(max_length=50, unique=50, index=True)
    address = peewee.TextField()
    status = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return self.name
    
class Product(peewee.Model):
    store = peewee.ForeignKeyField(Store, related_name='products')
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    price = peewee.DecimalField(max_digits=5, decimal_places=2)
    stock = peewee.IntegerField()
    create_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'products'

    def __str__(self):
        return f'{self.name} - {self.price} Dolares'

class Category(peewee.Model):
    name = peewee.CharField(max_length=50)
    description = peewee.TextField()
    create_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'categories'

    def __str__(self):
        return self.name

class CategoriesProduct(peewee.Model):
    product = peewee.ForeignKeyField(Product, related_name='categories')
    category = peewee.ForeignKeyField(Category, related_name='products')

    class Meta:
        database = database
        db_table = 'categories_products'

    def __str__(self):
        return f'{self.product} - {self.categorie}'