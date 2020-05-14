s1="Olá"
s2='Olá'
s3='''
SELECT *
  FROM EMP
 WHERE EMP.STATUS = "OK"
   AND COMPANY="P1"
   AND SALARY > 10.000
 ORDER BY DEPT
'''

print(s1, s2, s3)