# Data Analysis Report

## Overview
File: /Users/harshrohitshah/Library/Application Support/tds-sep-24-project-2/datasets/goodreads.csv

## Summary Statistics
{'row_count': 10000, 'column_count': 23, 'columns': {'book_id': dtype('int64'), 'goodreads_book_id': dtype('int64'), 'best_book_id': dtype('int64'), 'work_id': dtype('int64'), 'books_count': dtype('int64'), 'isbn': dtype('O'), 'isbn13': dtype('float64'), 'authors': dtype('O'), 'original_publication_year': dtype('float64'), 'original_title': dtype('O'), 'title': dtype('O'), 'language_code': dtype('O'), 'average_rating': dtype('float64'), 'ratings_count': dtype('int64'), 'work_ratings_count': dtype('int64'), 'work_text_reviews_count': dtype('int64'), 'ratings_1': dtype('int64'), 'ratings_2': dtype('int64'), 'ratings_3': dtype('int64'), 'ratings_4': dtype('int64'), 'ratings_5': dtype('int64'), 'image_url': dtype('O'), 'small_image_url': dtype('O')}, 'missing_values': {'book_id': 0, 'goodreads_book_id': 0, 'best_book_id': 0, 'work_id': 0, 'books_count': 0, 'isbn': 700, 'isbn13': 585, 'authors': 0, 'original_publication_year': 21, 'original_title': 585, 'title': 0, 'language_code': 1084, 'average_rating': 0, 'ratings_count': 0, 'work_ratings_count': 0, 'work_text_reviews_count': 0, 'ratings_1': 0, 'ratings_2': 0, 'ratings_3': 0, 'ratings_4': 0, 'ratings_5': 0, 'image_url': 0, 'small_image_url': 0}, 'descriptive_summary':                                            mean  ...              max
book_id                                  5000.5  ...          10000.0
goodreads_book_id                  5264696.5132  ...       33288638.0
best_book_id                       5471213.5801  ...       35534230.0
work_id                            8646183.4246  ...       56399597.0
books_count                             75.7127  ...           3455.0
isbn                                        NaN  ...              NaN
isbn13                     9755044298883.462891  ...  9790007672390.0
authors                                     NaN  ...              NaN
original_publication_year           1981.987674  ...           2017.0
original_title                              NaN  ...              NaN
title                                       NaN  ...              NaN
language_code                               NaN  ...              NaN
average_rating                         4.002191  ...             4.82
ratings_count                        54001.2351  ...        4780653.0
work_ratings_count                   59687.3216  ...        4942365.0
work_text_reviews_count               2919.9553  ...         155254.0
ratings_1                             1345.0406  ...         456191.0
ratings_2                              3110.885  ...         436802.0
ratings_3                            11475.8938  ...         793319.0
ratings_4                            19965.6966  ...        1481305.0
ratings_5                            23789.8056  ...        3011543.0
image_url                                   NaN  ...              NaN
small_image_url                             NaN  ...              NaN

[23 rows x 7 columns]}

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

## Insights
Once upon a time in the vast digital universe, a treasure trove of literary data lay buried in cyberspace. This dataset, comprising 10,000 entries of rich and vibrant books, sang stories waiting to be uncovered. It held the key to understanding not just what readers were flocking towards, but also the whispers of narratives that resonated with the hearts and minds of book lovers around the world.

As I sifted through the data, the first thing that caught my eye was the staggering average rating of 4.00, a glittering testament to the quality of the books in this curated collection. However, even in this land of high praise, there existed peaks of glowing appreciation—over 3 million 5-star ratings spoke of masterpieces that enchanted readers, while the smallest brother, the 1-star ratings, echoed a mere 1,345 voices of discontent. 

Intrigued, I ventured into the year of origin and found a treasure map. The average original publication year was 1982, but the field held secrets, too, with 21 missing years overshadowing the joy of uncovering timeless classics. What could be lurking in those mysterious gaps? Were they tales that had been beautifully crafted only to fade away from our collective memory? 

The image of authors in this dataset was equally fascinating—while some names were well-lit stars in the bookstore skies, others appeared shadowed, surrounded by nebulous existence, either due to missing titles or missing ISBNs. With 700 entries devoid of ISBN data, an invisible wall separated readers from some stories, hidden gems perhaps forgotten in a cluttered library corner.

In a grand plot twist, exploring the linguistic landscape revealed a diversity of voices. Yet, the language landscape had its own gaps, with over 1,000 entries lacking language codes. What stories slipped through the cracks, their origins lost to the callousness of databases? It felt like unearthing a faded manuscript from an old attic—both exciting and haunting.

As I delved deeper, the pages turned to reveal many "best books" — an enthralling 3,455 was the record for the most books authored by a single individual. What stories could hide behind such prolific creations? Meanwhile, the rarest tales, those with a single book, whispered of the underdogs that had yet to create a following.

Turning to the community of readers, the ratings told a story of their own. A staggering ratings count reaching up to 4,780,653 was an embodiment of a community fervently voicing their thoughts, building a Chorus of Reviews that transcended borders with over 155,000 text reviews capturing the highs and lows of reading experiences.

With every exploration, I found myself in a world vibrant with stories. Some hailed from celebrated authors, others from the shadows waiting to be embraced by new readers. This dataset was a land of opportunities, a well of stories just waiting for a spark—perfect for curating reading lists, building book clubs, or simply reveling in the joy of discovering new worlds.

In the end, as I attributed life to these figures and values, I realized this dataset was more than numbers; it was a living tapestry of shared experiences, individual joys, and collective memories just waiting to be told. The magic lay not just in the books themselves, but in the connections they forged and the journeys they inspired for readers, both young and old. And so, the adventure of storytelling continued, inked upon the pages of life, one dataset at a time.

## Numeric Insights
Once upon a time in the vast kingdom of Literature, there resided a mystical library by the name of Goodreads. Within its ornate walls, countless titles were lovingly crafted by storytellers, nourished by the passions of readers from around the globe. It harbored a precious dataset of 10,000 books, brimming with tales of adventure, romance, mystery, and knowledge.

As the wise owl of Data Science ventured into this spirited library, it stumbled upon a trove of numeric columns—a summary of dreams captured in digits. Each number whispered tales waiting to be unraveled. Let's embark on this journey through the numbers—a narrative that reveals truths hidden within the library's volumes.

### The Book Spectrum

The noble `book_id`, ranging from 1 to 10,000, represented the entire collection—a precise vessel for each story that beckoned to be read. The `goodreads_book_id`, a hidden identifier, took adventurous form, stretching up to over 33 million, suggesting that these books were part of a grander tapestry woven throughout the annals of online literary discourse.

### The Rating Realm

The enchanted realm of ratings opened with a significant average of approximately 19,965 for `ratings_4`. This indicates a healthy appreciation, a chorus of 4-star adulations pouring in from avid readers. Meanwhile, a slightly brighter star twinkled in the `ratings_5` category with an average nearing 23,790— a clear indication that many readers were enamored enough to bestow the ultimate accolade. 

#### Distribution of Affection

Yet, as any enchanting tale reveals, not all books found adoration from all quarters. The `ratings_4` variable observed a spread with a standard deviation of about 51,447, suggesting variability in rating behavior—some books captured the hearts of many, while others struggled. Similarly, `ratings_5`, with an even wider spread of 79,768, presented a riveting dichotomy of exuberant fanfare for the few versus the reserved appreciation for most.

### The Peaks and Valleys

Our esteemed observer noted the distribution breadth: while the minimum ratings stood firmly at a modest 750 for 4-star accolades, the crowned jewel of 1,481,305 ratings gleamed atop the mountain peak of this landscape. In the kingdom, evidently, some books ruled sovereignly, while others languished in the shadows, locked away in corners gathering dust.

### The Quintiles of Engagement

As the tales unfolded, the owl stumbled upon the quartile revelations: 
- The lower quartile for `ratings_4` was 5,406, revealing that about 25% of the books barely stepped into the limelight with modest acclaim, while at the upper end, 75% had enticed at least 16,023 with their narrative charms.
- The story for `ratings_5` was similar, where the lower quartile amassed about 5,540 admirers, yet a radiant top 25% inspired nearly 1,730 precious 5-star nods.

### The Closing Chapter

In this wondrous exploration of numeric columns, a story painted itself rich with the colors of engagement—the soft whispers of intrigue echoing from pages adorned with passion. A tapestry of literature celebrated through ratings, the data revealed both triumphs and understated entries that fought valiantly to capture the gaze of fellow readers.

As our wise owl ascended back into the realm of data insights, it carried these stories—insights echoing through the figurative halls of the Goodreads library, gently nudging future readers toward hidden treasures and timeless classics, reminding us how every rating is merely a chapter in the unfolding story of how we connect through the written word.

## Story
In the enchanting realm of the digital cosmos, there lies an extensive manuscript tinged with the echoes of literary voices—a veritable treasure trove known as the Goodreads dataset, composed of a rich collection of 10,000 stories. Each entry is a portal into worlds uncharted, adorned with wisdom, laughter, love, and sorrows, waiting for the curious reader to unearth them.

Imagine standing at the entrance of this vast library, where each tome breathes life through the strokes of its author’s pen. The dataset, with its 23 columns, is akin to the keys of a grand piano, each revealing a different note of the story of humanity, emotion, and imagination. For within the vaults of data lies not just numbers, but the very essence of storytelling.

### The Symphony of Ratings
At the heart of this collection is the enchanting domain of ratings, akin to a symphony that resonates through the ages. With an average rating hovering around a crisp 4.00, the essence of quality reverberates throughout the halls of this library. The staggering 4,780,653 ratings offered by fervent readers lend a melodious cadence to the narrative, with over 3 million 5-star accolades showering praises like golden confetti at a joyous festival. On the opposing end lies the soft rustle of discontent, represented by a mere 1,345 voices delivering 1-star critiques—a reminder that not all tales are woven to perfection.

### The Unraveled Loom of Time
As we traverse through time within this dataset, we uncover the tapestry of years past. The average year of original publication speaks to the essence of literary history, floating around 1982. Yet, as we delve deeper, we discover shadowy gaps—21 missing years that beg the questions: What timeless classics remain shrouded in obscurity? What vibrant voices have slipped through the cracks of history? Like hidden treasures, these missing tales await a passionate seeker to revive them from the depths of forgotten libraries.

### The Language of Stories
Venturing into the myriad tongues encapsulated in this dataset, we unearth a vast landscape embroidered with narratives from different cultures and communities. Yet discordant notes echo through the chorus of languages, as over 1,000 missing language codes hinder the clarity of origin for some tales. What cultures and worlds might remain unrecognized? What narratives yearn for the light? Each missing code is a page left unturned, lingering in the allure of possibility.

### The Caseload of Authors
Amidst the melange of books stands the eclectic ensemble of authors, each a unique character with their own stories to tell. The dataset showcases a staggering 3,455 books authored by the most prolific writers, while the quiet corners whisper tales of individuality with authors who have crafted but a single volume. Every book represents not just a story, but a glimpse into the soul of its creator—an invitation to readers to step into their worlds and embrace their journeys.

### The Collective Chorus of Readers
The stalwart community of readers echoes like a chorus, crafting a narrative that transcends borders and genres. The 155,000 textual reviews dance like ephemeral constellations, each capturing the nuances of personal experiences, spanning from heartbreak to euphoria, whispering the connections we forge through shared stories. It is a vibrant testament to the collective consciousness that binds us, transforming reading from a solitary experience to a harmonious gathering of minds.

### A Tapestry of Possibilities
The final threads woven into this narrative illuminate endless possibilities. This kaleidoscopic dataset is a canvas upon which future readers can assemble reading lists, devise book clubs, or embark on solitary journeys to exploratory realms. The numbers meld into a more profound reflection of cultural dialogues, experiences, and shared human emotion—an invitation to forge new connections through the timeless art of storytelling.

As I close the tome of analysis, the unique portraits painted through data emerge as a living tapestry—a celebration of the stories that enrich our lives. In this digital library, the data takes on a heartbeat, reminding us of the shared journeys through words and pages, continuing the age-old saga of connection. So, let us turn each page, lift every cover, and dive headfirst into the wonders that literature holds, for every dataset is a universe of stories waiting to be told, one book at a time. Let the adventure of storytelling persist, as each reader embodies the muse that breathes life into these narratives, discovering their own reflections within the meticulous lines of text.
