SELECT CompanyName
FROM SalesLT.Customer
WHERE CustomerID IN(SELECT CustomerID FROM SalesLT.CustomerAddress a RIGHT
OUTER JOIN SalesLT.Address b 
ON a. AddressID = b.AddressID AND City='Dallas')