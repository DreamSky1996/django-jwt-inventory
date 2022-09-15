## CONFIG
in the setting.py of inventory folder
Please set config
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database-name', 
        'USER': 'username', 
        'PASSWORD': 'password',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```
## INSTALL & RUN
```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Set User
1. http://127.0.0.1:8000/admin/
2. login with superuser
3. add user (name and password)

# Test Token service
1. Endpoint A - token with `read_product` permission
```
curl -X POST http://127.0.0.1:8000/api/token/read_product/ -H "content-type: application/json"   -d "{ \"username\": \"{username}\",\"password\": \"{password}\"}"
```
2. Endpoint B - token with `manage_product` permission
```
curl -X POST http://127.0.0.1:8000/api/token/manage_product/ -H "content-type: application/json"   -d "{ \"username\": \"{username}\",\"password\": \"{password}\"}"
```
3. Endpoint C - token with both: `read_product` and `manage_product` permission
```
curl -X POST http://127.0.0.1:8000/api/token/read_manage_product/ -H "content-type: application/json"   -d "{ \"username\": \"{username}\",\"password\": \"{password}\"}"
```
4. Endpoint D - token with `admin` permission
```
curl -X POST http://127.0.0.1:8000/api/token/admin/ -H "content-type: application/json"   -d "{ \"username\": \"{username}\",\"password\": \"{password}\"}"
```

You can get access token from above command.

# Products service
1. Get all product
```
curl --location --request GET http://127.0.0.1:8000/api/v1/products/ --header "Authorization:Bearer {token}"
```
2. Get product from id
```
curl --location --request GET http://127.0.0.1:8000/api/v1/products/{product_id}/ --header "Authorization:Bearer {token}"
```
3. Update product
```
curl --request PUT "http://127.0.0.1:8000/api/v1/products-update/{product_id}/" --header "Authorization: Bearer {token}" --header "Content-Type: application/x-www-form-urlencoded" --data-urlencode "data={updateData}"
```

4. create product
```
curl --location --request POST http://127.0.0.1:8000/api/v1/products-create/ --header "Authorization: Bearer {token}" --header "Content-Type: application/x-www-form-urlencoded" --data-urlencode "data={new_product_data}"
```

5. delete product (soft)
```
curl --location --request GET http://127.0.0.1:8000/api/v1/products-soft-del/{product_id}/ --header "Authorization: Bearer {token}"
```

6. delete product (hard)
```
curl --location --request DELETE http://127.0.0.1:8000/api/v1/products-hard-del/{product_id}/ --header "Authorization: Bearer {token}"
```

# UNIT TEST
```
python manage.py test
```

# DOCKER
```
docker-compose up
```

`You have to migrate and create superuser and user(for test).`