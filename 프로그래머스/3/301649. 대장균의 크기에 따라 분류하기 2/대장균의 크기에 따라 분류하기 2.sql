SELECT 
    id,
    CASE
        WHEN NTILE(4) OVER (ORDER BY size_of_colony DESC) = 1 THEN 'CRITICAL'
        WHEN NTILE(4) OVER (ORDER BY size_of_colony DESC) = 2 THEN 'HIGH'
        WHEN NTILE(4) OVER (ORDER BY size_of_colony DESC) = 3 THEN 'MEDIUM'
        WHEN NTILE(4) OVER (ORDER BY size_of_colony DESC) = 4 THEN 'LOW'
    END AS colony_name
FROM ecoli_data
ORDER BY id ASC