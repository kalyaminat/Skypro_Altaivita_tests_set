   SELECT product_name
   FROM products;


   SELECT p.product_id,
          p.product_name,
          p.product_price,
   FROM products as p
   RIGHT JOIN nutritional_information as n
   on p.product_id = n.product_id
   WHERE fiber < 5;


   SELECT p.product_name
   FROM product AS p
   JOIN nutritional_information AS n
   ON p.product_id = n.product_id
   GROUP BY protein desc
   LIMIT 1;

   Select p.category_id, SUM(p.calories) As total_calories
   FROM products AS p
   JOIN nutritional_information AS n
   ON p.product_id = n.product_id
   WHERE fat != 0
   GROUP BY p.category_id;   


   SELECT species_name, AVG(species_amount) AS medium_species_amont
   FROM species
   GROUP BY species_name;