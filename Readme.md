
# Technologies and big data analysis tools
These are the practices from some AI-related course from my university. It was taught by 
our department of applied mathematics.

_# noinspection MachineTranslation_

_# noinspection Math_

---

## Practice 1 - Getting started with Python language

### Task 1
Install Python - _Seriously!_

### Task 2

Write a program that calculates the area of a figure,
the parameters of which are supplied to the input. Figures that are submitted for input:
triangle, rectangle, circle. The result of the work is a dictionary, where
the key is the name of the figure, and the value is the area.

P1T2

__Output__
```
t2 {'triangle': 1.0, 'rectangle': 12.0, 'circle':
78.53981633974483}
```

### Task 3

Write a program that takes two numbers as input and
the operation that needs to be applied to them. Must be implemented
the following operations: +, -, /, //, abs – modulus, pow or ** – exponentiation.

P1T3

__Output__
```
t3 3.0 2.0 1.0
```

### Task 4

Write a program that reads numbers from the console (by
one per line) until the sum of the entered numbers is equal to 0 and
after that it displays the sum of the squares of all read numbers.

P1T4

__Output__
```
t4:
1
2
-3
t4 14
```

### Task 5

Write a program that prints the sequence
numbers of length N, where each number is repeated as many times as it is equal to.
A non-negative integer N is passed to the program input. For example, if
N = 7, then the program should print 1 2 2 3 3 3 4. Printing list elements
separated by a space – print(*list).

P1T5

__Output__
```
t5 [1, 2, 2, 3, 3, 3, 4]
```

### Task 6

Given two lists: A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2] B =
['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', ' b', 'a']. Create a dictionary in
in which the keys are the contents of list B, and the values for the dictionary keys are
is the sum of all elements of list A according to the letter contained in
the same position in list B. Example program result: {‘a’ : 10, ‘b’ : 15, ‘c’
: 6}.

P1T6

__Output__
```
t6 {'a': 17, 'b': 11, 'c': 17}
```

### Task 7-12

Tasks seven to twelve were combined into
due to their small size. 7. Download and Upload Home Value Data
in California using the sklearn library. 8. Use the info() method. 9.
Find out if there are missing values using isna().sum(). 10. Withdraw
records where the average age of houses in the area is more than 50 years and the population is more than
2500 people using the loc() method. 11. Find out the maximum and minimum
median house price values. 12. Using the apply() method, output to
screen the name of the characteristic and its average value.

P1T7_12

__Output__
```
t7:
        MedInc  HouseAge  AveRooms  ...  AveOccup  Latitude  Longitude
0      8.3252      41.0  6.984127  ...  2.555556     37.88    -122.23
1      8.3014      21.0  6.238137  ...  2.109842     37.86    -122.22
2      7.2574      52.0  8.288136  ...  2.802260     37.85    -122.24
3      5.6431      52.0  5.817352  ...  2.547945     37.85    -122.25
4      3.8462      52.0  6.281853  ...  2.181467     37.85    -122.25
...       ...       ...       ...  ...       ...       ...        ...
20635  1.5603      25.0  5.045455  ...  2.560606     39.48    -121.09
20636  2.5568      18.0  6.114035  ...  3.122807     39.49    -121.21
20637  1.7000      17.0  5.205543  ...  2.325635     39.43    -121.22
20638  1.8672      18.0  5.329513  ...  2.123209     39.43    -121.32
20639  2.3886      16.0  5.254717  ...  2.616981     39.37    -121.24

[20640 rows x 8 columns]

t8:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   MedInc      20640 non-null  float64
 1   HouseAge    20640 non-null  float64
 2   AveRooms    20640 non-null  float64
 3   AveBedrms   20640 non-null  float64
 4   Population  20640 non-null  float64
 5   AveOccup    20640 non-null  float64
 6   Latitude    20640 non-null  float64
 7   Longitude   20640 non-null  float64
dtypes: float64(8)
memory usage: 1.3 MB

t9:
MedInc        0
HouseAge      0
AveRooms      0
AveBedrms     0
Population    0
AveOccup      0
Latitude      0
Longitude     0
dtype: int64

t10:
       MedInc  HouseAge  AveRooms  ...    AveOccup  Latitude  Longitude
460    1.4012      52.0  3.105714  ...    9.534286     37.87    -122.26
4131   3.5349      52.0  4.646119  ...    5.910959     34.13    -118.20
4440   2.6806      52.0  4.806283  ...    4.007853     34.08    -118.21
5986   1.8750      52.0  4.500000  ...   21.333333     34.10    -117.71
7369   3.1901      52.0  4.730942  ...    4.182735     33.97    -118.21
8227   2.3305      52.0  3.488860  ...    3.955439     33.78    -118.20
13034  6.1359      52.0  8.275862  ...  230.172414     38.69    -121.15
15634  1.8295      52.0  2.628169  ...    4.164789     37.80    -122.41
15652  0.9000      52.0  2.237474  ...    2.237474     37.80    -122.41
15657  2.5166      52.0  2.839075  ...    1.621520     37.79    -122.41
15659  1.7240      52.0  2.278566  ...    1.780142     37.79    -122.41
15795  2.5755      52.0  3.402576  ...    2.108696     37.77    -122.42
15868  2.8135      52.0  4.584329  ...    3.966799     37.76    -122.41

[13 rows x 8 columns]

t11:
15.0001 0.4999

t12:
MedInc           3.870671
HouseAge        28.639486
AveRooms         5.429000
AveBedrms        1.096675
Population    1425.476744
AveOccup         3.070655
Latitude        35.631861
Longitude     -119.569704
dtype: float64
```

---

## Practice 2 - Familiarize yourself with various data visualization libraries

### Task 1

Find and download multidimensional data (with a large number of features - columns) 
using the pandas library. Describe the data found in the report.

### Task 2

Display information about the data using the .info(), .head() methods.
Check data for empty values. If present, remove row data or interpolate missing
values. If necessary, additionally pre-process the data for further work with it.

t1-t2

__Output__
```
t2:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 197 entries, 0 to 196
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   income             195 non-null    float64
 1   life_exp           195 non-null    float64
 2   population         195 non-null    float64
 3   year               197 non-null    int64
 4   country            197 non-null    object
 5   four_regions       193 non-null    object
 6   six_regions        193 non-null    object
 7   eight_regions      193 non-null    object
 8   world_bank_region  193 non-null    object
dtypes: float64(3), int64(1), object(5)
memory usage: 14.0+ KB
t2:
     income  life_exp  ...       eight_regions           world_bank_region
0   1910.0      61.0  ...           asia_west                  South Asia
1  11100.0      78.1  ...         europe_east       Europe & Central Asia
2  11100.0      74.7  ...        africa_north  Middle East & North Africa
3  46900.0      81.9  ...         europe_west       Europe & Central Asia
4   7680.0      60.8  ...  africa_sub_saharan          Sub-Saharan Africa

[5 rows x 9 columns]
```

### Task 3

Plot a bar chart (.bar) using the graph_objs module from the Plotly library with the following parameters:
1. On the X-axis indicate the date or name, on the Y-axis indicate the quantitative indicator.
2. Make the column take on a color depending on the value of the indicator (marker=dict(color=attribute, coloraxis="coloraxis")).
3. Make sure that the borders of each column are highlighted with a black line with a thickness of 2.
4. Display the chart title, centered at the top, with text size 20.
5. Add labels for the X and Y axes with a text size of 16. For the x-axis, rotate the labels so that they are read at an angle of 315.
6. Make the text size of the axis labels equal to 14.
7. Place the graph across the entire width of the work area and set the height to 700 pixels.
8. Add a grid to the graph, make its color 'ivory' and thickness equal to 2. (You can do this when setting the axes using gridwidth=2, gridcolor='ivory').
9. Remove extra padding along the edges.

t3

__Output__
![](images/p2_1.png)

### Task 4

Create a pie chart (go.Pie) using the data and design style from the previous graph. 
Make sure that the boundaries of each share are highlighted with a black line with a 
thickness of 2 and the categories of the pie chart are readable (for example, combine 
some objects).

t4

__Output__
![](images/p2_2.png)

### Task 5

Construct linear graphs, take one of the parameters and determine the relationship 
between several other (from 2 to 5) indicators using the matplotlib library. Draw a 
conclusion. Make a graph with lines and markers, line color 'crimson', point color 
'white', point border color 'black', point border thickness 2. Add a grid to the 
graph, make its color 'mistyrose' and width equal to 2. (You can do this when 
setting the axes using linewidth=2, color='mistyrose').

t5

__Output__
![](images/p2_3.png)
![](images/p2_4.png)

__Conclusion__\
The first graph shows that the higher the income, the longer the life expectancy.
The second graph shows that the majority of income is concentrated in the vast 
minority of people, and also that most people have incomes that do not exceed $20,000.

### Task 6

Visualize multidimensional data using t-SNE. It is necessary to use the MNIST or 
fashion MNIST data set (you can also use other ready-made data sets where you can 
observe the division of objects into clusters). Consider the visualization results 
for different perplexity values.

t6

__Output__
```
t6:    label  1x1  1x2  1x3  1x4  1x5  ...  28x23  28x24  28x25  28x26  28x27  28x28
0      5    0    0    0    0    0  ...      0      0      0      0      0      0
1      0    0    0    0    0    0  ...      0      0      0      0      0      0
2      4    0    0    0    0    0  ...      0      0      0      0      0      0
3      1    0    0    0    0    0  ...      0      0      0      0      0      0
4      9    0    0    0    0    0  ...      0      0      0      0      0      0

[5 rows x 785 columns]
t6: Elapsed time: 1.5147051811218262 seconds
```
![](images/p2_5.png)
![](images/p2_6.png)
![](images/p2_7.png)

__Conclusion__\
From the resulting graphs it follows that the higher the perplexity value, the larger the 
clusters become. Perplexity (a variable parameter) describes the expected density around 
each point. Low values focus the algorithm on fewer neighbors, high values reduce the 
number of more densely packed groups.

### Task 7

Visualize multidimensional data using UMAP with different n_neighbors and min_dist 
parameters. Calculate the running time of the algorithm using the time library and 
compare it with the running time of t-SNE.

t7

__Output__
```
t7: Elapsed time: 1.9380676746368408 seconds
```
![](images/p2_8.png)
![](images/p2_9.png)
![](images/p2_10.png)
![](images/p2_11.png)
![](images/p2_12.png)
![](images/p2_13.png)

__Conclusion__\
Based on the obtained graphs, we can draw the following conclusion: Small values of 
the n_neighbors parameter mean that the algorithm is limited to a small neighborhood 
around each point - it tries to capture the local structure of the data. Large ones 
retain the global structure, but lose details. The min_dist parameter determines the 
minimum distance at which points can be located in the new space. Low values define 
the division of data into clusters, while high values define the structure of the data 
as a whole. Despite the fact that theoretically the UMAP method should be faster than 
the TSNE method, practical measurements have shown the opposite, although the difference 
is less than a second. The likely reason is that only the first 1000 data items are used, 
so both methods are fast, but if you increase the number of data items, the UMAP method 
is faster.

---

## Practice 3 - Familiarize yourself with various methods of statistical research

### Task 1

Load data from file

### Task 2

Use the describe() method to view statistics on the data. Draw conclusions.

t1-t2

__Output__
```
t2:
   age     sex     bmi  children smoker     region      charges
0   19  female  27.900         0    yes  southwest  16884.92400
1   18    male  33.770         1     no  southeast   1725.55230
2   28    male  33.000         3     no  southeast   4449.46200
3   33    male  22.705         0     no  northwest  21984.47061
4   32    male  28.880         0     no  northwest   3866.85520

               age          bmi     children       charges
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.207025    30.663397     1.094918  13270.422265
std      14.049960     6.098187     1.205493  12110.011237
min      18.000000    15.960000     0.000000   1121.873900
25%      27.000000    26.296250     0.000000   4740.287150
50%      39.000000    30.400000     1.000000   9382.033000
75%      51.000000    34.693750     2.000000  16639.912515
max      64.000000    53.130000     5.000000  63770.428010
--------------------------------------------------
```

__Conclusion__\
You can see a count of all the attributes of the dataset, and also that age in the dataset goes 
from 18 to 64, bmi (body mass index) from 15.9 to 53, children (number of children) from 0 to 5, 
charges (expenses) from 1121.9 up to 63770. Average value (mean) of each attribute: 39 for age, 
30.6 for bmi, 1 for children, 13270 for charges. Standard deviation is an estimate for a sample 
that allows you to evaluate how much the data changes relative to their average: 14 for age, 6 
for bmi, 1 for children, 12110 for charges. Each subsequent quarter increases (25%, 50%, 75%, 
100%), the charges attribute increases more strongly. The count attribute is the same everywhere.

### Task 3

Construct histograms for numerical indicators. Draw conclusions.

t3

__Output__
![](images/p3_1.png)

__Conclusion__\
The x-axis indicates the values of the variable, and the y-axis indicates how often the value of 
this variable occurs in a certain interval. The interval length was chosen to be 15. From left to 
right, top to bottom, you can see how often the value of the variable appears. Charges values close 
to zero appear more often. The most common age value is close to zero, while the rest are evenly 
distributed. The bmi values have a normal distribution. The most common value of children is zero; 
the larger the number, the less repeated it is.

### Task 4

Find measures of central tendency and measures of dispersion for body mass index (bmi) and charges 
(charges). Display results as text and in histograms (3 vertical lines). Add a legend to graphs. 
Draw conclusions.

t4

__Output__
```
t4:
Mean BMI = 30.663397
Mode BMI:  32.3
Median BMI = 30.400000

Mean Charges = 13270.422265
Mode Charges:  1639.5631
Median Charges = 9382.033000

Standard Deviation of charges:  12110.011236694001
Range of charges:  62648.554110000005
Quarter range of charges using numpy:  11879.80148
Quarter range of charges with scipy:  11879.80148

Standard Deviation of bmi:  6.098186911679014
Range of bmi:  37.17
Quarter range of bmi using numpy:  8.384999999999998
Quarter range of bmi with scipy:  8.384999999999998
--------------------------------------------------
```
![](images/p3_2.png)


__Conclusion__\
The bmi graph shows that the values in it have a normal distribution. According to the charges graph, 
from left to right the values are repeated less. You can also see from the bmi graph that mode and 
median are close to each other - the mean and central values are almost the same. The most common 
value is mode. In charges, the mode value is the most repeated (on the left), also in charges there 
is much more variability in values, the average differs from the central one. The measure of dispersion 
includes: Standard Deviation, Range, Quarter range (the difference between the 1st and 3rd quarters 
is the most common). The range y of the charges attribute is very large (max – min).

### Task 5

Construct a box-plot for numerical indicators. The names of the graphs must correspond to the names 
of the features. Draw conclusions.

t5

__Output__
![](images/p3_3.png)
![](images/p3_4.png)

__Conclusion__\
In bmi and charges, the points outside the “whiskers” (quarters 1 and 3 (second 50%)) are outliers (values 
that are very different from other values, they are very rare), the orange line inside the “box” (clusters 
of average values) – median, outliers outside the category are too large to characterize the category. The 
graph shows the distribution of information in a certain category. Categories: age, bmi, charges and children. 
There are outliers only in the bmi and charges attributes, and these outliers are strictly greater than the 
maximum; in the rest they are not present. In charges, half of the values are outliers.

### Task 6

Using the charges or imb attribute, check whether the central limit theorem holds. Use different sample 
lengths n. Number of samples = 300. Display the result in the form of histograms. Find the standard deviation 
and mean for the resulting distributions. Draw conclusions.

t6

__Output__
```
t6:
Mean of  n=1    12198.327287   Std of  n=1    10855.966798
Mean of  n=10    13357.920196   Std of  n=10    4062.840514
Mean of  n=50    13118.524016   Std of  n=50    1833.114858
Mean of  n=100    13378.232319   Std of  n=100    1197.308316
Mean of  n=150    13309.708941   Std of  n=150    800.090288
Mean of  n=200    13260.895946   Std of  n=200    735.038002

Standard Deviation:  12110.011236694001
Range:  62648.554110000005
Quarter range using numpy:  11879.80148
Quarter range with scipy:  11879.80148
--------------------------------------------------
```

![](images/p3_5.png)
![](images/p3_6.png)

__Conclusion__\
Dataset values pass the central limit theorem in general and for various sample lengths (except n = 1) in particular. 
The larger n, the closer to the ideal form of the normal distribution. The value n is the length of samples. All mean 
values are around 12 thousand. The larger the sample length, the smaller the standard deviation and the closer the 
graph is to a very accurate form of normal distribution.

### Task 7

Construct 95% and 99% confidence intervals for the mean expenditure and mean BMI.

t7

__Output__
```
t7:
90% confidence interval for Charges:  (12725.864762144516, 13814.979768137997)
95% confidence interval for Charges:  (12621.54197822916, 13919.302552053354)
90% confidence interval for BMI:  (30.389176352638128, 30.93761736933497)
95% confidence interval for BMI:  (30.336642971534822, 30.990150750438275)
--------------------------------------------------
```

### Task 8

Check the distribution of the following characteristics for normality: body mass index, expenses. Formulate the null 
and alternative hypotheses. For each characteristic, use the KS test and q-q plot. Draw conclusions based on the 
obtained p-values.

t8

__Output__
```
t8:
KstestResult(statistic=0.02613962682509635, pvalue=0.31453976932347394, statistic_location=28.975, statistic_sign=1)
KstestResult(statistic=0.18846204110424236, pvalue=4.39305730768502e-42, statistic_location=13470.86, statistic_sign=1)
--------------------------------------------------
```
![](images/p3_7.png)
![](images/p3_8.png)

__Conclusion__\
The task is to test the null and alternative hypotheses, null – there is no difference (or there are few significant 
differences), alternative – there are significant differences (visible differences). They are determined by the p-level 
value (pvalue) - if it is less than 0.05, then the null hypothesis is rejected and the alternative is accepted, if it 
is more, vice versa. Hypotheses are always about difference. Normality – comparison of the dependence of the original 
sample values with the values of an ideal normal distribution. If the values follow the line exactly, then they are 
normally distributed. If the deviations are higher than the straight line, then the values are higher than normal and 
vice versa. Conclusions from the graphs: the bmi graph shows a fairly normal distribution, but the charges graph is 
very different from the normal distribution. The x-axis shows the standard normal distribution, and the y-axis shows 
the distribution of the sample under study. Null hypothesis - we assume that there are no differences between the ideal 
normal distribution and the dependence of our initial values (charges, for example). Alternative hypothesis - we assume 
that significant differences exist between the sample values and the normal distribution. For the bmi characteristic, 
the null hypothesis was chosen and the alternative was rejected, and for the charges characteristic, vice versa. The 
essence of the KS test is to assess the significance of the differences between two samples, as in the previous test 
(q-q). Here too, hypotheses are selected based on the pvalue. For the bmi feature, the pvalue is higher than 0.05, 
which means we need to accept the null hypothesis, since the sample has a normal distribution. The charges attribute 
has a much smaller pvalue, which means the null hypothesis is rejected since the sample does not have a normal 
distribution.

### Task 9

Load data from file

t9

__Output__
```
t9:
          dateRep  day  month  year  cases  deaths countriesAndTerritories  \
0      14/12/2020   14     12  2020    746       6             Afghanistan
1      13/12/2020   13     12  2020    298       9             Afghanistan
2      12/12/2020   12     12  2020    113      11             Afghanistan
3      12/12/2020   12     12  2020    113      11             Afghanistan
4      11/12/2020   11     12  2020     63      10             Afghanistan
...           ...  ...    ...   ...    ...     ...                     ...
61899  25/03/2020   25      3  2020      0       0                Zimbabwe
61900  24/03/2020   24      3  2020      0       1                Zimbabwe
61901  23/03/2020   23      3  2020      0       0                Zimbabwe
61902  22/03/2020   22      3  2020      1       0                Zimbabwe
61903  21/03/2020   21      3  2020      1       0                Zimbabwe

      geoId countryterritoryCode  popData2019 continentExp  \
0        AF                  AFG   38041757.0         Asia
1        AF                  AFG   38041757.0         Asia
2        AF                  AFG   38041757.0         Asia
3        AF                  AFG   38041757.0         Asia
4        AF                  AFG   38041757.0         Asia
...     ...                  ...          ...          ...
61899    ZW                  ZWE   14645473.0       Africa
61900    ZW                  ZWE   14645473.0       Africa
61901    ZW                  ZWE   14645473.0       Africa
61902    ZW                  ZWE   14645473.0       Africa
61903    ZW                  ZWE   14645473.0       Africa

       Cumulative_number_for_14_days_of_COVID-19_cases_per_100000
0                                               9.013779
1                                               7.052776
2                                               6.868768
3                                               6.868768
4                                               7.134266
...                                                  ...
61899                                                NaN
61900                                                NaN
61901                                                NaN
61902                                                NaN
61903                                                NaN

[61904 rows x 12 columns]

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 61904 entries, 0 to 61903
Data columns (total 12 columns):
 #   Column                                             Non-Null Count  Dtype
---  ------                                             --------------  -----
 0   dateRep                                            61904 non-null  object
 1   day                                                61904 non-null  int64
 2   month                                              61904 non-null  int64
 3   year                                               61904 non-null  int64
 4   cases                                              61904 non-null  int64
 5   deaths                                             61904 non-null  int64
 6   countriesAndTerritories                            61904 non-null  object
 7   geoId                                              61629 non-null  object
 8   countryterritoryCode                               61781 non-null  object
 9   popData2019                                        61781 non-null  float64
 10  continentExp                                       61904 non-null  object
 11  Cumulative_number_for_14_days_of_COVID-19_cases_per_100000
                                                        59025 non-null  float64
dtypes: float64(2), int64(5), object(5)
memory usage: 5.7+ MB
--------------------------------------------------
```

### Task 10

Check the data for missing values. Display the number of missing values as a percentage. Remove the two features that 
have the most missing values. For the remaining features, process gaps: for a categorical feature, use filling with 
the default value (for example, “other”), for a numeric feature, use filling with the median value. Show that there 
are no more gaps in the data.

t10

__Output__
```
t10:
 dateRep : 0.0%
 day : 0.0%
 month : 0.0%
 year : 0.0%
 cases : 0.0%
 deaths : 0.0%
 countriesAndTerritories : 0.0%
 geoId : 0.4%
 countryterritoryCode : 0.2%
 popData2019 : 0.2%
 continentExp : 0.0%
 Cumulative_number_for_14_days_of_COVID-19_cases_per_100000 : 4.7%

          dateRep  day  month  year  cases  deaths countriesAndTerritories  \
0      14/12/2020   14     12  2020    746       6             Afghanistan
1      13/12/2020   13     12  2020    298       9             Afghanistan
2      12/12/2020   12     12  2020    113      11             Afghanistan
3      12/12/2020   12     12  2020    113      11             Afghanistan
4      11/12/2020   11     12  2020     63      10             Afghanistan
...           ...  ...    ...   ...    ...     ...                     ...
61899  25/03/2020   25      3  2020      0       0                Zimbabwe
61900  24/03/2020   24      3  2020      0       1                Zimbabwe
61901  23/03/2020   23      3  2020      0       0                Zimbabwe
61902  22/03/2020   22      3  2020      1       0                Zimbabwe
61903  21/03/2020   21      3  2020      1       0                Zimbabwe

      countryterritoryCode  popData2019 continentExp
0                      AFG   38041757.0         Asia
1                      AFG   38041757.0         Asia
2                      AFG   38041757.0         Asia
3                      AFG   38041757.0         Asia
4                      AFG   38041757.0         Asia
...                    ...          ...          ...
61899                  ZWE   14645473.0       Africa
61900                  ZWE   14645473.0       Africa
61901                  ZWE   14645473.0       Africa
61902                  ZWE   14645473.0       Africa
61903                  ZWE   14645473.0       Africa

[61904 rows x 10 columns]

 dateRep : 0.0%
 day : 0.0%
 month : 0.0%
 year : 0.0%
 cases : 0.0%
 deaths : 0.0%
 countriesAndTerritories : 0.0%
 countryterritoryCode : 0.0%
 popData2019 : 0.0%
 continentExp : 0.0%
--------------------------------------------------
```

### Task 11

View statistics on data using describe(). Draw conclusions about which features contain outliers. See for which 
countries the number of deaths per day exceeded 3000 and how many such days there were.

t11

__Output__
```
t11:
                day         month          year          cases        deaths  \
count  61904.000000  61904.000000  61904.000000   61904.000000  61904.000000
mean      15.629232      7.067104   2019.998918    1155.079026     26.053987
std        8.841624      2.954816      0.032881    6779.010824    131.222948
min        1.000000      1.000000   2019.000000   -8261.000000  -1918.000000
25%        8.000000      5.000000   2020.000000       0.000000      0.000000
50%       15.000000      7.000000   2020.000000      15.000000      0.000000
75%       23.000000     10.000000   2020.000000     273.000000      4.000000
max       31.000000     12.000000   2020.000000  234633.000000   4928.000000

        popData2019
count  6.190400e+04
mean   4.091909e+07
std    1.529798e+08
min    8.150000e+02
25%    1.324820e+06
50%    7.169456e+06
75%    2.851583e+07
max    1.433784e+09

0        False
1        False
2        False
3        False
4        False
         ...
61899    False
61900    False
61901    False
61902    False
61903    False
Name: deaths, Length: 61904, dtype: bool

There are 11 days where deaths >= 3000

          dateRep  day  month  year   cases  deaths   countriesAndTerritories  \
2118   02/10/2020    2     10  2020   14001    3351                 Argentina
16908  07/09/2020    7      9  2020   -8261    3800                   Ecuador
37038  09/10/2020    9     10  2020    4936    3013                    Mexico
44888  14/08/2020   14      8  2020    9441    3935                      Peru
44909  24/07/2020   24      7  2020    4546    3887                      Peru
59007  12/12/2020   12     12  2020  234633    3343  United_States_of_America
59009  10/12/2020   10     12  2020  220025    3124  United_States_of_America
59016  03/12/2020    3     12  2020  203311    3190  United_States_of_America
59239  24/04/2020   24      4  2020   26543    3179  United_States_of_America
59245  18/04/2020   18      4  2020   30833    3770  United_States_of_America
59247  16/04/2020   16      4  2020   30148    4928  United_States_of_America

      countryterritoryCode  popData2019 continentExp
2118                   ARG   44780675.0      America
16908                  ECU   17373657.0      America
37038                  MEX  127575529.0      America
44888                  PER   32510462.0      America
44909                  PER   32510462.0      America
59007                  USA  329064917.0      America
59009                  USA  329064917.0      America
59016                  USA  329064917.0      America
59239                  USA  329064917.0      America
59245                  USA  329064917.0      America
59247                  USA  329064917.0      America
--------------------------------------------------
```

![](images/p3_9.png)

__Conclusion__\
Outliers are present in the cases and deaths characteristics because there the minima are negative (can be seen from 
describe()) – the values to the left of the significant minimum. It is also clear from the general graph that outliers 
are also present in the year and popData2019 features. The latter has more of them than the others. A total of 11 days 
were found when the number of deaths exceeded 3000. Countries in which these days were recorded: Argentina (Argentina), 
Ecuador (Ecuador), Mexico (Mexico), Peru (Peru), United_States_of_America (USA).

### Task 12

Find data duplication. Remove duplicates.

t12

__Output__
```
t12:
          dateRep  day  month  year  cases  deaths countriesAndTerritories  \
3      12/12/2020   12     12  2020    113      11             Afghanistan
218    12/05/2020   12      5  2020    285       2             Afghanistan
48010  29/05/2020   29      5  2020      0       0             Saint_Lucia
48073  28/03/2020   28      3  2020      0       0             Saint_Lucia

      countryterritoryCode  popData2019 continentExp
3                      AFG   38041757.0         Asia
218                    AFG   38041757.0         Asia
48010                  LCA     182795.0      America
48073                  LCA     182795.0      America

          dateRep  day  month  year  cases  deaths countriesAndTerritories  \
0      14/12/2020   14     12  2020    746       6             Afghanistan
1      13/12/2020   13     12  2020    298       9             Afghanistan
2      12/12/2020   12     12  2020    113      11             Afghanistan
4      11/12/2020   11     12  2020     63      10             Afghanistan
5      10/12/2020   10     12  2020    202      16             Afghanistan
...           ...  ...    ...   ...    ...     ...                     ...
61899  25/03/2020   25      3  2020      0       0                Zimbabwe
61900  24/03/2020   24      3  2020      0       1                Zimbabwe
61901  23/03/2020   23      3  2020      0       0                Zimbabwe
61902  22/03/2020   22      3  2020      1       0                Zimbabwe
61903  21/03/2020   21      3  2020      1       0                Zimbabwe

      countryterritoryCode  popData2019 continentExp
0                      AFG   38041757.0         Asia
1                      AFG   38041757.0         Asia
2                      AFG   38041757.0         Asia
4                      AFG   38041757.0         Asia
5                      AFG   38041757.0         Asia
...                    ...          ...          ...
61899                  ZWE   14645473.0       Africa
61900                  ZWE   14645473.0       Africa
61901                  ZWE   14645473.0       Africa
61902                  ZWE   14645473.0       Africa
61903                  ZWE   14645473.0       Africa

[61900 rows x 10 columns]

Empty DataFrame
Columns: [dateRep, day, month, year, cases, deaths, countriesAndTerritories, countryterritoryCode, popData2019, continentExp]
Index: []
--------------------------------------------------
```

### Task 13

Load data from the file “bmi.csv”. Take two samples from there. One sample is the body mass index of people from the 
northwest region, the second sample is the body mass index of people from the southwest region. Compare the means of 
these samples using Student's t-test. Preliminarily check samples for normality (Shopiro-Wilk test) and homogeneity of 
variance (Bartlett test).

t13

__Output__
```
t13:
      bmi     region
0  22.705  northwest
1  28.880  northwest
2  27.740  northwest
3  25.840  northwest
4  28.025  northwest

        bmi     region
0    22.705  northwest
1    28.880  northwest
2    27.740  northwest
3    25.840  northwest
4    28.025  northwest
..      ...        ...
320  26.315  northwest
321  31.065  northwest
322  25.935  northwest
323  30.970  northwest
324  29.070  northwest

[325 rows x 2 columns]

      bmi     region
325  27.9  southwest
326  34.4  southwest
327  24.6  southwest
328  40.3  southwest
329  35.3  southwest
..    ...        ...
645  20.6  southwest
646  38.6  southwest
647  33.4  southwest
648  44.7  southwest
649  25.8  southwest

[325 rows x 2 columns]

The variance of both data groups: 26.305165492071005 32.29731162130177

TtestResult(statistic=-3.2844171500398582, pvalue=0.001076958496307695, df=648.0)

(-3.2844171500398667, 0.0010769584963076643, 648.0)

ShapiroResult(statistic=0.9954646825790405, pvalue=0.4655335247516632)
 ShapiroResult(statistic=0.9949268698692322, pvalue=0.3629520535469055)

BartlettResult(statistic=3.4000745256459286, pvalue=0.06519347353581818)
--------------------------------------------------
```

__Conclusion__\
Null hypothesis - there will be no significant difference between the average bmi values of the northwest and southwest 
regions, alternative - there will be a difference. Since 0.001 (T test) is less than 0.005, the null theory must be 
rejected - there is a significant difference between the average bmi values of the two regions. Normality: in both 
tests the pvalue (Shapiro) is above 0.05, which means we need to accept the null hypothesis - bmi in both regions has 
a normal distribution. Homogeneity – testing the equality of depressions in two samples. Null hypothesis – the samples 
under consideration are obtained from general populations with the same depression. The alternative hypothesis is the 
opposite. Since 0.06 (Barlett) > 0.05 – we accept the null hypothesis – the depressions of the samples are the same – 
there are no significant differences between the bmi values of the regions.

### Task 14

The dice was rolled 600 times and the following results were obtained (see Listing 13). Use the Chi-square test to 
check whether the resulting distribution is uniform. Use the scipy.stats.chisquare() function.

t14

__Output__
```
t14:
   N  Observed  Expected
0  1        97       100
1  2        98       100
2  3       109       100
3  4        95       100
4  5        97       100
5  6       104       100

Power_divergenceResult(statistic=1.44, pvalue=0.9198882077437889)
--------------------------------------------------
```

__Conclusion__\
The null hypothesis is that there will be a uniform distribution in the number of drops. Since 0.92 > 0.05, we accept 
the null hypothesis – uniform distribution.

### Task 15

Use the Chi-square test to test whether the variables are dependent. Create a dataframe using the following code 
(see Listing 14). Use the scipy.stats.chi2_contingency() function. Does marital status affect employment?

t15

__Output__
```
t15:
                        Married  Civil marriage  Isn't in relationships
Full working day             89              80                      35
Part-time employment         17              22                      44
Temporary doesn't work       11              20                      35
On the household             43              35                       6
Retired                      22               6                       8

1.7291616900960234e-21
--------------------------------------------------
```

__Conclusion__\
The null hypothesis is that marital status does not affect employment, the alternative hypothesis does (there is a 
significant relationship). Since the pvalue is very small (< 0.05), we reject the null hypothesis and accept the 
alternative - there is a relationship (marital status affects employment).


---
# TODO
...


---

### Task *



*

__Output__
```

```

---
