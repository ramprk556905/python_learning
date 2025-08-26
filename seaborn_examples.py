import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print(tips)


##Creating scatter plot
sns.scatterplot(x='total_bill',y='tip',data=tips)
plt.title("Scatter Plot of total bill")
# plt.show()

## Creating Line plot
sns.lineplot(x='size',y='total_bill',data=tips)
plt.title('Line Plot of tips data')
# plt.show()

##Creating CategoricalPlot

sns.barplot(x='day',y='total_bill',data=tips)
plt.title('CategoryPlot fot total bill')
# plt.show()


##Creating HeatMap
corr = tips[['total_bill','tip','size']].corr()
# print(corr)

# sns.heatmap(corr,annot=True,cmap='coolwarm')
# plt.show()

sales_df = pd.read_csv('sales_data.csv')
print(sales_df.head())

##Plot total sales by product
plt.figure(figsize=(10,6))
sns.barplot(x='Product Category',y='Total Revenue', data=sales_df,estimator=sum)
plt.xlabel('Product Category')
plt.ylabel('Total sales')
plt.title('Total Sales by Product')
plt.show()
