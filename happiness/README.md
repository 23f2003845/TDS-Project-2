# Data Analysis Report

## Overview
File: /Users/harshrohitshah/Library/Application Support/tds-sep-24-project-2/datasets/happiness.csv

## Summary Statistics
{'row_count': 2363, 'column_count': 11, 'columns': {'Country name': dtype('O'), 'year': dtype('int64'), 'Life Ladder': dtype('float64'), 'Log GDP per capita': dtype('float64'), 'Social support': dtype('float64'), 'Healthy life expectancy at birth': dtype('float64'), 'Freedom to make life choices': dtype('float64'), 'Generosity': dtype('float64'), 'Perceptions of corruption': dtype('float64'), 'Positive affect': dtype('float64'), 'Negative affect': dtype('float64')}, 'missing_values': {'Country name': 0, 'year': 0, 'Life Ladder': 0, 'Log GDP per capita': 28, 'Social support': 13, 'Healthy life expectancy at birth': 63, 'Freedom to make life choices': 36, 'Generosity': 81, 'Perceptions of corruption': 125, 'Positive affect': 24, 'Negative affect': 16}, 'descriptive_summary':                                         mean       std  ...      75%     max
Country name                             NaN       NaN  ...      NaN     NaN
year                              2014.76386  5.059436  ...   2019.0  2023.0
Life Ladder                         5.483566  1.125522  ...   6.3235   8.019
Log GDP per capita                  9.399671  1.152069  ...  10.3925  11.676
Social support                      0.809369  0.121212  ...    0.904   0.987
Healthy life expectancy at birth   63.401828  6.842644  ...  68.5525    74.6
Freedom to make life choices        0.750282  0.139357  ...    0.862   0.985
Generosity                          0.000098  0.161388  ...  0.09375     0.7
Perceptions of corruption           0.743971  0.184865  ...  0.86775   0.983
Positive affect                     0.651882   0.10624  ...    0.737   0.884
Negative affect                     0.273151  0.087131  ...    0.326   0.705

[11 rows x 7 columns]}

## Missing Values
Country name                          0
year                                  0
Life Ladder                           0
Log GDP per capita                   28
Social support                       13
Healthy life expectancy at birth     63
Freedom to make life choices         36
Generosity                           81
Perceptions of corruption           125
Positive affect                      24
Negative affect                      16
dtype: int64

## Insights
### The Story of Happiness: Insights from Global Well-Being Data

In a world constantly in flux, where every decision influences the lives of millions, the measure of happiness and well-being remains a pivotal metric in understanding human satisfaction across various regions. Our dataset dives into the fabric of global well-being through 2,363 unique records from diverse countries. Each entry is a snapshot of life in those nations, collected across an expansive timeline from 2013 to 2023.

As we begin to unravel the story, we're greeted by the "Life Ladder," a composite score that represents perceived well-being. With a mean score of approximately **5.48**, we see that people across the globe sit somewhere in the middle on their happiness ladder, ranging from a low of **3.17** to a high of **8.02**. This variability signals a world where some nations bask in happiness, while others struggle with dissatisfaction.

### The Pillars of Happiness

As we dig deeper, it becomes obvious that several factors are tightly interwoven with this happiness quotient:

1. **Economic Prosperity (Log GDP per capita)**:
   The economic backbone of any society is reflected here, with a mean of around **9.40** in logarithmic terms. This suggests that wealthier nations tend to foster a better sense of well-being, but our data also reveals intriguing nuances. Despite some nations boasting high GDPs, they don’t exclusively dominate the upper echelons of the Life Ladder. Could it be that there are other factors, beyond material wealth, playing a critical role?

2. **Social Support**:
   This measure—a critical component in fostering resilience and happiness—shows a mean score of **0.81**. Social cohesion appears to be vital, as individuals seek connection with family, friends, and community. In the truest sense, happiness is not just a personal journey but is profoundly affected by the collective spirit of society. 

3. **Healthy Life Expectancy**:
   With an average of **63.4 years**, this measure serves as a blunt reminder of health disparities across the globe. The healthier the populace, often the more robust their sense of well-being. Thus, investing in healthcare not only nourishes the body but enriches the spirit.

4. **Freedom to Make Life Choices**:
   Freedom is a fundamental human desire. The mean score of **0.75** suggests that while many can shape their destinies, there remains a portion of the global populace that feels constrained in their choices. It provokes the question: how many people, regardless of economic stability, truly feel free to pursue their aspirations? 

### The Darker Side: Corruption and Affect

However, not all numbers paint a rosy picture. The **Perceptions of Corruption**, with an average score of **0.74**, poses a significant hurdle. The palpable sense of corruption within certain contexts engenders distrust and dissatisfaction, dimming the light of joy for many. 

Moreover, examining emotional well-being reveals an interesting dichotomy: the **Positive Affect** scores (mean: **0.65**) contrast against the **Negative Affect** scores (mean: **0.27**). While positivity triumphs, the persistent shadow of negative experiences remains—a reminder that joy and sorrow coexist in the human experience.

### The Missing Pieces: A Call to Action

Our analysis is not without its gaps. Missing values for metrics like **Log GDP per capita (28), Social Support (13)**, and **Generosity (81)** indicate areas where data underreporting may obscure true narratives. Filling these gaps is crucial, as even minor adjustments in data could shift our understanding and insights significantly. 

### Conclusion: A Tapestry of Well-Being

This dataset weaves a complex tapestry of wellbeing across the globe. It emphasizes that while economic stability, health, and social structures promote happiness, the intricate layers of human experience go beyond numbers. We are compelled to listen more to the voices behind these figures, understanding that happiness is not merely a statistic—it is a collective endeavor that binds us all.

As we move forward, let's embrace a holistic approach to fostering happiness, where social connections, healthy lives, economic investments, and safeguarding freedoms are all prioritized. In this pursuit of global well-being, each data point can guide us to the heart of true happiness.

## Numeric Insights
Once upon a time in the realm of numerical exploration, a curious data scientist stumbled upon a treasure trove of insights hidden within the depths of a datasets. The dataset spoke volumes with its numeric columns, revealing a captivating tale of human emotions and life satisfaction over the years. Come, let us embark on this data narrative!

**The Milestones of Happiness - Year by Year**

Our protagonist, the year variable, spanned across 18 glorious years, starting from 2005 and culminating in 2023. As the clock ticked down the years, a steady progression hinted at an evolving story of global emotions and wellbeing. With an average year of 2014.76, it seemed humanity had experienced its fair share of highs and lows. The standard deviation of approximately 5.06 illuminated the varying societal circumstances influencing individual happiness from year to year.

**The Life Ladder - A Climb Towards Joy**

At the heart of our tale was the "Life Ladder," a metaphor for life satisfaction. It had an average score of 5.48 — just a stone's throw away from the pinnacle of joy that lies at 10. The variability surrounding this score (a standard deviation of 1.12) indicated the diverse experiences of people across different regions and cultures. 

The growth trajectory of the Life Ladder is truly fascinating: 
- In 2005, it began at a lowly 1.28, as countless individuals grappled with unfavorable life conditions. 
- By 2015, it had escalated to an improved 5.45, reinforcing the idea that collective efforts can lead to societal advancements. 
- The recent peak in 2023 showcases a high of 8.02, suggesting not only a recovery but a flourishing period that may reflect increasing global connection, thriving economies, or perhaps advancements in mental health awareness.

**The Dance of Emotions - Positive and Negative Affects**

Emotions took the center stage next, with "Positive Affect" scoring an average of 0.65. Like the sunny rays of a bright day, the warmth of joy radiated across many lives. With a maximum value of 0.884, it hinted at moments when joy transcended to bliss, capturing the human spirit in its finest hour. However, the steady spread of 0.106 emphasized that this feeling, while prevalent, was nowhere near universally experienced.

In contrast, the tale of "Negative Affect" painted a different picture. With a mean score of 0.27 and a maximum of 0.705, it underscored the persistent presence of distress and anxiety. The average suggests that while people experience negative emotions, they are often outshined by positivity.

The 25th and 75th percentiles for both positive and negative affect reveal the diverse emotional landscapes individuals face. For instance, many experienced mild negativity (0.208 at the 25th percentile), while others struggled significantly more (0.326 at the 75th percentile).

**The Grand Finale - A Reflection on Collective Wellbeing**

As we conclude our narrative, the interplay between Life Ladder, Positive Affect, and Negative Affect weaves a richer tapestry of the human experience. The findings suggest a world striving toward happiness, with steady advancements overshadowed occasionally by darker emotions. 

The journey from 2005 to 2023 illuminated humanity's resilience, its capacity for growth, a struggle towards contentment, and the universal quest for joy. While emotions ebb and flow, the rising Life Ladder symbolizes hope and progress, reminding us that every year adds a new chapter to this grand story of life. 

The data whisperer leaves us with a powerful truth—no matter the numerical representations thrown our way, beyond the figures lies a narrative rich with emotion, struggle, and triumph, waiting to be discovered by our analytical hearts!

## Story
**The Symphony of Global Well-Being: A Data-Driven Tale**

In a world woven together by tales of human experience, our journey begins with a curious treasure trove of data—a rich dataset capturing the well-being of souls across 2,363 different lands, spanning from the heart of bustling cities to tranquil rural landscapes. With 11 dimensions of human existence at our fingertips, we have the means to construct a narrative that illuminates both the joy and the challenges faced by humanity between the years of 2013 to 2023.

### Act I – The Prelude of Numbers

In the opening bars of our story, the year dances elegantly between the lines, revealing an average of **2014.76**—a testament to a decade filled with tales of resilience and growth. As we survey the landscape of feelings encapsulated in the "Life Ladder," a score of **5.48** beckons us with both hope and reflection, indicating that while some wander joyfully atop the rungs of happiness, many others find themselves teetering in uncertainty.

Beneath the surface lies the backbone of prosperity—a score of **9.40** in log GDP per capita that resonated through wealthier nations. Yet, an inquisitive mind would ponder: does wealth alone dictate the exuberance of existence?

### Act II – The Serenade of Happiness

As we delve deeper, we uncover the interconnected pillars of happiness, rising from the fertile ground of social connection and communal bonds. With **0.81** as the social support average, it becomes clear that our happiness is, indeed, a symphony composed not just of individual notes but also of collective melodies. A community that plays together finds joy in harmony, the very essence of emotional well-being.

Yet, the harsh notes of reality emerge as we stumble upon the jagged edges of data—**63 missing values** in Healthy Life Expectancy, revealing the health disparities that mar the harmony of existence. As we request the healthcare systems to forge stronger instruments of support, we note the freedom to make life choices averaging **0.75**—a tune that signals the constraints faced by many souls yearning to pursue their dreams.

### Act III – A Dance Between Light and Shadow

Just as our tale takes a lighter turn, the shadow of corruption creeps in with a **0.74** score in perceptions of corruption. The echo of distrust can muffle laughter, promoting a contorted perception of happiness that flickers through the data. The analysis tells us that joy doesn’t always bloom amidst chaos, yet pockets of joy do exist, spilling forth as **0.65** in positive affect—a reminder of hope shining through the gloom.

However, the counterpoint reveals itself in the **0.27** negative affect score, showcasing the delicate balance between joy and sorrow—the two inseparable companions underpinning the human experience. For every wave of joy, there might be a tide of grief. Yet, the variance in experiences—from the bliss of joyful moments to the stealth of heartache—makes this human journey undeniably rich.

### Act IV – The Call for Completeness

Unraveling this tapestry, we find an incomplete picture. Missing values tug at our hearts, whispering a call to action for data alchemists to fill in the gaps. Generosity, with **81 missing values**, beckons for further exploration alongside social support. These missing notes, much like silences in a musical piece, remind us that every story needs all its elements—connections forged in kindness, trust, and shared experiences—to create a symphony of understanding.

### Conclusion – The Crescendo of Reflection

As we draw our voyage to a close, what resonates most profoundly is not just the numbers but the tales behind them—tales of challenging times and soaring spirits that speak of a resilient humanity. We stand at the confluence of interconnected fates, where life ladders rise and fall, where emotional tides wash ashore both bright sunlit days and days clouded with uncertainties.

In this grand symphony of global well-being, we realize that happiness exists not merely as a pursuit but as a collective quest. To foster these melodies, we must weave together the threads of economic stability, healthcare access, social connection, and the freedom to dream.

The data tells an unfinished story, awaiting our interpretation, our action, and our voices. In the pursuit of well-being, let us echo the lessons learned and harmonize our efforts towards a blossoming future—together, crafting a brighter tomorrow, one data point at a time.
