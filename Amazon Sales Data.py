import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'AmazonSalesData.csv'
sales_data = pd.read_csv(file_path)

# Basic information about the dataset
sales_data.info()
sales_data.head()

# Summary statistics of numeric columns
summary_stats = sales_data.describe()

# Distribution of sales across different regions
region_sales_distribution = sales_data['Region'].value_counts()

# Relationship between units sold and total profit
units_sold_vs_profit = sales_data[['Units Sold', 'Total Profit']]

# Top 5 countries by total revenue
top_5_countries_revenue = sales_data.groupby('Country')['Total Revenue'].sum().nlargest(5)

# Plotting the distribution of sales across different regions
plt.figure(figsize=(10, 6))
sns.countplot(y='Region', data=sales_data, order=sales_data['Region'].value_counts().index)
plt.title('Distribution of Sales Across Different Regions')
plt.xlabel('Number of Sales')
plt.ylabel('Region')
plt.show()

# Plotting the relationship between units sold and total profit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units Sold', y='Total Profit', data=sales_data)
plt.title('Relationship Between Units Sold and Total Profit')
plt.xlabel('Units Sold')
plt.ylabel('Total Profit')
plt.show()

# Additional analyses
# 1. Average Unit Price and Unit Cost by Item Type
avg_price_cost_by_item = sales_data.groupby('Item Type')[['Unit Price', 'Unit Cost']].mean()

# 2. Total Revenue by Sales Channel
total_revenue_by_channel = sales_data.groupby('Sales Channel')['Total Revenue'].sum()

# 3. Monthly sales trend (assuming Order Date format is MM/DD/YYYY)
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['Month'] = sales_data['Order Date'].dt.to_period('M')
monthly_sales_trend = sales_data.groupby('Month')['Total Revenue'].sum()

# Plotting the average unit price and unit cost by item type
plt.figure(figsize=(14, 8))
avg_price_cost_by_item.plot(kind='bar')
plt.title('Average Unit Price and Unit Cost by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Average Price / Cost')
plt.show()

# Plotting the total revenue by sales channel
plt.figure(figsize=(10, 6))
total_revenue_by_channel.plot(kind='pie', autopct='%1.1f%%', startangle=140, explode=[0, 0.1])
plt.title('Total Revenue by Sales Channel')
plt.ylabel('')
plt.show()

# Plotting the monthly sales trend
plt.figure(figsize=(14, 8))
monthly_sales_trend.plot(marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Display all results
{
    'Summary Statistics': summary_stats,
    'Region Sales Distribution': region_sales_distribution,
    'Top 5 Countries by Total Revenue': top_5_countries_revenue,
    'Average Price and Cost by Item Type': avg_price_cost_by_item,
    'Total Revenue by Sales Channel': total_revenue_by_channel,
    'Monthly Sales Trend': monthly_sales_trend.head()
}
