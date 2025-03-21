-- 3. Old school band
-- lists all bands with Glam rock as main style, ranked by longevity
SELECT DISTINCT `band_name`, 
       IFNULL(`split`, YEAR(CURDATE())) - `formed` AS `lifespan` 
FROM `metal_bands` 
WHERE style LIKE 'Glam rock%' 
ORDER BY `lifespan` DESC;

