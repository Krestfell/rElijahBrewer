--1
SELECT
    v.vendor_id,
    SUM( invoice_total )
FROM
    vendors AS v,
    invoices AS i
WHERE
    v.vendor_id = i.vendor_id
GROUP BY
    v.vendor_id;

--2
SELECT
    vendor_name,
    SUM(payment_total) AS payment_total_sum
FROM
    vendors AS v
    JOIN invoices AS i
    ON v.vendor_id = i.vendor_id
GROUP BY
    vendor_name
ORDER BY
    payment_total_sum DESC

--3
SELECT
    vendor_name,
    COUNT(*) AS invoice_count,
    SUM(invoice_total) AS invoice_total_sum
FROM
    vendors v
    JOIN
    invoices i
    ON
    v.vendor_id = i.vendor_id
GROUP BY
    vendor_name
ORDER BY
    invoice_count DESC

--4
SELECT
    account_description,
    COUNT(*) AS line_item_count,
    SUM(line_item_amount) AS line_item_amt_sum
FROM
    general_ledger_accounts gl
    JOIN
    invoice_line_items li
    ON
    gl.account_number = li.account_number
GROUP BY
    gl.account_description
HAVING
    COUNT(*) > 1
ORDER BY
    line_item_amt_sum DESC

--5
SELECT
    account_description,
    COUNT(*) AS line_item_count,
    SUM(line_item_amount) AS line_item_amt_sum
FROM
    general_ledger_accounts gl
    JOIN
    invoice_line_items li
    ON
    gl.account_number = li.account_number
    JOIN
    invoices i
    ON
    li.invoice_id = i.invoice_id
WHERE
    invoice_date BETWEEN '01-Apr-2014' AND '30-June-2014'
GROUP BY
    gl.account_description
HAVING
    COUNT(*) > 1
ORDER BY
    line_item_amt_sum DESC