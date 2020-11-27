Title: Parsing the USDA's National Agriculture Statistics Service Data
Date: 2020-11-23
Save_as: programming/usda-nass.html
Slug: parsing-nsaa-data
url: programming/parsing-nsaa-data
Summary: This is the first post in a series of posts working with the USDA NASS data.

This is the first blog post in what will be a series of posts on retrieving, formatting, querying and visualizing data from the USDA National Agricultural Statistics Service (NSAA). To understand what kinds of data we'll be working with, we can first take a gander over to the NASS quickstats website at [https://quickstats.nass.usda.gov/](https://quickstats.nass.usda.gov/). The homepage brings up a rather innocuous design:

![usda homepage](https://trimbljk.github.io/theme/images/usda_ws_screenshot.png)

You can pick from a variety of options that generates a dataset for perusing. It will be displayed after selecting the _Get Data_ button at the bottom left corner of browser window. You can even download a csv with all the selected values by selecting _spreadsheet_ in the top right corner of your window. Unfortunately, we're only able to work with datasets that contain a max of 50,000 records at a time. 

I don't know about you, but any csv or excel file over a 1000 rows is virtually impossible to work with. This isn't a fun way to operate and it doesn't scale if you want to look at the millions of records the NASS database contains. Instead, we're going to use the NASS API to request our desired data and combine it, programmatically, with other data. This gives us the ability to build a much larger dataset. This is the first step in the process of building a dataset to analyze.

Let's jump start this journey by first navigating to the _Developers_ tab located in the top right corner next to the _Help_ tab. Select _Request API Key_ on the left. Once all the steps are followed, we'll receive a key, via email, that must be provided to each HTTP Request in order to receive the data we desire. I like to set keys to variables in my shell. As an example, I'll set this key to the variable name:```USDAKEY```. Setting values like this to the shell environment allows quick retrieval and exporting to common applications, like Jupyter, when programming. More importantly, it hides sensitive credentials from being hard coded. The next step in this process is to retrieve our desired data, format it, and push it to AWS S3. We'll do that in the next post. Until then, I'd get familiar with the available data at NASS.

Related posts include:
- xxxx
- xxxx
- xxxx







