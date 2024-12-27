# Flask E-commerce API for Customer and Product Management

## Customer Management

### Create Customer
```python
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone_number=data['phone_number']
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### Read Customer
```python
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify({
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
        'phone_number': customer.phone_number
    }), 200
```

### Update Customer
```python
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    try:
        data = request.get_json()
        customer = Customer.query.get_or_404(id)
        customer.name = data.get('name', customer.name)
        customer.email = data.get('email', customer.email)
        customer.phone_number = data.get('phone_number', customer.phone_number)
        db.session.commit()
        return jsonify({'message': 'Customer updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### Delete Customer
```python
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully!'}), 200
```

## Customer Account Management

### Create Customer Account
```python
@app.route('/customer-accounts', methods=['POST'])
def create_customer_account():
    try:
        data = request.get_json()
        new_account = CustomerAccount(
            username=data['username'],
            password=generate_password_hash(data['password']),
            customer_id=data['customer_id']
        )
        db.session.add(new_account)
        db.session.commit()
        return jsonify({'message': 'Customer account created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### Read Customer Account
```python
@app.route('/customer-accounts/<int:id>', methods=['GET'])
def get_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    return jsonify({
        'id': account.id,
        'username': account.username,
        'customer': {
            'id': account.customer.id,
            'name': account.customer.name,
            'email': account.customer.email
        }
    }), 200
```

### Update Customer Account
```python
@app.route('/customer-accounts/<int:id>', methods=['PUT'])
def update_customer_account(id):
    try:
        data = request.get_json()
        account = CustomerAccount.query.get_or_404(id)
        account.username = data.get('username', account.username)
        if 'password' in data:
            account.password = generate_password_hash(data['password'])
        db.session.commit()
        return jsonify({'message': 'Customer account updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### Delete Customer Account
```python
@app.route('/customer-accounts/<int:id>', methods=['DELETE'])
def delete_customer_account(id):
    account = CustomerAccount.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({'message': 'Customer account deleted successfully!'}), 200
```

## Product Management

### Create Product
```python
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        new_product = Product(
            name=data['name'],
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### Read Product
```python
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price
    }), 200
```

### Update Product
```python
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        data = request.get_json()
        product = Product.query.get_or_404(id)
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        db.session.commit()
        return jsonify({'message': 'Product updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

### Delete Product
```python
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'}), 200
```

### List Products
```python
@app.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    return jsonify([
        {'id': product.id, 'name': product.name, 'price': product.price}
        for product in products
    ]), 200
```
