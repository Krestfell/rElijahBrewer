SELECT
    v.vendor_id,
    v.vendor_name,
    v.vendor_state,
    i.invoice_id,
    i.invoice_total,
    invoice_line_items.line_item_amount,
    general_ledger_accounts.account_description
FROM
    vendors AS v
    JOIN
    invoices AS i
    ON
        v.vendor_id = invoices.vendor_id
    JOIN
    invoice_line_items
    ON
        i.invoice_id = invoice_line_items.invoice_id
    JOIN
    general_ledger_accounts
    ON
        invoice_line_items.account_number = general_ledger_accounts.account_number
WHERE
    vendor_state IN ("CA", "NY", "WI")
HAVING
    outstanding > 0
ORDER BY
    vendor_name;