Industry Intelligence Python Backend Test

Objective:
REST API for managing category tree. 

Tasks:
- :Create a table in Postgres to keep the data that user enter.
- :Create a REST API for display, save, delete and update the data.

API endpoint: /web/category

1. GET
Output:
- :tree (array of item)
- :item model:
    - :id (number)
    - :name (string)
    - :level (number)
    - :children (array of item)

2. POST:
Input:
- :name (string/required)
- :parent (number)
Output:
- :status (boolean)

3. PUT:
Input:
- :id (number/required)
- :name (string/required)
Output:
- :status (boolean)

4. DELETE:
Input:
- :id (number/required)
Output:
- :status (boolean)

Development setup:
- :execute `docker-compose -f docker-compose.yml up`

Postgres Info:
- :Host: `localhost`
- :Port: `5432`
- :Database name: `i2`
- :Database username: `i2fwd`
- :Database password: `i2fwd`
