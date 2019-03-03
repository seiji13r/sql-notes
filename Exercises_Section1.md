# SQL Exercises <!-- omit in toc -->

- [Introduction](#introduction)
- [Topics Section 1](#topics-section-1)
- [Questions](#questions)
  - [Solutions](#solutions)
- [Assessment](#assessment)
  - [Solutions](#solutions-1)

# Introduction

All the Following Exercises have been done using the sample database Sakila, Pakila or DVDRental

# Topics Section 1

* SELECT
* SELECT DISTINCT
* SELECT ... WHERE
* COUNT
* COUNT ... DISTINCT
* LIMIT
* ORDER BY ... ASC or DESC
* WHERE ... BETWEEN
* WHERE ... BETWEEN [LOW] AND [HIGH]
* WHERE ... NOT BETWEEN [LOW] AND [HIGH]
* WHERE ... IN
* WHERE ... LIKE
* AGGREGATE FUNCTIONS [COUNT, MIN, MAX, AVG, SUM]
* GROUP BY
* HAVING
  
# Questions

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
25. Get the total payments amount from each customer.
26. Get the total payments transactions processed by staff_id;
27. Get the amount of films per rating.
28. Get the rental durations occurrence.
29. Get the average rental rate per film rating.
30. How many payments transactions and amounts did each staff member handle.
31. Get the average replacement cost of movies by rating.
32. Get the Top 5 spender customers.
33. Get all the customers that spend more that $200
34. Get the Store which total customer is greater than 300.
35. From the rating R, G and PG get the rates which rental_rate average is lower than 3.
36. What customers has at least total of 40 transactions.
37. What movie ratings have an average duration of more than 5 days.

## Solutions

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

-- Get the total payments amount from each customer.
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id;

-- Get the total payments transactions processed by staff_id;
SELECT staff_id, COUNT(*) FROM payment GROUP BY staff_id;

-- Get the amount of films per rating.
SELECT rating, COUNT(*) FROM film GROUP BY rating ORDER BY count DESC;

-- Get the rental durations occurrence
SELECT rental_duration, COUNT(*) FROM film GROUP BY rental_duration ORDER BY COUNT(*) DESC;

-- Get the average rental rate per film rating.
SELECT rating, ROUND(AVG(rental_rate),2) FROM film GROUP BY rating ORDER BY AVG(rental_rate) DESC;

-- How many payments transactions and amounts did each staff member handle.
SELECT staff_id, COUNT(*), SUM(amount) FROM payment GROUP BY staff_id;

-- Get the average replacement cost of movies by rating.
SELECT rating, ROUND(AVG(replacement_cost),2) FROM film GROUP BY rating ORDER BY AVG(replacement_cost) DESC;

-- Get the Top 5 spender customers.
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id ORDER BY SUM(amount) DESC LIMIT 5;

-- Get all the customers that spend more that $200
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id HAVING SUM(amount) > 200;

-- Get the Store which total customer is greater than 300
SELECT store_id, COUNT(*) FROM customer GROUP BY store_id HAVING COUNT(*) > 300;

-- From the rating R, G and PG get the rates which rental_rate average is lower than 3.
SELECT rating, AVG(rental_rate)
FROM film
WHERE rating IN ('R', 'G', 'PG')
GROUP BY rating
HAVING AVG(rental_rate) < 3;

-- What customers has at least total of 40 transactions.
SELECT customer_id, COUNT(amount)
FROM payment
GROUP BY customer_id
HAVING COUNT(amount)>=40;

-- What movie ratings have an average duration of more than 5 days.
SELECT rating, AVG(rental_duration)
FROM film
GROUP BY rating
HAVING AVG(rental_duration)>5;

```

# Assessment

1. Return the customer IDs of customers who have spent at least $110 with the staff member who has an ID of 2.

The answer should be customers 187 and 148.

2. How many films begin with the letter J?

The answer should be 20.

3. What customer has the highest customer ID number whose name starts with an 'E' and has an address ID lower than 500?


## Solutions

```sql
SELECT customer_id, SUM(amount) FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) >= 110
ORDER BY SUM(amount) ASC;

SELECT COUNT(*) FROM film WHERE title LIKE 'J%'

SELECT * 
FROM customer
WHERE first_name LIKE 'E%' AND address_id < 500
ORDER BY customer_id DESC
LIMIT 1;
```