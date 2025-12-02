WITH part_1 AS (
  SELECT MAX(x.value * y.value) AS result_1
  FROM joell-dev.aoc_2020.data_1 x
  CROSS JOIN joell-dev.aoc_2020.data_1 y

  WHERE x.value > y.value
    AND x.value + y.value = 2020
),

part_2 AS (
  SELECT MAX(x.value * y.value * z.value) AS result_2
  FROM joell-dev.aoc_2020.data_1 x
  CROSS JOIN joell-dev.aoc_2020.data_1 y
  CROSS JOIN joell-dev.aoc_2020.data_1 z

  WHERE x.value > y.value
    AND x.value > z.value
    AND y.value > z.value
    AND x.value + y.value + z.value = 2020
)

SELECT *
FROM part_1, part_2

-- 646779 246191688
