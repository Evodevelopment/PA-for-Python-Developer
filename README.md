# PA-for-Python-Developer

Assignment SpecificationYour task is to implement a command line application that will process and storemalicious IOCs1from all specified data sources on the Internet into a database.• Technical requirements(bold text) and recommendations:–Programming language: Python 3(ideally in Python 3.8 or higher).–Database: any relational database(ideally PostgreSQL).–Some unit and integration tests are nice to have, but not required.• Database schemais not strictly defined, but:–There must be a separate table for storing IP addresses and anothertable for storing URLs.Let’s consider http://178.62.47.209/banks/ATB/last.htmlto be URLand not IP address.–One line in a given data source (for example one URL) must be storedas one row in a database table.Consider a hypothetical use case, that each URL and IP addressmustbe unique and easily searchable. You cannotstore the whole input froma given data source into one database record.–There must be a table containing origin of a given data.For example, if URL http://domain.comwas extracted from Open-Phish, then this URL must be associated with OpenPhish somehow.• Data sources:–https://urlhaus.abuse.ch/downloads/csv_recent/–http://reputation.alienvault.com/reputation.data–https://openphish.com/feed.txt• Everything else depends on your imagination. Good luck, and most importantly, have fun!


Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. It is designed with an emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.

Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In simpler terms, this means it’s flexible and allows you to write code in different ways, whether that's like giving the computer a to-do list (procedural), creating digital models of things or concepts (object-oriented), or treating your code like a math problem (functional).

Over the years, Python has become one of the most popular programming languages due to its simplicity, versatility, and wide range of applications. - https://www.tiobe.com/tiobe-index/

These reasons also mean it is a highly favored language for data science as it allows data scientists to focus more on data interpretation rather than language complexities.

