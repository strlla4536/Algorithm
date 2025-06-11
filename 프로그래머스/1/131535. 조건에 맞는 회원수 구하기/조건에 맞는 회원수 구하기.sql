-- 코드를 입력하세요
SELECT COUNT(*) as USERS FROM user_info
WHERE (date_format(joined, '%Y') = '2021')
    AND (age between 20 and 29)