# Write your MySQL query statement below
SELECT p.product_name ,s.year,s.price from Product p right JOIN Sales s on s.product_id=p.product_id 