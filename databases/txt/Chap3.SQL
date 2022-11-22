--3
SELECT
    v.vendor_id,
    v.vendor_name,
    v.vendor_state,
    v.vendor_zip_code
FROM
    vendors AS v;


--4
SELECT
    v.vendor_id,
    v.vendor_name,
    v.vendor_state,
    v.vendor_zip_code
FROM
    vendors AS v
WHERE
    v.vendor_state = 'CA';


--5
SELECT
    *
FROM
    invoices AS i
WHERE
    credit_total > 0;

--6
SELECT
    *
FROM
    invoice_line_items AS i
WHERE
    i.account_number = 553;

--7
SELECT
    *
FROM
    invoice_line_items AS i
WHERE
    i.line_item_amount > 2500.00;

--8
SELECT
    *
FROM
    invoices AS i
WHERE
    i.invoice_total > 2500.00;

--9
SELECT
    *
FROM
    vendors AS v
WHERE
    v.vendor_state = 'CA';

--10
SELECT
    g.account_number
FROM
    general_ledger_accounts AS g
WHERE
    account_number > 499 AND account_number < 600;