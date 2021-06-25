Title: Fun with USDA NASS Data - Part 1: Setting Up API Access Credentials 
Date: 2021-01-07-
Save_as: programming/usda-nass.html
Slug: Apply for a USDA API Key
url: programming/usda-nass
Summary: This is the first post in a series of posts working with the USDA NASS data.

This is the first blog post in what will be a series of posts on retrieving, formatting, querying and visualizing data from the USDA National Agricultural Statistics Service (NASS). To understand what kinds of data we'll be working with, we can take a gander over to the NASS quickstats website at <a href="https://quickstats.nass.usda.gov/" class="inlinelink">https://quickstats.nass.usda.gov/</a>. The homepage brings up a rather innocuous design:

<img class="articleimg" src=https://trimbljk.github.io/theme/images/usda_ws_screenshot.png>

You can pick from a variety of options that generates a dataset for perusing. It will be displayed after selecting the _Get Data_ button at the bottom left corner of your browser window. Once you've created some data, you can download a CSV file with all the selected values by clicking _spreadsheet_ in the top right corner of your window. Unfortunately, we're only able to work with datasets that contain a maximum of 50,000 records at a time. 

I don't know about you, but any CSV/Excel file over 500 rows is virtually impossible for me to handle in a coherent manner. It's not a fun way to operate and it doesn't scale if you want to look at the millions of records contained in the NASS database. Instead, we're going to use the NASS API to request our desired data and combine it programmatically. The API gives us the ability to build a much larger dataset. It's also our first step in the process of building a dataset to analyze.

Let's jump start this journey by first navigating to the _Developers_ tab located in the top right corner. After that, select _Request API Key_ on the left. Once all the steps are followed, we'll receive a key, via email, that must be provided to each HTTP Request in order to retrieve the data we desire. It's good practice to set keys as variables in your terminal's shell. As an example, I'll set this key to the variable name: ```USDAKEY```. Setting values like this to the shell environment allows quick retrieval and exporting to common applications, like Jupyter, when programming. More importantly, it prevents the hard coding of sensitive credentials. In the next post, we're going to build some infrastructure using Amazon Web Services to handle the data we retrieve from the NASS datbase.

