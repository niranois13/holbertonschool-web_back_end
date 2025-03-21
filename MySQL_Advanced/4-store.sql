-- 4. Buy buy buy
-- 4. Buy buy buy
CREATE TRIGGER stock_handle BEFORE INSERT ON orders
FOR EACH ROW 
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;