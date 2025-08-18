CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commission REAL

);

INSERT INTO Salesman(Salesman_id, name, city, Commission) VALUES
    ('5001','JAMES','NEW YORK',0.15),
    ('5002','JAMES','NEW YORK',0.14),
    ('5003','JAMES','NEW YORK',0.13),
    ('5004','JAMES','NEW YORK',0.12),
    ('5005','JAMES','NEW YORK',0.11),
    ('5006','JAMES','NEW YORK',0.10);

SELECT * FROM Salesman;
