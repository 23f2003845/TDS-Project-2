# Data Analysis Report

## Overview
File: datasets/goodreads.csv

## Insights
Once upon a dataset, nestled in the realm of literature, lay a treasure trove of 10,000 tomes waiting to tell their tales. Each book carried its unique identifier, from book_id to work_id, yet they were more than just numbers; they were the gateways to the stories and knowledge bound within their pages.

### **A Glimpse into the Literary Landscape**

In our dataset, the literary universe is vast and varied. It describes books with an **average rating of 4.00**, suggesting that most readers are quite pleased with their choices. However, one might argue that the **standard deviation of 0.25** reflects a certain share of controversial narratives that either rose to great acclaim or fell flat in the eyes of some critics. The highest rated tome boasts an impressive score of **4.82**, while the surprisingly low end dips down to **2.47** – a reminder that not every story resonates with every heart.

### **The Readers' Engagement**

With an astonishing total of **over 54,000 ratings**, the readers are not shy in expressing their love or disdain. Yet, their voices are not just reflected in numbers; rather, they are conveyed through a community of reviewers, with a staggering **2,919 reviews** recorded on average. The engagement reaches peaks of **155,254** reviews for the most vocal book – a crowd of opinions intertwining like the plots of a great novel.

### **Snapshots of Publications**

In scrolling through the dataset, one cannot help but notice that books published over the years hint at evolving tastes. A range of **original publication years** stretches across nearly a millennium, with the earliest works tracing back to **-1750**—a mystery begging to be unraveled, while others only just sprouted in the last decade. With a mean publication year of **1982**, it indicates a strong leaning toward contemporary narratives. Yet, **21 titles were lost to time** with undisclosed publication years – those authors’ stories remain untold, their bibliographic identities shrouded in mystery.

### **Language Diversity**

Language is a bridge to cultures and ideas, but alas, our dataset shows that **1,084 entries** are devoid of language codes. The colors of narratives portrayed are tantalizing but incomplete, hinting that the aching beauty of many tales may be lost in translation. What stories could be buried behind those missing language indicators? Stories that could highlight the great expanse of human experience across different tongues.

### **Popularity's Echoes**

While some books bask in the limelight with over **4.7 million ratings**, there are others that barely muster enough to stay afloat above the proverbial wave. The highest book count stands at **3,455**, a product of sheer popularity and demand. This bell curve of ratings illustrates how certain literary pieces shine brightly while others serve as quiet whispers in the grand library of existence.

### **An Ongoing Saga**

As we conclude this tale of numbers and narratives, it’s evident that this dataset is an archive of human emotion, intellectual pursuit, and the power of storytelling. Each figure holds within it the sparkle of many vibrant lives and experiences, urging us to turn the pages and dive deeper into the books that captivate the minds of readers around the globe.

In the end, it's not just about the books, but the stories within each book – the tales of love, loss, joy, and discovery that connect readers across time and space. So, the next time you reach for a book, remember, you aren’t just picking up a bound collection of pages—you’re embarking on an adventure steeped in history, emotion, and the boundless human spirit.

## Numeric Insights
Once upon a time in the land of books, where words danced in delight and stories flowed like rivers of wisdom, we found ourselves with a treasure trove of data from 10,000 unique book adventures. Each book was a portal to a different universe, and our numeric columns served as the compass guiding us through this vast literary landscape.

### The Heartbeat of the Library:
Among our characters, **book_id** reigned supreme, as it numbered from 1 to 10,000 and each number held the promise of a journey awaiting its reader. The average book would carry an identity nestled firmly at **5,000**, like the hero in the middle of their saga, surrounded by a plethora of options—yet only a flick away from another world.

### The Influence of Good Reads:
Our good friends—**goodreads_book_id** and **best_book_id**—shone with mean values of about **5.26 million** and **5.47 million**, respectively, suggesting that each book was not just another tale, but a part of a larger conversation amongst readers, spoken in the whispers of social engagement and collective wisdom.

### The Works of Work:
Drawing our attention further was the **work_id**, which stood tall with an average of **8.65 million**. Each work could represent multiple books, echoing the profound impact books have over generations, like the ripple of a good deed that influences even the most distant shores.

### The Count of Books:
With **books_count** averaging **75.71**, we realized the insatiable appetite readers have for more stories. As this column grew with a max of **3,455**, it beckoned the readers into deeper libraries—the more they read, the more they craved!

### The Numbers Speak: Ratings Take Center Stage
Ah, the ratings! The lifeblood of the literary world—our **ratings_1** through **ratings_5** provided a glimpse into the hearts of readers. 

1. **ratings_5**, the crowning jewel, boasted a mean of **23,789**—a testament to how many people loved certain stories enough to wrap them in five-star blankets. The highest rating hit a staggering **3,011,543**—a rave that echoed through the ages for some undisputed classic. 
   
2. Conversely, as we stepped down to **ratings_1**, we saw a mere **1,345.04** ratings—a hint that even in the world of books, not every tale captures the imagination, with the maximum plummeting to **456,191**, perhaps a reflection of tastes gone awry. 

### The Climb from Novice to Aficionado:
The spread of ratings further painted a picture. A standard deviation that oscillated widely—from **6,635.63** in ratings_1 to an impressive **79,768.89** in ratings_5—hinted at the dynamic and diverse opinions held by readers who wander into different realms of thought. Indeed, ratings shared more than numbers; they mirrored the emotional landscape and the diverse palettes of readers.

### The Interplay of Mean and Median:
When we looked at the median ratings, it became clear: while the mean painted a rosy picture of ‘average enjoyment,’ the median quietly whispered that many readers were also firmly positioned at lower levels of satisfaction. This contrast of **391 for ratings_1** and **8,836 for ratings_5** showcased the deep chasm between adoration and indifference in reader response.

### Conclusion: A Tapestry of Stories
As our analysis drew to a close, it became evident that this dataset was a rich tapestry—woven with threads of joy, disappointment, engagement, and indifference. Each book, more than a string of characters on a page, carried the weight of opinions, experiences, and emotions gathered from readers around the globe.

Thus, the library of 10,000 stood not merely as a collection of books but as a living entity, where stories transform into legends, and every rating becomes a heartbeat—a reminder that within every number lies a narrative waiting to be unveiled. And so, dear reader, the story of the numeric columns unfolds, inviting you to embark on your literary journey, with every book a new adventure and every rating a reflection of your own ever-evolving taste.

## Story
## The Chronicles of the Literary Cosmos: A Dataset Saga

In a world defined by stories, nestled deep within the glimmering constellations of data, lies a vast library of **10,000 books**, each one a vessel of imagination, waiting to transport its reader to realms unknown. This tale unfolds not merely through words, but through the dance of numbers and the whispers of literary critics, beckoning us to explore the rich narratives interwoven within our beloved books.

### **The Awakening of Dreams**

Our journey begins at the very heart of this dataset, where each **book_id** stands tall among its peers, beckoning the aspirants of literature. Picture, if you will, our average traveler in this literary realm—**Book 5,000**, resting in the eye of the storm, surrounded by an eclectic library bursting with stories. Each unique **goodreads_book_id** and **best_book_id** glow with the promise of connection; numbers soaring in the **millions**, hinting that these aren’t just numbers, but links to a global conversation vibrant with readers' whispers and shouts.

### **An Array of Reactions**

But what is a book without the essence of its readers? Lost in the enigmatic sea of critiques are **over 54,000 ratings**, each one a gossamer thread binding the reading community. Readers don’t shy away from sharing their emotions; every **rating** that finds a home is like a pebble dropped in a pond, sending ripples across the stratosphere of opinions. Immerse yourself in the enthusiasm of our average book; it has garnered **2,919 reviews**, with one particularly vocal title reaching epic proportions—**155,254 reviews** that paint an intricate portrait of affection, critique, and profound musings over a single narrative.

### **A Tapestry of Time**

As we navigate deeper into these pages, **original_publication_year** offers us a glimpse into the timelines of these literary gems; a continuum extending from the mysterious origins of **-1750** to the quickly shifting landscapes of contemporary storytellers. With a mean year snugly settled in **1982**, the dataset echoes the desires of modern audiences, yet 21 stories remain shrouded in the mists of time—silent witnesses to history, whose voices fade away into oblivion.

### **Linguistic Legacies**

The saga of languages also captivates; while the richness of storytelling thrives, **1,084 entries** dwell in silence, devoid of their language codes. These omissions hint at a loss of cultural vibrancy, urging us to contemplate what narratives have slipped through the cracks—what diverse experiences lie hidden, yearning to emerge in passionate prose or poetic verse.

### **The Dance of Popularity**

The figures come alive as we observe how some tomes bask in the limelight of popularity, while others linger in obscurity like unsung heroes. Consider, for instance, the most coveted tales, which boast a staggering **3,455 works**—each beloved story a tribute to the human spirit and its unquenchable thirst for adventure. Yet, our dataset reveals a poignant truth: while some stories captivate, ushering millions into their embrace, others lay quietly, contributing their wisdom in a more subdued manner.

### **The Joys and Sorrows of Ratings**

Ah, the ratings! The tapestry of opinions weaves itself vividly through our columns **ratings_1 to ratings_5**. The **5-star ratings** overflow with praise, averaging **23,789**—a testament to the literary magic that could sweep readers off their feet. Yet, in stark contrast, the **1-star ratings** breathe the whispers of disappointment, averaging just **1,345.04**. They remind us that in the sprawling universe of literature, not every tale captures the heart, just as not every star shines bright against the tapestry of night.

### **The Call of the Adventurer**

The heartbeats of readers thrum in the pulse of the **median and mean** ratings, revealing a world where joy and discontent intersect—a metronome of literary pursuits. While the ratings reflect happiness radiating from a beloved classic, they simultaneously illuminate the stillness surrounding an underrated paperback. The contrast becomes a poignant reminder: every book holds dualities within—joy and despair, connection and solitude.

### **Conclusion: The Ever-Continuing Expedition**

Thus, dear reader, as we navigate through this dataset, we unveil a grand narrative—one that transcends numbers and emerges as a living chronicle of human experiences. Each data point becomes not merely an isolated figure but an emblem of shared journeys, cherished moments, and the indomitable spirit of storytelling. 

This collection of **10,000** books stands not simply as an archive but an odyssey, reminding us that every title is an invitation to explore, and every rating is a heartbeat of connection. The literary cosmos, forever expanding and captivating the hearts and minds of those brave enough to turn the page, calls out, beckoning you to embark on your adventure—a sacred journey awaiting your discovery in the infinite expanse of books.
## Outliers Analysis
![Image](./outliers_bloxplot.png)
From the provided boxplot, you can infer several things about the dataset and its outliers:

1. **Identification of Outliers**: The plot indicates that there are several outliers in the dataset, specifically for variables like `isbn13`, which has extreme values significantly higher than the rest. This suggests there could be issues with data entry or that some values represent rare cases.

2. **Data Distribution**: The boxplot shows the interquartile range (IQR) and the median for each variable. Variables such as `original_publication_year`, `average_rating`, and others are likely to have a more normal distribution without extreme outliers.

3. **Potential Data Quality Issues**: The presence of extreme values, especially in variables like `isbn13`, might warrant further investigation to ensure data validity and consistency.

4. **Comparison Across Variables**: By comparing the length of the boxes (IQR) and the position of the median line within the boxes, you can assess which variables have higher variability and potentially skewed distributions.

5. **Quartile Insights**: The lengths of the boxes can provide insight into the spread of the central 50% of the data in each variable, giving an idea about consistency or variability across different attributes.

Overall, while the boxplot provides a clear visual representation of potential outliers, further analysis may be necessary to understand their impact on the dataset and the overall implications for your analysis.
## Correlation Matrix Analysis
![Image](./correlation_matrix_heatmap.png)
From the correlation matrix heatmap you provided, several inferences can be drawn:

1. **High Positive Correlation**:
   - The variable `work_id` and `book_id` have a strong correlation of 0.993. This suggests that they are highly related, which may indicate that they refer to the same or very similar entities in the dataset.
   - The `work_ratings_count` exhibits a high positive correlation with `ratings_1`, `ratings_2`, and `ratings_3`. This suggests that as the number of ratings increases, the counts in these categories also increase.

2. **Moderate Positive Correlation**:
   - The variables `original_publication_year` and `average_rating` show a moderate positive correlation (0.590), implying that newer books tend to have slightly higher average ratings.
   - `average_rating` is also positively correlated with `work_ratings_count` (0.731) indicating that books with more ratings tend to have higher average ratings.

3. **Negative Correlation**:
   - There is a noticeable negative correlation between `ratings_1` and some of the other rating categories, suggesting that as one rating category increases, another tends to decrease.

4. **No or Low Correlation**:
   - Some variables might show low correlations, which implies that they are relatively independent of each other in terms of the relationships represented in this dataset.

5. **General Observations**:
   - High correlations might suggest redundancy among certain variables, meaning they may convey similar information.
   - The absence of strong negatives indicates that there's a general trend of positive relationships among the ratings and book-related metrics.

This heatmap serves as a useful tool for identifying potential dependencies and relationships among various features in your dataset, which can inform further analysis or modeling efforts.
## Custom LLM Plot![Image](./custom_llm_plot.png)
## Summary Statistics
{'row_count': 10000, 'column_count': 23, 'columns': {'book_id': dtype('int64'), 'goodreads_book_id': dtype('int64'), 'best_book_id': dtype('int64'), 'work_id': dtype('int64'), 'books_count': dtype('int64'), 'isbn': dtype('O'), 'isbn13': dtype('float64'), 'authors': dtype('O'), 'original_publication_year': dtype('float64'), 'original_title': dtype('O'), 'title': dtype('O'), 'language_code': dtype('O'), 'average_rating': dtype('float64'), 'ratings_count': dtype('int64'), 'work_ratings_count': dtype('int64'), 'work_text_reviews_count': dtype('int64'), 'ratings_1': dtype('int64'), 'ratings_2': dtype('int64'), 'ratings_3': dtype('int64'), 'ratings_4': dtype('int64'), 'ratings_5': dtype('int64'), 'image_url': dtype('O'), 'small_image_url': dtype('O')}, 'missing_values': {'book_id': 0, 'goodreads_book_id': 0, 'best_book_id': 0, 'work_id': 0, 'books_count': 0, 'isbn': 700, 'isbn13': 585, 'authors': 0, 'original_publication_year': 21, 'original_title': 585, 'title': 0, 'language_code': 1084, 'average_rating': 0, 'ratings_count': 0, 'work_ratings_count': 0, 'work_text_reviews_count': 0, 'ratings_1': 0, 'ratings_2': 0, 'ratings_3': 0, 'ratings_4': 0, 'ratings_5': 0, 'image_url': 0, 'small_image_url': 0}, 'descriptive_summary':                                            mean                  std          min              25%              50%              75%              max
book_id                                  5000.5           2886.89568          1.0          2500.75           5000.5          7500.25          10000.0
goodreads_book_id                  5264696.5132        7575461.86359          1.0         46275.75         394965.5       9382225.25       33288638.0
best_book_id                       5471213.5801        7827329.89072          1.0         47911.75         425123.5        9636112.5       35534230.0
work_id                            8646183.4246       11751060.82408         87.0        1008841.0        2719524.5      14517748.25       56399597.0
books_count                             75.7127           170.470728          1.0             23.0             40.0             67.0           3455.0
isbn                                        NaN                  NaN          NaN              NaN              NaN              NaN              NaN
isbn13                     9755044298883.462891  442861920665.573364  195170342.0  9780316192995.0  9780451528640.0  9780830777175.0  9790007672390.0
authors                                     NaN                  NaN          NaN              NaN              NaN              NaN              NaN
original_publication_year           1981.987674           152.576665      -1750.0           1990.0           2004.0           2011.0           2017.0
original_title                              NaN                  NaN          NaN              NaN              NaN              NaN              NaN
title                                       NaN                  NaN          NaN              NaN              NaN              NaN              NaN
language_code                               NaN                  NaN          NaN              NaN              NaN              NaN              NaN
average_rating                         4.002191             0.254427         2.47             3.85             4.02             4.18             4.82
ratings_count                        54001.2351        157369.956436       2716.0         13568.75          21155.5          41053.5        4780653.0
work_ratings_count                   59687.3216        167803.785237       5510.0         15438.75          23832.5          45915.0        4942365.0
work_text_reviews_count               2919.9553          6124.378132          3.0            694.0           1402.0          2744.25         155254.0
ratings_1                             1345.0406          6635.626263         11.0            196.0            391.0            885.0         456191.0
ratings_2                              3110.885          9717.123578         30.0            656.0           1163.0          2353.25         436802.0
ratings_3                            11475.8938         28546.449183        323.0           3112.0           4894.0           9287.0         793319.0
ratings_4                            19965.6966         51447.358384        750.0          5405.75           8269.5          16023.5        1481305.0
ratings_5                            23789.8056         79768.885611        754.0           5334.0           8836.0          17304.5        3011543.0
image_url                                   NaN                  NaN          NaN              NaN              NaN              NaN              NaN
small_image_url                             NaN                  NaN          NaN              NaN              NaN              NaN              NaN}

## Missing Values
book_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0
dtype: int64

