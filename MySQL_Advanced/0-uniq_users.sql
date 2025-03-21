-- 0. We are all unique!
-- 0. We are all unique!

CREATE TABLE IF NOT EXISTS 'users' (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE
);