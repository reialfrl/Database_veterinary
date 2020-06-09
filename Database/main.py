import peewee
from models import User, Store, Product, Category, CategoriesProduct
#Función que elimina una tabla si ya existe. Ademas crea nuevas tablas al final
def create_tables():
    if CategoriesProduct.table_exists:
        CategoriesProduct.drop_table()

    if Category.table_exists:
        Category.drop_table()

    if Product.table_exists:
        Product.drop_table()

    if Store.table_exists:
        Store.drop_table()

    if User.table_exists:
        User.drop_table()

    User.create_table()
    Store.create_table()
    Product.create_table()
    Category.create_table()
    CategoriesProduct.create_table()
#Inserta valores en la tabla users
def insert_users():
    User.create(username='johaesfy', password='123456', email='johaesfy@gmail.com')
    User.create(username='Naireth', password='12345', email='naireth@gmail.com')
#Inserta valores en la tabla stores
def insert_stores():
    Store.create(user_id=1, name='Veterinaria Ramírez', address='Av. Venezuela 202')
    Store.create(user_id=2, name='Veterinaria Jei', address='Av. 5 de Abril 05-04')
#Inserta valores en la tabla products
def insert_products():
    Product.create(store_id=1, name='Supercan de 20 kilos', description='Alimento para perros', price='20', stock='20')
    Product.create(store_id=1, name='Sextuple', description='Vacuna para perros', price='5', stock='10')
    Product.create(store_id=1, name='Hueso de goma', description='Juguete para perros', price='2', stock='15')
    Product.create(store_id=1, name='Paté Happydog', description='Enlatado para perros', price='3', stock='8')

    Product.create(store_id=2, name='Supercat de 20 kilos', description='Alimento para gatos', price='22', stock='20')
    Product.create(store_id=2, name='Triple felina', description='Vacuna para gatos', price='5', stock='12')
    Product.create(store_id=2, name='Ratón de goma', description='Juguete para gatos', price='2', stock='8')
    Product.create(store_id=2, name='Paté Ricocat', description='Enlatado para gatos', price='3', stock='25')
#Inserta valores en la tabla categories    
def insert_categories():
    Category.create(name='Alimento', description='Alimento')
    Category.create(name='Enlatado', description='Enlatado')
    Category.create(name='Juguete', description='Juguete')
    Category.create(name='Vacuna', description='Vacuna')
#Inserta valores en la tabla categories_products, organizandolos mediante su id
def insert_categories_products():
    CategoriesProduct.create(category_id=1, product_id=1)
    CategoriesProduct.create(category_id=4, product_id=2)
    CategoriesProduct.create(category_id=3, product_id=3)
    CategoriesProduct.create(category_id=2, product_id=4)
    CategoriesProduct.create(category_id=1, product_id=5)
    CategoriesProduct.create(category_id=4, product_id=6)
    CategoriesProduct.create(category_id=3, product_id=7)
    CategoriesProduct.create(category_id=2, product_id=8)
#Función que inserta todos los valores a la tabla correspondiente
def create_schema():
    create_tables()
    insert_users()
    insert_stores()
    insert_products()
    insert_categories()
    insert_categories_products()

if __name__ == "__main__":
    create_schema()

    query = (Product.select().join(Store).join(User).where(User.id == 1).order_by(Product.price.asc()))#FORMA MAS OPTIMA DE CONSULTAR DATOS
    for product in query:
        print(product)
