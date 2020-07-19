SELECT FirstName, LastName, City, State 
FROM Person p
JOIN Address a
ON p.PersonID = a.PersonId;