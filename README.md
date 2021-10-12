## Task

Dr. John Wesley has a spreadsheet containing a list of student's ***IDs, marks, class*** and ***name***.  

Your task is to help Dr. Wesley calculate the average marks of the students.  
  
<p align="center">
    <img src="https://bit.ly/3mIb5Gp" align="center" border="0" alt=" Average = \frac{Sum\;of\;all\;marks}{Total\;students} " width="221" height="36" />
</p>

**Note:**  
<font size="3"> 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.</font>  
<font size="3"> 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)</font>  

**Input Format**

The first line contains an integer ***N***, the total number of students.  
The second line contains the names of the columns in any order.  
The next ***N*** lines contains the ***IDs, marks, class*** and ***name***, under their respective column names.  

**Output Format**

Print the average marks of the list corrected to 2 decimal places.

### Sample Input

#### TESTCASE 01
```
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
```
#### TESTCASE 02
```
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
```
### Sample Output

#### TESTCASE 01
```
78.00
```
#### TESTCASE 02
```
81.00
```
**Explanation**

#### TESTCASE 01

Average = **(97 + 50 + 91 + 72 + 80)/5**
