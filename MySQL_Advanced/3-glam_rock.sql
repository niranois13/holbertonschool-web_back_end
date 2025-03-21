-- 3. Old school band
-- 3. Old school band
SELECT DISTINCT `band_name`, IFNULL(`split`, YEAR(CURDATE())) - `formed` as `lifespan` 
FROM `metal_bands` 
WHERE style LIKE 'Glam rock%' 
ORDER BY `lifespan` DESC;
