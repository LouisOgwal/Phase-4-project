#!/usr/bin/env python3

from app import app
from models import db, Store, Product, StoreProduct

with app.app_context():
    # Delete existing data
    print("Deleting data...")
    Product.query.delete()
    Store.query.delete()
    StoreProduct.query.delete()

    print("Creating stores...")
    store1 = Store(name="Apple Store NYC", address="123 Apple Street, New York, NY")
    store2 = Store(name="Apple Store LA", address="456 Orange Avenue, Los Angeles, CA")
    stores = [store1, store2]

    print("Creating products...")
    iphone = Product(name="iPhone 15", description="Latest iPhone with A16 Bionic chip")
    macbook = Product(name="MacBook Pro", description="16-inch MacBook Pro with M2 Max chip")
    airpods = Product(name="AirPods Pro", description="Noise-cancelling AirPods with Spatial Audio")
    products = [iphone, macbook, airpods]

    print("Creating store products...")
    sp1 = StoreProduct(store=store1, product=iphone, price=999)
    sp2 = StoreProduct(store=store1, product=macbook, price=2499)
    sp3 = StoreProduct(store=store2, product=airpods, price=249)
    store_products = [sp1, sp2, sp3]

    db.session.add_all(stores)
    db.session.add_all(products)
    db.session.add_all(store_products)
    db.session.commit()

    print("Seeding done!")