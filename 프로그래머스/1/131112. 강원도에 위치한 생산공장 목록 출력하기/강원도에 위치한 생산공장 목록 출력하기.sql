SELECT factory_id, factory_name, address FROM FOOD_FACTORY
WHERE SUBSTR(address,1,3) = '강원도'
ORDER BY factory_id asc
