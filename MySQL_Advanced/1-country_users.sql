-- 1. In and not out
-- 1. In and not out

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255),
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `country` ENUM('US', 'CO', 'TN') NOT NULL
);