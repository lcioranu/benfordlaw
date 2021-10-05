# Benford 's law

This is a repository containg an implementation for demonstrating  Benford's law on a given dataset

Benford's law, also called the Newcomb–Benford law, the law of anomalous numbers, or the first-digit law, is an observation about the frequency distribution of leading digits in many real-life sets of numerical data. The law states that in many naturally occurring collections of numbers, the leading digit is likely to be small.[1] In sets that obey the law, the number 1 appears as the leading significant digit about 30 % of the time, while 9 appears as the leading significant digit less than 5 % of the time. If the digits were distributed uniformly, they would each occur about 11.1 % of the time.[2] Benford's law also makes predictions about the distribution of second digits, third digits, digit combinations, and so on.

Source: [https://en.wikipedia.org/wiki/Benford%27s_law](Wikipedia)

**Features:**
  - autodetect delimiter in csv files
  - data preview
  - choose target column 
  - basic error handling
  - basic data parsing
  - basic UI design

There is nothing implemented related to security, perfomance, etc.

These service is implemented in Python using Flask, and the data is being read and process mostly using Pandas dataframes.The UI is using chartJS for rendering chart, jquery for js handling and bootstrap for css styling.

**To run the program:**
Python:

  From the root of the project run:

  `python .\service.py`

Docker:
Build docker image

` docker build . -f ./Dockerfile --tag benford-test:latest`

Run docker image

  `docker run --name benford-test --publish 8080:8080 benford-test:latest`
