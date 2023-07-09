import json

import falcon

from connectDB import insert, select, update, delete

class Users:
    def on_get(self, req, resp):
        # user = req.media
        # print(user)
        query = f"SELECT * FROM _672020113_marketplace_users"

        data = select(query)

        # print(data)

        data_list = []

        for row in data:
            data_list.append({
                'username': row[0],
                'password': row[1],
                'email': str(row[2]),
                'firstname': row[3],
                'lastname': row[4],
                'role': row[5],
                'status': 'Loged In'
            })


        # if len(data) != 0:
        #     for row in data:
        #         if user['password'] == row[1]:
        #             data_list.append({
        #                 'username': row[0],
        #                 'email': str(row[2]),
        #                 'firstname': row[3],
        #                 'lastname': row[4],
        #                 'role': row[5],
        #                 'status': 'Loged In'
        #             })
        #         else:
        #             data_list.append({
        #                 'status': 'Failed Login'
        #             })


        resp_data = json.loads(json.dumps(data_list))

        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        new_users = req.media
        users_ref = db.collection('users')
        users_ref.document(new_users['id']).set(new_users)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        updated_users = req.media
        users_ref = db.collection('users')
        users_ref.document(updated_users['id']).update(updated_users)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, id):
        users_ref = db.collection('users')
        users_ref.document(id).delete()
        resp.status = falcon.HTTP_204


class Products:
    def on_get(self, req, resp):
        # Query
        query = "SELECT * FROM _672020113_marketplace_products"

        # Get data from postgres
        data = select(query)

        # Convert data list from postgres to dictionary
        data_list = []
        for row in data:
            data_list.append({
                'products_id': row[0],
                'name': row[1],
                'brand': row[2],
                'price': str(row[3]),
                'description': row[4],
                'status': row[5]
            })

        # Convert data dictionary to json string and convert again to json
        resp_data = json.loads(json.dumps(data_list))

        # Send respon to front-end
        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        # Request product from front-end
        new_product = req.media

        # Create query
        query = f"INSERT INTO _672020113_marketplace_products (products_id, name, brand, price, description, status) VALUES ('{new_product['products_id']}', '{new_product['name']}', '{new_product['brand']}', {new_product['price']}, '{new_product['description']}', '{new_product['status']}');"

        # Insert query into postgre
        insert(query)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        updated_product = req.media

        query = f"UPDATE _672020113_marketplace_products SET name = '{updated_product['name']}', brand = '{updated_product['brand']}', price = {updated_product['price']}, description = '{updated_product['description']}', status = '{updated_product['status']}' WHERE products_id = '{updated_product['products_id']}'"

        update(query)

        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        delete_products = req.media

        query = f"DELETE FROM _672020113_marketplace_products WHERE products_id = '{delete_products['products_id']}'"

        delete(query)

        resp.status = falcon.HTTP_204


class Stocks:
    def on_get(self, req, resp):
        # Query
        query = "SELECT * FROM _672020113_marketplace_stocks ORDER BY size ASC"

        # Get data from postgres
        data = select(query)

        # Convert data list from postgres to dictionary
        data_list = []
        for row in data:
            data_list.append({
                'stocks_id': row[0],
                'size': row[1],
                'stock': row[2],
                'products_id': row[3],
                'last_updated': str(row[4])
            })

        # Convert data dictionary to json string and convert again to json
        resp_data = json.loads(json.dumps(data_list))

        # Send respon to front-end
        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        new_stock = req.media
        query = f"INSERT INTO _672020113_marketplace_stocks (stocks_id, size, stock, products_id, last_updated) VALUES ('{new_stock['stocks_id']}', '{new_stock['size']}', {new_stock['stock']}, '{new_stock['products_id']}', '{new_stock['last_updated']}');"
        insert(query)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        updated_stock = req.media

        query = f"UPDATE _672020113_marketplace_stocks SET stock = '{updated_stock['stock']}', last_updated = '{updated_stock['last_updated']}' WHERE stocks_id = '{updated_stock['stocks_id']}' AND size = '{updated_stock['size']}'"

        update(query)

        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        delete_stocks = req.media

        query = f"DELETE FROM _672020113_marketplace_stocks WHERE products_id = '{delete_stocks['products_id']}'"

        delete(query)

        resp.status = falcon.HTTP_204


class Carts:
    def on_get(self, req, resp):
        # Query
        query = "SELECT * FROM _672020113_marketplace_carts"

        # Get data from postgres
        data = select(query)

        # Convert data list from postgres to dictionary
        data_list = []
        for row in data:
            data_list.append({
                'cart_id': row[0],
                'username': row[1],
                'products_id': row[2],
                'cart_status': row[3],
                'size': row[4]
            })

        # Convert data dictionary to json string and convert again to json
        resp_data = json.loads(json.dumps(data_list))

        # Send respon to front-end
        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        # Request product from front-end
        new_cart = req.media

        # Create query
        query = f"INSERT INTO _672020113_marketplace_carts (cart_id, username, products_id, cart_status, size) VALUES ('{new_cart['cart_id']}', '{new_cart['username']}', '{new_cart['products_id']}', '{new_cart['cart_status']}', '{new_cart['size']}')"

        # Insert query into postgre
        insert(query)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        updated_cart = req.media

        query = f"UPDATE _672020113_marketplace_carts SET cart_status = '{updated_cart['cart_status']}' WHERE cart_id = '{updated_cart['cart_id']}'"

        update(query)

        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        delete_cart = req.media

        query = f"DELETE FROM _672020113_marketplace_carts WHERE cart_id = '{delete_cart['cart_id']}'"

        delete(query)

        resp.status = falcon.HTTP_204


class Orders:
    def on_get(self, req, resp):
        # Query
        query = "SELECT * FROM _672020113_marketplace_orders ORDER BY order_datetime DESC;"

        # Get data from postgres
        data = select(query)

        # Convert data list from postgres to dictionary
        data_list = []
        for row in data:
            data_list.append({
                'order_id': row[0],
                'username': row[1],
                'subtotal': str(row[2]),
                'order_status': row[3],
                'order_datetime': str(row[4]),
                'verif_image': str(row[5]),
                'resi': row[6]
            })

        # Convert data dictionary to json string and convert again to json
        resp_data = json.loads(json.dumps(data_list))

        # Send respon to front-end
        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        # Request product from front-end
        new_orders = req.media

        # Create query
        query = f"INSERT INTO _672020113_marketplace_orders (order_id, username, subtotal, order_status, order_datetime, verif_image, resi) VALUES ('{new_orders['order_id']}', '{new_orders['username']}', '{new_orders['subtotal']}', '{new_orders['order_status']}', '{new_orders['order_datetime']}', '{new_orders['verif_image']}', '{new_orders['resi']}')"

        # Insert query into postgre
        insert(query)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        updated_order = req.media

        query = f"UPDATE _672020113_marketplace_orders SET order_status = '{updated_order['order_status']}', subtotal = {updated_order['subtotal']}, verif_image = '{updated_order['verif_image']}', resi = '{updated_order['resi']}' WHERE order_id = '{updated_order['order_id']}'"

        update(query)

        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        delete_order = req.media

        query = f"DELETE FROM _672020113_marketplace_orders WHERE order_id = '{delete_order['order_id']}'"

        delete(query)

        resp.status = falcon.HTTP_204


class Ordered_Products:
    def on_get(self, req, resp):
        # Query
        query = "SELECT * FROM _672020113_marketplace_ordered_products"

        # Get data from postgres
        data = select(query)

        # Convert data list from postgres to dictionary
        data_list = []
        for row in data:
            data_list.append({
                'op_id': row[0],
                'products_id': row[1],
                'price': str(row[2]),
                'size': row[3],
                'order_id': row[4],
                'name': row[5]
            })

        # Convert data dictionary to json string and convert again to json
        resp_data = json.loads(json.dumps(data_list))

        # Send respon to front-end
        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        # Request product from front-end
        new_op = req.media

        # Create query
        query = f"INSERT INTO _672020113_marketplace_ordered_products (op_id, products_id, price, size, order_id, name) VALUES ('{new_op['op_id']}', '{new_op['products_id']}', {new_op['price']}, '{new_op['size']}', '{new_op['order_id']}', '{new_op['name']}')"

        # Insert query into postgre
        insert(query)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        updated_op = req.media

        query = f"UPDATE _672020113_marketplace_ordered_products SET name = '{updated_op['name']}' WHERE order_id = '{updated_op['op_id']}'"

        update(query)

        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        delete_op = req.media

        query = f"DELETE FROM _672020113_marketplace_ordered_products WHERE op_id = '{delete_op['op_id']}'"

        delete(query)

        resp.status = falcon.HTTP_204


class Images:
    def on_get(self, req, resp):
        # Query
        query = "SELECT * FROM _672020113_marketplace_images"

        # Get data from postgres
        data = select(query)

        # Convert data list from postgres to dictionary
        data_list = []
        for row in data:
            data_list.append({
                'image_url': row[0],
                'products_id': row[1]
            })

        # Convert data dictionary to json string and convert again to json
        resp_data = json.loads(json.dumps(data_list))

        # Send respon to front-end
        resp.media = resp_data
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        # Request product from front-end
        new_image = req.media

        # Create query
        query = f"INSERT INTO _672020113_marketplace_images (image_url, products_id) VALUES ('{new_image['image_url']}', '{new_image['products_id']}')"

        # Insert query into postgre
        insert(query)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        delete_image = req.media

        query = f"DELETE FROM _672020113_marketplace_images WHERE products_id = '{delete_image['products_id']}'"

        delete(query)

        resp.status = falcon.HTTP_204


class Coba:
    def on_get(self, req, resp):
        query = "SELECT current_date"
        data = select(query)
        resp.text = str(data)
        resp.status = falcon.HTTP_200


app = falcon.App()

app.add_route('/products', Products())
app.add_route('/users', Users())
app.add_route('/stocks', Stocks())
app.add_route('/carts', Carts())
app.add_route('/orders', Orders())
app.add_route('/ordered-products', Ordered_Products())
app.add_route('/images', Images())
app.add_route('/coba', Coba())
