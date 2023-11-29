import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = r'C:\Users\msthu\PycharmProjects\pythonProject1\semester5\datascience\data\reviewsfile.csv'
df = pd.read_csv(file_path)

# Extract the numerical part from "Review Rating" column
df['Review Rating'] = df['Review Rating'].str.extract('(\d+)').astype(float)

# Function to categorize reviews as positive or negative based on the "Review Rating"
def categorize_review(row):
    if pd.notna(row['Review Rating']):
        if row['Review Rating'] < 6:
            return 'Negative'
        else:
            return 'Positive'
    else:
        return 'Unknown'

# Create a new column "Sentiment" based on the categorization function
df['Sentiment'] = df.apply(categorize_review, axis=1)

# Plot the number of positive and negative reviews
sentiment_counts = df['Sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['red', 'green'])
plt.title('Number of Positive and Negative Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Save the modified DataFrame to a new CSV file
df.to_csv(r'C:\Users\msthu\PycharmProjects\pythonProject1\semester5\datascience\data\modified_reviewsfile.csv', index=False)