

```python
import os
import pandas as pd
import matplotlib.pyplot as plt

cityfile = os.path.join('raw_data', 'city_data.csv')
ridefile = os.path.join('raw_data', 'ride_data.csv')
city = pd.read_csv(cityfile)
ride = pd.read_csv(ridefile)

merged = city.merge(ride, on='city', how='inner')

```


```python
#filter by city type
rural = merged.loc[merged["type"] == "Rural",:]
urban = merged.loc[merged["type"] == "Urban",:]
suburban = merged.loc[merged["type"] == "Suburban",:]
```


```python
# Rural Data = Average Fare ($) Per City, Total Number of Rides * Total Number of Drivers

rural_groups = rural.groupby('city')
rural_avfare = rural_groups['fare'].mean()
rural_drivercount = (rural_groups['driver_count'].mean())**2
rural_totalrides = rural_groups['city'].count()

rural_totalrides
```




    city
    East Leslie             11
    East Stephen            10
    East Troybury            7
    Erikport                 8
    Hernandezshire           9
    Horneland                4
    Jacksonfort              6
    Kennethburgh            10
    Kinghaven                6
    Manuelchester            1
    Matthewside              4
    New Johnbury             4
    North Whitney           10
    Shelbyhaven              6
    South Elizabethmouth     5
    South Joseph            12
    Stevensport              5
    West Kevintown           7
    Name: city, dtype: int64




```python
# Urban Data = Average Fare ($) Per City, Total Number of Rides * Total Number of Drivers

urban_groups = urban.groupby('city')
urban_avfare = urban_groups['fare'].mean()
urban_drivercount = (urban_groups['driver_count'].mean())**2 
urban_totalrides = urban_groups['city'].count()

# urban_totalrides
```


```python
# Suburban Data = Average Fare ($) Per City, Total Number of Rides * Total Number of Drivers
suburban_groups = suburban.groupby('city')
suburban_avfare = suburban_groups['fare'].mean()
suburban_drivercount = (suburban_groups['driver_count'].mean())**2 
suburban_totalrides = suburban_groups['city'].count()

# suburban_totalrides
```


```python
plt.figure(figsize=(20,10))

#urban plot
plt.scatter(urban_totalrides, urban_avfare, c='Gold', edgecolor='cccccc', s=urban_drivercount, alpha=0.5, label = "Urban")
#suburban
plt.scatter(suburban_totalrides, suburban_avfare, c='lightskyblue', edgecolor='cccccc', s=suburban_drivercount, alpha=0.5, label = "Suburban")
#rural
plt.scatter(rural_totalrides,rural_avfare, c='lightcoral',edgecolor='cccccc', s=rural_drivercount, alpha=0.5,label = "Rural")
lgnd = plt.legend(loc='lower right', labelspacing=3, markerfirst=False, scatteryoffsets=[.5], markerscale=.5)

plt.xlim(0, 40)
plt.ylim()
plt.grid(True)
plt.title('Ride Data by City Type, Fare, and No. of Drivers')
plt.suptitle('The size of the bubble represents the number of drivers available in each city')
plt.xlabel("Total Number of Rides")
plt.ylabel("Average Fare ($)")
```




    Text(0,0.5,'Average Fare ($)')




![png](output_5_1.png)



```python
merged_groupby_data=(merged.groupby(['type']))
x_axis=merged_groupby_data['ride_id'].count()
explode = (0,0,0.1)
colors = ["Gold", "LightSkyBlue", 'LightCoral']
x_axis.plot(kind='pie',autopct="%1.1f%%", shadow=True,colors=colors, explode=explode, startangle=150)
plt.title("% of Total Rides by City Type")
plt.axis("off")
```




    (-1.25, 1.25, -1.25, 1.25)




![png](output_6_1.png)



```python
# * % of Total Fares by City Type
merged_groupby_data=(merged.groupby(['type']))
x_axis=merged_groupby_data['fare'].sum()
explode = (0,0,0.1 )
colors = ["Gold", "LightSkyBlue", 'LightCoral']
x_axis.plot(kind='pie',autopct="%1.1f%%", shadow=True,colors=colors,explode=explode, startangle=150)
plt.title("% of Total Fares by City Type")
plt.axis("off")
```




    (-1.25, 1.25, -1.25, 1.25)




![png](output_7_1.png)



```python
# * % of Total Drivers by City Type
merged_groupby_data=(merged.groupby(['type']))
x_axis=merged_groupby_data['driver_count'].count()
explode = (0,0,0.1 )
colors = ["Gold", "LightSkyBlue", 'LightCoral']
x_axis.plot(kind='pie',autopct="%1.1f%%", shadow=True,colors=colors, explode=explode, startangle=150)
plt.title("% of Total Drivers by City Type")
plt.axis("off")
```




    (-1.25, 1.25, -1.25, 1.25)




![png](output_8_1.png)

