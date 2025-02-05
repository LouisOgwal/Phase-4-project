from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Store(db.Model, SerializerMixin):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    # Relationships
    store_products = db.relationship('StoreProduct', back_populates='store', cascade='delete')
    products = association_proxy('store_products', 'product',
                                 creator=lambda product_obj: StoreProduct(product=product_obj))

    # Serialization rules
    serialize_rules = ('-store_products.store', '-products.stores',)

    def __repr__(self):
        return f"<Store {self.name}>"


class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    # Relationships
    store_products = db.relationship('StoreProduct', back_populates='product', cascade='delete')
    stores = association_proxy('store_products', 'store',
                               creator=lambda store_obj: StoreProduct(store=store_obj))

    # Serialization rules
    serialize_rules = ('-store_products.product', '-stores.products',)

    def __repr__(self):
        return f"<Product {self.name}, {self.description}>"


class StoreProduct(db.Model, SerializerMixin):
    __tablename__ = "store_products"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    # Foreign keys
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # Relationships
    store = db.relationship('Store', back_populates='store_products')
    product = db.relationship('Product', back_populates='store_products')

    # Serialization rules
    serialize_rules = ('-store.store_products', '-product.store_products',)

    # Validation
    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 10000):  # Adjusted for Apple product prices
            raise ValueError("Price must be between 1 and 10,000")
        return price

    def __repr__(self):
        return f"<StoreProduct ${self.price}>"