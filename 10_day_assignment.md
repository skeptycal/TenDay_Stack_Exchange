
Response from 
# **Roman Trusov**

## I teach machines

*Artificial Intelligence, Machine Learning, Computer Programming and occasional ramblings about human behavior.*

---

>Man, I envy you. What an opportunity you have ahead.

>If you have 100 hours spread over 10 days, you want this experience to be as diverse as possible. And it's a huge investment, so you might as well get pretty serious about it and aim at the results like an internship depending on the outcome.

>Honestly, I don't see the point of MOOCs for this, even though they give you sense of accomplishment. If you have decent knowledge of basic math and programming, it will be much more fun diving into the code and aiming at getting real results. And 100 hours, damn, if you honestly, dutifully put in 100 hours in the next 10 days, that will cover 1% of becoming a world expert in the field. That's a lot in a very short time. Get ready.

>There will be plenty of time to learn all the internals of your libraries and algorithms, but you don't need them right now. I am going to give you an enormous task that will require all your focus and ideally you will get a very broad exposure to the main tools.```

# Days One and Two

[Download StackExchange data: Stack Exchange Data Dump : Stack Exchange, Inc. : Free Download & Streaming : Internet Archive](https://archive.org/details/stackexchange)

- You will need an RDBMS to handle the data, so the first day would look like this:

Install and configure [MySQL](https://www.mysql.com/). Import the dump into the database
Read SQL basics. Spend some time doing simple exercises to get the hang of manipulating the data. Write a script that pulls, for example, set of questions about Python and SQL that have >3 answers and the best answer is written by someone who has >= 10 chose answers in either of those two topics. Observe performance issues.
Read about indexes in SQL. Hashing, sorting etc. Speed up the query from the bullet 2 so that it run instantaneously.
Write a class in Python that handles the queries for you. This will require you to learn about Python MySQL driver. As a result you need a tool that pulls required data from your database and presents it in a convenient format.
I don't know about your background, but I think it's totally doable even for a beginner, all you need is some general experience with Python.

- For the second day, you will need to get familiar with reading data using pandas and manipulating numerical data with numpy. The documentation is quite voluminous, you don't need to read all of it, just be comfortable with importing CSV files, extracting and adding columns, merging two datasets and that's it.

- Day Three

While on the actual job you will often run queries on the whole database, it's important to get the gist of how to work with small data and still get meaningful results. Play aroung with pulling random subsamples and compare the distributions of, say, scores, with the ground truth - the distribution of all scores.

Let's move further. You have a whole SE database in front of you, but I'll stick to StackOverflow since it contains a lot of data I'm familiar with. One exercise off the top of my head - build a timeline of languages' popularity.

Why is it so cool?

How do you extract the questions about the languages and omit the ones related only to technology? (e. g. asking about Python syntax and not about how to mate Django with MongoDB)
Lots of tags there, you need to visualize the results, so filter your sources wisely
You get to learn at least one visualization framework
Lots of cool pics
Of course, once you did that example, there are many more interesting properties of your data that you should explore. Asking the right questions is a key ability.

- Days Four and Five

Data Scientist was named "The sexiest job of 21st century". You know what else is sexy? Graph theory.

How are the tags connected? Is it possible to build a technology map using just SO answers? What metrics would you choose to calculate the proximity of two tags? How would you visualize the graph? Have you tried Gephi?

Once you are done, the graph needs to be described. Thing is, the picture of a graph has poor value in terms of comprehensibility - you need to stare and stare at it before you know for sure what's going on.

So, you will need to learn about clustering algorithms (at least k-means and DBSCAN), K nearest neighbors. If you go full von Neumann on this task, some graph metrics and algorithms won't hurt. I suggest you try networkx and some parts of scikit-learn for this, they make everything much easier.

Why is it so cool?

You learn about different formats of data. CSV, Gephi, list of edges, ets.
K-means is very useful algorithm that will serve you well in the future
Discovering the meaningful groups is one of the most important tasks when you explore the data
Distribute the workload as you prefer, I'd spend the first day tinkering with networkx and Gephi just because graphs, you know. The second day I'd give to clustering, because there are going to be some non-trivial things like "how the hell do I get vector representations for each tag that would preserve the distances between them?!"

Day Six

OK, now you have general understanding of what's going on in your database. But you haven't touched the texts yet - word counts don't count (terrible pun unintended).

So, today you need to read briefly about text analysis. For this step good ol' Latent Semantic Indexing would be enough, everything you need you will find in scikit-learn, also you will need to work with SQL. General pipeline you want to see:

Select the data you will work with
Build text features with special extractors in scikit (TF-IDF Vectorizer is the best)
Assign the labels for the text. Let's say for example that you want to predict how many point will the answer get based only on the text. So, you take a score as a label and the feature vector is TF-IDF
It would be better to prepare several datasets in the numpy format, one for every hypothesis. I will give you a couple just to get you started:

Predict the score of the answer.
Classify the main topic of the answer (choose, say, 20 languages and sample answers about them).
Be sure that your datasets are clean and you know what's inside. This description might seem easy, it's not.

Day Seven, Eight, Nine

Okay, so you have clean datasets from the previous day. I will assume that you have one dataset for classification and one for prediction (you should know the difference by the fifth day). On the fifth day you need to focus on regression models. Granted, scikit gives you a wide range of tools. You definitely want to try at least there methods:

Linear model. There are tons of them, first compare how they perform, then read a bit about the best ones to know the difference better. Hint: take a good look at ElasticNet regression. If you are mathematically savvy, read a couple of chapters from Bishop's "Pattern Recognition and Machine Learning", he gives a good explanation why it works. Skip this if you don't have enough time
Regression trees
KNN regression. They usually perform quite well, never underestimate these methods.
Ensemble models. Random Forests and AdaBoost.
The whole idea is not to become an algorithm expert instantly, but to get it to work first, ask questions later.

The same stands for classification task. Take your time to read and think about metrics of quality. Imagine that you are building a smart content platform that sorts the news - how would you evaluate the performance in that case?

It's absolutely necessary to perform cross-validations for all of your models. Read about k-fold CV, find out how to do it with scikit and cross-validate the hell out of your models.

Day Ten

Since you are on your way to become a data scientist, this adventure wouldn't be complete without the most interesting part of your work. You will need to present it.

The format is only your choice (you will rarely have this luxury again in the future). A semi-academic paper, presentation, blog post, app - whatever you like. Tell your story. Describe your findings in the dataset, tell about your hypotheses, give a couple of suggestions why they may be true of false, describe the algorithms, present the results of cross-validations in a clear format and, in the name of Sir Ronald Fisher, show more pics.

As for this part, there's no way to overdo it. And I guarantee you, if you do make great presentation and show it to the right people, your entry-level offer will follow very soon.