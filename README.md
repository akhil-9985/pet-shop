<p align="center">
  <h2 align="center"><a> petshop ecommerce </a></h2>
  <p align="center">An online store for pet accessories, including products for dogs, cats, and other pets. It offers items like toys, food, grooming supplies, and more. <p>
</p>

## :star: Highlights
- Product management (via admin route)
- Category management (via admin route)
- User management (via admin route)
- Shipping cart
- Checkout and payment
- Order management
- Search and filtering
- Product reviews and ratings
- Promotions and discounts
- Admin dashboard
- Responsive design and  email notifications

## Demo Images
![pet_shop7](https://github.com/user-attachments/assets/f417e026-e206-49e4-9413-b1b59f2432bd)
![pet_shop6](https://github.com/user-attachments/assets/ce3cdf5b-2699-4dac-8b5f-99abf4d79260)
![Screenshot_20250518_171414](https://github.com/user-attachments/assets/2a10329f-d4e7-4cd3-9dde-8a429118e883)

## Development

Clone the repository, install the dependencies and start the application

**_Code Setup_**
```bash

# Clone the repo
git clone https://github.com/Ramalalshmi6304/petshop_ecommerce
cd petshop_ecommerce

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# For Windows
cd venv
cd Scripts
.\activate.bat

# Install Requirements
pip install -r requirements.txt

# Create admin as superuser
python manage.py createsuperuser

# Enter the admin details to manage the users, groups products, orders, etc...
Example view:
Username (leave blank to use 'user'): admin
Email address: test@gmail.com
Password: 
Password (again): 
Superuser created successfully.

# Make necessary Migrations
python manage.py makemigrations
python manage.py migrate
```

**_Routes_**
- Admin Routes
  - http://127.0.0.1:8000/admin/ - Login with admin credentials that previously created
  - http://127.0.0.1:8000/admin/auth/user/ - Manage Normal users
  - http://127.0.0.1:8000/admin/auth/group/ - Manage Groups for staff like to manage products list (having certain previlege only)
  - http://127.0.0.1:8000/admin/shop/product/ - Able to add products with stocks, discount, price, name, description, etc
  - http://127.0.0.1:8000/admin/shop/category/ - Able to add Categories to a Product
  - http://127.0.0.1:8000/admin/shop/cartitem/ - Mange Cart Items for a user
  - http://127.0.0.1:8000/admin/shop/orderitem/ - Manage Order Items that a user is placed
  - http://127.0.0.1:8000/admin/shop/order/ - Manage Order List of a user

- User Routes
  - http://127.0.0.1:8000/ - homepage
  - http://127.0.0.1:8000/accounts/login/ - login page
  - http://127.0.0.1:8000/signup/ - register page
  - http://127.0.0.1:8000/profile/ - profile
  - http://127.0.0.1:8000/password-change/ - for chaning password (can be manage under admin route for user specific)
  - http://127.0.0.1:8000/cart/ - Cart list
  - http://127.0.0.1:8000/orders/ - Order History
  - http://127.0.0.1:8000/product/1/ - More about product details
  - http://127.0.0.1:8000/checkout/ - checkout and place order after selection
