## 4.1 Lesson Plan - Introduction to Pandas & Jupyter

### Overview

Today's lesson will introduce students to Jupyter Notebook and the basics of the Pandas module.

### Notes

* The objective of today's class is to ease you into Pandas and, as such, the tone of the lesson should err on the side of exploratory. It's okay for you to ask questions, make mistakes, and take it slow as you get started with this challenging module.

* Pandas is not a simple topic to pick up and use straight away since the syntax is complicated and can be rather confusing for beginners. Patience and perseverence is key. As with all things, practice makes perfect, and you will find yourself picking up on Pandas's quirks before too long.

- - -

### Class Objectives

* Students should be able to serve Jupyter notebook files from local directories and connect to their development environment
* Students should be able to create Pandas DataFrames from scratch
* Students should understand how to run functions on Pandas DataFrames
* Students should know how to read/write DataFrames from/to CSV files using Pandas
* The class should understand how to navigate through DataFrames using Loc and Iloc
* The class should understand how to filter and slice Pandas DataFrames

- - -

### 1. Welcome (0:01)

* Welcome to what may be one of the most challenging weeks in the entire course. Pandas, just like a real panda, may seem cuddly at first, but there are claws under all that fuzz. The Pandas module is an extremely powerful tool, however, and is worth pushing through every hurdle you may face.

* As with all things, Pandas will get easier with time. Rest assured that despite the challenges you will face, Pandas will make your life easier with its mastery.

### 2. Introduction to Jupyter Notebook (0:10)

* Before diving into Pandas, however, let's take some time to introduce Jupyter Notebook.

  * Jupyter Notebook is an open-source application that allows its users to create documents that contain live code, equations, visualizations, and explantory text.

  * In other words, Jupyter Notebook combines a text editor, the console, and a markdown file into one application.

* Activate the `PythonData` development environment that was created last week before typing `jupyter notebook` into the terminal.

  ![Jupyter Notebook Terminal](Images/01-Jupyter_Terminal.png)

  * Running `jupyter notebook` will automatically open up a webpage where users can navigate into any files/folders within the folder they ran the command from.

  * Users can create new Jupyter Notebook files from the webpage that is opened by clicking the "new" button and selecting their development environment from the list that appears.

  * Python files created through Jupyter Notebook are given the `ipynb` extension rather than `py` and cannot be easily read/altered within a typical text editor.

  ![Jupyter Notebook Page](Images/01-Jupyter_Webpage.png)

* Create a new Python file using Jupyter Notebook, making sure to set the kernel as "PythonData"

  * Setting the kernel for Jupyter projects is important because these kernels let the program know which libraries will be available for use. Only those libraries loaded into the development environment selected can be used in a Jupyter Notebook project.

  * If your development environment does not show up within Jupyter Notebook, simply run the command `conda install -c anaconda nb_conda_kernels` within the terminal so that Anaconda environments can be used as kernels.

* Navigate into [01-JupyterIntro](Activities/01-Ins_JupyterIntro/JupyterIntro.ipynb) and note how Jupyter notebook organizes Python code into cells.

  * Note how each cell contains Python code that can be run independently by placing the cursor inside a cell and pressing `Shift + Enter`.

  * Modify some of the code in a cell and note how Jupyter notebooks allow users to both experiment with code directly and save it for later.

  * Make sure to run the second-to-last cell one more time after running the final cell on its own. This shows how values in Jupyter Notebooks are stored based on what lines of code were run previously.

### 3. Netflix Remix (0:10)

* For this activity, your will be creating a Jupyter Notebook that performs the same functions as the Netflix activity from last week.

![Netflix Remix Output](Images/02-NetflixRemix_Outputs.png)

* **File:**

  * [Netflix.py](Activities/02-Stu_NetflixRemix/Unsolved/Netflix.py)

  * [Netflix_Ratings.csv](Activities/02-Stu_NetflixRemix/Resources/netflix_ratings.csv)

* **Instructions:**

  * Using `Netflix.py` as a jumping off point, convert the application so that it runs properly within a Jupyter Notebook.

  * Make sure to have the application print out the user's input, the path to `Netflix_Ratings.csv`, and the final rating/review for the film in different cells.

* **Bonus:**

  * Go through any of the activities from last week and attempt to convert them to run within a Jupyter Notebook. While doing this, try to split up the code into cells and print out the outputs.

* **Hints:**

  * If your development environment does not appear as a potential kernel within Jupyter Notebook, close out of Jupyter Notebook and run `conda install -c anaconda nb_conda_kernels` within the terminal. Upon reloading Jupyter Notebook, all possible kernels should now appear.

### 4. Introduction to Pandas (0:05)

* The way Jupyter Notebook allows for the testing and visualization of code really starts to shine through when these features are applied to large tables. As you have likely realized, however, it can be rather stressful modifying huge datasets using pure Python.

  * Thankfully, there exists a library that, despite its cute and cuddly name, is extraordinarily powerful when it comes to visualizing, analyzing, and altering large datasets. This library is **Pandas**.

* While Python alone is stuck using lists, tuples, and dictionaries, Pandas lets Python programmers work with "Series" and "DataFrames"

  * These two datatypes - unique to Pandas - are essentially structured lists, with many built-in convenience methods that allow for quick and easy manipulation of data

  * A Pandas Series is a one-dimensional labeled array capable of holding any data type. This means that, like an array, the data is linear, but also that, like a dictionary, it has an index that acts like a key.

  ![Pandas Series](Images/03-IntroToPandas_Series.png)

  * A Pandas DataFrame is a two-dimensional labeled data structure with columns of potentially different types. The easiest way to think of it is like an Excel spreadsheet with each column being a Series.

  ![Pandas DataFrame](Images/03-IntroToPandas_DataFrame.png)

### 5. DataFrame Creation (0:05)

* Open [03-IntroToPandas](Activities/03-Ins_IntroToPandas/creating_data_frames.ipynb) within Jupyter Notebook in order to see what Pandas Series and DataFrames are and how to create them.

  * Before doing anything else, the Pandas library is imported using `import pandas as pd`. This method of import allows Pandas functions/methods to be called using the variable `pd`.

  * To create a Series, simply use the `pd.Series()` function and place a list within the parentheses. The index for the values within the Series will be the numeric index of the initial list.

  ![Pandas Series Creation](Images/03-IntroToPandas_SeriesCode.png)

  * There are multiple ways through which to create DataFrames from scratch. One way is to use the `pd.DataFrame()` function and provide it with a list of dictionaries. Each dictionary will represent a new row where the keys become column headers and the values will be placed inside the table.

  * Another way is to use the `pd.DataFrame()` function like before but this time provide it with a dictionary of lists. The keys of the dictionary will be the column headers and the listed values will be placed into their respective rows.

  ![Pandas DataFrame Creation](Images/03-IntroToPandas_DataFrameCode.png)

### 6. Data-Frame Shop (0:10)

* You will now try your hand at creating DataFrames from scratch using the two methods discussed earlier. This will also provide you with the opportunity to better understand what DataFrames look like.

![DataFrame Shop Code](Images/04-DataFrameShop_Output.png)

* **Instructions:**

  * Create a DataFrame for a frame shop that contains three columns - "Frame", "Price", and "Sales" - and has five rows of data stored within it.

  * Using an alternate method from that used before, create a DataFrame for an art gallery that contains three columns - "Painting", "Price", and "Popularity" - and has four rows of data stored within it.

* **Bonus:**

  * Once both of the DataFrames have been created, discuss with those around you which method you prefer to use and why.

### 8. DataFrame Functions (0:05)

* The benefits of using Pandas DataFrames do not lie solely in its visualization of tables. There are also many functions/methods that come packaged with Pandas that allow for quick and easy analysis of large datasets.

* Open up [05-Ins_DataFunctions](Activities/05-Ins_DataFunctions/data_functions.ipynb) within Jupyter Notebook and note how an external CSV file is being imported. You will learn how to do this later in today's lesson.

  * The first method to note is that of `head()` which takes a DataFrame and shows only the first five rows of data inside of it. This number can be increased/decreased, however, by placing an integer within the parentheses.

  * The `head()` method is helpful in that it allows the programmer to look at a minified version of a much larger table, thus allowing them to make informed changes without having to search through the entire dataset.

  * Another useful method comes in the form of `describe()` which will print out a DataFrame containing some analytic information on the table and its columns. It is also helpful in showing what other data functions can be performed on a DataFrame or Series.

  ![Head and Describe](Images/05-DataFunction_HeadDescribe.png)

  * Most data functions can also be performed on a Series by referencing a single column within the whole DataFrame. This is done in a similar way to referencing a key within dictionary by taking the DataFrame and following it up with brackets with the desired column's header contained within like a key.

  * Multiple columns can be referenced as well by placing all of the column headers desired within a pair of double brackets. If two sets of brackets are not used then Pandas will return an error.

  ![Column Reference](Images/05-DataFunction_ColumnReference.png)

  * There are situations in which it is helpful to list out all of the unique values stored within a column. This is precisely what the `unique()` function does by looking into a Series and returning all of the different values within.

  * Another method that holds similar functionality is that of `value_counts()` which not only returns a list of all unique values within a series but also counts how many times a value appears.

  ![Unique Values](Images/05-DataFunction_UniqueValue.png)

  * Calculations can also be performed on columns and then added back into a DataFrame as a new column by referencing the DataFrame, placing the desired column header within brackets, and then setting it equal to a Series.

  ![Column Calculations](Images/05-DataFunction_ColumnCalc.png)

### 9. Training Grounds (0:10)

* You will now take a large DataFrame consisting of 200 rows, analyze it using some data functions, and then add a new column into it.

![Training Grounds Starter](Images/06-TrainingGrounds_Start.png)

* **File:**

  * [TrainingGrounds.ipynb](Activities/06-Stu_TrainingGrounds/Unsolved/TrainingGrounds.ipynb)

* **Instructions:**

  * Using the DataFrame provided, perform all of the following actions...

  * Provide a simple, analytical overview of the dataset's numeric columns

  * Collect all of the names of the trainers within the dataset

  * Figure out how many students each trainer has

  * Find the avergae weight of the students at the gym

  * Find the combined weight of all of the students at the gym

  * Convert the "Membership (Days)" column into weeks and then add this new series into the DataFrame

### 11. Modifying Columns (0:05)

* As the class already discovered during the previous activity, columns within a DataFrame are not always placed within the desired position by default. In fact, they sometimes may not even have a descriptive or concise enough name.

  * Thankfully, it is very easy to modify the names/placement of columns using the `rename()` function and the use of double brackets.

* Open up [07-Ins_ColumnManipulation](Activities/07-Ins_ColumnManipulation/ColumnManipulation.ipynb) within Jupyter Notebook and walk through the code.

  * In order to collect a list of all the columns contained within a DataFrame, simply use the `df.columns` call, and an object containing the column headers will be printed to the screen.

  * To reorder the columns, create a reference to the DataFrame followed by two brackets with the column headers placed in the order desired.

  * It is also possible to remove columns in this way by simply not creating a reference to them. This will, in essence, drop them from the newly made DataFrame.

  * To rename the columns within a DataFrame, use the `df.rename()` method and place `columns={}` within the parentheses. Inside of the dictionary, the keys should be references to the current columns and the values should be the desired column names.

  ![Column Changes](Images/07-ColumnManipulation_Code.png)

### 12. Hey Arnold! (0:05)

* For this activity, you will be taking a premade DataFrame of "Hey Arnold!" characters and reorganizing it so that it is more understandable and organized.

![Hey Arnold Starter](Images/08-HeyArnold_Starter.png)

* **Instructions:**

  * Rename the columns of the DataFrame to the following: `Character`, `Hair Color`, `Height`, `Football Head`

  * Create a new DataFrame that contains all of the columns in the following order: `Character`, `Football Head`, `Hair Color`, `Height`

- - -

### 14. BREAK (0:15)

- - -

### 15. Reading and Writing CSVs (0:05)

* Up until this point in time, you have had to manually create DataFrames using the `pd.DataFrame()` method. There is a far more effective means by which to create large DataFrames: importing CSVs.

* Open up [09-Ins_ReadingWritingCSV](Activities/09-Ins_ReadingWritingCSV/pandas_reading_files.ipynb) within Jupyter Notebook and walk through the code.

  * Create a reference to the CSV's path and pass it in into the `pd.read_csv()` method, making certain to store the returned DataFrame within a variable. From then on, the DataFrame can be altered and manipulated like normal.

  * In most cases, it is not important to use or define the encoding of the base CSV file, but if the encoding is different than UTF-8, it may become necessary so that the CSV is translated correctly.

  ![Reading CSV](Images/09-ReadingWritingCSV_Read.png)

  * It is just as easy to write to a CSV file as it is to read from one. Simply use the `df.to_csv()` method, passing the path to the desired output file. By using the `index` and `header` parameters, programmers can also manipulate whether they would like the index or header for the table to be passed as well.

  * If the file referenced within the path does not exist, Pandas will return an error. The file must already exist in order for the DataFrame to be written in.

  ![Writing CSV](Images/09-ReadingWritingCSV_Write.png)

### 16. GoodReads - Part 1 (0:15)

* You will now take a large CSV of books, read it into Jupyter Notebook using Pandas, clean up the columns, and then write your modified DataFrame to a new CSV file.

* Open up [10-Stu_GoodReads/Resources/books.csv](Activities/10-Stu_GoodReads/Resources/books.csv) to see what you will be working with.

![GoodReads Output](Images/10-GoodReads_Output.png)

* **Files:**

  * [books.csv](Activities/10-Stu_GoodReads/Resources/books.csv)

* **Instructions:**

  * Read in the GoodReads CSV using Pandas

  * Remove unecessary columns from the DataFrame so that only the following columns remain: `isbn`, `original_publication_year`, `original_title`, `authors`, `ratings_1`, `ratings_2`, `ratings_3`, `ratings_4`, and `ratings_5`

  * Rename the columns to the following: `ISBN`, `Publication Year`, `Original Title`, `Authors`, `One Star Reviews`, `Two Star Reviews`, `Three Star Reviews`, `Four Star Reviews`, and `Five Star Reviews`

  * Write the DataFrame into a new CSV file

* **Hints:**

  * The base CSV file uses UTF-8 encoding. Trying to read in the file using some other encoding could lead to strange characters appearing within the dataset.

### 18. GoodReads - Part II (0:15)

* You will now take the modified version of the GoodReads DataFrame and create a new Summary DataFrame based upon that dataset using some of Pandas' built-in data functions.

![GoodReads Summary Output](Images/11-GoodReads_Summary.png)

* **File:**

  * [books_clean.csv](Activities/11-Stu_GoodReadsSummary/Resources/books_clean.csv)

* **Instructions:**

  * Using the modified DataFrame that was created earlier, create a summary table for the dataset that includes the following pieces of information...

  * The count of unique authors within the DataFrame

  * The year of the earliest published book in the DataFrame

  * The year of the latest published book in the DataFrame

  * The total number of reviews within the DataFrame

### 20. Exploring Data With Loc and Iloc (0:10)

* One of the most powerful aspects of Pandas is how easily programmers can collect specific rows/columns of data from a DataFrame using the `loc()` and `iloc()` methods.

  * The `loc()` method allows its users to select data using label-based indexes. In other words, it takes in strings as the keys and returns data based upon that.

  * Using `loc()` to search through rows is only really useful when the index of a dataset is a collection of strings. It is almost always useful when selecting data from rows, however, since column headers are exclusively strings. This can be done by using the `df.set_index()` function and passing in the desired column header for the index.

  ![Set Index](Images/12-LocAndIloc_SetIndex.png)

  * The `iloc()` method also allows its users to select data, but instead of using labels, it uses integer-based indexing for selection by position. In other words, it selects data in much the same way as one would select data from within a list—using a numeric index.

* Open up [12-Ins_LocAndIloc](Activities/12-Ins_LocAndIloc/LocAndIloc.ipynb) within Jupyter Notebook and run through the code line by line.

  * The typical way in which data is called using both `loc[]` and `iloc[]` is by using a pair of brackets which contain the rows desired, followed by a comma, and then the columns desired. For example: `loc["Berry","Phone Number"]` or `iloc[1,2]`

  ![Row and Column](Images/12-LocAndIloc_RowColumn.png)

  * It is also possible to select a range of data using `loc[]` and `iloc[]` by placing all of the values within brackets and/or using a colon to tell Pandas to look for a range. For example: `loc[["Richardson", "Berry", "Hudson", "Mcdonald", "Morales"],["id", "first_name", "Phone Number"]]` or `iloc[0:4, 0:3]`

  * By passing in a colon by itself, `loc[]` and `iloc[]` will select all rows or columns depending on where it is placed in relation to the comma. For example: `loc[:, ["first_name", "Phone Number"]` will select all rows of data but will only return the "first_name" and "Phone Number" columns.

  ![Exploring Data](Images/12-LocAndIloc_ExploringData.png)

* Another exciting feature of `loc[]` and `iloc[]` is that these methods can be used to conditionally filter rows of data based upon the values contained within a column.

  * The way in which this is done is by calling `loc[]` or `iloc[]` on a DataFrame and passing a logic test in place of the rows section of the call. For example: `loc[df["id"] >= 10, :]` will return all rows of data with a value equal to or greater than 10 within the "id" column.

  * It is possible to then select which columns to return by simply adding their references into the columns section of the `loc[]` or `iloc[]` expression.

  * If there are multiple conditions that should be checked for, `&` and `|` may also be added into the logic test as representations of `and` and `or`. This allows for a great amount of customization.

  ![Loc Conditions](Images/12-LocAndIloc_Conditions.png)

### 21. Good Movies (0:15)

* Now that you have covered exploring/filtering DataFrames using `loc[]` and `iloc[]`, you will now create an application that looks through IMDB data in order to find the best movies out there.

![Good Movies Output](Images/13-GoodMovies_Output.png)

* **Files:**

  * [goodMovies_unsolved.ipynb](Activities/13-Stu_GoodMovies/Unsolved/goodMovies.ipynb)

  * [movie_scores.csv](Activities/13-Stu_GoodMovies/Resources/movie_scores.csv)

* **Instructions:**

  * Use Pandas to load and display the CSV provided in `Resources`.

  * List all the columns in the data set.

  * We're only interested in IMDb data, so create a new table that takes the Film and all the columns relating to IMDB.

  * Filter for only the good movies—i.e., any film with an IMDb score greater than or equal to 7.

  * Filter for less popular movies that you may not have heard about - i.e., anything with under 20K votes

  * Finally, export this file to a spreadsheet, excluding the index, so we can keep track of our future watchlist.

### 23. Cleaning Data (0:05)

* When dealing with massive datasets, it is almost inevitable that duplicate rows, inconsistent spelling, and missing values will crop up.

  * While these issues may not seem significant in the grand scheme of things, they can severely hinder the analysis and visualization of a dataset by skewing the data one way or another.

  * Thankfully, Pandas includes methods through which its users can remove missing values, replace duplicates, and change values with relative ease.

* Open up [14-Ins_CleaningData](Activities/14-Ins_CleaningData/CleaningData.ipynb) within Jupyter Notebook and run through the code line-by-line.

  * In order to delete a column of extraneous information from a DataFrame: `del <DataFrame>[<Column>]`

  * In order to figure out if any rows are missing data, simply run the `count()` method on the DataFrame and check that all columns contain equal values.

  * In order to drop rows with missing information from a DataFrame: `<DataFrame>.dropna(how="any")`

  ![Drop NaN](Images/14-CleaningData_DropNa.png)

  * Sometimes the rows containing "NaN" values should not be removed but should instead be filled with another value. In cases like these, simply using the `<DataFrame>.fillna(value=<Value>)` method and pass the value desired into the parentheses.

  * In order to find values that have similar/mispelled values, simply run the `value_counts()` method on the column in question and look through the values that are returned.

  * To replace similar/mispelled values, simply run the `replace()` method on the column in question and pass a dictionary into it with the keys being those values to replace and the values being those to replace the originals with.

  ![Replace Values](Images/14-CleaningData_Replace.png)

### 24. Portland Crime (0:15)

* You will now take a crime dataset from Portland and do your best to clean it up so that the DataFrame is consistent and no rows with missing data are present.

![Portland Crime Output](Images/15-PortlandCrime_Output.png)

* **Files:**

  * [crime_incident_data2017.csv](Activities/15-Par_PortlandCrime/Resources/crime_incident_data2017.csv)

* **Instructions:**

  * Read in the CSV using Pandas and print out the DataFrame that is returned

  * Get a count of rows within the DataFrame in order to determine if there are any null values

  * Drop the rows which contain null values

  * Search through the "Offense Type" column and replace any similar values with one consistent value

  * Create a couple DataFrames that look into one neighborhood only and print them to the screen
