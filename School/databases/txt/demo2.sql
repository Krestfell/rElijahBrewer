SELECT
    vendors.vendor_id,
    vendors.vendor_name,
    invoices.invoice_total
FROM
    vendors AS V
LEFT JOIN
    invoices AS i
ON
    v.vendor_id = i.vendor_id
ORDER BY
    vendor_name;