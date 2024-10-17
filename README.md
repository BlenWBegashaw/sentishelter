# 🏡🌍 SentiShelter: Climate Change & Housing Sentiment Analysis

Have you ever thought about buying a house and found yourself considering the climate of the region? What about worrying about rent increases or the next natural disaster lurking around the corner? We’ve all been there. Now, imagine having a tool that not only provides insights into the shifting perspectives about climate change but also its relationship with the housing market.

## 🌟 What It Does

**SentiShelter** aims to analyze and track how people feel when they discuss the relationship between **climate change** and **housing** over time. By using sentiment analysis on Reddit data, this project answers two key questions: **"Why"** and **"How"** is climate change affecting housing discussions?

### Key Features:
1. **Sentiment Analysis for Insights**
   - Using Reddit discussions, SentiShelter examines conversations about climate change and housing. We dive into why and how people talk about these topics and identify the root causes of these discussions.

2. **Interactive Website for Users**
   - To communicate these insights, we built an interactive website where users can explore sentiments and trends.
   - **Visualizations:** Bar charts and scatter plots help explain the relationship between variables.
   - **Chatbot Integration:** Using LangFlow, we implemented a chatbot that answers user questions in real-time, specifically addressing topics related to climate change and housing.

## 🔨 How We Built It

- **Data Source:** We used the Kaggle dataset available [here](https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset/data) that contains Reddit comments about climate change.
- **Data Processing:** In a Kaggle notebook, we cleaned, reduced, and analyzed the dataset using **Python**. We leveraged **SpaCy's NLP** tools to teach our system to read, assess, understand, and extract useful insights from human language.
  - We focused on key terms associated with **climate** and **housing** to monitor the mentions of people, organizations, or locations.
- **Visualization:** Using **Seaborn** and **Matplotlib**, we created visually appealing graphs to communicate trends and insights from the data.
- **Website:** A responsive web application where users can explore our findings. It features:
  - Sentiment data visualizations.
  - A **LangFlow-powered chatbot** that allows users to ask climate change and housing-related questions with real-time responses.

## 🚧 Challenges We Faced

- **Large Dataset:** The dataset required significant memory, which slowed down processing. We worked around this by sampling data that still provided accurate insights without skewing results.
- **Choosing the Right Tools:** Deciding on the best tools for processing, analyzing, and visualizing the data took careful consideration and discussion among the team.

## 🎉 Accomplishments

We’re proud of the insights and the interactive website we developed for **SentiShelter**. The chatbot integration and the clear, data-driven visualizations allow users to easily navigate and explore sentiment trends related to climate change and housing.

## 💡 What We Learned

- We learned how to combine **AI and NLP** to extract insights from large datasets and implemented an AI-powered chatbot to enhance user interaction with our findings.
  
## 👩‍💻 Team Members
- Sneha Joshi
- Blen Begashaw
- Lucy Wu
- Lily Eap



