
LaChandra Ash
Jan 4, 2020

Summary

The relationship between the amount of siblings the respondent had and amount of children
they had displayed a close relationship, For example if a respondent had three siblings, they more
than likely had approxiamelty three children. The linear line of regression showed a positve relationship
between the variables.

The coverance of siblings and children was 0.8241575. The correlation results between the variables was
0.1813177. I used the spearman, kendall, and pearson methods to calculate both correlation and covariance.
The variables had an 82 percent covariance and 18 percent correlation.

I used the kendall and pearson test to analyse the two variables and the kendall test ranked correlation coefficient tau.
The variables had a p-value of 9.439e-16, z = 8.0339, and tau was 0.1413747 for the correlation coefficient. The 
pearson test yielded a lower positive relationship. The two variables had a 95 percent confidence level of 0.1384257 result using
the pearson test.

I did not see any skewness nor significant scores. Adding the sex variable showed that there was a 0.2235308 correlation between
all three variable.

The y-intercept is 1.396 and the slope is 0.138. The coefficient of determination = r^2 = 0.050
coefficient of correlation = r = 0.223. The predictied number of children for a person with three siblings are is
y^ = a +b*x
= 1.396 + 0.138 *x
= 1.396 + 0.138* 3
= 1.81 predicted amount of children. 

The predicted number of children for someone without siblings is 
y^ = a +b*x
= 1.396 + 0.138 *x
= 1.396 + 0.138* 0
= 1.396 predicted amount of children.

The regression model shows a better prediction of the amount children a respondent may have versus using the mean value 
siblings.

Codes

library(ggplot2)
install.packages("ggplot2")

install.packages("corrplot")


gss <- gss_2016_
gss

library(ggplot2)
ggplot(data = gss, aes(x = CHILDS , y = SIBS, Z = SEX, Colour(distinct = FALSE, main = "GSS Survey"))) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE)


cov(CHILDS , SIBS, use = "complete.obs",
    method = c("pearson", "kendall", "spearman"))

cor(CHILDS, SIBS, use = "complete.obs",
    method = c("pearson", "kendall", "spearman"))


cor.test(CHILDS, SIBS, method = c("pearson", "Kendall", "spearman"))


res <- cor.test(gss$CHILDS, gss$SIBS, 
                method = "pearson")
res

res$estimate

res2 <- cor.test(gss$CHILDS, gss$SIBS,  method="kendall")
res2