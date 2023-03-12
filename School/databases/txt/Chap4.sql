--1
SELECT
    v.vendor_id,
    v.vendor_name,
    i.invoice_id,
    i.invoice_number,
    i.invoice_date,
    l.invoice_sequence,
    l.line_item_amount,
    l.line_item_description
FROM
    vendors as v
    LEFT JOIN
    invoices as i
    ON
    v.vendor_id = i.vendor_id
    LEFT JOIN
    invoice_line_items as l
    ON
    i.invoice_id = l.invoice_id;

-- 2 !
SELECT
    v.vendor_id,
    v.vendor_name,
    i.invoice_id,
    i.invoice_number,
    i.invoice_date,
    l.invoice_sequence,
    l.line_item_amount,
    l.line_item_description,
    g.account_number,
    g.account_description
FROM
    vendors as v
    JOIN
    invoices as i
    ON
    v.vendor_id = i.vendor_id
    JOIN
    invoice_line_items as l
    ON
    i.invoice_id = l.invoice_id
    JOIN
    general_ledger_accounts as g
    ON
    l.account_description = g.account_description
WHERE
    invoice_date = 'May';


-- 3
SELECT
    e.employee_id,
    e.last_name,
    e.first_name,
    e.manager_id,
    m.employee_id,
    CONCAT (m.last_name, " ", m.first_name) AS manager
FROM
    employees AS e
    LEFT JOIN
    employees AS m
    ON
    e.manager_id = m.employee_id;

-- 4
SELECT
    v.vendor_id,
    v.vendor_name,
    i.invoice_id,
    i.invoice_number,
    i.invoice_total,
    i.payment_total,
    i.credit_total,
    i.invoice_date,
    l.invoice_sequence,
    l.line_item_amount,
    l.line_item_description,
    g.account_description,
    (invoice_total - payment_total - credit_total) AS outstanding
FROM
    vendors AS V
    JOIN
    invoices AS i
    ON
    v.vendor_id = i.vendor_id
    JOIN
    invoice_line_items AS l
    ON
    i.invoice_id = l.invoice_id
    JOIN
    general_ledger_accounts AS g
    ON
    l.account_number = g.account_number
WHERE
(invoice_total - payment_total - credit_total) > 0

-- 5
SELECT
    c.customer_last_name,
    c.customer_first_name,
    e.last_name,
    e.first_name,
    CONCAT(m.last_name, ", ", m.first_name) AS manager_name
FROM
    employees AS e
    JOIN
    employees AS m
    ON
        e.manager_id = m.employee_id
    JOIN
    customers AS c
    ON
    e.last_name = c.customer_last_name AND
        e.first_name = c.customer_first_name;