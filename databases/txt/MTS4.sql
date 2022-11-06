SELECT
    vendors.vendor_id,
    vendors.vendor_name,
    invoices.invoice_id,
    invoices.invoice_number,
    invoices.invoice_total,
	invoices.payment_total,
	invoices.credit_total,
	invoice_line_items.invoice_sequence, 
	invoices.invoice_date,
	invoice_line_items.line_item_amount,
	invoice_line_items.line_item_description,
	general_ledger_accounts.account_description 
    (invoice_total - payment_total - credit_total) AS outstanding
FROM
    vendors
JOIN
    invoices
ON
    vendors.vendor_id = invoices.vendor_id
JOIN
    invoice_line_items
ON
    invoices.invoice_id = invoice_line_items.invoice_id
JOIN
    general_ledger_accounts
ON
    invoice_line_items.account_number = general_ledger_accounts.account_number
WHERE
    (invoice_total - payment_total - credit_total) > 0