[![Build Status](https://travis-ci.com/ds997/PyStatisticalCalculator.svg?token=LogVxqzVJkyBNsiAfq33&branch=master)](https://travis-ci.com/ds997/PyStatisticalCalculator)


# PyStatiscalCalculator


## Group Members
1. ds997 - Divyanshu Sachdeva
2. js2547 - Jasman Preet Singh
3. sb2344 - Soham Banerjee


Statistical calculator functions

1. Population Mean 
2. Median
3. Mode
4. Population Standard Deviation
5. Variance of population proportion
6. Z-Score
7. Standardized score
8. Population Correlation Coefficient
9. Confidence Interval
10. Population Variance
11. P Value
12. Proportion
13. Sample Mean
14. Sample Standard Deviation
15. Variance of sample proportion

#Checklist
- [x] Population Mean 
- [x] Median
- [x] Mode 
- [x] Population Standard Deviation 


**Population Mean**

The term population mean, which is the average score of the population on a given variable, is represented by:
```
μ = ( Σ Xi ) / N
```
The symbol ‘μ’ represents the population mean.  The symbol ‘Σ Xi’ represents the sum of all scores present in the population (say, in this case) X1 X2 X3 and so on.  The symbol 
‘N’ represents the total number of individuals or cases in the population.


**Median**

The median of a set of data is the middlemost number in the set. The median is also the number that is halfway into the set. To find the median, the data should first be arranged in order from least to greatest.
If there is an odd number of observations,

For example, consider the list of numbers
```
1, 3, 3, 6, 7, 8, 9
```
This list contains seven numbers. The median is the fourth of them, which is 6.

If there is an even number of observations,

For example, consider the list of numbers
```
1, 2, 3, 4, 5, 6, 8, 9
```
This list contains eight numbers. the median is the mean of the middle two numbers i.e. (4+5)/2 is 4.5.

**Mode**

To find the mode, or modal value, it is best to put the numbers in order. Then count how many of each number. A number that appears most often is the mode.
Example:
```
3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29
```
In order these numbers are:
```
3, 5, 7, 12, 13, 14, 20, 23, 23, 23, 23, 29, 39, 40, 56
```
This makes it easy to see which numbers appear most often.
In this case the mode is 23.

**Population Standard Deviation**

Standard deviation measures the spread of a data distribution. It measures the typical distance between each data point and the mean.
Here's the formula again for population standard deviation:
```
σ = ([Σ(x - u)2]/N)1/2
```
Where:
-	σ is the population standard deviation
-	Σ represents the sum or total from 1 to N
-	x is an individual value
-	u is the average of the population
-	N is the total number of the population

**Variance of population proportion**

A population proportion, is a parameter that describes a percentage value associated with a population. A population proportion is usually estimated through an unbiased sample statistic obtained from an observational study or experiment.

**Z-Score**

A Z-score is a numerical measurement used in statistics of a value's relationship to the mean (average) of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score.
The basic z score formula for a sample is:
```
z = (x – μ) / σ 
```
**Standardized score**

In statistics, the standard score is the signed fractional number of standard deviations by which the value of an observation or data point is above the mean value of what is being observed or measured.
When a frequency distribution is normally distributed, we can find out the probability of a score occurring by standardizing the scores, known as standard scores (or z scores). The standard normal distribution simply converts the group of data in our frequency distribution such that the mean is 0 and the standard deviation is 1.

![Standard_score](https://statistics.laerd.com/statistical-guides/img/DIAGRAM8.gif)

**Population Correlation Coefficient**

The correlation coefficient of two variables in a data set equals to their covariance divided by the product of their individual standard deviations.
The population correlation coefficient uses σx and σy as the population standard deviations, and σxy as the population covariance.


![](https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2012/12/population-correlation-coefficient.png)


**Confidence Interval**

 A confidence interval is a range of values, derived from sample statistics, that is likely to contain the value of an unknown population parameter. The confidence level is designated prior to examining the data. Most commonly, the 95% confidence level is used. However, other confidence levels can be used, for example, 90% and 99%.

**Population variance**

Population variance (σ2) tells us how data points in a specific population are spread out. It is the average of the distances from each data point in the population to the mean, squared.
σ2 is usually represented as σ2 and can be calculated using the following formula:

![](https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2017/07/population-variance.png)


Here N is the population size and the xi are data points. μ is the population mean.





