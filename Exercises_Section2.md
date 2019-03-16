# SQL Exercises Part 2 <!-- omit in toc -->

- [Introduction](#introduction)
- [Topics Section 1](#topics-section-1)
- [Questions](#questions)
	- [Solutions](#solutions)
- [Assessment](#assessment)
	- [Import the Data required for the assessment questions.](#import-the-data-required-for-the-assessment-questions)
	- [Solutions](#solutions-1)

# Introduction

All the Following Exercises have been done using the sample database Sakila, Pakila or DVDRental

# Topics Section 1

* AS STATEMENT
* INNER JOIN
* LEFT JOIN, RIGHT JOIN
* UNION
* Timestamps and the EXTRACT function
* Mathematical Functions
* String Functions and Operators
* SubQuery
* Self-Join

  
# Questions

1. Change payment_id column name to id in the SELECT statement
2. Get the totals payments per customer and show that column as total.
3. Get the Information (First, Last Name and Email) Attached in the payment table.
4. From the previous Exercise use a Filtering and Ordering Clause
5. From the previous Exercise get also de total payment per Customer.
6. From the previous Exercise get also de customer address and district with a second Join clause.
7. Using Join get the staff name per payment.
8. Get the Film titles and language of it.
9. Find what Films are not in the Inventory.
10. Using EXTRACT, get the day of the payment and the customer_id.
11. Get the total amount per Month.
12. Find the rental films whose rental rate is higher than the average rental rate.
13. Find all the film titles that where rented between '2005-05-29' and '2005-05-30'
14. Using Self Join Find all Customers which last name matches the first name of other customer.
   
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

-- Find what Films are not in the Inventory
SELECT film.film_id, film.title, inventory_id
FROM film
LEFT OUTER JOIN inventory
ON inventory.film_id = film.film_id
WHERE inventory.film_id IS NULL
ORDER BY film.title ASC;

-- Using EXTRACT, get the day of the payment.
SELECT customer_id, EXTRACT(day from payment_date) AS day FROM payment;

-- Get the total amount per Month.
SELECT EXTRACT(month from payment_date) AS month, SUM(amount) AS total FROM payment GROUP BY month ORDER BY total DESC;

-- Find the rental films whose rental rate is higher than the average rental rate.
SELECT title, rental_rate FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- Find all the film titles that where rented between '2005-05-29' and '2005-05-30'
SELECT film.film_id, film.title
FROM film
WHERE film.film_id IN 
(
	SELECT inventory.film_id
	FROM rental
	INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
	WHERE rental.rental_date BETWEEN '2005-05-29' AND '2005-05-30'
)

-- Using Self Join Find all Employees with same location as Joe.
SELECT a.first_name, a.last_name, b.first_name, b.last_name
FROM customer AS a, customer AS b
WHERE a.first_name = b.last_name;

SELECT a.first_name, a.last_name, b.first_name, b.last_name
FROM customer AS a
INNER JOIN customer AS b
ON a.first_name = b.last_name;
```

# Assessment

## Import the Data required for the assessment questions.

* Create the Exercises Database
* Import exercise.tar file

```bash
pg_restore -h localhost -U pgremote -d exercises -v /home/ubuntu/exercises.tar
```

1. How can you retrieve all the information from the cd.facilities table?
2. You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?
3. How can you produce a list of facilities that charge a fee to members?
4. How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.
5. How can you produce a list of all facilities with the word 'Tennis' in their name?
6. How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
7. How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.
8. How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
9. You'd like to get the signup date of your last member. How can you retrieve this information?
10. Produce a count of the number of facilities that have a cost to guests of 10 or more.
11. Skip this one, no question for #11.
12. Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.
13. Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and total slots, sorted by facility id.
14. How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
15. How can you produce a list of the start times for bookings by members named 'David Farrell'?

## Solutions

```sql
-- 1. How can you retrieve all the information from the cd.facilities table?

-- 2. You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?

-- 3. How can you produce a list of facilities that charge a fee to members?

-- 4. How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

-- 5. How can you produce a list of all facilities with the word 'Tennis' in their name?

-- 6. How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

-- 7. How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.

-- 8. How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.

-- 9. You'd like to get the signup date of your last member. How can you retrieve this information?

-- 10. Produce a count of the number of facilities that have a cost to guests of 10 or more.

-- 11. Skip this one, no question for #11.

-- 12. Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.

-- 13. Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and total slots, sorted by facility id.

-- 14. How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.

-- 15. How can you produce a list of the start times for bookings by members named 'David Farrell'?

```