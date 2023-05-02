# Industry Intelligence Python Backend Test #

## Objective: ##
- REST API for managing product category tree. 

## Tasks: ##
- Create single/one table in Postgres for the persistent storage.
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
- execute `docker-compose -f docker-compose.yml up`

## Postgres Info: ## 
- Host: `localhost`
- Port: `5432`
- Database name: `i2`
- Database username: `i2fwd`
- Database password: `i2fwd`
