# Quotes API Assignment


## Introduction:

Sproutt Insurance offers life insurance policies to customers.

Our goal is to offer a customer the best policy he is eligable to by utlizing analytics, smart routing, data feedback loops, etc.

As of today, Sproutt sells policies through two main channels: Agents Portal (via agents) and D2C (Direct To Consumer) - both online, quick, and effortless.

Now and then Sproutt introduces a new product and offers it to customers.


**Please read the full description before coming up with a solution.**

## Description:

This story will focus on the Quoting step which is one part of supporting the product in our application process.

Attached to this story is an excel spreadsheet with rates according to parameters.

The goal is to develop a server that can fetch the right quote.

The API should calculate the price according to this formula:
  - price = coverage/1000 * factor

#### Input: 

  1. term - The policy duration.
  2. coverage - The policy death benefit.
  3. age - customer age.
  4. height - customer height.
  5. weight - customer weight.

#### Output: 
  1. price
  2. health-class
  3. term
  4. coverage

### Example: 

- Input:
```
{
  “term”: 10,
  “coverage”: 250000,
  “age”: 25,
  “height: “5 ft 1”,
  “weight”: 160
}
```

- price = 250000/1000 * 0.4291 = 107.275
  
- Output:
```
{
  “price”: 107.275,
  “health-class”: “Preferred”,
  “term”: 10,
  “coverage”: 250000
}
```

## Requirements: 
1. A running server.
2. A Working API.
3. Describe/draw a basic HLD for the application.
4. Be able to test and demonstrate.
5. Push it to Github - send us a link with your solution.

## Notes:
1. You can implement it in any language you desire.
2. You can assume the input is valid.
3. Don't hesitate to reach out with ANY questions you might have - our goal is to make sure you don't get unnecessarily stuck while working on the assignment.
4. We're trying to get a good grasp of how you code and think, while not taking up too much of your time.
5. To be clear, we just need a working code that can be run locally on an IDE (no need to deploy anything). 

