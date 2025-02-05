#!/usr/bin/env python3
from flask import Flask, request, make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from dotenv import load_dotenv
import os
from models import db, Store, StoreProduct, Product

load_dotenv()

app = Flask(__name__)
CORS(app) 

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route("/")
def index():
    return "<h1>Apple Store Manager</h1>"


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(BASE_DIR, "build", path)):
        return send_from_directory(os.path.join(BASE_DIR, "build"), path)
    else:
        return send_from_directory(os.path.join(BASE_DIR, "build"), "index.html")


@app.route("/stores", methods=["GET"])
def get_stores():
    stores = Store.query.all()
    stores_dict = [store.to_dict(only=("id", "name", "address")) for store in stores]
    return make_response(stores_dict, 200)


@app.route("/stores/<int:id>", methods=["GET", "DELETE"])
def get_store_by_id(id):
    store = Store.query.filter(Store.id == id).first()
    if request.method == "GET":
        if store:
            store_dict = store.to_dict(
                only=("id", "name", "address", "store_products.id", "store_products.price",
                      "store_products.product_id", "store_products.store_id",
                      "store_products.product.id", "store_products.product.name",
                      "store_products.product.description")
            )
            return make_response(store_dict, 200)
        else:
            return make_response({"error": "Store not found"}, 404)
    elif request.method == "DELETE":
        if store:
            db.session.delete(store)
            db.session.commit()
            return make_response({"deleted": True}, 204)
        else:
            return make_response("", 404)


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    products_dict = [product.to_dict(only=("id", "name", "description")) for product in products]
    return make_response(products_dict, 200)


@app.route("/store_products", methods=["POST"])
def add_store_product():
    data = request.get_json()
    price = data.get("price")
    product_id = data.get("product_id")
    store_id = data.get("store_id")

    if not (price and product_id and store_id):
        return make_response({"errors": ["validation errors"]}, 400)
    
    try:
        new_store_product = StoreProduct(price=price, product_id=product_id, store_id=store_id)
        db.session.add(new_store_product)
        db.session.commit()

        store = Store.query.filter(Store.id == store_id).first()
        product = Product.query.filter(Product.id == product_id).first()
        response_data = {
            "id": new_store_product.id,
            "price": new_store_product.price,
            "product_id": new_store_product.product_id,
            "store_id": new_store_product.store_id,
            "product": {
                "id": product.id,
                "name": product.name,
                "description": product.description,
            },
            "store": {
                "id": store.id,
                "name": store.name,
                "address": store.address,
            },
        }
        return make_response(response_data, 201)
    except ValueError:
        return make_response({"errors": ["validation errors"]}, 400)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
