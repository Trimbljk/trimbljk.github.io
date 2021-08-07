Title: Retrieving Data from Kaggle via the Kaggle API 
Date: 2021-08-05
Save_as: programming/retrieving-data-from-kaggle-via-api.html
Slug: retrieving-data-from-kaggle-via-api
Url: programming/retrieving-data-from-kaggle-via-api


A great website for finding datasets to help expand skills and expertise in data science is <a href="https://www.kaggle.com/" class="inlinelink">Kaggle</a>. In this short post, we'll discuss a quick set-up of Kaggle at the command line and then pull a dataset from the many available. It will be followed up with a post where we'll use the <a href="https://www.r-project.org/" class="inlinelink">R-programming</a> language to build a plot with <a href="https://ggplot2.tidyverse.org/" class="inlinelink">Ggplot2</a>. Before getting started, be sure to set up an account on Kaggle. You'll it to request an API key. After setting up an account, we'll  install the Kaggle package using your Python package manager, PIP. Run <b><code>pip install kaggle</code></b> to download the Kaggle package locally and create a hidden <em><b>.kaggle/</b></em> folder in your home directory.

Next, we'll navigate to our account settings. Select the <em>Create New API Token</em> button to download a <em>kaggle.json</em> file that you'll then need to store in the hidden <em>.kaggle/</em> folder discussed in the previous paragraph. This will allow us to access datasets programmatically.

<img class="articleimg" src=https://trimbljk.github.io/theme/images/kaggle-api.png>

Now we're ready to download some data. For visualizations in the next blog I'd like to use the dataset provided by <a href="https://www.kaggle.com/raghavramasamy/crop-statistics-fao-all-countries" class="inlinelink">raghavramasamy</a>. This person pulled information about world-wide crop statistics on many different crops from Food and Agricultural Organization (FAO). This is a nice dataset because it's already in <a href="https://vita.had.co.nz/papers/tidy-data.pdf" class="inlinelink">tidy</a> format. To download this dataset run: <b><code>kaggle download datasets -d raghavramasamy/crop-statistics-fao-all-countries</b></code>. It will download a file to your local directory. Once this is complete, we're ready to using the data.
