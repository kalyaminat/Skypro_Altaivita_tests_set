-- 1. Все уникальные названия продуктов
SELECT DISTINCT product_name
FROM products;

-- 2. ID, название и цена продуктов с содержанием клетчатки более 5 г
SELECT p.product_id, p.product_name, p.price
FROM products AS p
JOIN nutritional_information AS n ON p.product_id = n.product_id
WHERE n.fiber > 5;

-- 3. Названия продуктов с максимальным содержанием белка
SELECT p.product_name
FROM products AS p
JOIN nutritional_information AS n ON p.product_id = n.product_id
WHERE n.protein = (SELECT MAX(protein) FROM nutritional_information);

-- 4. Сумма калорий по категориям для продуктов с ненулевым жиром
SELECT p.category_id, SUM(p.calories) AS total_calories
FROM products AS p
JOIN nutritional_information AS n ON p.product_id = n.product_id
WHERE n.fat <> 0
GROUP BY p.category_id;

-- 5. Средняя цена продуктов по категориям
SELECT c.category_name, AVG(p.price) AS average_price
FROM categories AS c
JOIN products AS p ON c.category_id = p.category_id
GROUP BY c.category_id, c.category_name;
