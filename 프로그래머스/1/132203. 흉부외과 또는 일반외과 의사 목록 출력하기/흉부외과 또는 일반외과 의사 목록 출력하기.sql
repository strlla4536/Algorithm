SELECT dr_name, dr_id, mcdp_cd, DATE_FORMAT(hire_ymd,'%Y-%m-%d') as HIRE_YMD
FROM doctor
WHERE mcdp_cd IN ('CS', 'GS')
ORDER BY hire_ymd desc, dr_name asc;