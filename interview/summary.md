#### AARRR
acquisition --> activation --> retention --> referel --> revenue


#### Anomaly detection
isolation forest

#### power law 2/8

#### false discovery rate (more lenient); family wise error rate (bonferroni, Sidak) (more conservative)

#### unit of diversion  >  unit of analysis 

#### diagnose problem
1. clarify the scenario and metric
  - how to aggregate by day or hour 
  - outlier: extreme value
    - compare the distribution of the variable
    - compare percentiles
    - extreme values due to technical issues

2. analyze the temporal factor
  - sudden change vs. progressive change
  
  sudden change
  - algorithm change, data collection process 

  progressive change
  - historical trendl weekly pattern, etc.
  - is there ground truth to compare

  internal - data source, data collection, bug
  external - seasonality, industry trend, competitors, special event, natural disaster

3. Check other products by the same company
  - if they experience the same change
  - it may lead to a bigger problem

4. segment users by dimensions by demographic and behavior features
  - region, platform (ios, android or web): release or feature launch

5. decompose the metric 
  e.g. day = existing users + new users + resurrected users - churned users

6. summarize the overall approach: we have a systematic solution


#### improve a product

- Clarifying the question
 - what is the goal of the improvement: engagement, retention or revenue
 - what feature / product should we focus on 
 - for improvement of a specific feature: how the feature works?
  - how to increase the awareness of the product (larger icon / button, notification / email, popup window)

- Identify product improvement opportunities
  - Product improvement ideas - User journey map
    - reduce friction in current user experience
    - identify different scenarios of users 
  - Product improvement ideas - User segmentation
    - reason to be that segment and what we can do for the segment
    - difference btw active / inactive users
      -- ML model
    
- Prioritize ideas
  - proportion of users impacted by each idea(frequency of each user segmentation)
  - cost effective

- Measure success
  - define 1 ~ 2 success metrics
  - network networks / two sidered market
  - how to design the experiment

- Summary


#### measure success
1. clarify function and goal of the product / feature
  - what it does? how is it used? who is it for?

2. define metrics
  2 success metrics + 1 guardrail metric

#### launch or not
1. clarify goal and define metrics (similar to measure success)
2. experimentation
  - how to design it
  - how to split users
  - how long to run it
3. recommendation based on experiment results
- link results to goals and business impact
- conflicting results
- short-term vs. long term


#### learning effect, user retention
cohort

How to reduce the size of an experiment to get it done faster? You can increase the practical significance boundary, significance level alpha, or reduce power (1-beta) which means increase beta, or change the unit of diversion if originally it is not the same with unit of analysis. Or you
can target experiment to specific traffic, unrelated traffic will dilute the result and impact choice of practical significance boundary.

4-23 Learning Effect
When there’s a new change, in the beginning, users may against the change (change version) or use the change a lot (novelty effect). But over time, user behavior becomes stable, which is called the plateau stage. The key thing to measure learning effect is time, but in reality, you don’t have that much luxury of taking that much time to make a decision. Suggestion: run on a smaller group of users, for a longer period of time.
If you do have much time, you also need to notice the following points: 1) choosing the unit of diversion correctly; 2) dosage: how often we see the change, then you probably want to be using cohort as opposed to just a population; 3) risk and duration
Pre-periods and post-periods: A/A test before and after the experiment.


Novelty effect or change aversion: cohort analysis may be helpful