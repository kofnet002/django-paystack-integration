# Django Paystack Integration

## Step 1
Create a paystack account ```https://paystack.com```

## Step 2
git clone the project ```git clone https://github.com/kofnet002/django-paystack-integration.git```

## Step 3
- navigate to the project folder ```cd django-paystack-integration```
- create a virtual environment ```python -m venv venv``` and activate it:
  - for linux base machine ```. venv/bin/activate```
  - for window base machine ``` venv\Scripts\activate```
- install the necessary requirements ```pip install -r requirements.txt```

## Step 4
- create a ```.env``` file in the base directory of the project
- create the following variables and replace them with the your paystack_secret and paystack_public, and any secret for the SECRET_KEY
  - ```SECRET_KEY=XXXXX```
  - ```PAYSTACK_SECRET_KEY=XXXXX```
  - ```PAYSTACK_PUBLIC_KEY=XXXXX```

## Step 5
- create the neceseary migration:
- ```python manage.py makemigrations```
- ```python manage.py migrate```

## Step 6
run the application ```python manage.py runserver``` to get the application starting
you can create a superadmin to get access to the django admin dashboard ```python manage.py createsuperuser```, url ```127.0.0.1:8000/admin/```
