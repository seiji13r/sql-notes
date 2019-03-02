# SQL Exercises <!-- omit in toc -->

- [Introduction](#introduction)
- [SELECT](#select)
- [Solutions](#solutions)

# Introduction

All the Following Exercises have been done using the sample database Sakila, Pakila or DVDRental


# SELECT

1. Display the Unique rental Rates in Films
2. Display all customer emails.
3. Display the films rating types.
4. Display the Data of the customer named Jamie.
5. Display Payments between 1 and 8 USDs.
6. Display the description of Outlaw Hanky movie.
7. Get the phone number of the customer that lives in '259 Ipoh Drive'
8. Display the number of Customers.
9. Get the customer id numbers from the TOP 10 highest payments.
10. Get the titles of the Movies with film ids from 1 through 5.
11. Get all Payments greater or equal to 2.99 and lower or equal to 8.99
12. Get all Payments NOT greater or equal to 2.99 and lower or equal to 8.99
13. Get all Payments Performed Between Feb 07 2007 and Feb 15 2007
14. Get all rentals From customers (7, 3, 13).
15. Get all Payments equal to (2.99, 4.99, 10.99)
16. Get the customers with name beginning with Jen
17. Get the customers whose names end with 'y'
18. How many payment transactions are greater than $5.00
19. How many actors have a first name that starts with the petter P?
20. How many unique districts are our customers from?
21. Retrieve the list of names for those distinct districts from previous question.
22. How many films have a rating of R and replacement cost between $5 and $15?
23. How many films have the word truman somewhere in the title?
24. Get the Min, Max, Sum, Average and Count of payments.

# Solutions

```sql
-- Display the Unique rental Rates in Films
SELECT DISTINCT rental_rate FROM film;

-- Display all customer emails.
SELECT email FROM customer;

-- Get the customer id numbers from the TOP 10 highest payments.
SELECT  customer_id, amount FROM payment ORDER BY amount DESC, customer_id ASC LIMIT 10;

-- Get the titles of the Movies with film ids from 1 through 5.
SELECT film_id, title FROM film ORDER BY film_id ASC LIMIT 5;
SELECT film_id, title FROM film WHERE film_id >= 1 AND film_id <=5 ORDER BY film_id ASC;

-- Get all Payments greater or equal to 2.99 and lower or equal to 8.99
SELECT * FROM payment WHERE amount BETWEEN 2.99 AND 8.99 ORDER BY amount DESC;

-- Get all Payments NOT greater or equal to 2.99 and lower or equal to 8.99
SELECT * FROM payment WHERE amount NOT BETWEEN 2.99 AND 8.99 ORDER BY amount DESC;

-- Get all Payments Performed Between Feb 07 2007 and Feb 15 2007
SELECT * FROM payment WHERE payment_date BETWEEN '2007-02-07' AND '2007-02-15' ORDER BY payment_date DESC;

-- Get all rentals From customers (7, 3, 13).
SELECT *
FROM rental
WHERE customer_id IN (7, 3, 13)
ORDER BY customer_id DESC;

-- Get all Payments equal to (2.99, 4.99, 10.99)
SELECT *
FROM payment
WHERE amount IN (2.99, 4.99, 10.99)
ORDER BY amount DESC;

-- Get the customers with name beginning with Jen
SELECT * FROM customer WHERE first_name LIKE 'Jen%';

-- Get the customers whose names end with 'y'
SELECT * FROM customer WHERE first_name LIKE '%y';

-- How many payment transactions are greater than $5.00
SELECT COUNT(*) FROM payment WHERE amount > 5;

-- How many actors have a first name that starts with the petter P?
SELECT COUNT(first_name) FROM actor WHERE first_name LIKE 'P%';

-- How many unique districts are our customers from?
SELECT COUNT(DISTINCT district) FROM address;

-- Retrieve the list of names for those distinct districts from previous question
SELECT DISTINCT district FROM address ORDER BY district ASC;

-- How many films have a rating of R and replacement cost between $5 and $15?
SELECT COUNT(*) FROM film WHERE rating = 'R' AND replacement_cost BETWEEN 5 AND 15;

-- How many films have the word truman somewhere in the title?
SELECT * FROM film WHERE title ILIKE '%truman%';

-- Get the Min, Max, Sum, Average and Count of payments.
SELECT COUNT(amount) FROM payment;
SELECT MAX(amount) FROM payment;
SELECT MIN(amount) FROM payment;
SELECT SUM(amount) FROM payment;
SELECT AVG(amount) FROM payment;

```
