#### 175. Combine Two Tables
Table: Person
| Column Name | Type    |
|-------------|---------|
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
PersonId is the primary key column for this table.
Table: Address

| Column Name | Type    |
|-------------|---------|
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
AddressId is the primary key column for this table.

```sql
# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
FROM Person tb1
LEFT JOIN Address tb2
ON tb1.PersonId = tb2.PersonId;
```


#### 176. Second Highest Salary
Write a SQL query to get the second highest salary from the Employee table.

| Id | Salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

| SecondHighestSalary |
|---------------------|
| 200                 |
```sql
Write your MySQL query statement below
SELECT IFNULL(
    (SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1), NULL
) SecondHighestSalary;


SELECT MAX(Salary) SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
```

#### 177. Nth Highest Salary
Write a SQL query to get the nth highest salary from the Employee table.

| Id | Salary |
| ---| -------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.


| getNthHighestSalary(2) |
|---|
| 200                    |

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;  
  RETURN (
      # Write your MySQL query statement below.
      # SELECT IFNULL(
      #   (SELECT DISTINCT Salary
      #   FROM Employee
      #   ORDER BY Salary DESC
      #   LIMIT 1 OFFSET M), NULL)
      SELECT DISTINCT Salary
      FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 OFFSET M
  );
END
```

#### 178. Rank Scores
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+---------+
| score | Rank    |
+-------+---------+
| 4.00  | 1       |
| 4.00  | 1       |
| 3.85  | 2       |
| 3.65  | 3       |
| 3.65  | 3       |
| 3.50  | 4       |
+-------+---------+
Important Note: For MySQL solutions, to escape reserved words used as column names, you can use an apostrophe before and after the keyword. For example `Rank`.
```sql
/* Write your T-SQL query statement below */

SELECT tb1.Score score, (SELECT COUNT(DISTINCT tb2.Score)
                         FROM Scores tb2
                         WHERE tb2.Score > tb1.Score)+1 Rank
FROM Scores tb1
ORDER BY tb1.Score DESC;
```

#### 184. Department Highest Salary
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
```sql
SELECT d1.Name Department, e1.Name Employee, e1.Salary Salary
FROM Employee e1
JOIN Department d1
ON e1.DepartmentId = d1.Id
WHERE (e1.Salary, e1.DepartmentId) IN (
    SELECT MAX(Salary), DepartmentId
    FROM Employee e2
    GROUP BY DepartmentId
);
```
```sql
SELECT dep.Name AS Department, emp.Name AS Employee, emp.Salary as Salary
FROM Employee AS emp, Department AS dep
WHERE emp.DepartmentId = dep.Id 
AND emp.Salary = (SELECT MAX(Salary) FROM Employee WHERE DepartmentID = emp.DepartmentId);
```
```sql
SELECT dep.Name Department, emp1.name Employee, emp1.Salary Salary
FROM Employee emp1
JOIN (
    SELECT MAX(Salary) max_salary, DepartmentId depId
    FROM Employee
    GROUP BY DepartmentID
) AS table1
ON emp1.Salary = table1.max_salary and emp1.DepartmentId = table1.depId
JOIN Department dep
ON emp1.DepartmentId = dep.Id;
```


#### 185. Department Top Three Salaries
SQL Schema
The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.

| Id | Name  | Salary | DepartmentId |
|----|-------|--------|--------------|
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
The Department table holds all departments of the company.

| Id | Name     |
|----|----------|
| 1  | IT       |
| 2  | Sales    |
Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows (order of rows does not matter).
| Department | Employee | Salary |
|------------|----------|--------|
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
Explanation:

In IT department, Max earns the highest salary, both Randy and Joe earn the second highest salary, and Will earns the third highest salary. There are only two employees in the Sales department, Henry earns the highest salary while Sam earns the second highest salary.

```sql
SELECT dep.Name Department, emp1.Name Employee, emp1.Salary Salary
FROM Department dep
JOIN Employee emp1
ON dep.Id = emp1.DepartmentId
WHERE (SELECT COUNT(DISTINCT Salary)
       FROM Employee emp2
       WHERE emp2.DepartmentId = emp1.DepartmentId AND emp2.Salary > emp1.Salary)<3;
```


### 197. Rising Temperature
Table: Weather

| Column Name   | Type    |
|---------------|---------|
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
id is the primary key for this table.
This table contains information about the temperature in a certain day.
 

Write an SQL query to find all dates' id with higher temperature compared to its previous dates (yesterday).

Return the result table in any order.

The query result format is in the following example:

Weather
| id | recordDate | Temperature |
|----|------------|-------------|
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |

Result table:
| id |
|----|
| 2  |
| 4  |
In 2015-01-02, temperature was higher than the previous day (10 -> 25).
In 2015-01-04, temperature was higher than the previous day (20 -> 30).

```sql
# Write your MySQL query statement below
SELECT w2.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = -1 AND w1.Temperature < w2.Temperature;
```

#### 262. Trips and Users

The Trips table holds all taxi trips. Each trip has a unique Id, while Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users table. Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’).
| Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
|----|-----------|-----------|---------|--------------------|----------|
| 1  |     1     |    10     |    1    |     completed      |2013-10-01|
| 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
| 3  |     3     |    12     |    6    |     completed      |2013-10-01|
| 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
| 5  |     1     |    10     |    1    |     completed      |2013-10-02|
| 6  |     2     |    11     |    6    |     completed      |2013-10-02|
| 7  |     3     |    12     |    6    |     completed      |2013-10-02|
| 8  |     2     |    12     |    12   |     completed      |2013-10-03|
| 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
| 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
The Users table holds all users. Each user has an unique Users_Id, and Role is an ENUM type of (‘client’, ‘driver’, ‘partner’).
| Users_Id | Banned |  Role  |
|----------|--------|--------|
|    1     |   No   | client |
|    2     |   Yes  | client |
|    3     |   No   | client |
|    4     |   No   | client |
|    10    |   No   | driver |
|    11    |   No   | driver |
|    12    |   No   | driver |
|    13    |   No   | driver |
Write a SQL query to find the cancellation rate of requests made by unbanned users (both client and driver must be unbanned) between Oct 1, 2013 and Oct 3, 2013. The cancellation rate is computed by dividing the number of canceled (by client or driver) requests made by unbanned users by the total number of requests made by unbanned users.

For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.

|     Day    | Cancellation Rate |
|------------|-------------------|
| 2013-10-01 |       0.33        |
| 2013-10-02 |       0.00        |
| 2013-10-03 |       0.50        |

```sql
# Write your MySQL query statement below
SELECT t1.Request_at Day, ROUND(SUM(CASE WHEN t1.Status="completed" THEN 0 
                                    ELSE 1 END)/COUNT(*), 2) "Cancellation Rate"
FROM Trips t1
LEFT JOIN Users t2
ON t1.Client_Id = t2.Users_id AND t2.Banned = "NO"
LEFT JOIN Users t3
ON t1.Driver_Id = t3.Users_Id AND t3.Banned = "NO"
WHERE t1.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY t1.Request_at
ORDER BY t1.Request_at;
```

#### 620. Not Boring Movies
X city opened a new cinema, many people would like to go to this cinema. The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and a description that is not 'boring'. Order the result by rating.

 

For example, table cinema:

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
For the example above, the output should be:
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+

```sql
# Write your MySQL query statement below
SELECT *
FROM cinema
WHERE mod(id,2)=1 AND description != 'boring'
ORDER BY rating DESC;
```

#### 626. Exchange Seats
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:

If the number of students is odd, there is no need to change the last one's seat.
```sql
# Write your MySQL query statement below
SELECT (CASE
            WHEN mod(tb1.id,2)=1 AND tb1.id < tb2.seatCount THEN tb1.id+1
            WHEN mod(tb1.id,2)=0 THEN tb1.id-1
            ELSE tb1.id
        END) id, tb1.student
FROM seat tb1, (SELECT COUNT(*) seatCount FROM seat) as tb2
ORDER BY id;
```




#### 601. Human Traffic of Stadium
Table: Stadium

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the primary key for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
No two rows will have the same visit_date, and as the id increases, the dates increase as well.
 

Write an SQL query to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.

The query result format is in the following example.

 

Stadium table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+

Result table:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended. Note that row 8 was included even though the visit_date was not the next day after row 7.
The rows with ids 2 and 3 are not included because we need at least three consecutive ids.

```sql
# Write your MySQL query statement below
SELECT DISTINCT tb1.id, tb1.visit_date, tb1.people
FROM Stadium tb1, Stadium tb2, Stadium tb3
WHERE tb1.people >= 100 AND tb2.people >=100 AND tb3.people>=100
    AND ((tb1.id = tb2.id-1 AND tb2.id = tb3.id-1) OR
    (tb1.id = tb2.id+1 AND tb1.id = tb3.id-1) OR
    (tb1.id = tb2.id+1 AND tb2.id = tb3.id+1))
ORDER BY tb1.visit_date;
```