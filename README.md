
# 🏡🌍 SentiShelter: Climate Change & Housing Sentiment Analysis

Have you ever thought about buying a house and found yourself considering the climate of the region? Or worried about rent increases or the next natural disaster lurking around the corner? We’ve all been there. Now, imagine having a tool that not only provides insights into the shifting perspectives about climate change but also its relationship with the housing market.

---

## 🌟 What It Does

SentiShelter aims to analyze and track how people feel when they discuss the relationship between climate change and housing over time. By using sentiment analysis on Reddit data, this project answers two key questions: **"Why" and "How" is climate change affecting housing discussions?**

### Key Features

* **Sentiment Analysis for Insights**
  Using Reddit discussions, SentiShelter examines conversations about climate change and housing. We dive into why and how people talk about these topics and identify the root causes of these discussions.

* **Interactive Website for Users**
  To communicate these insights, we built an interactive website where users can explore sentiments and trends.

  * **Visualizations**: Bar charts and scatter plots help explain the relationship between variables.
  * **Chatbot Access**: Users can open a [Hugging Face chatbot](https://huggingface.co/spaces/blenbegashaw/sentishelter-chatbots) to explore climate change and housing-related discussions. *Note: the chatbot is not real-time integrated on the website; it opens a separate space.*

---

## 🔨 How We Built It

* **Data Source**: We used the [Kaggle Reddit Climate Change dataset](https://www.kaggle.com/) containing comments discussing climate change.
* **Data Processing**: Using Python in a Kaggle notebook, we cleaned, reduced, and analyzed the dataset. SpaCy NLP tools were leveraged to extract meaningful insights from human language.
* **Focus Areas**: We monitored key terms associated with climate and housing, including mentions of people, organizations, and locations.
* **Visualization**: Seaborn and Matplotlib were used to create clear and visually appealing charts to show trends and sentiment over time.
* **Website**: A responsive web application allows users to:

  * Explore sentiment data and trends
  * Open a Hugging Face chatbot to explore questions about climate change and housing data
  * Visit the live website: [SentiShelter Website](https://blenwbegashaw.github.io/sentishelter/)

---

## 🚧 Challenges We Faced

* **Large Dataset**: The dataset required significant memory and processing time. We overcame this by sampling data while maintaining meaningful insights.
* **Choosing the Right Tools**: Selecting the best combination of Python libraries, NLP tools, and visualization methods took careful consideration.

---

## 🎉 Accomplishments

* Developed an **interactive website** presenting sentiment analysis insights.
* Provided **data visualizations** for easier understanding of trends and patterns.
* Offered **chatbot access** through Hugging Face for exploring questions about climate change and housing.

---

## 💡 What We Learned

* How to combine AI, NLP, and data visualization to extract insights from large datasets.
* How to present analysis and findings in a user-friendly website.

---

## 👩‍💻 Team Members

* Sneha Joshi
* Blen Begashaw
* Lucy Wu
* Lily Ea

---

## 🌐 Links

* **Website**: [SentiShelter Live Site](https://blenwbegashaw.github.io/sentishelter/)
* **Chatbot**: [Hugging Face Space](https://huggingface.co/spaces/blenbegashaw/sentishelter-chatbots)

---

If you want, I can also make a **version with GitHub-style emojis, table of contents, and badges** to make it look super professional and organized.

Do you want me to do that next?
