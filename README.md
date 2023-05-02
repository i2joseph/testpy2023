# Industry Intelligence Python Backend Test #

## Objective: ##
- REST API for managing category tree. 

## Tasks: ##
- Create a table in Postgres to keep the data that user enter.
- Create a REST API for display, save, delete and update the data.

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
