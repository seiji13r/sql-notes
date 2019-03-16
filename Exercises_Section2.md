# SQL Exercises Part 2 <!-- omit in toc -->

- [Introduction](#introduction)
- [Topics Section 1](#topics-section-1)
- [Questions](#questions)
  - [Solutions](#solutions)
- [Assessment](#assessment)
  - [Solutions](#solutions-1)

# Introduction

All the Following Exercises have been done using the sample database Sakila, Pakila or DVDRental

# Topics Section 1

* AS STATEMENT
* INNER JOIN
* UNION

  
# Questions

1. Change payment_id column name to id in the SELECT statement
2. Get the totals payments per customer and show that column as total.
3. Get the Information (First, Last Name and Email) Attached in the payment table.
4. From the previous Exercise use a Filtering and Ordering Clause
5. From the previous Exercise get also de total payment per Customer.
6. From the previous Exercise get also de customer address and district with a second Join clause.
7. Using Join get the staff name per payment.
8. Get the Film titles and language of it.
   
## Solutions

```sql
-- Change payment_id column name to id in the SELECT statement
SELECT payment_id AS id FROM payment;

-- Get the totals payments per customer and show that column as total.
SELECT customer_id, SUM(amount) AS total FROM payment GROUP BY customer_id ORDER BY total DESC;

-- Get the Information (First, Last Name and Email) Attached in the payment table.
SELECT P.payment_id, C.first_name, C.last_name, C.email, P.amount
FROM payment AS P
INNER JOIN customer AS C
ON P.customer_id = C.customer_id

-- From the previous Exercise use a Filtering and Ordering Clause
SELECT P.payment_id, C.first_name, C.last_name, C.email, P.amount
FROM payment AS P
INNER JOIN customer AS C
ON P.customer_id = C.customer_id
WHERE C.first_name LIKE '%en%'
ORDER BY C.last_name ASC

-- From the previous Exercise get also de total payment per Customer.
SELECT customer_id, customer.first_name, customer.last_name, total
FROM (
	SELECT customer_id, SUM(amount) AS total
	FROM payment
	GROUP BY customer_id
) AS totals
INNER JOIN customer
ON totals.customer_id = customer.customer_id
ORDER BY customer.last_name ASC, totals.total DESC;

-- From the previous Exercise get also de customer address and district with a second Join clause.
SELECT totals.customer_id, customer.first_name, customer.last_name, address.address, address.district, total
FROM (
	SELECT customer_id, SUM(amount) AS total
	FROM payment
	GROUP BY customer_id
) AS totals
INNER JOIN customer
ON totals.customer_id = customer.customer_id
INNER JOIN address
ON customer.address_id = address.address_id
ORDER BY totals.total DESC, customer.last_name ASC;

-- Using Join get the staff name per payment.
SELECT payment.payment_id, staff.first_name, staff.last_name, payment.amount
FROM payment
INNER JOIN staff ON payment.staff_id = staff.staff_id

-- How many copies of each movie are in store 1
SELECT film.title, COUNT(title) as total
FROM inventory
INNER JOIN film ON inventory.film_id = film.film_id
WHERE store_id = 1
GROUP BY film.title
ORDER BY total DESC;

-- Get the Film titles and language of it.
SELECT film.title, language.name AS movie_language
FROM film
INNER JOIN language
ON film.language_id = language.language_id;

```

# Assessment


## Solutions

```sql

```