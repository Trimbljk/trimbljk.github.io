Title: Fun with UDSA NASS Data - Part 2: Building Cloud Infrastructure
Date: 2020-11-23
Save_as: programming/Fun-with-USDA-Data-part2-infrastructure.html
Slug: Fun-with-USDA-Data-part2-infrastructure
url: programming/Fun-with-USDA-Data-part2-infrastructure

Before we start gathering crop data to analyze, we should build some serverless infrastructure that can handle large datasets. Fortunately, our favorite major tech companies (Google, Amazon, Microsoft) have wonderful cloud-platforms that allow customers to build any type of infrastructure to support many kinds of applications.

We're going to use Amazon Web Services (AWS) to build the infrasture we need to manage the data we collect. If you haven't created AWS credentials yet, go ahead and follow the intructions <a href="https://portal.aws.amazon.com/billing/signup#/start" class="inlinelink">here</a>. Once you're set up, navigate to the <a href="https://aws.amazon.com" class="inlinelink">AWS Homepage</a> and hover over the *Products* tab, you'll see a variety of solutions from which to choose. For this project, we'll be using <a href="https://aws.amazon.com/s3" class="inlinelink">AWS Simple Storage Service</a> or S3, <a href="https://aws.amazon.com/glue/?nc2=h_ql_prod_an_glu&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc" class="inlinelink">AWS Glue</a>, and <a href="https://aws.amazon.com/athena/?nc2=h_ql_prod_an_ath&whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc" class="inlinelink">AWS Athena</a>. We'll be using S3 to store the data we request from the USDA NASS API. We'll use Glue to crawl our S3 bucket and then use Athena to query that information and perform an analysis of some of the data. To set it all up, we'll use <a href="https://docs.aws.amazon.com/serverless-application-model/?id=docs_gateway" class="inlinelink">AWS Serverless Application Management (SAM)</a> and <a href="https://aws.amazon.com/cloudformation/?nc2=h_ql_prod_mg_cfA" class="inlinelink">AWS Cloudformation</a>.

Let's get started.

To build our infrastructure, we'll be using a Cloudformation template. Each template is a set of directions AWS uses to contruct a "stack" of resources. Each stack is passed a name, given by us, at build time and can be viewed in your account on AWS. A template can be constructed using either JSON or YAML formats. The template specifies infrastructure needs using code allowing portability. We'll specify our format in YAML (I find it easier to read). Because we're using AWS Serverless Application Management (SAM), instead of just cloudformation, our template requires that the following two headers be placed on the top two lines of the file:
<pre class="setpre">
<code class="aws-infrastructure-code"><span class="infra-variable">AWSTemplateFormatVersion</span><span class="colon">:</span><span class="infra-string-value"> '2010-09-09'</span>
<span class="infra-variable">Transform</span><span class="colon">:</span><span class="infra-noq-string-value"> AWS::Serverless-2016-10-31</span></code>
</pre>
Next, we'll specify some resources. We need an S3 bucket to which we'll eventually upload our raw data, a crawler to pull information from that S3 bucket and create a proper schema, and a database to write the new schematic output. All resources are grouped under the **Resources** header. First we'll draft our bucket:
<pre class="setpre">
<code class="aws-infrastructure-code"><span class="infra-variable">Resources</span><span class="colon">:</span>
  <span class="infra-variable">OutputBucket</span><span class="colon">:</span>
    <span class="infra-variable">Type</span><span class="colon">:</span><span class="infra-noq-string-value"> AWS::S3::Bucket</span>
    <span class="infra-variable">Properties</span><span class="colon">:</span>
      <span class="infra-variable">BucketName</span><span class="colon">:</span><span class="infra-string-value"> 'jkt-usda-api-crop-data'</span>
      <span class="infra-variable">PublicAccessBlockConfiguration</span><span class="colon">:</span>
        <span class="infra-variable">BlockPublicAcls</span><span class="colon">:</span><span class="infra-noq-string-value"> True</span>
        <span class="infra-variable">BlockPublicPolicy</span><span class="colon">:</span><span class="infra-noq-string-value"> True</span>
        <span class="infra-variable">IgnorePublicAcls</span><span class="colon">:</span><span class="infra-noq-string-value"> True</span>
        <span class="infra-variable">RestrictPublicBuckets</span><span class="colon">:</span><span class="infra-noq-string-value"> True</span></code></pre>
We first assign a template name to the bucket resource with **OutputBucket**. This designation is called a logical ID. Every resource specified in a Cloudformation template has to have a logical ID. Other resources can even refer to the ID in the template. Next, we tell AWS what kind of resource it is using the **Type** variable and one of AWS's custom resource values: **AWS::S3::Bucket**. We then describe what features the bucket maintains under the **Properties** variable. The bucket name must be unique in the S3 global namespace. For my bucket, I have also set all access restrictions to **True** because I want my bucket to be private. Even though private is the default setting on S3, it's good practice to specify it explictly by blocking any public access.

Next, we'll specify our database resource. When the data in our bucket is crawled via AWS Glue, the information will be nicely formatted in the database setforth here. 
<pre class="setpre">
<code class="aws-infrastructure-code">  <span class="infra-variable">Cropdatabase</span><span class="colon">:</span>
    <span class="infra-variable">Type</span><span class="colon">:</span><span class="infra-noq-string-value"> AWS::Glue::Database</span>
    <span class="infra-variable">Properties</span><span class="colon">:</span>
      <span class="infra-variable">CatalogId</span><span class="colon">:</span><span class="aws-intrinsic-func"> !Ref</span><span class="infra-noq-string-value"> AWS::AccountId </span>
      <span class="infra-variable">DatabaseInput</span><span class="colon">:</span>
        <span class="infra-variable">Name</span><span class="colon">:</span><span class="infra-string-value"> "crop_data"</span></code></pre>
After we designate a logical ID, the database resource is specified by the AWS value: **AWS::Glue::Database**. It's properties are simple. We give it a name and assign our AWS account ID, using an <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html" class="inlinelink">instrinsic fuction</a> to the CatalogId object. Each AWS account receives a catalog to which all data can be written and viewed. Think table of contents for all your data.

The last resource that needs to be constructed is the crawler. The crawler will read all the files in a specific path in a bucket and construct, or write, the information contained therein to tables that will appear in our database above.
<pre class="setpre">
<code class="aws-infrastructure-code">  <span class="infra-variable">Crawler</span><span class="colon">:</span>
    <span class="infra-variable">Type</span><span class="colon">:</span><span class="infra-noq-string-value"> AWS::Glue::Crawler</span>
    <span class="infra-variable">Properties</span><span class="colon">:</span>
      <span class="infra-variable">Name</span><span class="colon">:</span><span class="infra-string-value"> 'crop-data-crawler' </span>
      <span class="infra-variable">SchemaChangePolicy</span><span class="colon">:</span>
        <span class="infra-variable">UpdateBehavior</span><span class="colon">:</span><span class="infra-noq-string-value"> UPDATE_IN_DATABASE</span>
        <span class="infra-variable">DeleteBehavior</span><span class="colon">:</span><span class="infra-noq-string-value"> DELETE_FROM_DATABASE</span>
      <span class="infra-variable">TablePrefix</span><span class="colon">:</span><span class="infra-noq-string-value"> usda_</span>
      <span class="infra-variable">DatabaseName</span><span class="colon">:</span><span class="aws-intrinsic-func"> !Ref</span><span class="infra-noq-string-value"> Cropdatabase</span>
      <span class="infra-variable">Targets</span><span class="colon">:</span>
        <span class="infra-variable">S3Targets</span><span class="colon">:</span>
          <span class="infra-list-dash">-</span><span class="infra-variable"> Path</span><span class="colon">:</span><span class="aws-intrinsic-func"> !Sub</span>
            <span class="infra-list-dash">-</span><span class="infra-string-value"> 's3://${Bucket}/crop-data'</span>
            <span class="infra-list-dash">-</span><span class="colon"> { </span><span class="infra-variable">Bucket</span><span class="colon">:</span><span class="infra-noq-string-value"> !Ref OutputBucket</span><span class="colon"> }</span>
      <span class="infra-variable">Schedule</span><span class="colon">:</span>
        <span class="infra-variable">ScheduleExpression</span><span class="colon">:</span><span class="infra-string-value"> 'cron(0 0 ? \* MON \*)'</span>
      <span class="infra-variable">Role</span><span class="colon">:</span><span class="infra-noq-string-value"> AWSglueServiceRole</span></code></pre>
So, there's a lot going on in this code. Again, we give the resource a logical ID for the template, **Crawler** and assign it it's AWS resource type with: **AWS::Glue::Crawler**. We then provide its name as will appear on AWS, as **crop-data-crawler**. The **SchemaChangePolicy** property is dictating the proper operations the crawler will conduct when data is deleted or added to its target path. For example, if you originally had 5 columns located at your target path and updated or deleted a column where the path now contained 6 or 4 respectively, the crawler knows to add in the new column or delete the old column from the data catalog. The **TablePrefix** is what's assigned to the data catalog, after crawling, and appears when using AWS Athena. The database to which we want to write output can be referenced using the intrinsic function, **\! Ref** if the resource is built in the template. Next, the targets where the crawler will search for data are specified. A path is declared inside the bucket, and since we want to reference our bucket we built earlier, we can, again, use an intrinsic function **\! Ref**. We can set our crawler to run each week and look for schema changes, though it's not necessary if you're not constantly updating your schema. Finally, we specify a Role. This is very important. Without a Role, the crawler will not have the security credentials it needs to access the data in the bucket, or any other resrouce for that matter. All AWS resources require a role in order to interact with other services. If you want more detail, go to<a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html" class="inlinelink">the Identity and Access Management guide.</a>.

Once we have our template prepared, we can use the AWS SAM CLI to deploy our infrastructure. AWS SAM is built on top of Cloudformation and much could be written about both. If you want extensive detail, please refer to the links in the second paragraph. In an effort to keep this section brief, essentialy we have to *build a package* and then *deploy* it. Here is where we finally name our stack. An example of the first command is provided in the next code snippet.
<pre class="setpre">
<code class="aws-infrastructure-code"><span class="commandline-code">sam build --skip-pull-image --use-container  \\</span>
		<span class="commandline-code">--region "us-east-1" --profile lopcer</span></code></pre>
This first command builds our package in a local build folder. This folder is used to deploy the package in the next command. We specify the region we want the infrastructure deployed and use a container to build it. Finally, since I have multiple accounts, I designate which account I want it to build in. The next code snippet is what we'll use to deploy our stack.
<pre class="setpre">
<code class="aws-infrastructure-code"><span class="commandline-code">sam deploy --template-file package.yml \\</span>
	<span class="commandline-code">--stack-name "jkt-crop-data-usda" \\</span>
	<span class="commandline-code">--capabilities CAPABILITY_IAM \\</span>
	<span class="commandline-code">--no-fail-on-empty-changeset \\</span> 
	<span class="commandline-code">--region "us-east-1" --profile locper</span></code></pre>
In our deploy command, we specify our template file where we assigned resources, the package.yaml file that was built from the sam deploy command and the name of our "stack". Next we pass a security permission parameter --capabilities CAPABILITY_IAM and an option to not throw an error if we deploy again but don't make any changes. If you want to learn about each of these, please refer to the information in the second paragraph about AWS SAM. You should receive a success notification at the CLI. If not you'll have to determine what the error was and fix it accordingly. Once our infrastructure is deployed, we can shift back to thinking about what data we want to collect from the USDA NASS website. In the next post, I'll be using Jupyter to request data from NASS, format the info into files, and upload them to the bucket we built in this post. 




