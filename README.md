# Crime Analysis
## Academic mini project on the topic "PREDICTION AND ANALYSIS OF UNLAWFUL ACTIVITIES".

### Abstract
The development of creative technical solutions to address the challenges of crime research and forecasting has become increasingly important. In response to this growing need, we have developed a comprehensive web-based tool that aims to anticipate and analyze crime trends, ultimately assisting law enforcement agencies in enhancing their crime-fighting techniques. 
Our research tool leverages the power of machine learning to construct a predictive model using regression analysis. To achieve this, we utilize the widely acclaimed scikit-learn package, which allows us to train our model on a rich historical dataset of crime incidents provided in a CSV format. Once the model is trained, it is saved as a pickle file, enabling swift retrieval and utilization whenever required.
To ensure a user-friendly experience, we have created an intuitive web page using Flask, a popular web framework, in conjunction with HTML. This interface simplifies data input, making it easier for users to interact with the tool and obtain meaningful results. Additionally, we have incorporated the Folium library, which facilitates the visualization of crime hotspots on interactive maps, aiding in the understanding and interpretation of the data.
The key elements of this project revolve around crime prediction, machine learning, regression analysis, Flask, HTML, pickle files, and Folium. By harnessing the capabilities of this application, our objective is to empower decision-makers and law enforcement agencies with valuable insights for effective resource allocation and proactive crime prevention strategies. By identifying crime hotspots and predicting future trends, we aim to contribute to the collective efforts in creating safer communities. Key terms: crime prediction, machine learning, regression analysis, flask, html, pickle files, folium.


### Introduction
Understanding crime patterns, averting criminal situations, and sustaining public safety all depend heavily on the prediction and analysis of illegal activity. Predictive modelling has developed into a useful tool for locating probable crime hotspots and enhancing law enforcement tactics as a result of the expanding accessibility of massive datasets and improvements in data analysis techniques. The goal of this project is to analyse a dataset and forecast illegal behaviours using random forest regression, a potent machine learning method. The study also aims to map crime hotspots for better resource allocation and geographical comprehension.
The effects of crime go beyond the lives of the individual and have an effect on communities, businesses, and the general well-being of society. For law enforcement organisations, decision-makers, and researchers, the capacity to anticipate and analyse illegal activity is of the utmost importance. Law enforcement organisations can strategically deploy resources, improve patrol routes, and create focused crime prevention initiatives by acquiring knowledge into crime patterns. This data can be used by policymakers to put in place effective policies that lower crime rates and protect individuals. Understanding the underlying causes of criminal behaviour will help researchers investigate cutting-edge techniques for crime analysis and prevention.
The project makes use of a large dataset with a variety of factors connected to illegal activity, including time, place, crime type, and demographic data. With the help of the random forest regression technique, an accurate prediction model may be constructed using this dataset as the basis. A robust and adaptable model that can handle complex interactions between predictors and crime outcomes is created using the strong ensemble learning technique known as random forest regression. This method combines numerous decision trees. The algorithm can learn patterns and correlations by being trained on historical crime data, which enables it to predict future criminal episodes with accuracy.
The study uses geographical visualisation in addition to predictive modelling to pinpoint crime hotspots. Law enforcement organisations and other interested parties can identify locations where crime is concentrated and direct their efforts there by superimposing crime statistics on a map. With the use of this spatial analysis, patrols may be sent to high-crime areas, and preventive measures can be put in place.
The results of this initiative could make a substantial contribution to the study of crime and its prevention. The crime hotspot visualisation and predictive model can help law enforcement agencies allocate resources more effectively, make more informed decisions, and improve community safety. The results of this project can also be used as a foundation for future study and the creation of more complex crime prediction models that incorporate other data sources and cutting-edge analytical methods.


### Literature Survey
Recent years have seen a substantial increase in the use of machine learning approaches for crime analysis and prediction. For law enforcement agencies, being able to predict and analyze  crime patterns with accuracy can offer useful insights that help with resource allocation and the creation of preventative programmes. This study of the literature focuses on the use of machine learning algorithms while exploring numerous studies and academic articles on crime analysis and prediction.

#### 2.1 Literature Review

Roopa, Prof. Thouseef Ulla Khan [1], “Crime analysis and prediction using machine learning”. In this paper, Their work underscores the significance of using historical
crime data to train models and the advantages for law enforcement organizations. . By using data mining techniques and machine learning, the proposed paradigm aims to increase prediction reliability, privacy, and precision in identifying criminal hotspots and areas with high crime rates.

B.Thanuja, Konda Pranitha, Challagundla Vamshi, Pabbu Naveen, Puntikura Srinivas [2]. Machine Learning Based Crime Rate Analysis Using Python”. This paper the authors of this study emphasize the need for advanced technology to address the rising crime rates. They explore various crime analysis techniques, including machine learning algorithms, and present a case study on crime rate analysis using Python and machine learning techniques, highlighting the effectiveness of Random Forest in forecasting crime rates with a high accuracy of 94.74%.

Aziz, Rabia Musheer; Hussain, Aftab; Sharma, Prajwal; and Kumar, Pavan  [3].Machine Learning-based Soft Computing Regression Analysis Approach for Crime Data Prediction," Karbala International Journal of Modern Science. This paper highlights the need for reliable crime prediction models to combat the increasing crime rate. They propose a soft computing strategy that combines machine learning algorithms like Artificial Neural Networks, Support Vector Regression, and Random Forest and demonstrate that their method outperforms conventional regression analysis techniques, potentially improving the accuracy of crime prediction models.

Azwad Tamir, Eric Watson, Brandon Willett, Qutaiba Hasan, Jiann-Shiun Yuan [4]. “Crime Prediction and Forecasting using Machine Learning Algorithms”. This paper focuses on using machine learning algorithms to accurately predict crime in metropolitan areas, allowing the police department to allocate resources more effectively. The research uses machine learning models and data visualization to identify trends in crime and arrest rates, with a Neural Network achieving the highest accuracy of 90.77%.

M. Suhail, I. Babar, Y.A. Khan, M. Imran, Z. Nawaz [5]. “Quantile-based estimation of liu parameter in the linear regression model: applications to portland cement and US crime data”. This paper has proposed a new approach to estimate the Liu parameter using datasets on Portland cement and crime in the US, and compared its performance with other approaches. They found that their approach provides more accurate and reliable estimates, indicating its potential usefulness in various applications.

Shanjana A.S, Dr. R. Porkodi [6], “Crime analysis and prediction using data mining”. In this paper the authors explore different types of criminal analysis and crime prediction using data mining techniques, and emphasize the main goal of crime analysis. They conclude that their proposed system has the ability to predict high-probability crime regions and visualize crime-prone areas.

Pratibha Kumari, Lokesh Chouhan, Akanksha Gahalot [7], “Crime Prediction and Analysis”. In this paper the authors emphasize the importance of crime analysis and prediction to reduce crime and ensure public safety. Their study examines the effectiveness of various machine learning algorithms, including Decision Trees, K-Nearest Neighbors, Naive Bayes, and Support Vector Machines, in predicting crimes and presents a case study of using the Random Forest algorithm to forecast crime in Jaipur, concluding that machine learning algorithms can provide practical tools for crime prediction, potentially enhancing public safety and law enforcement.

V. Srinidhi, P. Saranya, M. Ashok [8], “An affirmative learning technique to analyze the crime scene in jewel theft murder”. This paper has proposed an affirmative learning method that analyzes positive and negative instances of a crime scene to identify key elements and predict potential paths taken by perpetrators. The research uses data mining techniques and a case study to demonstrate the effectiveness of the approach and suggests that it can provide valuable insights for law enforcement in complex criminal cases.
M.K. Anser, Z. Yousaf, A.A. Nassani, S.M. Alotaibi, A. Kabbani, K. Zaman [9], “Dynamic linkages between poverty, inequality, crime, and social expenditures in a panel of 16 countries: two-step GMM estimates”. In this paper the authors have conducted a study examining the relationship between inequality, poverty, and crime, finding evidence of a positive connection between inequality and crime and a link between poverty and crime. They suggest that investing in social spending to reduce inequality and poverty can ultimately lead to a decrease in crime rates.
Kang, H. and Kang .H [10], Prediction of crime occurrence from multimodal data using deep learning. This project suggests the use of deep learning models that combine convolutional neural networks and recurrent neural networks (RNN) to predict crime likelihood, by integrating various data sources such as social media, weather information, and crime reports. The authors tested their model using crime statistics from Chicago and highlight the potential of deep learning methods in predicting crimes when combined with multimodal data sources.
Andrey Bogomolov, Bruno Lepri, Jacopo Staiano, Nuria Oliver, Fabio Pianesi, Alex Pentland [11]. Once Upon a Crime: Towards Crime Prediction from Demographics and Mobile Data” ,in ACM International Conference on Multimodal Interaction .In this paper they have employed machine learning algorithms to predict the probability of a crime occurring in different areas using data on demographics, call logs, and location history. Their findings suggest that mobile data has the potential to provide valuable insights into crime prevention and prediction, with implications for law enforcement and public safety.

#### 2.2 Motivation

The motivation behind this project stems from the pressing need to address and mitigate the pervasive issue of crime within society. Criminal activity has wide-ranging effects on people, communities, and society as a whole. For efficient law enforcement, proactive crime prevention, and the general welfare and safety of residents, it is essential to be able to accurately forecast and analyse crime patterns.

Traditional crime analysis techniques frequently rely on anecdotal evidence, historical crime statistics, and human intuition. Although these methods have their advantages, they might not be able to offer complete and timely insights into new trends and patterns in crime. The development of sophisticated data analysis methods and the accessibility of big datasets present a previously unheard-of chance to improve crime analysis and prediction.

This project aims to overcome the constraints of old methodologies and give a more data-driven and proactive approach to crime investigation by utilising the power of data and sophisticated machine learning algorithms. In order to identify hidden patterns and connections within the information and produce precise crime predictions, random forest regression, a powerful machine learning method, is used. The incorporation of spatial visualisation tools improves our comprehension of crime hotspots and helps us allocate resources and conduct focused crime prevention strategies.

This project may have a wide range of effects. The model's predictive skills can help law enforcement agencies better allocate their resources, plan out patrol routes, and concentrate their efforts in high-risk locations. Policymakers and city planners may make educated judgements regarding urban growth, lighting, and other infrastructure improvements to promote safer settings by detecting crime hotspots through spatial visualisation. The knowledge gathered from this initiative can also be used to design evidence-based policies and interventions that target the causes of crime.

By examining the use of geographical visualisation and random forest regression in crime prediction, this study also advances the broader subject of crime analysis and prevention. By proving the effectiveness of these techniques, it creates opportunities for additional study and invention in the area, maybe leading to more sophisticated predictive models and analytical techniques.

The main driving force behind this project is the goal to use cutting-edge technology and data analytic techniques to significantly advance our knowledge of and ability to combat illegal activity. This project intends to support law enforcement agencies, policymakers, and researchers in their efforts to build safer communities and enhance the quality of life for people affected by crime by giving precise crime predictions and visualising crime hotspots. 

#### 2.3 Scope of the project

The scope of this project is the development and implementation of a predictive model using random forest regression for analyzing and predicting unlawful activities. The project aims to use the given dataset which contains the attributes related to crime, such as date, latitude, longitude, time and type of the crime and predict the possible crime that might occur based on their pattern and label the areas which have relatively more crime occurrences as crime hotspots.

The project's main goal is to use the potent machine learning technique random forest regression to identify patterns and correlations in the dataset and produce precise predictions about upcoming criminal occurrences. To capture the correlations between different predictors and crime outcomes, the model will be trained using historical crime data. The goal is to create an accurate and effective predictive model that will help detect prospective crime hotspots and enhance law enforcement tactics.

Although the main goal is to analyse and predict crime, in order to identify and depict crime hotspots, the project also has a spatial visualisation component. The project's goal is to give law enforcement agencies and stakeholders a visual picture of concentrated areas of criminal activity by superimposing crime data on a map. This will help them better understand crime trends and allocate resources.


#### 2.4 Problem statement

For law enforcement agencies and communities throughout, crime is a huge concern. It is difficult to predict crime rates since crimes are expected to increase across the board as the population expands. 

Police personnel may not have the tools or knowledge to foresee potential crimes since they are focused on so many other situations. Despite their efforts, the police may not be able to reduce crime rates in a full-fledged manner. There is no data that includes the criminal occurrence date and time coupled with methods that can precisely forecast what crimes will occur in the future, despite the fact that enormous datasets have been evaluated and crime hotspots based on locations have been found. This lack of information poses a significant obstacle in the fight against crime and underscores the need for a reliable and accurate crime prediction system.
 
 
### Machine Learning

Machine learning is a branch of artificial intelligence (AI) that focuses on creating models and algorithms that let computers learn and anticipate the future or make decisions on their own. To train a machine learning model, which can then analyze and interpret fresh data to make predictions or take action, a lot of data must be used. 
Algorithms used in machine learning are created to find patterns and connections in data so that users can learn from them. To discover the underlying patterns and relationships, the model must be trained on a labeled dataset where the desired output or outcome is known. Once the model has been trained, it can be used to classify or forecast fresh data that has not yet been observed.

#### 3.1 Fundamentals of machine learning

A branch of artificial intelligence called "machine learning" focuses on creating algorithms and models that can learn from data and make predictions or take actions without explicit programming. It is predicated on the notion that computers can examine patterns and draw insightful conclusions from data to enhance their performance over time. supervised learning, unsupervised learning, and reinforcement learning are the three primary categories of machine learning, which includes a variety of techniques and methodologies.
Supervised Learning: In supervised learning, the algorithm picks up new information from training data that has been labelled and where each data point corresponds to a known result or goal variable. The objective is to develop a mapping function that can correctly forecast the target variable from unobserved data. Techniques for supervised learning include classification, where the objective is to categorise data points, and regression, which entails forecasting continuous values. For the model to be trained and its performance to be assessed, these techniques rely on the availability of labelled data.
Unsupervised Learning: With unlabeled data, unsupervised learning seeks to find patterns or structures in the data without knowing the results in advance. Finding hidden connections, clusters, or latent features in the data is the goal. The goal of dimensionality reduction techniques is to represent the data in a lower-dimensional space in order to reduce the complexity of the data, whereas clustering algorithms combine similar data points together based on their inherent properties. For tasks like exploratory data analysis, anomaly detection, or data pretreatment, unsupervised learning is frequently utilised.
Reinforcement Learning: To learn through trial-and-error in order to maximise cumulative rewards, reinforcement learning requires an agent interacting with an environment. The agent acts in the world, gets feedback from it in the form of rewards or penalties, and modifies its behaviour in response to that feedback. The goal is to discover an ideal policy that maximises long-term benefits. Applications for reinforcement learning can be found in robotics, gaming, autonomous systems, and resource management, among other fields.

#### 3.2 History of machine learning

During the middle of the 20th century, machine learning has a long and illustrious history. Important turning points and advancements have molded its development into the potent field it is today. The Dartmouth Workshop, which gave rise to artificial intelligence, provided the groundwork for investigating robots that might learn from experience in 1956. The perceptron, an early neural network capable of binary predictions, was introduced by Frank Rosenblatt in 1957. It was a key innovation for subsequent neural network studies.
The funding for and interest in AI and machine learning fell during the AI Winter in the 1970s and 1980s. But Rumelhart, Hinton, and Williams' invention of the backpropagation method in 1986 marked a substantial advance. This approach overcame earlier restrictions and allowed neural networks to learn from examples with numerous layers.
Support vector machines (SVM), developed in 1992 by Vapnik and Chervonenkis, were an effective method for classification and regression applications. In the 1990s, boosting techniques like AdaBoost were developed to improve classification accuracy by fusing weak learners into a robust ensemble model.
Due to advances in processing power, the availability of massive datasets, and novel neural network topologies, deep learning had a renaissance in the 2000s. Convolutional neural networks (CNNs) and deep belief networks (DBNs), developed by Geoffrey Hinton, have contributed to substantial advances in speech and image recognition.
The invention of more precise and scalable machine learning models was made possible by the emergence of big data and scalable computing in the 2010s. In 2016, Google's AlphaGo defeated the Go world champion, drawing attention to reinforcement learning and highlighting the possibility of discovering the best strategy through trial and error.
Several industries, including healthcare, banking, autonomous cars, natural language processing, and computer vision, are being transformed by machine learning, which is still evolving quickly. The world will be shaped and revolutionized in the future thanks to ongoing research and technology developments.

#### 3.3  Advantages of machine learning

Machine learning offers numerous advantages across various domains and industries. These are some of the primary advantages of machine learning:

1.Accurate Predictions and Decisions: Making Informed Decisions and Accurate forecasts is Made Possible by Machine Learning Algorithms Large datasets can be analyzed to find patterns that can be used to make accurate forecasts and decisions. They can find underlying patterns and insights that people might miss, resulting in more precise predictions and better results.

2.Automation and Efficiency: Businesses may perform more effectively because machine learning eliminates time-consuming, routine tasks. It can process data and do complex calculations at a rate and scale that is faster than what humans are capable of, which boosts production and lowers costs.

3.Personalization and Recommendations: As they can recognise unique preferences and behaviors, machine learning algorithms are excellent at personalisation. They fuel recommendation engines that make recommendations for goods, services, or information based on the interests of individual users, improving user engagement and satisfaction.

4.Fraud Detection and Cybersecurity: Real-time anomaly detection and fraud detection are made possible by machine learning. It can boost cybersecurity safeguards by analyzing massive amounts of data, identifying patterns of fraudulent behavior, and flagging questionable transactions or activities.

5.Enhanced Customer Insights:Real-time anomaly detection and fraud detection are made possible by machine learning. It can boost cybersecurity safeguards by analyzing massive amounts of data, identifying patterns of fraudulent behavior, and flagging questionable transactions or activities.

6.Autonomous Vehicles and Robotics:Robots and self-driving automobiles are made possible by machine learning, which analyzes sensor data and makes judgements in real time. It improves object detection, navigation, and control systems, which aids in the development of automated and transportation systems.

7.Continuous Learning and Adaptability: By constantly incorporating fresh data, machine learning models can continually learn and advance. They adjust to changing settings and shifting patterns, ensuring that forecasts and judgements are current and useful.

8.Autonomous Vehicles and Robotics:Robots and self-driving automobiles are made possible by machine learning, which analyzes sensor data and makes judgements in real time. It improves object recognition, navigation, and control systems, advancing automation and transportation.

Overall, machine learning empowers businesses and industries with advanced capabilities, enabling data-driven insights, automation, personalization, and enhanced decision-making across a wide range of applications.

#### 3.4 Applications of  machine learning

Machine learning enables computers to learn and make decisions like humans, and its applications span various industries and tasks, including business improvement, disease detection, weather forecasting, and more. Machine learning is now being used by businesses to enhance decision-making, boost production, find diseases, predict the weather, and perform many other things. Because of the technology's rapid advancement, we not only need better tools to comprehend the data we already have, but we also need to get ready for the data that will come in the future. We must create intelligent machines in order to fulfill this objective. To accomplish simple tasks, a programme can be written. However, it is frequently impossible to hardwire intelligence into it. Having a method for machines to learn things on their own is the greatest approach. If a machine can learn from input, it will do the labor-intensive work for us. Machine learning is used in this situation. Several of the more typical instances include:

1.Healthcare: Medical image analysis, drug development, personalized medicine, patient monitoring, and analysis of electronic health information are all areas where machine learning is applied.

2.Finance:For the detection of fraud, credit scoring, algorithmic trading, risk assessment, portfolio management, and consumer sentiment analysis, machine learning algorithms are used.

3.Retail and E-commerce: Personalized suggestions, demand forecasting, inventory control, price optimisation, customer segmentation, and fraud detection in online transactions are all made possible by machine learning.

4.Manufacturing and Supply Chain: Quality assurance, preventive maintenance, supply chain optimisation, demand forecasting, anomaly detection, and process automation are all made easier by machine learning.

5.Autonomous Vehicles: For object detection, scene understanding, navigation, path planning, and driver aid systems in autonomous vehicles, machine learning is essential.

6.Natural Language Processing (NLP): For analysis of sentiment, language translation, chatbots, speech recognition, text summarization, and information extraction in NLP, machine learning is used.

7.Image and Video Processing: For object detection, picture classification, image segmentation, facial recognition, video analytics, and video content analysis, machine learning approaches are used.

8.Cybersecurity:Machine learning is used to analyze network traffic for anomalies, identify malware and intrusion attempts, detect and prevent cyber threats, and improve overall cybersecurity measures.

9.Social Media and Marketing: Customer segmentation, targeted advertising, social network analysis, and content suggestion are all made easier by machine learning.

10.Energy and Utilities: Energy load forecasting, equipment predictive maintenance, energy optimisation, problem finding, and smart grid management all make use of machine learning.


### Regression

Regression is a useful technique for deciphering patterns and developing data-based predictions. It allows us to find trends, pinpoint crucial factors, and gain understanding of the underlying mechanisms. Regression offers a versatile and understandable framework for exploring and modelling relationships in a variety of disciplines, whether it be for predicting sales, examining economic patterns, or researching the effects of factors on health outcomes.

#### 4.1 Regression in  machine learning

A key machine learning method known as regression seeks to predict the connection between a dependent variable and one or more independent variables. When the dependent variable has a continuous or numerical nature, it is frequently utilised. Finding a mathematical function or model that accurately captures the relationship between the variables and enables predictions or estimates of values for additional data points is the aim of regression analysis.

Regression is predicting the value of the dependent variable using the independent variables as inputs. The procedure involves using a labelled dataset with known independent and dependent variables to train the regression model. By estimating the coefficients or weights connected to each independent variable during training, the model learns the patterns and relationships in the data. These coefficients specify the magnitude and axis of each variable's impact on the dependent variable.

Regression techniques come in a variety of forms, such as multiple regression, polynomial regression, linear regression, and more. In order to fit the data to a straight line, linear regression presupposes that the variables have a linear relationship. Because higher-degree elements are incorporated into the model with polynomial regression, curved relationships are possible. To account for their combined influence on the dependent variable, multiple regression combines numerous independent variables.

After being trained, the regression model may be used to predict fresh data by feeding it the values of the independent variables. The model computes a predicted value for the dependent variable by applying the discovered relationship to these inputs. By comparing the projected values to the actual values of the dependent variable, evaluation metrics like mean squared error or R-squared are used to determine how accurate the predictions are.

Regression is frequently employed in a variety of fields, including finance, economics, healthcare, and the social sciences, where it is essential to comprehend and anticipate numerical results. It permits making educated decisions based on data-driven predictions and sheds light on the interactions between variables. It also assists in identifying significant elements that have an impact on the dependent variable. Regression is a useful tool in the machine learning toolbox for analysing and modelling continuous variables because of its adaptability and interpretability.

#### 4.2 Regression method selection

Due to its unique benefits and adaptability for the task of predicting and analysing illegal activities, random forest is preferred above other regression approaches for this project. Here are some main justifications for choosing random forest:

1.	Accuracy and Robustness: Random forest is renowned for its accuracy and capacity to manage intricate interactions between variables. It is well suited for modelling real-world events because it can effectively capture non-linear correlations and interactions between features. In these cases, the relationship between predictors and outcomes is frequently complex and non-linear. In comparison to single decision tree models, random forest can provide predictions that are more accurate by utilising the power of numerous decision trees.

2.	Reducing Overfitting: Overfitting is the phenomenon when a model performs well on training data but underperforms on new data. By merging numerous decision trees that have been trained on various subsets of the data, random forest works to reduce overfitting. By minimising the effects of outliers and noise in the data, this ensemble technique enhances generalisation and performs better on untested data.

3.	High-dimensional data handling: Random forest can operate on datasets with a lot of features (high-dimensional data) without suffering much from it. At each split, it automatically chooses a random selection of features, which lessens the likelihood that any one feature will predominate the model's judgement. When working with datasets that may include several variables or a combination of useful and irrelevant aspects, this property is helpful.

4.	Feature Importance: Random forest offers a metric for feature importance that quantifies how much each variable contributed to the prediction of the result. In order to choose the most effective features for the study of illegal activity, this information can be useful. The model can perform more accurately in terms of prediction and offer insightful information about the elements influencing criminal events by concentrating on the most pertinent variables.

5.	Outlier and missing data resistance: Random forest is well renowned for its resistance to outliers and missing data. Due to the averaging effect of numerous decision trees, outliers have less of an impact on the model's predictions. Furthermore, random forest may deal with incomplete data by impute missing values or make use of surrogate splits when creating trees. The model can handle real-world datasets that frequently include noise, outliers, or insufficient information because to its resilience.

6.	Predictions from various decision trees are combined via the built-in ensemble method known as random forest. Compared to single decision tree models, this built-in ensemble technique helps minimise variation and enhance stability. Multiple trees can be averaged or voted upon to reduce individual errors and produce more accurate forecasts.

| **Task Assigned** | **Time allocated** |
| --- | --- |
| Data Collection and Preparation | 1 week |
| Data Cleaning and Pre-Processing | 1 week |
| Data Exploration and Visualization | 1 week |
| Model Selection and Training | 2 week |
| Model Evaluation and Tuning | 2 week |
| Deployment and Testing | 2 week |
