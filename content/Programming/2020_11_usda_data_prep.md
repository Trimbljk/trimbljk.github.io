Title: Parsing the USDA's National Agriculture Statistics Service Data
Date: 2020-11-23
Save_as: programming/usda-nass.html
Slug: Apply for a USDA API Key
url: programming/usda-nass
Summary: This is the first post in a series of posts working with the USDA NASS data.

This is the first blog post in what will be a series of posts on retrieving, formatting, querying and visualizing data from the USDA National Agricultural Statistics Service (NASS). To understand what kinds of data we'll be working with, we can take a gander over to the NASS quickstats website at <a href="https://quickstats.nass.usda.gov/" class="inlinelink">https://quickstats.nass.usda.gov/</a>. The homepage brings up a rather innocuous design:

<img class="articleimg" src=https://trimbljk.github.io/theme/images/usda_ws_screenshot.png>

You can pick from a variety of options that generates a dataset for perusing. It will be displayed after selecting the _Get Data_ button at the bottom left corner of your browser window. You can even download a csv with all the selected values by clicking _spreadsheet_ in the top right corner of your window. Unfortunately, we're only able to work with datasets that contain a max of 50,000 records at a time. 

I don't know about you, but any csv/excel file over a 500 rows is virtually impossible for me to handle in a coherent manner. It's not a fun way to operate and it doesn't scale if you want to look at the millions of records the NASS database contains. Instead, we're going to use the NASS API to request our desired data and combine it, programmatically, with other data. This gives us the ability to build a much larger dataset. It's also our first step in the process of building a dataset to analyze.

Let's jump start this journey by first navigating to the _Developers_ tab located in the top right corner next to the _Help_ tab. Select _Request API Key_ on the left. Once all the steps are followed, we'll receive a key, via email, that must be provided to each HTTP Request in order to receive the data we desire. It's good practice to set keys as variables in your terminal's shell. As an example, I'll set this key to the variable name: ```USDAKEY```. Setting values like this to the shell environment allows quick retrieval and exporting to common applications, like Jupyter, when programming. More importantly, it hides sensitive credentials from being hard coded. In the next post, We'll discuss the kind of data to be collected.  



