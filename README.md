# Simple data processing with hadoop


These are some of the basic task for beginners using hadoop. To test them locally pipe linux commad: 

`cat test.txt | python mapper.py | sort | reducer.py`

A text file for testing is there in every folder. 


* Task 1 lower cases the file. 

* Task 2 removes duplicated lines produced from task 1.

* Task 3 implements the `wc` command of linux eg:
  *bob had a little lamb and a small cat
   alice had one tiger
   mary had some small dogs and a rabbit*
  should give output: `21 3`

* Task 4 counts the no of two words sequence.

* Task 5 uses a combiner for Task 4.

* Task 6 prints top twenty two words sequences. 

* Task 7 prints the transpose of a matrix 

* Task 8 performs a relational join operation on two tables.

* Task 9 finds the lowest average of marks of a student whose subjects are more then 4. 
