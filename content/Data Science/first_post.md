Title: Clean Data: Art or Science? 
Date: 2020-07-17
slug: clean-data 
url: data-science/clean-data
Save_as: data-science/clean-data.html
Template: article
Summary: Clean data is important for all downstream applications. However, having a laid out plan before starting can help mitigate the issues of *dirty* data.

## Clean data: Art or Science? 
Having well planned steps for capturing data in the cleanest possible way, by that I mean, the steps to capture and record specific types of data are documented, standardized and well understood, are crucially important for any downstream application. It's an art that requires much thought and necessitates acceptance that the data will never be perfect. In this post, I'll give an example of bad data and offer some tips on how to clean it up.  

The data-science team for which I am a part, has been cleaning up dirty data at my company; all the work has inspired me to write this blog post. Have you ever started working with data you didn't collect, thinking you could quickly prepare an analysis, only to spend the majority of your time attempting to understand what was captured, and, ultimately, cleaning what's available? I'm sure every data scientist has experienced this. My experience pertains to biological sample collection and microbial metadata.

#### Bad Data

**Disclaimer** 
Before I break down the following table, I must confess, some of this was my own doing. However, when the dataset increases beyond 100 rows of data, into the thousands, on top of *no* standardized data collection conventions, this will happen to anyone. Sadly, I am not a computer because my brain does not have a nice CPU to help me out. 

Let's get started. Here is an example of some bad data:

| Collaborator | Organism | 
| :---         | :---     |
| NCSU         | Corn     |
| Louisiana State University | Lepidopteran | 
| John Doe | Cotton Ball |

What's wrong with the table above?
1. There are no documented data conventions explaining the data shown. (*In order to keep this blog post managable, understand that there should always be documentation about the data you are using.*)
2.  

#### Let's Clean It Up
First, there are no conventions laying out what each of these column headers mean. This is crucially important as it communicates what is being display and hints at the data types and content that comprises the rows that follow. The headers and data are capitalized and some instances have white space. These features can cause issues when attempting to parse data and columns and datashould be lowercase and whitespace replaced with underscores. Let's take a look at the first column, **Collaborator**. We have two universities, `NCSU` and `Louisiana State University`, and a person. If you didn't live in North Carolina, you probably wouldn't associate `NCSU` with North Carolina State University right off the bat. There are also two different kinds of data here, a person, `John Doe` and a kind of institution. We can differentiate these two by adding separate columns **collector\_type**, **collector\_institute** and **collector\_name**. We have also introduced the underscore. **Organism** is a little more tricky. What passes for an organism? Would a piece suffice? How about the whole thing? There are also different `kinds` of data in this column. `Corn` and `Cotton ball` are a both plants but `Lepidopteran` is a taxonomic nomenclature for a particular group of insects. In science, there are particular name conventions or ontologies that are readily accessible for us to use. I'm going to pull a few of those conventions for our **Organism** header. We can use the [Earth Microbiome Project Ontology](https://earthmicrobiome.org/protocols-and-standards/empo/) to help us with convention setting. The EMPO has built a nice standardized convention for peices of data. After applying their convention format and adding a little custom touch to the headers we get our new table:  

| collaborator\_type | collector\_institute | collector\_name | env\_description\_level\_1 | env\_description\_level\_2 |
| :--- | :--- |:--- |:--- |:--- |
| institute | north\_carolina\_state\_university | | host\_associated | plant |
| institute | louisiana\_state\_university | | host\_associated | animal |
| individual |  | john\_doe | host\_associated | plant |

Obviously we need descriptions for each column header describing the data held within, but the table already looks better. With data formatted the same throughout, it will be much easier to parse. We did introduce some `None` types in a two columns, but that's the nature of data never being perfect. I encourage you to read [*Tidy Data*](https://vita.had.co.nz/papers/tidy-data.pdf) by Hadley Wickham, the Cheif Science Officer for [RStudio](https://rstudio.com/). He discusses how to make data easier and faster to clean. 





