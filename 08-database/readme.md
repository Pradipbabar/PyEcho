# Database Mastery

## Advanced SQL Concepts

### Subqueries

Subqueries are queries nested within another query, allowing for more complex and dynamic database operations.

```sql
-- Example: Subquery to find employees with salaries above the average
SELECT employee_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### JOIN Operations

JOIN operations are used to combine rows from two or more tables based on a related column between them.

```sql
-- Example: INNER JOIN to retrieve information from two tables
SELECT employees.employee_id, employees.employee_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;
```

### Indexing

Indexing is a technique to improve the speed of data retrieval operations on a database table.

```sql
-- Example: Creating an index on the 'email' column
CREATE INDEX idx_email ON users(email);
```

### Transactions

Transactions ensure the atomicity, consistency, isolation, and durability (ACID) properties of database operations.

```sql
-- Example: Beginning a transaction
BEGIN TRANSACTION;

-- SQL statements within the transaction

-- Example: Committing the transaction
COMMIT;
```

## Working with Multiple Databases

### PostgreSQL Example

#### Connecting to PostgreSQL

```python
import psycopg2

# Replace the placeholders with your database details
conn = psycopg2.connect(database="your_database", user="your_user", password="your_password", host="your_host", port="your_port")

# Create a cursor
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM your_table")

# Fetch the results
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()
```

### MySQL Example

#### Connecting to MySQL

```python
import mysql.connector

# Replace the placeholders with your database details
conn = mysql.connector.connect(host="your_host", user="your_user", password="your_password", database="your_database")

# Create a cursor
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM your_table")

# Fetch the results
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()
```

These examples cover advanced SQL concepts such as subqueries, JOIN operations, indexing, and transactions. Additionally, they demonstrate how to connect to PostgreSQL and MySQL databases using Python. Replace the placeholders with your actual database details when using these examples.