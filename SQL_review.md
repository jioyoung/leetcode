

# BASIC SQL


![ERD](erd.png)
## ORDER BY


1. Write a query to return the 10 earliest orders in the orders table. 
Include the id, occurred_at, and total_amt_usd.

```sql
SELECT id, occurred_at, total_amt_usd
FROM orders
ORDER BY occurred_at
LIMIT 10;
```

2. Write a query to return the top 5 orders in terms of largest 
total_amt_usd. Include the id, account_id, and total_amt_usd.
*/
```sql
SELECT total_amt_usd, id, account_id
FROM orders
ORDER BY total_amt_usd DESC
LIMIT 5;
```


3. Write a query to return the lowest 20 orders in terms of smallest total_amt_usd. 
Include the id, account_id, and total_amt_usd.
```sql
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd
LIMIT 20;
```

4. Write a query that displays the order ID, account ID, and total dollar amount 
for all the orders, sorted first by the account ID (in ascending order), 
and then by the total dollar amount (in descending order).

```sql
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY account_id, total_amt_usd DESC;
```

5. Now write a query that again displays order ID, account ID, and total dollar amount for each order, 
but this time sorted first by total dollar amount (in descending order), 
and then by account ID (in ascending order).
```sql
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC, account_id;
```

6. Compare the results of these two queries above. How are the results different when you 
switch the column you sort on first?

In query #5, all of the orders for each account ID are grouped together, and then within each of those groupings, the orders appear from the greatest order amount to the least. In query #6, since you sorted by the total dollar amount first, the orders appear from greatest to least regardless of which account ID they were from. Then they are sorted by account ID next.


## WHERE

### numeric data:
#### arithmatic operators: >, <, >=, <=, =. !=

### non-numeric data: 
1. = and !=  
2. **single quotes** (just be careful if you have quotes in the original text) with the text data, not double quotes. 
3. LIKE, NOT, or IN operators

#### Examples

1. Pulls the first 5 rows and all columns from the orders table that 
have a dollar amount of gloss_amt_usd greater than or equal to 1000.
```sql
SELECT *
FROM orders
WHERE gloss_amt_usd >= 1000
LIMIT 5;
```

2. Pulls the first 10 rows and all columns from the orders table that 
have a total_amt_usd less than 500.
```sql
SELECT *
FROM orders
WHERE gloss_amt_usd < 500
LIMIT 10;
```

3. Filter the accounts table to include the company name, website, and the primary point of contact (primary_poc) just for the Exxon Mobil company in the accounts table.
```sql
SELECT name, website, primary_poc
FROM accounts
WHERE name = 'Exxon Mobil';
```

## derived columns
1. Creating a new column that is a combination of existing columns is known as a **derived** column (or "calculated" or "computed" column). Usually you want to give a name, or "alias," to your new column using the AS keyword.

2. This derived column, and its alias, are generally only **temporary**, existing just for the duration of your query. The next time you run a query and access this table, the new column will not be there.

### Example
```sql
SELECT id, (standard_amt_usd/total_amt_usd)*100 AS std_percent, total_amt_usd
FROM orders
LIMIT 10;
```

1. Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order. Limit the results to the first 10 orders, and include the id and account_id fields.
```sql
SELECT standard_amt_usd/standard_qty AS unit_price, id, account_id
FROM orders
LIMIT 10;
```

2. write a query that finds the percentage of revenue that comes from poster paper for each order. You will need to use only the columns that end with _usd. (Try to do this without using the total column.) Display the id and account_id fields also. LIMIT 10 orders
```sql
SELECT id, account_id, 
   100*poster_amt_usd/(standard_amt_usd + gloss_amt_usd + poster_amt_usd) AS post_per
FROM orders
LIMIT 10;
```


Pay Attention to **Order of Operations** use parentheses if needed


### Logical Operators:
1. **LIKE**
This allows you to perform operations similar to using WHERE and =, but for cases when you might not know exactly what you are looking for.
   
#### Wildcard Characters in SQL Server
|Symbol|Description|Example|
|---|---|---|
|%|Represents zero or more characters|bl% finds bl, black, blue, and blob|
|_|Represents a single character|h_t finds hot, hat, and hit|
|[]|Represents any single character within the brackets|h[oa]t finds hot and hat, but not hit|
|^|Represents any character not in the brackets|h[^oa]t finds hit, but not hot and hat|
|-|Represents a range of characters|c[a-b]t finds cat and c|

There are two wildcards often used in conjunction with the LIKE operator:
1. **%** - The percent sign represents zero, one, or multiple characters
2. **_** - The underscore represents a single character


#### Examples

For accounts table:
1. All the companies whose names start with 'C'.
```sql
SELECT name
FROM accounts
where name LIKE 'C%';

```

2. All companies whose names contain the string 'one' somewhere in the name.
```sql
SELECT name
FROM accounts
where name LIKE '%one%';
```


3. All companies whose names end with 's'.
```sql
SELECT name
FROM accounts
where name LIKE '%s';
```

|LIKE Operator|	Description|
|---|---|
|WHERE CustomerName LIKE 'a%'	|Finds any values that start with "a"|
|WHERE CustomerName LIKE '%a'	|Finds any values that end with "a"|
|WHERE CustomerName LIKE '%or%'	|Finds any values that have "or" in any position|
|WHERE CustomerName LIKE '_r%'	|Finds any values that have "r" in the second position|
|WHERE CustomerName LIKE 'a__%'	|Finds any values that start with "a" and are at least 3 characters in length|
|WHERE ContactName LIKE 'a%o'	|Finds any values that start with "a" and ends with "o"|
|WHERE CustomerName LIKE 'a_%_%'	|Finds any values that starts with "a" and are at least 3 characters in length|


2. **IN**
This allows you to perform operations similar to using WHERE and =, but for more than one condition.

IN (value1, ...)
non-numeric values should be included with a pair of single quotes ('')
numeric values are included directly 

May NEED to use double quotation marks if you have an apostrophe within the text you are attempting to pull.


#### Examples

1. Use the accounts table to find the account name, primary_poc, and sales_rep_id for Walmart, Target, and Nordstrom.

```sql
SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name IN ('Walmart', 'Target', 'Nordstrom');
```

2. Use the web_events table to find all information regarding individuals who were contacted via the channel of organic or adwords.
```sql
SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords');
```


3. **NOT**
This is used with IN and LIKE to select all of the rows NOT LIKE or NOT IN a certain condition.

The NOT operator is an extremely useful operator for working with the previous two operators we introduced: IN and LIKE. By specifying NOT LIKE or NOT IN, we can grab all of the rows that do not meet a particular criteria.

#### Example
1. Use the accounts table to find the account name, primary poc, and sales rep id for all stores except Walmart, Target, and Nordstrom.
```sql
SELECT name, primary_poc, sales_rep_id
FROM accounts
WHERE name NOT IN ('Walmart', 'Target', 'Nordstrom');
```

2. Use the web_events table to find all information regarding individuals who were contacted via any method except using organic or adwords methods.
```sql
SELECT *
FROM web_events
WHERE channel NOT IN ('organic', 'adwords');
```

3. Use the accounts table to find:
    - All the companies whose names do not start with 'C'.

    - All companies whose names do not contain the string 'one' somewhere in the name.

    - All companies whose names do not end with 's'.

```sql
SELECT name
FROM accounts
WHERE name NOT LIKE 'C%';

SELECT name
FROM accounts
WHERE name NOT LIKE '%one%';

SELECT name
FROM accounts
WHERE name NOT LIKE '%s';
```

4. **AND & BETWEEN**
These allow you to combine operations where all combined conditions must be true.

The AND operator is used within a WHERE statement to consider more than one logical clause at a time. Each time you link a new statement with an AND, you will need to specify the column you are interested in looking at. You may link as many statements as you would like to consider at the same time. This operator works with all of the operations we have seen so far including arithmetic operators (+, *, -, /). LIKE, IN, and NOT logic can also be linked together using the AND operator.

Sometimes we can make a cleaner statement using BETWEEN than we can using AND. Particularly this is true when we are using the same column for different parts of our AND statement.

#### Example

1. Write a query that returns all the orders where the standard_qty is over 1000, the poster_qty is 0, and the gloss_qty is 0.
```sql
SELECT *
FROM orders
WHERE standard_qty > 1000 AND poster_qty = 0 and gloss_qty = 0;
```

2. Using the accounts table, find all the companies whose names do not start with 'C' and end with 's'.
```sql
SELECT name
FROM accounts
WHERE name NOT LIKE 'C%' and name LIKE '%s'
```


3. When you use the BETWEEN operator in SQL, do the results include the values of your endpoints, or not? Figure out the answer to this important question by writing a query that displays the order date and gloss_qty data for all orders where gloss_qty is between 24 and 29. Then look at your output to see if the BETWEEN operator included the begin and end values or not.
```sql
SELECT occurred_at, gloss_qty 
FROM orders
WHERE gloss_qty BETWEEN 24 AND 29;
```

BETWEEN operator in SQL is inclusive; that is, the endpoint values are included. So the BETWEEN statement in this query is equivalent to having written "WHERE gloss_qty >= 24 AND gloss_qty <= 29."


4. Use the web_events table to find all information regarding individuals who were contacted via the organic or adwords channels, and started their account at any point in 2016, sorted from newest to oldest.
```sql
SELECT * 
FROM web_events 
WHERE channel IN (organic, adwords) and occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
ORDER BY occurred_at DESC;
```

While BETWEEN is generally inclusive of endpoints, it assumes the time is at 00:00:00 (i.e. midnight) for dates. This is the reason why we set the right-side endpoint of the period at '2017-01-01'.

5. **OR**
This allow you to combine operations where at least one of the combined conditions must be true.

Each time you link a new statement with an OR, you will need to specify the column you are interested in looking at.

When combining multiple of these operations, we frequently might need to use parentheses to assure that logic we want to perform is being executed correctly. 

#### Example
1. Find list of orders ids where either gloss_qty or poster_qty is greater than 4000. Only include the id field in the resulting table.

```sql
SELECT id
FROM orders
WHERE gloss_qty > 4000 or poster_qty > 4000;
```

2. Write a query that returns a list of orders where the standard_qty is zero and either the gloss_qty or poster_qty is over 1000.

```sql
SELECT *
FROM orders
WHERE (gloss_qty > 1000 or poster_qty > 1000) AND standard_qty=0;
```

3. Find all the company names that start with a 'C' or 'W', and the primary contact contains 'ana' or 'Ana', but it doesn't contain 'eana'.
```sql
SELECT name 
FROM accounts
WHERE (name LIKE 'C%' or name LIKE 'W%') 
   AND ((primary_poc LIKE '%ana%' or primary_poc LIKE '%Ana%')
   AND primary_poc NOT LIKE '%eana%');
```

order: Where > Group By > Having > Order by


# JOIN
## Database Normalization
When creating a database, it is really important to think about how data will be stored. This is known as normalization, and it is a huge part of most SQL classes. 

There are essentially three ideas that are aimed at database normalization:
- Are the tables storing logical groupings of the data?
- Can I make changes in a single location, rather than in many tables for the same information?
- Can I access and manipulate data quickly and efficiently?

Use **ON** clause to specify a JOIN condition which is a logical statement to combine the table in **FROM** and **JOIN** statements.

In the SELECT statement, you will need to know how to specify tables and columns in the SELECT statement:
1. The table name is always before the period.
2. The column you want from that table is always after the period.

#### JOIN EXAMPLE
1. If we want to pull only the account name and the dates in which that account placed an order, but none of the other columns, we can do this with the following query:
```sql
SELECT accounts.name, orders.occurred_at
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;
```

2. Try pulling all the data from the accounts table, and all the data from the orders table.
```sql
SELECT accounts.*, orders.*
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;
```

3. Try pulling standard_qty, gloss_qty, and poster_qty from the orders table, and the website and the primary_poc from the accounts table.

```sql
SELECT orders.standard_qty, orders.gloss_qty, orders.poster_qty, accounts.website, accounts.primary_poc
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;

```

## ERD---Entity Relationship Diagrams
### PK
The **PK** here stands for **primary key**. A **primary key** exists in every table, and it is a column that has a unique value for every row.

It is common that the primary key is the first column in our tables in most databases.
One and only one PK for each table in the database.

### FK----FOREIGN KEY
A foreign key is a column in one table that is a primary key in a different table
FK can appear muliple times in the column
A table can have 0, 1 or more than 1 FKs.

Notice our SQL query has the two tables we would like to join - one in the FROM and the other in the JOIN. Then in the ON, we will ALWAYs have the PK equal to the FK:

The way we join any two tables is in this way: linking the **PK** and **FK** (generally in an **ON** statement).
```sql
SELECT
FROM
JOIN
ON PK=FK
```
or 
```sql
SELECT
FROM
JOIN
ON FK=PK
```

## ALIAS
```sql
FROM tablename AS t1
JOIN tablename2 AS t2
```
Before, you saw something like:
```sql
SELECT col1 + col2 AS total, col3
```
Frequently, you might also see these statements **without** the **AS** statement. Each of the above could be written in the following way instead, and they would still produce the exact same results:
```sql
FROM tablename t1
JOIN tablename2 t2
```
and
```sql
SELECT col1 + col2 total, col3
```

### Aliases for Columns in Resulting Table
While aliasing tables is the most common use case. It can also be used to alias the columns selected to have the resulting table reflect a more readable name.
```sql
Select t1.column1 aliasname, t2.column2 aliasname2
FROM tablename AS t1
JOIN tablename2 AS t2
```

#### example
1. Provide a table for all web_events associated with account name of Walmart. There should be three columns. Be sure to include the primary_poc, time of the event, and the channel for each event. Additionally, you might choose to add a fourth column to assure only Walmart events were chosen.
```sql
SELECT a.primary_poc, w.occurred_at, w.channel, a.name
FROM accounts a
JOIN web_events w
ON a.id=w.account_id
WHERE a.name = 'Walmart';
```

2. Provide a table that provides the region for each sales_rep along with their associated accounts. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.

```sql
SELECT r.name region, s.name rep, a.name account
FROM sales_reps s
JOIN region r
on r.id = s.region_id
JOIN accounts a
ON a.sales_rep_id = s.id
ORDER BY a.name;
```

3. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. Your final table should have 3 columns: region name, account name, and unit price. A few accounts have 0 for total, so I divided by (total + 0.01) to assure not dividing by zero.
```sql
SELECT r.name region, a.name account, 
    (o.total_amt_usd/o.total+0.01) unit_price
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON o.account_id = a.id;
```

## LEFT JOIN = LEFT OUTER JOIN, RIGHT JOIN = RIGHT OUTER JOIN, OUTER JOIN = FULL OUTER JOIN, JOIN = INNER JOIN

**JOIN** - an INNER JOIN that only pulls data that exists in both tables.

**LEFT JOIN** - pulls all the data that exists in both tables, as well as all of the rows from the table in the FROM even if they do not exist in the JOIN statement.

**RIGHT JOIN** - pulls all the data that exists in both tables, as well as all of the rows from the table in the JOIN even if they do not exist in the FROM statement.

A simple rule to remember this is that, when the database executes this query, it executes the join and everything in the **ON** clause first. Think of this as building the new result set. That result set is then filtered using the **WHERE** clause.
```sql
ON a.c = b.c
AND a.c2 = xxxx;
```
This may show more rows that does not satisfy the ON clause with left or right join.

```sql
ON a.c = b.c
WHERE a.c2 = xxxx;
```
This only show rows with a.c2 = XXX

#### NO repeated names in the SELECT
If you have two or more columns in your SELECT that have the same name after the table name such as accounts.name and sales_reps.name you will need to alias them. Otherwise it will only show one of the columns. You can alias them like accounts.name AS AcountName, sales_rep.name AS SalesRepName
#### Example

1. Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.

```sql
SELECT r.name region_name, s.name sales_name, a.name accounts_name
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest'
ORDER BY a.name;
```

2. Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a first name starting with S and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.
```sql
SELECT r.name region_name, s.name sales_name, a.name accounts_name
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest' AND s.name LIKE 'S%'
ORDER BY a.name;
```

3. Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a last name starting with K and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.

```sql
SELECT r.name region_name, s.name sales_name, a.name accounts_name
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest' AND s.name LIKE '% K%'
ORDER BY a.name;
```

4. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100. Your final table should have 3 columns: region name, account name, and unit price. In order to avoid a division by zero error, adding .01 to the denominator here is helpful total_amt_usd/(total+0.01).

```sql
SELECT r.name region, a.name account, 
       o.total_amt_usd/(o.total+0.01) unit_price
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON a.id = o.account_id
WHERE o.standard_qty > 100;
```


5. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. Sort for the smallest unit price first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).

```sql
SELECT r.name region, a.name account, 
       o.total_amt_usd/(o.total+0.01) unit_price
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON a.id = o.account_id
WHERE o.standard_qty > 100 AND o.poster_qty>50;
```


6. Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) for the order. However, you should only provide the results if the standard order quantity exceeds 100 and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. Sort for the largest unit price first. In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).

```sql
SELECT r.name region, a.name account, 
       o.total_amt_usd/(o.total+0.01) unit_price
FROM region r
JOIN sales_reps s
ON r.id = s.region_id
JOIN accounts a
ON s.id = a.sales_rep_id
JOIN orders o
ON a.id = o.account_id
WHERE o.standard_qty > 100 AND o.poster_qty>50
ORDER BY unit_price DESC;
```

7. What are the different channels used by account id 1001? Your final table should have only 2 columns: account name and the different channels. You can try SELECT DISTINCT to narrow down the results to only the unique values.

```sql
SELECT DISTINCT w.channel, a.name
FROM web_events w
JOIN accounts a
ON w.account_id = a.id
WHERE w.account_id = 1001;
```

8. Find all the orders that occurred in 2015. Your final table should have 4 columns: occurred_at, account name, order total, and order total_amt_usd.
```sql
SELECT o.occurred_at, a.name, o.total, o.total_amt_usd
FROM accounts a
JOIN orders o
ON a.id = o.account_id
WHERE o.occurred_at BETWEEN '01-01-2015' AND '01-01-2016';

```

# SQL AGGREGATION
## NULL
**NULLs** are a datatype that specifies where no data exists in SQL. 
Notice that NULLs are different than a zero - they are cells where data does not exist.

When identifying NULLs in a WHERE clause, we write IS NULL or IS NOT NULL. We don't use =, because NULL isn't considered a value in SQL. Rather, it is a property of the data.

```sql
WHERE col IS NULL;
```
```sql
WHERE col IS NOT NULL;
```

There are two common ways in which you are likely to encounter NULLs:

- NULLs frequently occur when performing a LEFT or RIGHT JOIN. You saw in the last lesson when some rows in the left table of a left join are not matched with rows in the right table, those rows will contain some NULL values in the result set.

- NULLs can also occur from simply missing data in our database.

## COUNT
COUNT does not cosider the NULL row (all cols are NULL in the resulting table).

## SUM
SUM is similar to COUNT.
```sql 
COUNT(*)
``` 
is allowed while 
```sql
SUM(*)
``` 
is not allowed. Unlike COUNT, you can only use SUM on numeric columns. However, SUM will ignore NULL values, as do the other aggregation functions. (see NULL as 0)

#### Example

1. Find the total amount of poster_qty paper ordered in the orders table.

```sql
SELECT SUM(poster_qty) AS total_poster_sales
FROM orders;
```

2. Find the total amount of standard_qty paper ordered in the orders table.

```sql
SELECT SUM(starndard_qty) AS total_starndard
FROM orders;
```

3. Find the total dollar amount of sales using the total_amt_usd in the orders table.
```sql
SELECT SUM(total_amt_usd) AS total_dollar_sales
FROM orders;
```

4. Find the total amount spent on standard_amt_usd and gloss_amt_usd paper for each order in the orders table. This should give a dollar amount for each order in the table.

Notice, this solution did not use an aggregate.

```sql
SELECT standard_amt_usd + gloss_amt_usd 
       AS total_standard_gloss
FROM orders;
```


5. Find the standard_amt_usd per unit of standard_qty paper. Your solution should use both an aggregation and a mathematical operator.  

```sql
SELECT SUM(starndard_amt_usd)/SUM(standard_qty) AS 
       starndard_per_qty
FROM orders;
```

## MIN and MAX

Notice that MIN and MAX are aggregators that again ignore NULL values. 

### accept non-numerical cols
Functionally, MIN and MAX are similar to COUNT in that they can be used on non-numerical columns. Depending on the column type, MIN will return the lowest number, earliest date, or non-numerical value as early in the alphabet as possible. As you might suspect, MAX does the opposite—it returns the highest number, the latest date, or the non-numerical value closest alphabetically to “Z.”

## AVG
Similar to other software AVG returns the mean of the data - that is the sum of all of the values in the column divided by the number of values in a column. This aggregate function again ignores the NULL values in both the numerator and the denominator.

If you want to count NULLs as zero, you will need to use **SUM** and **COUNT** (no NULL row in resulting table). However, this is probably not a good idea if the NULL values truly just represent unknown values for a cell.

#### Example
1. When was the earliest order ever placed? You only need to return the date.

```sql
SELECT MIN(occurred_at) 
FROM orders;
```


2. Try performing the same query as in question 1 without using an aggregation function.
```sql
SELECT occurred_at
FROM orders
ORDER BY occurred_at
LIMIT 1;
```

3. When did the most recent (latest) web_event occur?
```sql
SELECT MAX(occurred_at)
FROM web_events;
```


4. Try to perform the result of the previous query without using an aggregation function.
```sql
SELECT occurred_at
FROM web_events
ORDER BY occurred_at DESC
LIMIT 1;
```

5. Find the mean (AVERAGE) amount spent per order on each paper type, as well as the mean amount of each paper type purchased per order. Your final answer should have 6 values - one for each paper type for the average number of sales, as well as the average amount.
```sql
SELECT AVG(standard_qty) mean_standard, AVG(gloss_qty) mean_gloss, 
           AVG(poster_qty) mean_poster, AVG(standard_amt_usd) mean_standard_usd, 
           AVG(gloss_amt_usd) mean_gloss_usd, AVG(poster_amt_usd) mean_poster_usd
FROM orders;
```

6. Via the video, you might be interested in how to calculate the MEDIAN. Though this is more advanced than what we have covered so far try finding - what is the MEDIAN total_usd spent on all orders?
```sql
SELECT *
FROM (SELECT total_amt_usd
      FROM orders
      ORDER BY total_amt_usd
      LIMIT 3457) as table1
ORDER BY total_amt_usd DESC
LIMIT 2;
```

## GROUP BY
The key takeaways here:
- **GROUP BY** can be used to aggregate data within subsets of the data. For example, grouping for different accounts, different regions, or different sales representatives.

- Any column in the **SELECT** statement that is not within an aggregator must be in the **GROUP BY** clause.

- The GROUP BY always goes between **WHERE** and **ORDER BY**.

- ORDER BY works like SORT in spreadsheet software.

GROUP BY - Expert Tip
Before we dive deeper into aggregations using GROUP BY statements, it is worth noting that SQL evaluates the aggregations **before** the LIMIT clause.

IF you group by a column with enough unique values that it exceeds the LIMIT number, the aggregates will be calculated based on the table without LIMIT restrictions, and then some rows will simply be omitted from the results. 

#### Example

1. Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order.
```sql
SELECT a.name
FROM accounts a
JOIN orders o
ON a.id = orders.account_id
ORDER BY o.occurred_at;
LIMIT 1;
```

2. Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name.

```sql
SELECT a.name, SUM(o.total_amt_usd)
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;
```


3. Via what channel did the most recent (latest) web_event occur, which account was associated with this web_event? Your query should return only three values - the date, channel, and account name.
```sql
SELECT w.occurred_at, w.channel, a.name
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
ORDER BY w.occurred_at DESC
LIMIT 1;
```


4. Find the total number of times each type of channel from the web_events was used. Your final table should have two columns - the channel and the number of times the channel was used.

```sql
SELECT w.channel, COUNT(*)
FROM web_events w
GROUP BY w.channel;
```
**NOTE**: HOW many times: USE COUNT rather than SUM

5. Who was the primary contact associated with the earliest web_event?
```sql
SELECT a.primary_poc
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
ORDER BY w.occurred_at
LIMIT 1;
```

6. What was the smallest order placed by each account in terms of total usd. Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.

```sql
SELECT a.name, MIN(o.total_amt_usd) min_usd
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name
ORDER BY min_usd;
```

7. Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from fewest reps to most reps.

```sql
SELECT r.name, COUNT(*) n_sales
FROM sales_reps s
JOIN region r
ON r.id = s.region_id
GROUP BY r.name
ORDER BY n_sales;
```


Key takeaways:

- You can GROUP BY multiple columns at once, as we showed here. This is often useful to aggregate across a number of different segments.

- The order of columns listed in the ORDER BY clause does make a difference. You are ordering the columns from left to right.

GROUP BY - Expert Tips
- The order of column names in your GROUP BY clause doesn’t matter—the results will be the same regardless. If we run the same query and reverse the order in the GROUP BY clause, you can see we get the same results.

- As with ORDER BY, you can substitute numbers for column names in the GROUP BY clause. It’s generally recommended to do this only when you’re grouping many columns, or if something else is causing the text in the GROUP BY clause to be excessively long.


A reminder here that **any column that is not within an aggregation must show up in your GROUP BY statement**. 

#### Example

1. For each account, determine the average amount of each type of paper they purchased across their orders. Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account.

```sql
SELECT a.name, AVG(o.standard_qty) avg_stand, AVG(o.gloss_qty) avg_gloss, AVG(o.poster_qty) avg_post
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;
```


2. For each account, determine the average amount spent per order on each paper type. Your result should have four columns - one for the account name and one for the average amount spent on each paper type.
```sql
SELECT a.name, AVG(o.standard_amt_usd) avg_stand, AVG(o.gloss_amt_usd) avg_gloss, AVG(o.poster_amt_usd) avg_post
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.name;
```

3. Determine the number of times a particular channel was used in the web_events table for each sales rep. Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.

```sql
SELECT s.name, w.channel, COUNT(*) n_occurrence
FROM web_events w
JOIN accounts a
ON w.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.name, w.channel
ORDER BY n_occurrence DESC;
```

4. Determine the number of times a particular channel was used in the web_events table for each region. Your final table should have three columns - the region name, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
```sql
SELECT r.name, w.channel, COUNT(*) n_occurrence
FROM web_events w
JOIN accounts a
ON w.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
JOIN region r
ON r.id = s.region_id
GROUP BY r.name, w.channel
ORDER BY n_occurrence DESC;
```


## DISTINCT
**DISTINCT** is always used in SELECT statements, and it provides the unique rows for all columns written in the SELECT statement. Therefore, you only use DISTINCT once in any particular SELECT statement.

You could write:
```sql
SELECT DISTINCT column1, column2, column3
FROM table1;
```
It’s worth noting that using **DISTINCT**, particularly in aggregations, can **slow your queries down** quite a bit.

#### Example
1. Use DISTINCT to test if there are any accounts associated with more than one region.

```sql
SELECT DISTINCT id, name
FROM accounts;
```

```sql
SELECT r.id region_id, r.name region_name,
a.id account_id, a.name account_name
FROM accounts a
JOIN sales_reps s
ON a.sales_rep_id = s.id
JOIN region r
ON s.region_id = r.id;
```


2. Have any sales reps worked on more than one account?
```sql
SELECT s.name, s.id, COUNT(*) accounts
FROM sales_reps s
JOIN accounts a
ON s.id = a.sales_rep_id
GROUP BY s.name, s.id;
```

## HAVING

**HAVING** is the “clean” way to filter a query that has been aggregated, but this is also commonly done using a subquery. Essentially, any time you want to perform a **WHERE** on an element of your query that was created by an aggregate, you need to use HAVING instead.

**Having** cols must appear in the **GROUP BY** clause or be used in an aggregate function


#### Example

1. How many of the sales reps have more than 5 accounts that they manage?

```sql
SELECT s.id, COUNT(a.id) n_accounts
FROM accounts a
JOIN sales_reps s
ON a.sales_rep_id = s.id
GROUP BY s.id
HAVING COUNT(a.id)>5;
```

2. How many accounts have more than 20 orders?
```sql
SELECT COUNT(o.id) n_order
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id
HAVING COUNT(o.id) > 20;
```

3. Which account has the most orders?
```sql
SELECT a.id, a.name, COUNT(o.id) n_order
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
ORDER BY n_order DESC
LIMIT 1;
```

4. Which accounts spent more than 30,000 usd total across all orders?
```sql
SELECT a.id, a.name
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
HAVING SUM(total_amt_usd) > 30000;
```

5. Which accounts spent less than 1,000 usd total across all orders?

```sql
SELECT a.id, a.name
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
HAVING SUM(total_amt_usd) < 1000;
```

6. Which account has spent the most with us?

```sql
SELECT a.id, a.name, SUM(o.total_amt_usd) total_usd
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
ORDER BY total_usd DESC
LIMIT 1;
```

7. Which account has spent the least with us?

```sql
SELECT a.id, a.name, SUM(o.total_amt_usd) total_usd
FROM accounts a
JOIN orders o
ON a.id = o.account_id
GROUP BY a.id, a.name
ORDER BY total_usd
LIMIT 1;
```

8. Which accounts used facebook as a channel to contact customers more than 6 times?

```sql
SELECT a.name, a.id
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
GROUP BY a.id, a.name, w.channel
HAVING COUNT(w.occurred_at) > 6 AND w.channel = 'facebook';
```

9. Which account used facebook most as a channel?
```sql
SELECT a.name, a.id, COUNT(w.occurred_at) number_channel
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
WHERE w.channel = 'facebook'
GROUP BY a.id, a.name
ORDER BY number_channel DESC
LIMIT 1;
```

10. Which channel was most frequently used by most accounts?

```sql
SELECT a.name, a.id, w.channel, COUNT(w.occurred_at) number_channel
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
GROUP BY a.id, a.name, w.channel
ORDER BY number_channel DESC
LIMIT 10;
```

## DATE

**GROUPing BY** a date column is not usually very useful in SQL, as these columns tend to have transaction data down to a second.

### DATE_TRUNC 
allows you to truncate your date to a particular part of your date-time column. Common trunctions are day, month, and year. 


### DATE_PART 
can be useful for pulling a specific portion of a date, but notice pulling month or day of the week (dow) means that you are no longer keeping the years in order. Rather you are grouping for certain components regardless of which year they belonged in.

You can reference the columns in your select statement in GROUP BY and ORDER BY clauses with numbers that follow the order they appear in the select statement. For example
```sql
SELECT standard_qty, COUNT(*)

FROM orders

GROUP BY 1 (this 1 refers to standard_qty since it is the first of the columns included in the select statement)

ORDER BY 1 (this 1 refers to standard_qty since it is the first of the columns included in the select statement)
```

#### Example
1. Find the sales in terms of total dollars for all orders in each year, ordered from greatest to least. Do you notice any trends in the yearly sales totals?

```sql
SELECT SUM(total_amt_usd) total_sales, DATE_PART('year', occurred_at) ord_year
FROM orders
GROUP BY ord_year
ORDER BY total_sales DESC;
```


2. Which month did Parch & Posey have the greatest sales in terms of total dollars? Are all months evenly represented by the dataset?

```sql
SELECT SUM(total_amt_usd) total_sales, DATE_PART('month', occurred_at) ord_month
FROM orders
WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
GROUP BY ord_month
ORDER BY total_sales DESC;
```


3. Which year did Parch & Posey have the greatest sales in terms of total number of orders? Are all years evenly represented by the dataset?

```sql
SELECT DATE_PART('year', occurred_at) ord_year, COUNT(*) n_order
FROM orders
GROUP BY ord_year
ORDER BY 2 DESC
```

Which month did Parch & Posey have the greatest sales in terms of total number of orders? Are all months evenly represented by the dataset?
```sql
SELECT DATE_PART('month', occurred_at) ord_month, COUNT(*) n_order
FROM orders
WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
GROUP BY ord_month
ORDER BY 2 DESC
```

In which month of which year did Walmart spend the most on gloss paper in terms of dollars?

```sql
SELECT DATE_TRUNC('month', o.occurred_at) month_year, SUM(o.gloss_amt_usd) total_gloss
FROM orders o
JOIN accounts a
ON a.id = o.account_id
WHERE a.name = 'Walmart'
GROUP BY 1
ORDER BY 2 DESC;
```


## CASE
The CASE statement always goes in the SELECT clause.
CASE must include the following components: **WHEN**, **THEN**, and **END**. **ELSE** is an optional component to catch cases that didn’t meet any of the other previous CASE conditions.

You can make any conditional statement using any conditional operator (like WHERE) between WHEN and THEN. This includes stringing together multiple conditional statements using AND and OR.

You can include multiple WHEN statements, as well as an ELSE statement again, to deal with any unaddressed conditions.

#### Example
Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order. Limit the results to the first 10 orders, and include the id and account_id fields

```sql
SELECT o.id, o.account_id, 
CASE WHEN o.standard_qty = 0 or o.standard_qty IS NULL THEN 0
ELSE o.standard_amt_usd/o.standard_qty END AS unit_price
FROM orders o
LIMIT 10;
```

## zy: do not forget **END**
Getting the same information using a WHERE clause means only being able to get one set of data from the CASE at a time.


#### Example

1. Write a query to display for each order, the account ID, total amount of the order, and the level of the order - ‘Large’ or ’Small’ - depending on if the order is $3000 or more, or smaller than $3000.

```sql
SELECT account_id, total_amt_usd, total_amt_usd total,
CASE WHEN total >= 3000 THEN 'Large' ELSE 'Small' END AS level
FROM orders;
```

2. Write a query to display the number of orders in each of three categories, based on the total number of items in each order. The three categories are: 'At Least 2000', 'Between 1000 and 2000' and 'Less than 1000'.

```sql
SELECT CASE WHEN total >= 2000 THEN 'At Least 2000'
            WHEN total < 2000 AND total >= 1000 THEN 'Between 1000 and 2000'
            ELSE 'Less than 1000' END AS category, 
        COUNT(*) order_count
FROM orders
GROUP BY 1;
```

3. We would like to understand 3 different levels of customers based on the amount associated with their purchases. The top level includes anyone with a Lifetime Value (total sales of all orders) greater than 200,000 usd. The second level is between 200,000 and 100,000 usd. The lowest level is anyone under 100,000 usd. Provide a table that includes the level associated with each account. You should provide the account name, the total sales of all orders for the customer, and the level. Order with the top spending customers listed first.

```sql
SELECT a.name, SUM(o.total_amt_usd) total_sales, 
    CASE WHEN SUM(o.total_amt_usd)>200000 THEN 'top'
         WHEN SUM(o.total_amt_usd)<=200000 AND SUM(o.total_amt_usd) > 100000 THEN 'Mid'
         ELSE 'Bottom' END AS level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
GROUP BY 1
ORDER BY 2 DESC;
```


4. We would now like to perform a similar calculation to the first, but we want to obtain the total amount spent by customers only in 2016 and 2017. Keep the same levels as in the previous question. Order with the top spending customers listed first.
```sql
SELECT a.name, SUM(total_amt_usd) total_spent, 
     CASE WHEN SUM(total_amt_usd) > 200000 THEN 'top'
     WHEN  SUM(total_amt_usd) > 100000 THEN 'middle'
     ELSE 'low' END AS customer_level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
WHERE occurred_at > '2016-01-01' 
GROUP BY 1
ORDER BY 2 DESC;
```

5. We would like to identify top performing sales reps, which are sales reps associated with more than 200 orders. Create a table with the sales rep name, the total number of orders, and a column with top or not depending on if they have more than 200 orders. Place the top sales people first in your final table.

```sql
SELECT s.name, COUNT(*) order_count,
    CASE WHEN COUNT(*) > 200 THEN 'TOP'
         ELSE 'NOT TOP' END AS level
FROM orders o
JOIN accounts a
ON o.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY 1
ORDER BY 2 DESC;
```

6. The previous didn't account for the middle, nor the dollar amount associated with the sales. Management decides they want to see these characteristics represented as well. We would like to identify top performing sales reps, which are sales reps associated with more than 200 orders or more than 750000 in total sales. The middle group has any rep with more than 150 orders or 500000 in sales. Create a table with the sales rep name, the total number of orders, total sales across all orders, and a column with top, middle, or low depending on this criteria. Place the top sales people based on dollar amount of sales first in your final table. You might see a few upset sales people by this criteria!

```sql
SELECT s.name, COUNT(*) order_count, SUM(total_amt_usd) sales_sum,
CASE WHEN COUNT(*) > 200 OR SUM(total_amt_usd)>750000 THEN 'top'
     WHEN COUNT(*) > 150 OR SUM(total_amt_usd)>500000 THEN 'middle'
     ELSE 'low' END AS LEVEL
FROM orders o
JOIN accounts a
ON o.account_id = a.id
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY 1
ORDER BY 3 DESC;  
```

# Subqueries and Temporary Tables

#### Example
1. We needed to group by the day and channel. Then ordering by the number of events (the third column) gave us a quick way to answer the first question.
```sql
SELECT DATE_TRUNC('day',occurred_at) AS day,
   channel, COUNT(*) as events
FROM web_events
GROUP BY 1,2
ORDER BY 3 DESC;
```

2. Here you can see that to get the entire table in question 1 back, we included an * in our SELECT statement. You will need to be sure to alias your table.

```sql
SELECT *
FROM (SELECT DATE_TRUNC('day',occurred_at) AS day,
           channel, COUNT(*) as events
     FROM web_events 
     GROUP BY 1,2
     ORDER BY 3 DESC) sub;
```

3. Finally, here we are able to get a table that shows the average number of events a day for each channel.

```sql
SELECT channel, AVG(events) AS average_events
FROM (SELECT DATE_TRUNC('day',occurred_at) AS day,
             channel, COUNT(*) as events
      FROM web_events 
      GROUP BY 1,2) sub
GROUP BY channel
ORDER BY 2 DESC;
```

## Subquery Format
### indenting the subquery in some way
```sql
SELECT *
FROM (SELECT DATE_TRUNC('day',occurred_at) AS day,
                channel, COUNT(*) as events
      FROM web_events 
      GROUP BY 1,2
      ORDER BY 3 DESC) sub
GROUP BY day, channel, events
ORDER BY 2 DESC;
```

In the first subquery you wrote, you created a table that you could then query again in the FROM statement. However, if you are only returning a single value, you might use that value in a logical statement like **WHERE, HAVING, or even SELECT** - the value could be nested within a CASE statement.


Expert Tip
Note that you should **not include** an alias when you write a subquery in a conditional statement. This is because the subquery is treated as an individual value (or set of values in the IN case) rather than as a table.

Also, notice the query here compared a single value. If we returned an entire column IN would need to be used to perform a logical argument. If we are returning an entire table, then we **must use an ALIAS for the table**, and perform additional logic on the entire table.

#### Example

1. The average amount of standard paper sold on the first month that any order was placed in the orders table (in terms of quantity).

2. The average amount of gloss paper sold on the first month that any order was placed in the orders table (in terms of quantity).

3. The average amount of poster paper sold on the first month that any order was placed in the orders table (in terms of quantity).

4. The total amount spent on all orders on the first month that any order was placed in the orders table (in terms of usd).

```sql
SELECT DATE_TRUNC('month', MIN(occurred_at)) 
FROM orders;
```
Then to pull the average for each, we could do this all in one query, but for readability, I provided two queries below to perform each separately.
```sql
SELECT AVG(standard_qty) avg_std, AVG(gloss_qty) avg_gls, AVG(poster_qty) avg_pst
FROM orders
WHERE DATE_TRUNC('month', occurred_at) = 
     (SELECT DATE_TRUNC('month', MIN(occurred_at)) FROM orders);

SELECT SUM(total_amt_usd)
FROM orders
WHERE DATE_TRUNC('month', occurred_at) = 
      (SELECT DATE_TRUNC('month', MIN(occurred_at)) FROM orders);
```


5. Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
```sql

SELECT t3.rep_name, t3.region_name, t3.total_amt
FROM(SELECT region_name, MAX(total_amt) total_amt
     FROM(SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
             FROM sales_reps s
             JOIN accounts a
             ON a.sales_rep_id = s.id
             JOIN orders o
             ON o.account_id = a.id
             JOIN region r
             ON r.id = s.region_id
             GROUP BY 1, 2) t1
     GROUP BY 1) t2
JOIN (SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
     FROM sales_reps s
     JOIN accounts a
     ON a.sales_rep_id = s.id
     JOIN orders o
     ON o.account_id = a.id
     JOIN region r
     ON r.id = s.region_id
     GROUP BY 1,2
     ORDER BY 3 DESC) t3
ON t3.region_name = t2.region_name AND t3.total_amt = t2.total_amt;

```


6. For the region with the largest sales total_amt_usd, how many total orders were placed?

    6.1 The first query I wrote was to pull the total_amt_usd for each region.

```sql
SELECT r.name retion_name, SUM(o.total_amt_usd) largest_usd
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
GROUP BY 1;
```

    6.2 Then we just want the region with the max amount from this table. There are two ways I considered getting this amount. One was to pull the max using a subquery. Another way is to order descending and just pull the top value.

```sql
SELECT MAX(largest_usd)
FROM (SELECT r.name retion_name, SUM(o.total_amt_usd) largest_usd
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
GROUP BY 1) t1;
```


```sql
SELECT r.name retion_name, COUNT(total) most_order
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
GROUP BY 1
HAVING SUM(o.total_amt_usd) = 
    (SELECT MAX(largest_usd)
    FROM (SELECT r.name retion_name, SUM(o.total_amt_usd) largest_usd
        FROM region r
        JOIN sales_reps s
        ON s.region_id = r.id
        JOIN accounts a
        ON a.sales_rep_id = s.id
        JOIN orders o
        ON o.account_id = a.id
        GROUP BY 1) t1);
```