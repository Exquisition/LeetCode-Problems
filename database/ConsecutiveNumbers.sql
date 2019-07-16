/* Write your MySQL query statement below

condition is nums are same, and consecutive >= 3 times means 3 joins where ids are incremented 
*/
SELECT DISTINCT l1.Num as ConsecutiveNums 
FROM Logs l1
JOIN Logs l2 ON l1.Num = l2.Num
JOIN Logs l3 ON l2.Num = l3.Num
WHERE (l1.Id + 1) = l2.Id 
       AND (l2.Id + 1) = l3.Id