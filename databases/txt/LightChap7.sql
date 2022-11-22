SELECT
    vendor_state, MAX(sum_of_invoices) AS max_sum_of_invoices,
    AVG(sum_of_invoices) AS averageTotal,
    MAX(sum_of_invoices) - AVG(sum_of_invoices) AS Diff
FROM (
SELECT v.vendor_state, v.vendor_id,
        SUM(i.invoice_total) AS sum_of_invoices
    FROM vendors v
        JOIN invoices i
        ON v.vendor
        )