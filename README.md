# Python Backend Test #

## Objective: ##
- REST API for managing product category tree. 

## Tasks: ##
- Create a REST API in Python to save, delete, update and display the data.
- Add the validation subcategory deep level. The maximum level is 3.    
- Test the API with Postman.

## API Info: ## 
- End point: /web/category

- GET
    - tree (array of item)
    - item model:
        - id (number)
        - name (string)
        - level (number)
        - children (array of item)

- POST
    - name (string/required)
    - parent (number)

- PUT
    - id (number/required)
    - name (string/required)

- DELETE
    - id (number/required)

## Development setup: ## 
- `docker-compose -f docker-compose.yml up`
- `pip install -r requirements.txt`
- `python init_db.py`

## Postgres / Database Info: ## 
- Host: `localhost`
- Port: `5432`
- DB name: `i2`
- DB user: `i2fwd`
- DB password: `i2fwd`
- Table: `Categories`
- Table sequence: `Category_Seq`