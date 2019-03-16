# SQL Topics  <!-- omit in toc -->

## Section 1

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

## Section 2

* AS STATEMENT
* INNER JOIN
* LEFT JOIN, RIGHT JOIN
* UNION
* Timestamps and the EXTRACT function
* Mathematical Functions
* String Functions and Operators
* SubQuery
* Self-Join



# IMPORTANT NOTES

## ORDER

In other DBMSs it is mandatory to include the column in the SELECT statement for example:

* RIGHT
  ```sql
  SELECT film_id, title FROM film ORDER BY film_id ASC LIMIT 5;
  ```
* WRONG
  ```sql
  SELECT title FROM film ORDER BY film_id ASC LIMIT 5;
  ```

In PostgreSQL both statements are valid.

## ... WHERE ... BETWEEN

... WHERE column BETWEEN [LOW] AND [HIGH]
Above Statement Means
... WHERE column >= [LOW] AND column <= [HIGH]

... WHERE column NOT BETWEEN [LOW] AND [HIGH]
Above Statement Means
... WHERE column < [LOW] OR column > [HIGH]

## WHERE ... LIKE

### WILDCARDS

**Percent** (%) for matching any sequence of characters.
**Underscore** (_) for matching any single Character.

**Examples:**
```sql
SELECT * FROM customer WHERE first_name LIKE 'Jen%';
SELECT * FROM customer WHERE first_name LIKE '%en%';
SELECT * FROM customer WHERE first_name LIKE '_en%';
```

**ILIKE** Case insensitive

## GROUP BY
### Without AGG Function

Without Aggregate Function, results in the same output as SELECT DISTINCT

```sql
SELECT column FROM table GROUP BY column;

SELECT DISTINCT column FROM table;
```

## INNER JOIN
### Syntax

```sql
SELECT A.pka, A.c1, A.pkb, B.c2
FROM A
INNER JOIN B ON A.pka = B.fkb
```

### Filtering and Ordering
All filtering and ordering clauses should be used after the Join
First filtering (WHERE) then ordering (ORDER BY)

```sql
SELECT A.pka, A.c1, A.pkb, B.c2
FROM A
INNER JOIN B ON A.pka = B.fkb
ORDER BY ...
WHERE ...
```

## LEFT JOIN

Left and Right Join help to find elements that are not present in other table.
Example: Find which movies/films are not in the inventory.

## Functions References

[PostgreSQL Aggregate Functions](https://www.postgresql.org/docs/10/functions-aggregate.html)

[PostgreSQL Date Time Functions](https://www.postgresql.org/docs/10/functions-datetime.html)

[PostgreSQL Math Functions](https://www.postgresql.org/docs/10/functions-math.html)

[PostgreSQL String Functions and Operators](https://www.postgresql.org/docs/10/functions-string.html)

## Further Investigation SELF JOIN

[Manager Employee Self Join Google Search](https://www.google.com/search?q=manager+employee+self+join&rlz=1C5CHFA_enMX808MX808&oq=manager+employee+sel&aqs=chrome.0.0j69i57j0l4.4150j0j7&sourceid=chrome&ie=UTF-8)