
/*
- if even studentid, get previous student name, 
- if odd studenid and not last element, get next student name
- if odd studentid and last element, same studentname
*/

SELECT s1.id, s2.student
FROM seat s1, seat s2
WHERE (CASE WHEN s1.id%2 = 1 AND s1.id = (SELECT MAX(id) FROM seat) THEN s1.id = s2.id
      WHEN s1.id%2=0 THEN s2.id = s1.id - 1
      ELSE s2.id = s1.id +1 
      END)
ORDER BY s1.id;