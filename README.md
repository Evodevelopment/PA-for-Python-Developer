# PA-for-Python-Developer

Writing efficient code in Python #3(ideally in Python 3.8 or higher).

Database: any relational database(ideally PostgreSQL).
Some unit and integration tests are nice to have, but not required.• 
Database schemais not strictly defined, but there must be a separate table for storing IP addresses and anothertable for storing URLs.Let’s consider http://178.62.47.209/banks/ATB/last.htmlto be URLand not IP address.–One line in a given data source (for example one URL) must be storedas one row in a database table.
Consider a hypothetical use case, that each URL and IP addressmustbe unique and easily searchable. You cannotstore the whole input froma given data source into one database record.–There must be a table containing origin of a given data.For example, if URL http://domain.comwas extracted from Open-Phish, then this URL must be associated with OpenPhish somehow.• 
Data sources:–https://urlhaus.abuse.ch/downloads/csv_recent/–http://reputation.alienvault.com/reputation.data–https://openphish.com/feed.txt• Everything else depends on your imagination. Good luck, and most importantly, have fun!


Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.

Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).

Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications. - https://www.tiobe.com/tiobe-index/

These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.

Let’s have a close look at some of the Python features that make it such a versatile and widely-used programming language:

Readability. Python is known for its clear and readable syntax, which resembles English to a certain extent.
Easy to learn. Python’s readability makes it relatively easy for beginners to pick up the language and understand what the code is doing.

Versatility. Python is not limited to one type of task; you can use it in many fields. Whether you're interested in web development, automating tasks, or diving into data science, Python has the tools to help you get there.

Rich library support. It comes with a large standard library that includes pre-written code for various tasks, saving you time and effort. Additionally, Python's vibrant community has developed thousands of third-party packages, which extend Python's functionality even further.

Platform independence. One of the great things about the language is that you can write your code once and run it on any operating system. This feature makes Python a great choice if you're working on a team with different operating systems.
Interpreted language. Python is an interpreted language, which means the code is executed line by line. This can make debugging easier because you can test small pieces of code without having to compile the whole program.

Open source and free. It’s also an open-source language, which means its source code is freely available and can be distributed and modified. This has led to a large community of developers contributing to its development and creating a vast ecosystem of Python libraries.

Dynamically typed. Python is dynamically typed, meaning you don't have to declare the data type of a variable when you create it. The Python interpreter infers the type, which makes the code more flexible and easy to work with.

Besides its wide popularity, Python has applications in numerous industries, from tech to finance, healthcare, and beyond. Learning Python opens up many career opportunities and guarantees improved career outcomes. 
We’ve already mentioned the versatility of Python, but let’s look at a few specific examples of where you can use it:

Data science. Python is widely used in data analysis and visualization, with libraries like Pandas, NumPy, and Matplotlib being particularly useful.

Web development. Frameworks such as Django and Flask are used for backend web development.

Software development. You can use Python in software development for scripting, automation, and testing.

*Game development.* You can even use it for game development using libraries like PyGame and tkinter.

Machine learning & AI. Libraries like TensorFlow, PyTorch, and Scikit-learn make Python a popular choice in this field. Find out how to learn AI in a separate guide.

According to a 2022 report from GitHub https://octoverse.github.com/2022/top-programming-languages, Python usage increased 22.5% year on year, making it the third-most used language on the platform.

How Long Does it Take to Learn Python?
While Python is one of the easier programming languages to learn, it still requires dedication and practice. The time it takes to learn Python can vary greatly depending on your prior experience with programming, the complexity of the concepts you're trying to grasp, and the amount of time you can dedicate to learning.

However, with a structured learning plan and consistent effort, you can often grasp the basics in a few weeks and become somewhat proficient in a few months.

Online resources can give you a firm basis for your skills and can range in length. As an example, our Python Programming skill track, covering the skills needed to code proficiently, takes around 24 study hours to complete, while our Data Analyst with Python career track takes around 36 study hours. Of course, the journey to becoming a true Pythonista is a long-term process, and much of your efforts will need to be self-study alongside more structured methods.
https://app.datacamp.com/learn/skill-tracks/python-programming
https://app.datacamp.com/learn/career-tracks/data-analyst-with-python

As a comparison of how long it takes to learn Python vs other languages:

Language

Time to Learn

Python

1-3 months for basics, 4-12 months for advanced topics

SQL

1 to 2 months for basics, 1-3 months for advanced topics

R

1-3 months for basics, 4-12 months for advanced topics

Julia

1-3 months for basics, 4-12 months for advanced topics

* The above comparisons are purely based on timelines needed to learn to become proficient with a programming language, not timelines needed to break into a career. Moreover, each person learns differently and goes at their own pace, we only aim to provide a framework with these timelines.

A comparison table of how long it would take to learn different programming languages
