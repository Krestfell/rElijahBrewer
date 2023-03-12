SELECT
    employees.employee_id,
    employees.last_name,
    employees.first_name,
    employees.manager_id,
    managers.employee_id,
    CONCAT(managers.last_name, " ", managers.first_name) AS manager
FROM
    employees
LEFT JOIN
    employees AS managers
ON
    employees.manager_id = managers.employee_id