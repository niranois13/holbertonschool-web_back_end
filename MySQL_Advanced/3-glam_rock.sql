-- 3. Old school band
-- 3. Old school band
SELECT DISTINCT `band_name`, IFNULL(`split`, 2025) - `formed` AS `lifespan` 
FROM `metal_bands` 
WHERE FIND_IN_SET('Glam rock', style) 
ORDER BY `lifespan` DESC;
