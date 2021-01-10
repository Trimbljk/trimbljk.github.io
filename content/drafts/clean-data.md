Title: Clean Data: Art or Science? 
Date: 2020-07-17
slug: clean-data 
url: data-science/clean-data
Save_as: data-science/clean-data.html
Template: article
Summary: Clean data is important for all downstream applications. However, having a laid out plan before starting can help mitigate the issues of *dirty* data.

## Good Data: Art or Science? 
Have you ever started working with data you didn't collect, thinking you could quickly prepare an analysis, only to spend the majority of your time attempting to understand what was captured, and, ultimately, fixing what's available? I'm sure every data scientist has experienced this. My experience pertains to biological sample collection and microbial metadata. Recently, I have been correcting some rather untidy data at my employer; the work has inspired me to write this blog post.

Well planned steps for data capture and record keeping are crucially important for any downstream application; especially if there is data analysis involved. Proper data types and formatting can prevent interpretation issues during an alysis. Good data practices are a form of art that requires much thought and necessitates acceptance that the data will never be perfect. As I've heard from time to time, an analysis is only as good as the underlying data. In this post, I'll supply an example of bad data I recently encountered and demonstrate how I fixed it.

#### Bad Data

Let's get started. Here is an example of some bad data:

| Collaborator | Organism | 
| :---         | :---     |
| NCSU         | Corn     |
| Louisiana State University | Lepidopteran | 
| John Doe | Cotton Ball |

Let's list some issues with the table above:
1. Right of the bat we can see the headers are capitalized, 
2. It appears there are two universities or institutions where one is abbreviated and the other is not
3. Under organism, **Cotton Ball** is a pretty granular description of the sample where **Corn** and **Lepidopteran** are not. 

#### Let's Clean It Up
Before addressing the issues, I'll preface with, originally, there were no conventions laying out what each column header meant. Data convention documentation is crucially important, as it communicates what is being displayed and hints at the data types and content that comprise the rows that follow. First, the headers are capitalized and some instances have white space. These features can cause issues when attempting to parse columns. In my opinion, headers should always be set in lowercase and whitespace replaced with underscores. 

Next, Let's take a look at the first column, **Collaborator**. We have two universities, `NCSU` and `Louisiana State University`, and a person. If you didn't live in North Carolina, you probably wouldn't associate `NCSU` with North Carolina State University right off the bat. There are also two different kinds of data here, a person, `John Doe` and a kind of institution. We can differentiate these two by adding separate columns **collector\_type**, **collector\_institute** and **collector\_name**. This allows us to introduce the underscore. 

Lastly, let's tackle **Organism**. It's a little more tricky. What passes for an organism? Would a piece of said "organism", like a leg or wing"suffice? How about the whole thing? There are also different `kinds` of data in this column. `Corn` and `Cotton ball` are a both plants but `Lepidopteran` is a taxonomic nomenclature for a particular group of insects. Fortunately, there are particular naming conventions or ontologies that are readily accessible for us to use. I'm going to pull a few of those conventions for our **Organism** header. We can use the [Earth Microbiome Project Ontology](https://earthmicrobiome.org/protocols-and-standards/empo/) to help us with convention setting. The EMPO has built a nice standardized convention for peices of data. After applying their convention format and adding a little custom touch to the headers we generate our new table:  

| collaborator\_type | collector\_institute | collector\_name | env\_description\_level\_1 | env\_description\_level\_2 |
| :--- | :--- |:--- |:--- |:--- |
| institute | north\_carolina\_state\_university | | host\_associated | plant |
| institute | louisiana\_state\_university | | host\_associated | animal |
| individual |  | john\_doe | host\_associated | plant |

Obviously we need descriptions for each column header describing the data held within, but the table already looks better. With data formatted the same throughout, it will be much easier to parse. We did introduce some `None` types in two columns, but that's the nature of data never being perfect. I encourage you to read [*Tidy Data*](https://vita.had.co.nz/papers/tidy-data.pdf) by Hadley Wickham, the Chief Science Officer for [RStudio](https://rstudio.com/). He discusses how to make data easier and faster to clean. Remember, the information that can be gleaned from data is only as informational as your data conventions are standardized. 





