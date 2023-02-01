select * from table where name = 'James';

select * from Customers;

-- this is a comment

select avg(price) from products
/*
 * Multi line
 select * where test is not uppercase;
 * Comments!
 */
where productID = 15 or productID < 2;
