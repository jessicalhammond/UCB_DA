

```python
# As final considerations:

# Your script must work for both data-sets given.
# You must use the Pandas Library and the Jupyter Notebook.
# You must submit a link to your Jupyter Notebook with the viewable Data Frames.
# You must include an exported markdown version of your Notebook called  README.md in your GitHub repository.
# You must include a written description of three observable trends based on the data.
# See Example Solution for a reference on the expected format.
```


```python
import pandas as pd
import os 
import numpy as np

filesch = os.path.join('raw_data', 'schools_complete.csv')
filestu = os.path.join('raw_data', 'students_complete.csv')

schoolsdf = pd.read_csv(filesch)
studentsdf = pd.read_csv(filestu)



```


```python
schoolsdf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
studentsdf.columns
```




    Index(['Student ID', 'name', 'gender', 'grade', 'school', 'reading_score',
           'math_score'],
          dtype='object')




```python
# renmae column title to match
schoolsdf.rename(inplace=True,columns={"name":"school"})
schoolsdf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge two dataframes using an inner join -- inner join will drop rows where there is not an exact match
merge = pd.merge(studentsdf, schoolsdf, on="school", how="inner")
merge
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>82</td>
      <td>80</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Nicole Baker</td>
      <td>F</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>69</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Michael Roth</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>95</td>
      <td>87</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Matthew Greene</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>84</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Andrew Alexander</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>70</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Daniel Cooper</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>78</td>
      <td>77</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Brittney Walker</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>79</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>William Long</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>71</td>
      <td>79</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Tammy Hebert</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>85</td>
      <td>67</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>Dr. Jordan Carson</td>
      <td>M</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>88</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>Donald Zamora</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>88</td>
      <td>55</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>Kimberly Santiago</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>74</td>
      <td>75</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>Kevin Stevens</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>69</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>Brandi Lyons</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>89</td>
      <td>80</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>Lisa Davis</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>91</td>
      <td>89</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>Kristen Lopez</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>77</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>Kimberly Stewart</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>99</td>
      <td>84</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>Christopher Parker</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>81</td>
      <td>68</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>Chelsea Griffith</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>85</td>
      <td>73</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>Cesar Morris</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>92</td>
      <td>70</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>Melanie Decker</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>63</td>
      <td>85</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>Tracey Oconnor</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>80</td>
      <td>58</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>Kelly James</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>73</td>
      <td>55</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>Nicole Brown</td>
      <td>F</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>88</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>39140</th>
      <td>39140</td>
      <td>Cheyenne Hernandez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>76</td>
      <td>99</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39141</th>
      <td>39141</td>
      <td>Jonathan Sullivan</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>86</td>
      <td>93</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39142</th>
      <td>39142</td>
      <td>Deborah Higgins DDS</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>96</td>
      <td>83</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39143</th>
      <td>39143</td>
      <td>Steven Jackson</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>71</td>
      <td>93</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39144</th>
      <td>39144</td>
      <td>Cristian Webster</td>
      <td>M</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>77</td>
      <td>87</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39145</th>
      <td>39145</td>
      <td>Audrey Fry</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>94</td>
      <td>74</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39146</th>
      <td>39146</td>
      <td>Michael Carroll</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>69</td>
      <td>95</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39147</th>
      <td>39147</td>
      <td>Raymond Hawkins</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>88</td>
      <td>81</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39148</th>
      <td>39148</td>
      <td>Christopher Wilson</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>89</td>
      <td>89</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39149</th>
      <td>39149</td>
      <td>Glenda Fletcher</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>82</td>
      <td>93</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39150</th>
      <td>39150</td>
      <td>Jennifer Hamilton</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>80</td>
      <td>75</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39151</th>
      <td>39151</td>
      <td>Shannon Williams</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>84</td>
      <td>73</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39152</th>
      <td>39152</td>
      <td>Lori Moore</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>98</td>
      <td>84</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39153</th>
      <td>39153</td>
      <td>William Hubbard</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>80</td>
      <td>75</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39154</th>
      <td>39154</td>
      <td>Bradley Johnson</td>
      <td>M</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>91</td>
      <td>71</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39155</th>
      <td>39155</td>
      <td>John Brooks</td>
      <td>M</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>92</td>
      <td>98</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39156</th>
      <td>39156</td>
      <td>Stephanie Contreras</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>79</td>
      <td>95</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39157</th>
      <td>39157</td>
      <td>Kristen Gonzalez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>79</td>
      <td>94</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39158</th>
      <td>39158</td>
      <td>Kari Holloway</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>87</td>
      <td>90</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39159</th>
      <td>39159</td>
      <td>Kimberly Cabrera</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>85</td>
      <td>72</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39160</th>
      <td>39160</td>
      <td>Katie Weaver</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>89</td>
      <td>86</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39161</th>
      <td>39161</td>
      <td>April Reyes</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>70</td>
      <td>84</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39162</th>
      <td>39162</td>
      <td>Derek Weeks</td>
      <td>M</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>94</td>
      <td>77</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39163</th>
      <td>39163</td>
      <td>John Reese</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>90</td>
      <td>75</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39164</th>
      <td>39164</td>
      <td>Joseph Anthony</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>97</td>
      <td>76</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39165</th>
      <td>39165</td>
      <td>Donna Howard</td>
      <td>F</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>99</td>
      <td>90</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39166</th>
      <td>39166</td>
      <td>Dawn Bell</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>95</td>
      <td>70</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39167</th>
      <td>39167</td>
      <td>Rebecca Tanner</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>73</td>
      <td>84</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39168</th>
      <td>39168</td>
      <td>Desiree Kidd</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>99</td>
      <td>90</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
    <tr>
      <th>39169</th>
      <td>39169</td>
      <td>Carolyn Jackson</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>95</td>
      <td>75</td>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
  </tbody>
</table>
<p>39170 rows × 11 columns</p>
</div>




```python
# Create a high level snapshot (in table form) of the district's key metrics, including:
# Total Schools, Total Students, Total Budget

totalschools = schoolsdf["school"].count()
totalstudents = merge["Student ID"].count()
totalbudget = schoolsdf['budget'].sum()

# Average Math Score, Average Reading Score
sumsch1 = studentsdf.loc[:,('school', 'reading_score', 'math_score',)]
rmean = round(merge['reading_score'].mean(), 2)
mmean = round(merge['math_score'].mean(), 2)

# % Passing Math, % Passing Reading, Overall Passing Rate (Average of the above two)
#get table of only students who passed math
pass_m = merge.loc[merge['math_score'] >= 70,]
pass_m2 = pass_m['math_score'].count()
#get percentage
percentm = ((pass_m2/totalstudents)*100)
# print("% Passing Math:", percentm)

#get table of only students who passed reading
pass_r = merge.loc[merge['reading_score'] >= 70,]
#count the number of students in that table
pass_r2 = pass_r['reading_score'].count()
#get percentage
percentr = ((pass_r2/totalstudents)*100)
# print("% Passing Reading:", percentr)

#get percentage for overall passing
overall = ((percentr + percentm)/2)

#format passing as percents

overall = "{0:.0f}%".format(overall)
percentr = "{0:.0f}%".format(percentr)
percentm = "{0:.0f}%".format(percentm)
totalbudget = '${:.2f}'.format(totalbudget)

Dsum = pd.DataFrame({'Total Schools' : [totalschools], 'Total Students' : [totalstudents], 
                     'Total Budget': [totalbudget], 'Average Reading Score': [rmean], 
                     'Average Math Score': [mmean], '% Passing Reading': [percentr], 
                     '% Passing Math': [percentm], '% Passing Overall': [overall]}, dtype=object)
Dsum
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Overall</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Total Budget</th>
      <th>Total Schools</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>75%</td>
      <td>80%</td>
      <td>86%</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>$24649428.00</td>
      <td>15</td>
      <td>39170</td>
    </tr>
  </tbody>
</table>
</div>




```python
merge.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create an overview table that summarizes key metrics about each school, including:
# School Name, School Type, Total Students, Total School Budget, Per Student Budget, 
# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
# Overall Passing Rate (Average of the above two)

schoolname = merge['school'].unique()
typesum = pd.DataFrame(grouped['type'].describe())
typesum = typesum.drop(columns=['count', 'unique', 'freq'])
totstu_byschool = grouped['name'].count()
budget_school = grouped.mean()["budget"]
budget_perstudent = budget_school/totstu_byschool

#get passing per type of test
passingmath = merge[merge["math_score"] > 70]
passingreading = merge[merge["reading_score"] > 70]

#group based on school
groupedmath = passingmath.groupby(['school'])
groupedread = passingreading.groupby(['school'])

#calculate percent passing per test by schoopl
perpass_m = groupedmath.count()["math_score"] / totstu_byschool * 100
perpass_r = groupedread.count()["reading_score"] / totstu_byschool * 100

#overall percent passing
overall_summary = ((perpass_m + perpass_r)/2)


summary = pd.DataFrame({"School":schoolname, "Type": typesum["top"], "Total Students": totstu_byschool, 
                        "Budget":budget_school, "Budget Per Student": budget_perstudent,
                        "Average Reading Score": rmean_summary, "Average Math Score": mmean_summary, 
                        "% Passing Reading":perpass_r, "% Passing Math": perpass_m, 
                        "Overall Passing": overall_summary
                       })

summary

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Budget</th>
      <th>Budget Per Student</th>
      <th>Overall Passing</th>
      <th>School</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>64.630225</td>
      <td>79.300643</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>71.965434</td>
      <td>Huang High School</td>
      <td>4976</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>91.711518</td>
      <td>Figueroa High School</td>
      <td>1858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>71.091896</td>
      <td>Shelton High School</td>
      <td>2949</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>65.753925</td>
      <td>77.510040</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>71.631982</td>
      <td>Hernandez High School</td>
      <td>2739</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>89.713896</td>
      <td>93.392371</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>91.553134</td>
      <td>Griffin High School</td>
      <td>1468</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>3022020.0</td>
      <td>652.0</td>
      <td>71.467098</td>
      <td>Wilson High School</td>
      <td>4635</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>248087.0</td>
      <td>581.0</td>
      <td>91.686183</td>
      <td>Cabrera High School</td>
      <td>427</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>1910635.0</td>
      <td>655.0</td>
      <td>71.066164</td>
      <td>Bailey High School</td>
      <td>2917</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>3094650.0</td>
      <td>650.0</td>
      <td>71.067003</td>
      <td>Holden High School</td>
      <td>4761</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>585858.0</td>
      <td>609.0</td>
      <td>91.943867</td>
      <td>Pena High School</td>
      <td>962</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>2547363.0</td>
      <td>637.0</td>
      <td>70.905226</td>
      <td>Wright High School</td>
      <td>3999</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>89.892107</td>
      <td>92.617831</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>1056600.0</td>
      <td>600.0</td>
      <td>91.254969</td>
      <td>Rodriguez High School</td>
      <td>1761</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>90.214067</td>
      <td>92.905199</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>1043130.0</td>
      <td>638.0</td>
      <td>91.559633</td>
      <td>Johnson High School</td>
      <td>1635</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>1319574.0</td>
      <td>578.0</td>
      <td>92.093736</td>
      <td>Ford High School</td>
      <td>2283</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>1049400.0</td>
      <td>583.0</td>
      <td>91.861111</td>
      <td>Thomas High School</td>
      <td>1800</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
# School Name
# School Type
# Total Students
# Total School Budget
# Per Student Budget
# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
# Overall Passing Rate (Average of the above two)
# Top Performing Schools (By Passing Rate)top_perform = summary.sort_values(["Overall Passing"], ascending=False)
top_perform.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Budget</th>
      <th>Budget Per Studnet</th>
      <th>Overall Passing</th>
      <th>School</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>1319574.0</td>
      <td>578.0</td>
      <td>92.093736</td>
      <td>Ford High School</td>
      <td>2283</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>585858.0</td>
      <td>609.0</td>
      <td>91.943867</td>
      <td>Pena High School</td>
      <td>962</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>1049400.0</td>
      <td>583.0</td>
      <td>91.861111</td>
      <td>Thomas High School</td>
      <td>1800</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>91.711518</td>
      <td>Figueroa High School</td>
      <td>1858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>248087.0</td>
      <td>581.0</td>
      <td>91.686183</td>
      <td>Cabrera High School</td>
      <td>427</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.
top_perform.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Budget</th>
      <th>Budget Per Studnet</th>
      <th>Overall Passing</th>
      <th>School</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Hernandez High School</th>
      <td>64.746494</td>
      <td>78.187702</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>3022020.0</td>
      <td>652.0</td>
      <td>71.467098</td>
      <td>Wilson High School</td>
      <td>4635</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.750424</td>
      <td>78.433367</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>71.091896</td>
      <td>Shelton High School</td>
      <td>2949</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>63.852132</td>
      <td>78.281874</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>3094650.0</td>
      <td>650.0</td>
      <td>71.067003</td>
      <td>Holden High School</td>
      <td>4761</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>63.318478</td>
      <td>78.813850</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>1910635.0</td>
      <td>655.0</td>
      <td>71.066164</td>
      <td>Bailey High School</td>
      <td>2917</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>64.066017</td>
      <td>77.744436</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>2547363.0</td>
      <td>637.0</td>
      <td>70.905226</td>
      <td>Wright High School</td>
      <td>3999</td>
      <td>District</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Math Scores by Grade
# Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.


# filter data out for 9th, 10th, 11th, 12th from merged_dataframe
merge.sort_values("grade", ascending=True)
grades =merge.sort_values("grade")
ninth = merge[merge["grade"]=="9th"]
tenth = merge[merge["grade"]=="10th"]
eleventh = merge[merge["grade"]=="11th"]
twelfth = merge[merge["grade"]=="12th"]
grades.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15978</th>
      <td>15978</td>
      <td>Victoria Hayden</td>
      <td>F</td>
      <td>10th</td>
      <td>Wilson High School</td>
      <td>85</td>
      <td>88</td>
      <td>5</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>13223</th>
      <td>13223</td>
      <td>Melissa Thomas</td>
      <td>F</td>
      <td>10th</td>
      <td>Griffin High School</td>
      <td>81</td>
      <td>86</td>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
    <tr>
      <th>7563</th>
      <td>7563</td>
      <td>David Ayala</td>
      <td>M</td>
      <td>10th</td>
      <td>Shelton High School</td>
      <td>72</td>
      <td>98</td>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>28170</th>
      <td>28170</td>
      <td>Cameron Perez</td>
      <td>M</td>
      <td>10th</td>
      <td>Rodriguez High School</td>
      <td>90</td>
      <td>99</td>
      <td>11</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>7565</th>
      <td>7565</td>
      <td>Daniel Stanley</td>
      <td>M</td>
      <td>10th</td>
      <td>Shelton High School</td>
      <td>80</td>
      <td>87</td>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
  </tbody>
</table>
</div>




```python
#math averages by grade
ninthave = ninth.groupby(["school"]).mean()["math_score"]
tenthave = tenth.groupby(["school"]).mean()["math_score"]
eleventhave = eleventh.groupby(['school']).mean()["math_score"]
twelfthave = twelfth.groupby(['school']).mean()["math_score"]

mathbygrade = pd.DataFrame({"9th Grade Average":ninthave, "10th Grade Average": tenthave, 
                            "11th Grade Average": eleventhave, "12th Grade Average":twelfthave, })
mathbygrade

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10th Grade Average</th>
      <th>11th Grade Average</th>
      <th>12th Grade Average</th>
      <th>9th Grade Average</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
      <td>83.094697</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
      <td>76.403037</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
      <td>77.361345</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
      <td>82.044010</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
      <td>77.438495</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
      <td>83.787402</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
      <td>77.027251</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
      <td>77.187857</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
      <td>83.625455</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
      <td>76.859966</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
      <td>83.420755</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
      <td>83.590022</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
      <td>83.085578</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading Scores by Grade
# Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

#reading averages by grade
ninthave = ninth.groupby(["school"]).mean()["reading_score"]
tenthave = tenth.groupby(["school"]).mean()["reading_score"]
eleventhave = eleventh.groupby(['school']).mean()["reading_score"]
twelfthave = twelfth.groupby(['school']).mean()["reading_score"]

readbygrade = pd.DataFrame({"9th Grade Average":ninthave, "10th Grade Average": tenthave, 
                            "11th Grade Average": eleventhave, "12th Grade Average":twelfthave, })
readbygrade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10th Grade Average</th>
      <th>11th Grade Average</th>
      <th>12th Grade Average</th>
      <th>9th Grade Average</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
      <td>81.303155</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
      <td>83.676136</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
      <td>81.198598</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
      <td>80.632653</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
      <td>83.369193</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
      <td>80.866860</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
      <td>83.677165</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
      <td>81.290284</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
      <td>81.260714</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
      <td>83.807273</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
      <td>80.993127</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
      <td>84.122642</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
      <td>83.728850</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
      <td>83.939778</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by School Spending

# Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
# Overall Passing Rate (Average of the above two)
# Scores by School Size

# Scores by School Spending
bins = [0, 585, 620, 645, 675]
groupnames = ["<$585", "$585-619", "$620-644", "$645-675"]

#bin budgets
summary["Range per Student"] = pd.cut(summary["Budget Per Student"], bins= bins, labels=groupnames)


spend_mathpass = summary.groupby(["Range per Student"]).mean()["% Passing Math"]
spend_readpass = summary.groupby(["Range per Student"]).mean()["% Passing Reading"]
spend_avemath = summary.groupby(["Range per Student"]).mean()["Average Reading Score"]
spend_averead = summary.groupby(["Range per Student"]).mean()["Average Math Score"]
spend_overall = summary.groupby(["Range per Student"]).mean()["Overall Passing"]

perspend = pd.DataFrame({"Average Math": spend_avemath, "Average Read": spend_averead,
                         "% Pass Math": spend_mathpass, "% Pass Read":spend_readpass, 
                        "Overall": spend_overall })


# Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).
perspend
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Pass Math</th>
      <th>% Pass Read</th>
      <th>Average Math</th>
      <th>Average Read</th>
      <th>Overall</th>
    </tr>
    <tr>
      <th>Range per Student</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>90.350436</td>
      <td>93.325838</td>
      <td>83.933814</td>
      <td>83.455399</td>
      <td>91.838137</td>
    </tr>
    <tr>
      <th>$585-619</th>
      <td>90.788049</td>
      <td>92.410786</td>
      <td>83.885211</td>
      <td>83.599686</td>
      <td>91.599418</td>
    </tr>
    <tr>
      <th>$620-644</th>
      <td>73.021426</td>
      <td>83.214343</td>
      <td>81.891436</td>
      <td>79.079225</td>
      <td>78.117884</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>63.972368</td>
      <td>78.427809</td>
      <td>81.027843</td>
      <td>76.997210</td>
      <td>71.200088</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Repeat the above breakdown, but this time group schools based on a reasonable approximation of school size (Small, Medium, Large).

# Scores by School Size
bins = [0, 750, 1500, 5000]
groupnames = ["Small", "Medium", "Large"]

#bin budgets
summary["School Size"] = pd.cut(summary["Total Students"], bins= bins, labels=groupnames)


size_mathpass = summary.groupby(["School Size"]).mean()["% Passing Math"]
size_readpass = summary.groupby(["School Size"]).mean()["% Passing Reading"]
size_avemath = summary.groupby(["School Size"]).mean()["Average Reading Score"]
size_averead = summary.groupby(["School Size"]).mean()["Average Math Score"]
size_overall = summary.groupby(["School Size"]).mean()["Overall Passing"]

persize = pd.DataFrame({"Average Math": size_avemath, "Average Read": size_averead,
                         "% Pass Math": size_mathpass, "% Pass Read":size_readpass, 
                        "Overall": size_overall })

persize


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Pass Math</th>
      <th>% Pass Read</th>
      <th>Average Math</th>
      <th>Average Read</th>
      <th>Overall</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>91.686183</td>
    </tr>
    <tr>
      <th>Medium</th>
      <td>90.698944</td>
      <td>92.798056</td>
      <td>83.930728</td>
      <td>83.595708</td>
      <td>91.748500</td>
    </tr>
    <tr>
      <th>Large</th>
      <td>75.082775</td>
      <td>84.529854</td>
      <td>82.188448</td>
      <td>79.624438</td>
      <td>79.806314</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).
# Scores by School Type

type_groups = merge.groupby('type')
type_count = type_groups['Student ID'].count()

type_passingM = passingmath.groupby('type')['Student ID'].count()/ type_count * 100
type_passingR = passingreading.groupby('type')['Student ID'].count()/ type_count * 100

type_avemath = merge.groupby(["type"]).mean()["reading_score"]
type_averead = merge.groupby(["type"]).mean()["math_score"]
type_overall = ((type_passingM+type_passingR)/2)

perdist = pd.DataFrame({"Average Math": type_avemath, "Average Read": type_averead,
                         "% Pass Math": type_passingM, "% Pass Read":type_passingR, 
                        "Overall": type_overall})

perdist
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Pass Math</th>
      <th>% Pass Read</th>
      <th>Average Math</th>
      <th>Average Read</th>
      <th>Overall</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>90.282106</td>
      <td>93.152370</td>
      <td>83.902821</td>
      <td>83.406183</td>
      <td>91.717238</td>
    </tr>
    <tr>
      <th>District</th>
      <td>64.305308</td>
      <td>78.369662</td>
      <td>80.962485</td>
      <td>76.987026</td>
      <td>71.337485</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Analysis of school performance based on budget per student doesn't actually appear to have impact on the success of the % passing. If we look at the overall passing in the chart below, the school with the higest percent of overall passing is a school that does not receive the most dollar per student. All schools in the top performing class are Charter schools, however. This may show that Charter schools whether funded exceptionally well or not, perform better than district schools.")
top_perform.head()

```

    Analysis of school performance based on budget per student doesn't actually appear to have impact on the success of the % passing. If we look at the overall passing in the chart below, the school with the higest percent of overall passing is a school that does not receive the most dollar per student. All schools in the top performing class are Charter schools, however. This may show that Charter schools whether funded exceptionally well or not, perform better than district schools.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Budget</th>
      <th>Budget Per Studnet</th>
      <th>Overall Passing</th>
      <th>School</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>90.932983</td>
      <td>93.254490</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>1319574.0</td>
      <td>578.0</td>
      <td>92.093736</td>
      <td>Ford High School</td>
      <td>2283</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.683992</td>
      <td>92.203742</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>585858.0</td>
      <td>609.0</td>
      <td>91.943867</td>
      <td>Pena High School</td>
      <td>962</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.277778</td>
      <td>93.444444</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>1049400.0</td>
      <td>583.0</td>
      <td>91.861111</td>
      <td>Thomas High School</td>
      <td>1800</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.558665</td>
      <td>93.864370</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>91.711518</td>
      <td>Figueroa High School</td>
      <td>1858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>248087.0</td>
      <td>581.0</td>
      <td>91.686183</td>
      <td>Cabrera High School</td>
      <td>427</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("It also appears that the larger the school the lower the overall passing % based on the rank by size chart.")
persize
```

    It also appears that the larger the school the lower the overall passing % based on the rank by size chart.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Pass Math</th>
      <th>% Pass Read</th>
      <th>Average Math</th>
      <th>Average Read</th>
      <th>Overall</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small</th>
      <td>90.632319</td>
      <td>92.740047</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>91.686183</td>
    </tr>
    <tr>
      <th>Medium</th>
      <td>90.698944</td>
      <td>92.798056</td>
      <td>83.930728</td>
      <td>83.595708</td>
      <td>91.748500</td>
    </tr>
    <tr>
      <th>Large</th>
      <td>75.082775</td>
      <td>84.529854</td>
      <td>82.188448</td>
      <td>79.624438</td>
      <td>79.806314</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("As was found in the top performing chart, Charter schools outperform District schools across the board.")
perdist
```

    As was found in the top performing chart, Charter schools outperform District schools across the board.





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Pass Math</th>
      <th>% Pass Read</th>
      <th>Average Math</th>
      <th>Average Read</th>
      <th>Overall</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>90.282106</td>
      <td>93.152370</td>
      <td>83.902821</td>
      <td>83.406183</td>
      <td>91.717238</td>
    </tr>
    <tr>
      <th>District</th>
      <td>64.305308</td>
      <td>78.369662</td>
      <td>80.962485</td>
      <td>76.987026</td>
      <td>71.337485</td>
    </tr>
  </tbody>
</table>
</div>


