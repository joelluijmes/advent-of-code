-- Counter used to see if we're still updating the intermediate result
DECLARE row_count INT64 DEFAULT 0;

-- Find all direct parents of shiny gold
CREATE TEMP TABLE subs AS (
  SELECT bag
  FROM `joell-dev.aoc_2020.data_7` 
  WHERE subbag = 'shiny gold'
);

-- We loop until the intermediate result doesn't grow
LOOP
  SET row_count = (SELECT COUNT(*) FROM subs);
  
  -- Select the original set
  -- Union with all the parent of the sub
  CREATE OR REPLACE TEMP TABLE subs AS (
    SELECT bag
    FROM subs
    
    UNION DISTINCT

    SELECT bag
    FROM `joell-dev.aoc_2020.data_7` 
    WHERE subbag IN (
      SELECT bag
      FROM subs
    )
  );
  
  -- If the subs contains the same number of records (i.e. didn't change), we reached max depth
  IF row_count = (SELECT COUNT(*) FROM subs) THEN
    BREAK;
  END IF;
END LOOP;

SELECT COUNT(*) AS result
FROM subs

