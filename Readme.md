# Binary search tree.

![Inserts time](https://github.com/ZadokhinDima/counting_sort_and_BSD/blob/main/inserts.png?raw=true)


![Search time](https://github.com/ZadokhinDima/counting_sort_and_BSD/blob/main/searches.png?raw=true)


![Delete time](https://github.com/ZadokhinDima/counting_sort_and_BSD/blob/main/deletes.png?raw=true)

From diagrams logariphmic complexity is clearly visible.

# Counting sort.

| Array Size | Max Element | Time Consumed |
|------------|-------------|---------------|
|10|10|0.00420|
|10|100|0.00510|
|10|1000|0.03670|
|10|10000|0.29110|
|10|100000|2.47880|
|100|10|0.02770|
|100|100|0.00960|
|100|1000|0.04260|
|100|10000|0.36410|
|100|100000|3.71670|
|1000|10|0.07030|
|1000|100|0.07390|
|1000|1000|0.12110|
|1000|10000|0.51600|
|1000|100000|4.58810|
|10000|10|0.69980|
|10000|100|0.66160|
|10000|1000|1.08990|
|10000|10000|1.19990|
|10000|100000|5.54420|
|100000|10|7.26770|
|100000|100|7.02070|
|100000|1000|8.51020|
|100000|10000|7.76150|
|100000|100000|15.59110|


Counting Sort works well for integer arrays where the range of input values is not significantly larger than the number of elements.