
# Hypothesis Testing with the Northwind Database

For this project, we will be working with the Northwind database--a free, open-source dataset created by Microsoft containing data from a fictional company. Here's the schema for the Northwind database:

<img src='https://raw.githubusercontent.com/learn-co-curriculum/dsc-mod-3-project/master/Northwind_ERD_updated.png'>

## Purpose: 

The purpose of this project is to practice hypothesis testing and answer the following questions in the process:
    
**Question_1**: _Does discount amount have a statistically significant effect on the quantity of a product in an order? If so, at what level(s) of discount?_

**Question_2:** _Is there a significant difference between local and international sales?_

**Question_3:** _Do the category/type of goods have a significant impact on the quantity ordered?_

**Question_4:** _Are there certain products that have a significant statistical difference, within the revenue generated with respective catgories?_

## Questions & Summary

### Overview

* Created query to pull the necessary information from the database
* We vizualized the data to get some insight into patterns present
* Test whether or not we reject or fail to reject our null hypothesis with ANOVA, Tukey, Shaprio, Levene, & Welch's T-test
* Calculate effect sizes & statistical power to see difference between populations
* Report the results of our hypothesis tests

### **Question_1:**  _Does discount amount have a statistically significant effect on the quantity of products order? If so, at what level(s) of discount?_

$H_0:$ Discounts do not have a significant effect on the quantity of a product in an order

$H_a:$ There is a significant effect of discounts on quantity of products ordered


### Summary:

Based on the statistics and the test received from the data, discounts are significant in determining the quantity of goods sold.  However, the level of discount does not seem to very different amongst the different discounts. 

To better capture the results of our tests, discounts levels without sufficient data were removed from our analysis.

The following discounts were removed:

0.01, 0.02, 0.03, 0.04, & 0.06

The higher discounts has an advantage over the lower ones that we did compare, but due to the large magnitutde of the p-test ran, the difference is slighty greater due to associated effect sizes.



For full notebook information and testing, click on the link below:

[Question_1 Notebook](Question_1.ipynb)
______________________


### Question_2: _Is there a significant difference between local and international sales?_

$H_0:$ There is not a significant differencec between local and international sales

$H_a:$ There is a significant difference between local and international sales


### Summary

Based on the results of our test, there is a significant difference in quantities of products ordered and sales generated in foreign regions compared to North America, when we look at them region by regions(North America, Scadindavia, Western Europe, etc).  This difference is only seen when we compare North America to Southern Europe.

When we look at the difference between North America and the cumulative results of every other region, there does not seem to be a significant differece.  There does seem to be a slight one, but not one that is large enough to be noteworthy, based on our graphs.




For full notebook information and testing, click on the link below:

[Question_2 Notebook](Question_2.ipynb)

_______________________


### Question_3:  _Do the category/type of goods have a significant impact on the quantity ordered?_

$H_0:$ Categories of goods all have the same effect on quantities ordered

$H_a:$ There is a significant difference of quantities ordered by Categories


### Summary: 

   - Based on the results of the test performed, a significant difference was not found for one category of goods over another.

For full notebook information and testing, click on the link below:

[Question_3 Notebook](Question_3.ipynb)
________________________


### Question_4:  _Are there certain products that have a significant statistical difference, within the revenue generated with respective catgories?_

$H_0:$ All products have the same effect on revenue generated within their respective categories

$H_a:$ There is at least one product that has a significant effect on revenue within respective category


### Summary

**Grains/Cereal:**
   - Gnocchi di nonna Alice & Wimmers gute Semmelknödel are the two products that stood out the most compared to others within the grain/cereal category.  They both share the top spot for the most significant grain products that have impacts on sales.
   - **Both of these product should be marketed more heavily**

**Seafood:**
  - Carnarvon Tigers stood out compared to all other products.  
  - Based on the data, I recommend marketing this product even more to clients.

**Confections:**
  - Schoggi Schokolade was one product that stood apart from many of the other products sold by the company.
  - This good has a more significant stastical impact than all other confections, with the exception of Sir Rodney's Marmalade.
  - **_Schoggi Schokolade_ and _Sir Rodney's Marmalade_ should be marketed more heavily**
  
  

**Beverages:** 
   - _Côte de Blaye_ is the beverage that has the most significant impact on sales, over all other beverages.
   - __This product should be marketed more heavily__

**Dairy Products, Produce, Condiments, & Meat/Poultry:**
   - There was not a specific dairy product that outperformed a majority of the others sold.  
   - They all tend to have the same amount of significance statistically.




For full notebook information and testing, click on the link below:

[Question_4 Notebook](Question_4.ipynb)
