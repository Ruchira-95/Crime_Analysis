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


### Software Description

A comprehensive solution for crime prediction and analysis is provided by the software created for the "Prediction and Analysis of Unlawful Activities" project, which comprises of multiple interrelated components. A script to create a map of crime hotspots using the Folium library is one of these components, along with a Flask-based web application for user interaction and a random forest classifier for crime prediction.

#### 5.1 Visual Studio Code

![Picture1](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/2526918f-7e96-4655-9bc4-ca4b8e7a6723)

Visual Studio Code

Microsoft created Visual Studio Code, also known as VS Code, a well-liked and potent source code editor. Due to its exceptional capabilities and versatility, it has experienced tremendous growth in popularity among programmers of many different programming languages since its release.

The lightweight nature of Visual Studio Code is one of its most remarkable features. It delivers a stable and feature-rich development environment yet being lightweight. It offers a large selection of extensions and supports a wide variety of programming languages, allowing developers to tailor their coding experience to suit their individual requirements. It is the perfect option for developers working on a variety of projects because of its flexibility.

The user-friendly interface of Visual Studio Code is one of its main advantages. Even for people who are completely new to coding, the layout and design make it simple to use. With the editor's intelligent code completion, syntax highlighting, and code snippets, developers can write code more quickly and with fewer errors.

The robust debugging features of Visual Studio Code are another noteworthy aspect. It has an extensive collection of debugging capabilities, like as breakpoints, variable inspection, and step-through debugging, which make it much easier to find and correct coding problems. Developer productivity is further increased by the seamless connection with version control tools like Git, which facilitates effective teamwork and code management.

Extensibility is another feature that Visual Studio Code prioritises highly. The editor may be enhanced with new functions and language support thanks to its extensive marketplace of extensions, making it suitable for a variety of development scenarios. These add-ons cover a wide range of topics, from tools for particular programming languages or workflows to integrations with widely used frameworks and libraries.

Additionally, a wide range of capabilities supported by Visual Studio Code improve productivity and simplify the development process. These consist of a built-in Git integration, integrated terminal support, live server previews, and a large ecosystem of integrated development environments (IDEs) that offer thorough tooling for certain frameworks and languages.

Even when working with big codebases, Visual Studio Code maintains a high level of performance despite its extensive feature set. Even during lengthy periods of coding, it ensures a smooth experience thanks to its ability to manage memory and system resources effectively.
In conclusion, Visual Studio Code has completely changed the way source code editors are created. It is a favourite choice for developers in a variety of industries because to its lightweight design, vast customization choices, potent debugging tools, and broad language compatibility. Visual Studio Code continues to set the bar for contemporary code editors with its ongoing innovation and active community, enabling developers to produce high-quality code quickly and easily.

#### 5.2 Training

The random forest classifier used in the prediction module is trained using the training code. A crime dataset that includes historical crime records and associated information is first loaded from a CSV file. In the data preprocessing stage, missing values are dealt with in order to make the dataset clean and suitable for analysis. Additional features are created from the existing data to improve the model's predicting skills. To be more precise, the year, month, day, hour, and minute are extracted from the date and time columns. These characteristics assist in identifying temporal patterns and raise the reliability of crime prediction models. After that, the dataset is divided into training and testing sets so that the model can be assessed. A StandardScaler is used to standardise the input characteristics, ensuring consistency and attribute comparability. Finally, the scaled training data is used to train the random forest classifier, which is then trained and saved for later use as "crime_model.pkl" along with the scaler.

![Picture2](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/54491629-64fd-4906-83b2-0d75fb24e53b)

Sample Dataset

#### 5.3 Hotspot

Based on the provided crime dataset, the hotspot code is intended to identify criminal hotspots. Similar to the training code, it reads the dataset from a CSV file and groups the data by latitude and longitude. The code calculates the frequency of criminal activity in various places by measuring the number of offences at each distinct location. In order to identify hotspots, it is necessary to set a threshold value that indicates the minimum number of crimes that must occur in a given area. A hotspot is defined as any location with a crime rate that is higher than this limit. The code uses the Folium package, which offers an interactive mapping interface, to visualise the hotspots. The mean latitude and longitude of the hotspots that were detected serve as the centre of the map of crime hotspots that was developed. On the map, each hotspot is represented by a marker that, when clicked, shows the related crime rate. The generated map is then archived as 'crime_hotspots_map.html' for quick access and dissemination.

#### 5.4 Flask Web App

The program's user interface is implemented in the primary code as a Flask web application. Users of the application can enter a certain date, latitude, and longitude to find out what kind of crime is most likely to happen there. The 'crime_model.pkl' file, which is loaded by the application, contains the trained random forest classifier. The classifier has learned patterns and relationships in the data by being trained on a dataset that contains a variety of crime variables. The input features are preprocessed and scaled using a StandardScaler, which is also loaded from the'scaler.pkl' file, before predictions are made. The online programme then presents the anticipated crime type on an analysis page, offering users insightful data.

#### 5.5 HTML

Within the Flask web application, HTML templates are used to render web pages and offer a user-friendly interface for entering data, viewing predictions, and accessing analysis findings. These designs guarantee an information presentation that is both aesthetically pleasing and user-friendly, making it simple for users to engage with the software.

#### 5.6 Summary

In conclusion, the programme combines machine learning methods with web programming using Flask and data visualisation with Folium to produce a complete analysis and prediction tool for criminal activity. The software enables users to make knowledgeable predictions about the kind of crime that may occur at a certain place based on historical data by utilising the power of the random forest algorithm. The hotspot detection module also aids in identifying regions where criminal activity occurs more frequently, enabling focused interventions and resource allocation. Users may smoothly engage with the programme because to the user-friendly online interface, which improves accessibility and usability.

### Project Implementation

The methodology, in short, entails gathering and preparing the data, cleaning and pre-processing the data, studying and visualizing the data, choosing suitable machine learning algorithms and techniques, evaluating and tuning the model, and finally deploying and testing the model. It is aimed to create a trustworthy and accurate crime prediction system using this methodology that will help law enforcement authorities stop and lower crime rates.

![Picture1](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/7e1c8073-479a-46b6-9413-9d2b5afc28f6)

Block Diagram

The steps used in the methodology are, 

1.	Data Collection and Preparation:-
Gathering and preparing the data is the first stage in creating a model that uses machine learning for analyzing and predicting crime. We will make use of a dataset that includes details on a variety of offenses, including theft, burglary, assault, and homicide, as well as pertinent elements like time, place, and demographics. If more information is needed, we will also gather it from reputable sources like law enforcement and governmental organizations.

2.	Data Cleaning and Pre-Processing:-
The data must then be cleaned and pre-processed. We will eliminate any unnecessary or redundant data, deal with missing values, and arrange the data so that machine learning algorithms can use it. To make sure that all features are on the same scale, we will also scale and normalise the features.

3.	Data Exploration and Visualization:-
We will study and display the data to obtain insights into the underlying patterns and trends prior to constructing the machine learning model. To show the data and find any relationships between the attributes, we will employ a variety of data visualization tools, including histograms, scatter plots, and heatmaps.

4.	Model Selection and Training:-
We will choose the best machine learning algorithms and methodologies after the data has been organised, cleansed, and investigated. We will compare the performance of various algorithms, including decision trees, logistic regression, and support vector machines, using various metrics, including accuracy, precision, recall, and F1-score.

5.	Model Evaluation and Tuning:-
We will assess the model's performance using a variety of evaluation measures after it has been trained. To enhance the model's performance and find the ideal collection of hyperparameters for the supplied data, we will also do hyperparameter tuning.

6.	Deployment and Testing:-
Lastly, we will apply the machine learning model and evaluate its effectiveness in the real world using fresh data. In order to assess the model's efficacy, we will also compare its performance to other crime prediction models that are already in use.


### Experimental Results and Discussions

Below is the screenshot of the landing page for the web app development for the before mentioned project.

![Picture4](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/07f68272-ea3b-417a-8247-b3a9acd6bf51)

Landing Page

The pre-trained model which is now saved as a pickle file is now loaded when it is needed.
The web application is made using flask and HTML. The main page or the home page consists of two buttons “Prediction” and “Hotspots”.

![Picture5](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/aade8ef7-fa48-4dd8-8ba7-3ed0d3fee5db)

Analysis Page

The “Prediction” button redirects to the analysis page where the user is asked to enter three inputs namely, date, latitude and longitude.
The “Prediction” is made by using the pre defined model which was saved as pickle file.
The analysis page has two buttons namely, “Submit” and “Home”.
The “Submit” button flashes the prediction based on the given inputs.
The ”Home” button redirects to the home page.

![Picture6](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/5452a1ea-f44d-4e5c-ad02-e4febc292c3a)

Prediction Example

The above image shows an example input and it’s predicted output.
If the “Hotspot” button is clicked on the home page, then it will redirect to the crime hotspot map which was created before.

![Picture7](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/ae491583-c0a9-4a19-a34f-e98e6d136b5c)

Crime Hotspot on Map

If the hotspot label is clicked on it shows the crime count of that particular spot as shown in the below image.

![Picture8](https://github.com/Ruchira-95/Crime_Analysis/assets/93994154/283077df-60ac-4ec7-8bf5-3f842948794e)

Crime count


### Time Scheduled

| **Task Assigned** | **Time allocated** |
| --- | --- |
| Data Collection and Preparation | 1 week |
| Data Cleaning and Pre-Processing | 1 week |
| Data Exploration and Visualization | 1 week |
| Model Selection and Training | 2 week |
| Model Evaluation and Tuning | 2 week |
| Deployment and Testing | 2 week |


### Conclusion

The goal of our project is to create a website that can accurately predict the crime on a particular location on a particular day based on the past records and generate a crime hotspot map which can be used by law enforcement agencies to work more effectively. Not just the law enforcement agencies but the tourists can also use this to know about the crime history and potential crimes of a place their about to visit beforehand and hence they can add it to one of the factor that affects their selection of a place to visit.


### Reference

[1] Roopa, Prof. Thouseef Ulla Khan (2022). CRIME ANALYSIS AND PREDICTION USING MACHINE LEARNING (IRJET).

[2] Azwad Tamir, Eric Watson, Brandon Willett, Qutaiba Hasan, Jiann-Shiun Yuan(2021). Crime Prediction and Forecasting using Machine Learning Algorithms (IJCSIT).

[3] Pratibha Kumari, Lokesh Chouhan, Akanksha Gahalot (2020). Crime Prediction and Analysis

[4] B. Thanuja, Konda Pranitha, Challagundla Vamshi, Pabbu Naveen, Puntikura Srinivas(2022). Machine Learning Based Crime Rate Analysis Using Python (IJRASET).

[5] Kang, H. and Kang, H. (2017). Prediction of crime occurrence from multimodal data using deep learning. PLOS ONE, 12(4).

[6] Aziz, Rabia Musheer; Hussain, Aftab; Sharma, Prajwal; and Kumar, Pavan (2022) "Machine Learning-based Soft Computing Regression Analysis Approach for Crime Data Prediction," Karbala International Journal of Modern Science: Vol. 8 : Iss. 1 , Article 1.

[7] V. Srinidhi, P. Saranya, M. Ashok, An affirmative learning techniques to analyse the crime scene in jewel theft murder, Int. Res. J. Multidiscip. Tech. 2 (2020).

[8] M.K. Anser, Z. Yousaf, A.A. Nassani, S.M. Alotaibi, A. Kabbani, K. Zaman, Dynamic linkages between pov-erty, inequality, crime, and social expenditures in a panel of 16 countries: two-step GMM estimates, J. Econ. Struct. 9 (2020).

[9] M. Suhail, I. Babar, Y.A. Khan, M. Imran, Z. Nawaz, Quantile-based estimation of liu parameter in the linear regression model: applications to portland cement and US crime data, Math. Probl Eng. 1 (2021).

 [10] Andrey Bogomolov, Bruno Lepri, Jacopo Staiano, Nuria Oliver, Fabio Pianesi, Alex Pentland.”Once Upon a Crime: Towards Crime Prediction from Demographics and Mobile Data” ,in ACM International Conference on Multimodal Interaction (ICMI 2014)

[11] Shanjana A.S, Dr. R. Porkodi (2021), CRIME ANALYSIS AND PREDICTION USING DATAMINING: A REVIEW (IJCRT).

[12] Aurélien Géron, Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow, Second Edition, 2019.

[13] Manning Publications, Machine Learning with TensorFlow Version 10, 2017.

[14] Matthew Scarpino, Tensorflow for Dummies, 2018.


