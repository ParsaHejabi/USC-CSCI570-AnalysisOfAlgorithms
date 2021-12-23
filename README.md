<div align="center">
    <h1 align="center">
        USC - CSCI570 - Analysis Of Algorithms
    </h1>
    <p align="center">
        This repository has the final project in the Analysis of Algorithms class at the University of Southern California in the Fall 2021 semester.
    </p>
</div>

## Guidelines

The project is related to the implementation of the two different solutions provided in chapter 6
of the Kleinberg textbook for the Sequence Alignment problem. You can work on this project in
groups of no more than 3 people.

## Project Description

Implement the basic Dynamic Programming solution to the Sequence Alignment problem. Run
the test set provided and show your results.

### Algorithm Description

Suppose we are given two strings X and Y, where X consists of the sequence of symbols
x1, x2 . . . xm and Y consists of the sequence of symbols y1, y2 . . . yn. Consider the sets {1,
2, . . . , m} and {1, 2, . . . , n} as representing the different positions in the strings X and Y,
and consider a matching of these sets; recall that a matching is a set of ordered pairs with
the property that each item occurs in at most one pair. We say that a matching M of these
two sets is an alignment if there are no “crossing” pairs: if (i, j), (i’ , j’ ) ∈ M and i < i’ ,
then j < j’ . Intuitively, an alignment gives a way of lining up the two strings, by telling
us which pairs of positions will be lined up with one another.
Our definition of similarity will be based on finding the optimal alignment between X
and Y, according to the following criteria. Suppose M is a given alignment between X
and Y:

1. First, there is a parameter δe > 0 that defines a gap penalty. For each position of X
   or Y that is not matched in M — it is a gap — we incur a cost of δ.
2. Second, for each pair of letters p, q in our alphabet, there is a mismatch cost of αpq
   for lining up p with q. Thus, for each (i, j) ∈ M, we pay the appropriate mismatch
   cost αxiyj for lining up xi with yj. One generally assumes that αpp = 0 for each letter
   p—there is no mismatch cost to line up a letter with another copy of
   itself—although this will not be necessary in anything that follows.
3. The cost of M is the sum of its gap and mismatch costs, and we seek an alignment
   of minimum cost.

### Input string Generator

The input to the program would be a text file, input.txt containing the following
information:

1. First base string
2. Next j lines would consist of indices corresponding the after which the
   previous string to be added to the cumulative string
3. Second base string
4. Next k lines would consist of where the base string to be added to the cumulative string

   This information would help generate 2 strings from the original 2 base strings.
   This file could be used as an input to your program and your program could use
   the base strings and the rules to generate the actual strings. Also note that the
   numbers j and k corresponds to the first and the second string respectively. Make
   sure you validate the length of the first and the second string to be
   `2^(j) * str1.length` and `2^(k) * str2.length`. Please note that the base strings need
   not have to be of equal length and similarly, j need not be equal to k.

   ```
   ACTG
   3
   6
   1
   TACG
   1
   2
   9
   ```

   Using the above numbers, the generated strings would be

   ```
   ACACTGACTACTGACTGGTGACTACTGACTGG
   and
   TATTATACGCTATTATACGCGACGCGGACGCG
   ```

   Following is the step by step process on how the above strings are generated.

   ```
   ACTG
   ACTGACTG
   ACTGACTACTGACTGG
   ACACTGACTACTGACTGGTGACTACTGACTGG
   ```

   ```
   TACG
   TATACGCG
   TATTATACGCGACGCG
   TATTATACGCTATTATACGCGACGCGGACGCG
   ```

### Values for Delta and Alphas

Values for α’s are as follows. δe is equal to 30.

|     |  A  |  C  |  G  |  T  |
| :-: | :-: | :-: | :-: | :-: |
|  A  |  0  | 110 | 48  | 94  |
|  C  | 110 |  0  | 118 | 48  |
|  G  | 48  | 118 |  0  | 110 |
|  T  | 94  | 48  | 110 |  0  |

### Programming/Scripting Languages

Following are the list of languages which could be used:

1. C
2. C++
3. Java
4. Python
5. Python3

### Bounds

Bounds on the length of the base strings and the values of m and n, along with the
zip file will be released on 17 November 2021, i.e. 3 weeks before the due date.

### Goals

Following are the goals to achieve for your project
A.

#### Your program should take input

1. 2 strings that need to be aligned, should be generated from the string
   generator mentioned above.
2. Gap penalty (δe).
3. Mismatch penalty (αpq).

#### Your solution should output output.txt file containing the following information at the respective lines

1. The first 50 elements and the last 50 elements of the actual alignment.
2. The time it took to complete the entire solution.
3. Memory required.

#### Implement the memory efficient version of this solution and repeat the tests in Part B.

#### Plot the results of Part A and Part B:

1. Single plot of CPU time vs problem size for the two solutions.
2. Single plot of Memory usage vs problem size for the two solutions.

### Notes and Hints

- You will be provided a zipfile which has a folder containing some sample test
  cases and corresponding output text files containing the correct answers. Please
  note that we will be having another set of test cases (that are not released) which
  will be used for testing your program/script.

- You should provide us with a zipfile containing your programs/scripts along with
  plots and a summary file.
- The name of your program/script, folder and all the other meta-data files should
  have the USC IDs (not email ids) of everyone in your group separated by
  underscore, as follows:

  1. Zip filename: `1234567890_1234567890_1234567890.zip`, of the original foldername `1234567890_1234567890_1234567890`.
  2. Program filename: `1234567890_1234567890_1234567890_basic.py` and
     `1234567890_1234567890_1234567890_efficient.py` (if using Python).
  3. Plots: `CPUPlot.png` and `MemoryPlot.png` (you can use `.jpg` as well).
  4. Summaries: `Summary.txt`.

- Your programs/script should take input as `input.txt` file as an argument and output
  an `output.txt` file.
- Summarize your results and include any insights or observations drawn from your
  results in `Summary.txt`
- You also need to state each group members contribution to the project, e.g.coding,
  testing, report preparation, etc. Do that in `Summary.txt`.

### Grading

- Basic Algorithm: 25 points.
- If your program outputs a `.txt` file having all the 3 lines with correct answers: 15
  points.
- Memory efficient version: 30 points.
- Plots, analysis of results, insights and observations: 30 points.

### Project Addendum

1. The string generation mechanism is same irrespective of the basic or the efficient version of the algorithm

2. You can write a utility string generation code and use that for generating your own test cases. These could be used to measure your programs time and memory performance.

3. No input string is going to exceed 2^10 (1024 or 1.02 Kilo bytes).

4. We are asking for first 50 and last 50 characters in each string in the sequence alignment to avoid comparing all the characters in the entire alignment, thereby reducing the computational cost.

5. If there are many valid multiple sequences with the same cost, you can output any of those. All of them are valid.

6. The length of the final string should be equal to the (2^(number of lines))\*length of base string, as mentioned in the document.

7. Only 1 person in the group needs to submit. We’ll get the USC IDs of all the other team members from the filenames.

8. We will never give an invalid input to your program

9. Deltas and alphas are fixed parameters which need to be hardcoded.

10. You should code both the basic version and memory efficient version. You cannot use the memory efficient version in both of the sub-problems.

11. You can code the algorithm in any language and plot the analysis using a program in another other language

12. Your solutions for the regular and memory-efficient algorithms be in two different programs and both the programs need to produce an output called `output.txt` and take `input.txt` file from command line?

13. Memory in the program should be in Kilobytes and Time taken by the program should be in seconds. You can use linux utility command time to measure the time and `/usr/bin/time` (<https://unix.stackexchange.com/a/18851>) to measure the memory usage respectively. These are one of the many examples, you can use anything for measuring the performance. Memory taken by your program refers to the amount of RAM/ Resident set size used.

14. You can use any python package to estimate time and memory for your program.

15. First line in the output file contains the first 50 characters and last 50 characters of the first string. The first 50 and last 50 characters are separated by a space. The secone line contains the same, but for the second string.

16. The memory plot and the time plot need to have just 2 line plots, one from the basic version and the other from the advanced version. You can estimate datapoints by generating multiple test cases by yourself. You need to generate valid pngs when you submit.

17. Memory and time values in the output txt file are float values.

18. We will have bounds on the runtime and memory of your program to account for different compiler and languages. But remember that these differences shouldn’t really affect your runtime and memory too much.

19. You all need to hardcode the mismatch costs.

20. Input strings will always contain A, C, G, T only.

21. Please delete the input and output txt file given by us. We will be releasing a new version in the next 60 mins, containing the cost of the alignment as well in the 3rd line, followed by memory and time taken in the 4th and the 5th line respectively.

22. Yes your code be tested on a series of input text files? You need to code your programs to take inputs from the user through the command line.

23. Please don’t use any fancy plots for the graphs for time and memory. Just a line graph of about 15-20 data points should be sufficient.

24. You can write your own string generator and give sample test cases to get more points in the plot. For each test case, you get one point on the plot

25. Your program should not print anything when it is run. It should only write to output.txt file.

26. X axis of the plot needs to be the problem size, which is m+n, i.e the sum of the lengths of the strings (not the length of the base strings but the length of the final strings).

27. Please make sure you also have a shell script named `1234567890_1234567890_1234567890_basic.sh` and `1234567890_1234567890_1234567890_efficient.sh` consisting of commands to run your programs. Refer to @2638 for more details.

28. Python users need to have 2.7 or 3 in their suffixes. Refer to @2638 for more details.

29. Don't worry about the python packages. We'll install all of them. As for the flags for `C++/C/Java`, we've asked you to write a script, so it should take care of that.

30. For the project report, just write these things:
    - Contributions of each student in the group.
    - Comments on why the efficient and basic versions have different memory and time plots.
