# Tell me about a project that your most proud of
## senario
When I joined SAS, SAS econometrics had a products that can only solve linear and gaussian state space model problems with Kalman filter or Hidden Markov Model algorithms. In HMM tool, only discrete latent varibales are allowed and in the Kalman filter only the continuous latent variables are allowed.

Many customers in the finance industry ask for tools that can handle stochastic volatility models which are important in derivative pricing. This family of models are nonlinear. And the IoT department of SAS also wants to deal with dynamic bayesian network in which there are both discrete and continuous latent variables. Therefore, we need to develop a time-series tool that can handle such situations.

## task
My task is to develop a tool which applies Sequential Monte Carlo from scratch. The tool needs to be comprehensive such that it can solve the filtering, smoothing, forecasting, and parameter learning problems in the State Space Model. Since Sequential Monte Carlo algorithm has a large computation complexity, I need to develop the tool for the SAS cloud server and distributed computation techniques should be applied. For a fresh employee, this task is not eash especially I need to develop it from 0 to 1 independently.

## action
1. I started the project with talking with the product manager about the requirements of the coustomers. I gradully enhance my awareness of all the examples and situations when the customers need this tool.

2. When I was a intern, I summarize the sequential monte carlo algorithms. Then I further dive deep into papers and keep talking with my manager about pros and cons of all the algorithms.

3. I read the product documents of the previous products of my team and kept meeting the corresponding developers to learn the development processs in SAS.

4. I design the map reduce functions of all the necessary algorithms and write simulation examples to test the parallel algorithms. I also pay attention to some open source products that can solve similar problems. Even thought they are not comprehensive, I can learn many things from them such as user's document and syntax.

5. Though most SAS documents use simulation examples, I use some real world examples in my user's document. I choose empirical cases based on the real data because these problems are practical and customers are more familiar with them. Through such examples, customers can learn how to use the product quickly.

## Result
I completed developing this tool in time. All the classical algorithms are included in the tool and all algorithms are written in the parallel version. Compared to the competitor products and the open-source products, my product is more comprehensive in features and options; moreover, it is much more efficient in computation.

# Tell me about the most challenging project you worked on
## scenario
apply dnn into causal inference
Causal inference is an important and active field in both academia and industry. It identifies the causes, measures their effects, and directs the policy making. Since the randomized controlled trials are often expensive or even impossible, the treatment effect is mostly estimated from observational data. There are several technical difficulties to do so, especially in the big-data world. Just name a few: there might exist huge amount of potential covariates;  there might exist unknown nonlinearity relationship between those covariates and the outcome and the treatment assignment; the variables might be discrete or continuous or mixed. Those problems might be easily overcome if deep learning, especially Deep Neural Networks (DNNs), can be applied in causal inference.

A problem in applying DNN to causal inference is interpretability. 

## task 
develop a sas procedure that applies dnn into causal inference;

## action
1. dive deep into the causal inference related papers especially how to apply machine learning methods into causal inference methods. I talked with the product manager and supervisor about the customers' requirements in the causal inference products. 

2. The double machine learning method is really inspiring for me. Based on the ideas of that paper, I designed a two-stage semiparametric algorithm that applies DNN into causal inference. And I also develop a framework of policy optimization where another DNN will be used as a mapping function from a observation to to the treatment assignment.

3. keep hosting conference meetings with developers of the previous causal inference procedures in SAS and adjust the features based on their feedbacks.

4. Read documents of the DNN products in SAS and get familiar with the internal API so that I can directly call the APIs when I need to build DNNs within my development.

## Result
Successfully deliver the procedure which is a indispensible compliment to the SAS causal inference procedures since all of the previous ones use the traditional statistics or econometrics models to have the causal inference while our new procedure is much more powerful and flexible in the big-data world.

# Tell me about a project that you had failed
## scenario
In the parameter learning feature of the Sequencial Monte Carlo produre, I developed a algorithm based on the gradient decent method. It works well in many cases and it is efficient in computation. However, sometimes this algorithm has unstable results and the performance depends on the initial values of the parameters to much extent. Moreover, the algorithm needs the derivative functions of all the distribution functions which is not user-friendly for complicated models.

## task
I need to solve the problem to guarantee the parameter learning in the product is stable and easy to learn.


## action 
1. I dive deep into papers about the gradient decent methods in the State space model and try to find some solutions. However, I found there are few papers that cover the compliated models which has issues in the gradient decent methods. 

2. I talked with my manager about add more options or features to the product about complicated models. For example, I can save built-in derivative functions for some common compliated models so they can be directly called when they are necessary. I can also give some instructions in the document about how to initialize the paramters to have a good result. However, such solutions still add to the complexity of the product and make it not user friendly, especially for some basic users who do not have enough experience in the parameter initialization.

## Result
Though the gradient decent method works well in most cases and it has unique advantages in the computaion complexity, we decide not to implement in our product. Then I use another algorithm that combines sequential monte carlo and MCMC method in the parameter learning for the state space mdoel.

The lesson I learned from this failure is that we need to think about a problem from the standpoint of the customers. As a developer, I am expertise in the product. But I need to simplify the product such that there are no subjective settings in the method that requires much experience in the area. It is important that our product is user friendly for all customers no matter whether they have expertise or not. Moreover, when developing a new product, besides some classical examples, we also need to test the product on practical problems to guarantee it covers all situations.

# Tell me about a time you took risk and succeed/failed
## succeed:
segment users into two groups; two systems of syntax

## failed:
the gradient decent method in the SMC

# Tell me about a time you had to deal with tight deadline and you were able/not able to meet the target
## scenario
In didi labs, I work in the internation carpool pricing team. Most of our customers are located in the Latin America. In latin america, only few people have credit card or debit card. Most of them pay by cash. Thus we introduce a fintech application such that usres can deposit the cash into the electronic wallet via the driver. The operations team also introduces the incentive coupon activities to encourage the riding users to register the product. However, the conversion rate is really low. 

## task
We need to develop a coupon dispatch policy in order to increase the conversion rate of the coupon. Since initializing a coupon campain costs much, it is better we can complete the dispatch policy as soon as possible

## action
1. I tried to figure out the problem quickly. I set up a conference meeting with my manager and the product manager. We do not have enough data for this new wallet coupon campains but we need to optimize the coupon dispatch policy. This is a cold-start problem. However, for the previous riding coupon campains, we have plenty of data. Thus, I come up with a solution that is similar to transfer learning. We use the previous riding coupon campains (like cash and discount coupons) data and treat it as a observational study. Though this is not a perfect solution, but it is what we can do currently for the cold-start problem.

2. I think about how to simplify the work. I select some representative coupon activities based on the number of customers that receive the coupons. I also think about how to build a model to help us make the coupon dispatch automatically. A stand-up meeting with my manager is setup every day and I will summarize the daily progress in the document. A causal inference model is proposed to estimate the treatment effect of each coupon on each user. We tried to find as many demographic and  behavior covariates as possible that can represent the customer. 

3. I hold a meeting with the data analytics team to check whether I can have the corresponding user related features. The dataset for each coupon is really large and training a model on that dataset is time consuming. I narrow the locations of the customers to the few main cities and quickly train the causal inference models to estimate the individual treatment effect of each user on each coupon. Dispatching the coupon is like a optimization problem since we want to maximize the general register rate of all riding users within the limit of the budget. I rank the ITE and choose the customer with the largest ITE to dispatch the coupon. This is like a greedy algorithm and very easy to implement compared to the traditional integer programming optimization problem.

## Result
The algorithm works well for the offline data and we double the conversion rate in the offline data. Then we cooperate with the enginners to design the experiments to test whether the new coupon dispatch can increase the metric significantly. The result is also satisfying. Though some steps is simplifed and not perfect, at least we give a solution quickly. Sometimes we need to make it work at first and then make it beautiful.

# Negative feedback
## Senario: 
I develop a algorithm to optimzie the coupon dispatch policy and have a good offline result. 

## Task: 
I need to present to the head of the operation team to show him the results.

## Actions: 
In the presentation, I went through my model in details including the algorithm, and  the features I chose. I presented to my team at first and receive high compliments on my work from many team members. However, I received nagative feedback of not showing the detailed metrics of the project in a more direct way. The details of model or algorithms are important; however, for a ops team, theay are very customer centric and care more about the results. I need to quantify the comparisons between the previous and current coupon dispatch methods and it's better to give some plots to show the difference. 

## Results:
I rewrote the slides and firstly show the offline metric results with highlights. I visualize the results and display the comparisons with the previous result in plots. Some ideas of the experiment design are also discussd but the details of the model and algorithm are summarized in a flowchart in just one page. The feedback is excellent.

# Tell me about a time you made a decision without your manager’s approval

## Scenarios
Our team is responible for designing a coupon dispath policy. We talked about the models and covariates to use. Three days later, we need to demo this to the all the internal audiences in our demo day.

## Tasks: 
I will give the demo. I wrote and update the slides on the night before the demo day. We use causal inference models to estiamte the individual treatment effects and use Operations Research techniques (integer programming) to optimize the average of ITE of all users via coupon dispatch. When I modified the slides, I also searched the research merits in this area and finally find one very promising application of DNN in policy optiomization. This is called direct rank model. This method is easy to understand and implement. Moreover, it is much more efficient in computation than the original operation research techniques. 

## Actions: 
Therefore, I write some pages of this algorithm and add them to the demo

## Results: 
I successfully made a demo and lots of teams express their big interests on this new project.


# 创新 innovation; beyond expectation
## DRM
### scenario
We want to optimize the coupon dispatch policy. The individual treatment effect on each coupon is estimated. Then an optimization problem needs to be solved. The objective function is to maximize the sum of the individual treatment effects of the treated group users. The constraint equation is the total cost should be less than the budget limit.

### Task
I need to find a solution to this optimization problem. 

### Action
1. My manager suggests using integer programming since this is a classical 0-1 programming problem-- a user will be given coupon or not. And the global maximum solution can be found. However, there are some problems of this solution. Firstly, the open source integer programming solver cannot handle such a large-scale problem. We have millions of users to consider. Secondly, the computation complexity is not acceptable even there are some commercial software available. 

2. I dive deep into papers about recommendation and causal inference and a paper inspired me. The paper is proposed by uber which applies neural networks to estimate the probability that a user should be selected for a coupon activity. That paper is based on experimental data while our data is observational data so there might be many confoundings. Thus, I talked with my manager and modified the formulas in the paper to extend that method for observational data. 

3. I also run simulations using the modified method with tensorflow and compare the results with the one of interger programming. Even though our new method cannot obatin the global maximum but the result is quite close. However, our method is much more efficient in the computation complexity and can be easily implemented using the open-source tool like tensorflow.

### Result
We use the modified model to solve the practial problem. The result is satisfying. We doulbe the conversion rate of the acquisiton coupon.

# 创新 multiple chain MCMC
## scenario 
In the sequential monte carlo procedure, which is my product in the SAS. We found the gradient decent method is not stable when learning parameters even though it is much more efficient in the computation complexity. Then we decided to implement the other method in the parameter learning which is the combination of MCMC and sequential monte carlo. Even thought the method is quite flexible which means it handle all kinds of state space model inlcuding complicated models, it is very slow since the computation burdern is large. 

## task 
I need to find a way to speed up the method

## actions
1. I refer to the MCMC product in the SAS and found it is only using one chain. I understand it. For the traditional MCMC, the likelihood has an analytical formula so the computation complexity is always not an issue. But for non-linear or non-gaussian state space model, the likelihood is estiamted via simulation and it tooks much time. 

2. 
I searched for papers about multiple chain MCMC method and keep talking with the developer of single chain MCMC product. I reviewed the problem and found the problem is to design a multichain MCMC diagnostics method. We dived deep into the papers and worked together 
to develop a self-tuning Metropolis within Gibbs sampler for the parallel multiple-chain MCMC method. 

## Result
The multichain MCMC method for parameter learning is easy to understand, and user friendly because it does not need any derivative functions. Compared to the gradient decent method, it is more time consuming. However, after multi chains are implemented, the total neessary time for computation is acceptable.

# 冲突
## scenario
For the sequential Monte Carlo procedure, it solves the non-linear or non-gaussian state space model. Such models are so complicated that API functions for the transition, initialization and observation equations need to be defined. For each equation, there are two versions of functions to be defined, one is for sampling and the other one is for probability density function. So there are about 6 API functions to be defined not to metion sometimes the importance sampling functions are also necessary. For our procedure, the users need to define each function and then input the function name as input arguments in the procedure syntax.

## task
The syntax is not user friendly becaues there are too many functions to be defined.  I talked with my manager about my concern and want to simplify it. My manager insisted on using the syntax for two reasons. Firstly, the syntax is comprehensive. It supports any ssm no matter whether it is simple or complicated. Secondly, most of our users have much experience in econometrics area and SAS products so they can handle the complicated syntax.

## action
1. I browsed the similar open source products and learned the information of their syntax. I summarized the pros and cons of the syntax of each similar product and show it to the manager. There is no doubt our product is more comprehensive and powerful than the open-source competitors. However, we also need to guarantee our syntax does not fall behind. For me, syntax is just like the first-glance impression. It is so important. If many users find the syntax too complicated they do not want to learn how to use it.

2. I proposed some syntax designs which are based on the distributions. Users can easily define the distribution by calling some built-in functions with the corresponding parameters. Such syntax is similar to the one of the popular bayesian open source software JAGS BUGS. Most usres are familiar with such design.

3. I also segment the usres into two groups: basic and advanced users. For the basic usres, they can choose the simplified syntax. It is easy to grasp though it cannot handle quite compliated models. But it does not matter. For the complicated models, they can choose the other syntax, which is the API based syntax.

4. I made a presentaion about the new design and the idea of keeping these two syntax system at the same time
## Result
I received positive feedbacks of the presentention and convinced my manager to implement the simplified syntax for the first version. In the second version of the procedure, I added the API based syntax. Our customers are also satisfied with my design