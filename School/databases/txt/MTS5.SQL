SELECT
    customers.customer_last_name,
    customers.customer_first_name,
    employees.last_name,
    employees.first_name,
    CONCAT (managers.last_name, " ", managers.first_name) AS manager_name
FROM
    employees
    JOIN
    employees AS managers
    ON
    employees.manager_id = managers.employee_id
    JOIN
    customers
    ON
    employees.last_name = customers.customer_last_name AND
        customers.first_name = customers.customer_first_name