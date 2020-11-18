-- FK CHECKS ON

-- Set the foreign keys checking on
PRAGMA foreign_keys = ON;
-- Check the foreign keys setting (1=ON, 0=OFF)
PRAGMA foreign_keys;

-- TABLE CREATION

-- Creating Branch table
CREATE TABLE Branch (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    telephone TEXT
);

-- Employee
CREATE TABLE Employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_branch INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    employment_start TEXT NOT NULL,
    employment_end TEXT,
    FOREIGN KEY (id_branch) REFERENCES Branch(id)
);

-- Salary
CREATE TABLE Salary (
    year INTEGER,
    month INTEGER,
    id_employee INTEGER,
    amount REAL NOT NULL,
    PRIMARY KEY (year, month, id_employee),
    FOREIGN KEY (id_employee) REFERENCES Employee(id)
);

-- INSERTING

-- Branches
INSERT INTO Branch (name, address, telephone) VALUES 
    ("Grosuplje's Fried Chicken", "Kolodvorska 1, Grosuplje", "01/786-42-31");
INSERT INTO Branch (name, address) VALUES 
    ("Hot Pork Wings", "Cesta v Kranj 35, Ljubljana");

-- Employees (still employed)
INSERT INTO Employee (id_branch, first_name, last_name, employment_start) VALUES
    (1, "Marko", "Novaković", "1972-01-25"),
    (1, "Jože", "Novak", "1995-08-22"),
    (1, "Janez", "Gruden", "1999-12-07"),
    (1, "Tine", "Stegel", "2002-04-28"),
    (1, "Nina", "Gec", "2010-03-08"),
    (1, "Petar", "Stankovski", "2018-10-01");

-- Employees (retired)
INSERT INTO Employee (id_branch, first_name, last_name, employment_start, employment_end) VALUES
    (1, "Jana", "Žitnik", "1987-06-07", "1987-06-12"),
    (1, "Patricio", "Rozman", "2010-04-22", "2022-01-01"),
    (1, "Robert", "Demšar", "1996-12-06", "1997-07-02");

-- Salaries
INSERT INTO Salary (year, month, id_employee, amount) VALUES 
    (2010, 05, 2, 950.37),
    (2010, 06, 2, 955.2),
    (2010, 07, 2, 990.49),
    (2010, 08, 2, 1200.5),
    (2010, 05, 6, 980.43),
    (2010, 05, 7, 1320.2),
    (2010, 05, 8, 2100.67),
    (2010, 06, 8, 2140.99),
    (2010, 07, 8, 2099.11);

-- SELECTING

-- Basic

-- Selecting all columns
SELECT * FROM Branch;
SELECT * FROM Employee;

-- Selecting a column with a condition
SELECT employment_start 
FROM Employee 
WHERE last_name = "Gec";

-- Result value concatenation
SELECT id, first_name || ' ' || last_name AS name 
FROM Employee 
WHERE employment_end IS NULL;

-- Grouping and aggregations
SELECT b.id, b.name, COUNT(e.id), MAX(s.amount)
FROM Branch b, Employee e, Salary s
WHERE
    e.id_branch = b.id AND  
    s.id_employee = e.id
GROUP BY b.id, b.name;

-- Grouping and outer joins
SELECT b.id, b.name, COUNT(e.id), MAX(s.amount)
FROM Branch b LEFT OUTER JOIN Employee e ON e.id_branch = b.id
     LEFT OUTER JOIN Salary s ON s.id_employee = e.id
GROUP BY b.id, b.name;

-- Nested select statement
SELECT * 
FROM (SELECT e.id, e.first_name, e.last_name, s.amount, e.employment_end, s.year, s.month
      FROM Employee e, Salary s
      WHERE
         e.id = s.id_employee AND
         e.employment_end IS NOT NULL) t
WHERE
    strftime('%Y', t.employment_end) < t.year OR
    (strftime('%Y', t.employment_end) = t.year AND
     strftime('%m', t.employment_end) < t.month);


-- CREATE AS SELECT
CREATE TABLE SalaryAnalysis AS
SELECT e.id, e.employment_start, e.employment_end, 
       s.year || '-' || s.month || '-01' AS month, s.amount 
FROM Employee e INNER JOIN Salary s ON e.id = s.id_employee;

SELECT * FROM SalaryAnalysis;

-- UPDATES

-- Set new phone number to the Hot Pork Wings branch
UPDATE Branch
 SET telephone = "05/869-22-54"
 WHERE name = "Hot Pork Wings";

-- Retire the Employee 3 starting today
UPDATE Employee
 SET employment_end = date('now')
 WHERE id = 3;

-- DELETIONS
DELETE FROM Employee WHERE employment_end IS NOT NULL;

DELETE FROM Salary WHERE id_employee IN (
    SELECT id FROM Employee WHERE employment_end IS NOT NULL
);