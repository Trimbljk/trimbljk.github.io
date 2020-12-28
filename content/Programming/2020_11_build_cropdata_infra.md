Title: Building Infrastructure to Support USDA NASS Data
Date: 2020-11-23
Save_as: programming/building-first-infrastructure.html
Slug: building-first-infrastructure
url: programming/building-first-infrastructure

Before we start gathering data we should build some infrastructure that can handle large amounts and doesn't require our own server. Fortunately, most major tech companies (Google, Amazon, Microsoft) have wonderful cloud-platforms that abstract the hardware allowing customers to build any type of infrastructure to support any application.

We're going to use Amazon Web Service (AWS) to build the infrasture we need to manage the data we collect. If you haven't created AWS credentials yet, go ahead and follow the intructions [here](https://portal.aws.amazon.com/billing/signup#/start). Once you're set up, navigate to the [AWS Homepage](https://aws.amazon.com) and hover over the ```Products``` tab, you'll see a variety of solutions from which to choose. For this project, we'll be using [AWS Simple Storage Service](https://aws.amazon.com/s3) or S3, [AWS Glue](https://aws.amazon.com/glue/?nc2=h_ql_prod_an_glu&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc), and [AWS Athena](https://aws.amazon.com/athena/?nc2=h_ql_prod_an_ath&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc). We'll be using S3 to store the files we request from the USDA NASS API. We'll use Glue to crawl our S3 bucket and then use Athena to query that information. To set it all up, we'll use [AWS Serverless Application Management (SAM)](https://docs.aws.amazon.com/serverless-application-model/?id=docs_gateway) and [AWS Cloudformation](https://aws.amazon.com/cloudformation/?nc2=h_ql_prod_mg_cfA). 

Let's get started.

To build our infrastructure, we'll be using a cloudformation template. This template can except JSON or YAML format. It's used to specify any infrastructure needs. We'll specify our format as a YAML (I find it easier to read). AWS requires two headers in our format:

INSERT FORMAT INFO HERE

Next, we'll specify some resources. We need an S3 bucket to which we upload our data, a crawler to pull information from the s3 bucket and a database to place the data once it's been crawled. Finally we're going to add another bucket for capturing queries from AWS Athena. This is require... (INSERT WHY HERE) Here is my template file from which I'll build the AWS infrastructure:

INSERT PICTURE OF TEMPLATE FILE HERE

Each resource has information describing various attributes. For example, we give the bucket a name and specify who has access to data in the bucket. Under the ```Crawler``` resource, we specify the bucket we want to crawl, shema change behaviors when adding or deleting information from the bucket. 

Once we have our template ready, we can use the AWS SAM CLI to deploy our infrastructure.

INSERT PICTURE OF THE SAM DEPLOY COMMANDS

You should receive a success notification at the CLI. If not you'll have to determine what the are was and fix it accordingly. Once our infrastructure is deployed, we can shift back to thinking about what data we want to collect from the USDA NASS website. 