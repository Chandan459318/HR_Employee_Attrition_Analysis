CREATE DATABASE hr_attrition;
USE hr_attrition;

CREATE TABLE employee_attrition (
    employee_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    department VARCHAR(20),
    job_role VARCHAR(20),
    monthly_income DECIMAL(10,2),
    years_at_company INT,
    job_satisfaction INT,
    work_life_balance INT,
    overtime VARCHAR(3),
    education_level VARCHAR(20),
    marital_status VARCHAR(10),
    attrition VARCHAR(3)
);

SELECT * FROM employee_attrition LIMIT 10;

SELECT 
    (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) 
    AS attrition_rate_percentage
FROM employee_attrition;

SELECT department, 
       COUNT(*) AS total_employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS attrition_rate
FROM employee_attrition
GROUP BY department
ORDER BY attrition_rate DESC;

SELECT attrition, AVG(monthly_income) AS avg_income
FROM employee_attrition
GROUP BY attrition;

SELECT job_role, 
       COUNT(*) AS total_employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS attrition_rate
FROM employee_attrition
GROUP BY job_role
ORDER BY attrition_rate DESC;

SELECT work_life_balance, 
       COUNT(*) AS total_employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS attrition_rate
FROM employee_attrition
GROUP BY work_life_balance
ORDER BY work_life_balance ASC;

SELECT overtime, 
       COUNT(*) AS total_employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS attrition_rate
FROM employee_attrition
GROUP BY overtime;

SELECT job_satisfaction, 
       COUNT(*) AS total_employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       (SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS attrition_rate
FROM employee_attrition
GROUP BY job_satisfaction
ORDER BY job_satisfaction ASC;
