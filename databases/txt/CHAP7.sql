-- 1
SELECT v.vendor_id,
    v.vendor_name,
    i.invoice_id,
    l.invoice_sequence,
    l.line_item_amount
FROM vendors AS v
NATURAL JOIN invoices AS i
NATURAL JOIN invoice_line_items AS l
WHERE i.invoice_id IN
(
        SELECT i.invoice_id
FROM invoice_line_items
WHERE invoice_sequence > 1
    );

-- 2
SELECT DISTINCT vendor_name
FROM vendors AS v
WHERE v.vendor_id IN (
        SELECT DISTINCT invoices.vendor_id
FROM invoices
    )
ORDER BY vendor_name;

-- 3
SELECT i.invoice_id,
    i.invoice_number,
    i.invoice_total,
    i.payment_total
FROM invoices AS i
WHERE i.payment_total > (
        SELECT AVG(i.payment_total) AS average
FROM invoices AS i
WHERE payment_total > 0
    );

-- 4
SELECT g.account_number,
    g.account_description
FROM general_ledger_accounts AS g
WHERE NOT EXISTS (
        SELECT DISTINCT account_number
FROM invoice_line_items AS l
WHERE l.account_number = g.account_number
    );

-- 5
SELECT
    v.vendor_id,
    v.vendor_name,
    i.invoice_id,
    i.invoice_total,
    i.payment_total,
    i.credit_total,
    (invoice_total - payment_total - credit_total) AS outstanding
FROM
    vendors AS v
    JOIN
    invoices AS i
    ON
    v.vendor_id = i.vendor_id
WHERE
    (invoice_total - payment_total - credit_total) >
        (SELECT AVG (invoice_total - payment_total - credit_total)
FROM invoices AS i
WHERE i.vendor_id = i.vendor_id)
ORDER BY
    vendor_id, invoice_total;