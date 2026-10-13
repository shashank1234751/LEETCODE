# Write your MySQL query statement below
select u.unique_id,e.name from Employees e LEFT join  EmployeeUNI u ON u.id =e.id 