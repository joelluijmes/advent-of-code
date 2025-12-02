WITH decomposed AS (
  SELECT 
    CAST(REGEXP_EXTRACT(value, r"(\d+)\-") AS INT64) AS min_count,
    CAST(REGEXP_EXTRACT(value, r"\d+\-(\d+)") AS INT64) AS max_count,
    REGEXP_EXTRACT(value, r"\d+\-\d+ (\w)") AS char,
    REGEXP_EXTRACT(value, r": (\w+)$") AS value,
    value AS input
  FROM `joell-dev.aoc_2020.data_2` 
),

part_1 AS (
  WITH counted AS (
    SELECT
      *,
      LENGTH(value) - LENGTH(REGEXP_REPLACE(value, char, '')) AS char_count
    FROM decomposed
  ),
  
  validation AS (
    SELECT
      *,
      char_count >= min_count AND char_count <= max_count AS is_valid
    FROM counted
  )
  
  SELECT COUNTIF(is_valid) AS result_1
  FROM validation
),

part_2 AS (
  WITH validation AS (
    SELECT 
      *,
      (SUBSTRING(value, min_count, 1) = char) != (SUBSTRING(value, max_count, 1) = char) AS is_valid
    FROM decomposed
  )
  
  SELECT COUNTIF(is_valid) AS result_2
  FROM validation
)

SELECT *
FROM part_1, part_2

-- 560, 303