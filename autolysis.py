# /// script
# dependencies = [
#   "requests",
#   "matplotlib",
#   "seaborn",
#   "pandas"
# ]
# ///
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys


outputDir = os.path.dirname(os.path.abspath(__file__))


# Utility function to talk to llm
def question_llm(question, context=""):
    auth_token = os.environ["AIPROXY_TOKEN"]
    res = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a well experienced data scientist and analyst. You have been provided some data and you need to narrate a story from it. Go ahead and make it creative",
                },
                {"role": "user", "content": f"{question}. \n Context: f{context}"},
            ],
        },
    )

    result = res.json()

    print(result)
    return result["choices"][0]["message"]["content"] if "error" not in result else None


# Utility function to open file.
def open_file(file_path):
    df = pd.read_csv(file_path)
    return df


# Utitlity function to save visualisations
def save_visualisation(visualisation, filename):
    try:
        visualisation.tight_layout()
        visualisation.savefig(os.path.join(outputDir, filename), bbox_inches="tight")
        visualisation.close()
    except Exception as e:
        print("An error occured while saving visualisation", e)


# Function to summarize dataset
def summarize(dataset):
    # Describing dataset
    descriptive_summary = dataset.describe(include="all").transpose()

    summary = {
        "row_count": len(dataset),
        "column_count": len(dataset.columns),
        "columns": dataset.dtypes.to_dict(),
        "missing_values": dataset.isnull().sum().to_dict(),
        "descriptive_summary": descriptive_summary[
            ["mean", "std", "min", "25%", "50%", "75%", "max"]
        ]
        if not descriptive_summary.empty
        else None,
    }

    return summary


# Function to find correlation matrix and plot it
def visualise_correlation(dataset):
    filtered_numeric_dataset = dataset.select_dtypes(include=["number"])
    if filtered_numeric_dataset.empty:
        print("No numeric columns found")
        return None

    correlation_matrix = filtered_numeric_dataset.corr()

    # Printing correlation matrix
    print("Correlation Matrix")
    print(correlation_matrix)

    # Plotting the figure
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        correlation_matrix, annot=True, cmap="coolwarm", fmt=".3f", linewidth=0.8
    )
    plt.title("Correlation Matrix Heatmap")
    save_visualisation(plt, "correlation_matrix_heatmap.png")
    print("Saved correlation matrix heatmap")

    return correlation_matrix


# Function to visualise outliers
def visualise_outliers(dataset):
    filtered_numeric_dataset = dataset.select_dtypes(include=["number"])
    if filtered_numeric_dataset.empty:
        print("No numeric columns found")
        return None

    # Plotting the figure
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=filtered_numeric_dataset)
    plt.title("Outliers Boxplot")

    plt.xticks(rotation=90)  # Changing orientation of the x-axis labels

    save_visualisation(plt, "outliers_boxplot.png")
    print("Saved Outlier Boxplot heatmap")


# Function to visualise time series data
def visualise_time_series(dataset):
    if "Date" in dataset.columns:
        try:
            dataset["Date"] = pd.to_datetime(dataset["Date"])
            dataset = dataset.sort_values("Date")
            numeric_columns = dataset.select_dtypes(include=["number"]).columns
            if numeric_columns.empty:
                print("No numeric columns for time series analysis.")
                return
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=dataset, x="Date", y=numeric_columns[0])
            plt.title(f"Time Series Analysis for {numeric_columns[0]}")
            save_visualisation(plt, "time_series.png")
        except Exception as e:
            print(f"Error in Time Series Analysis: {e}")
    else:
        print("Date column not found for time series analysis.")


# Function to visualise geographic data
def visualise_geographic_analysis(dataset):
    if "Latitude" in dataset.columns and "Longitude" in dataset.columns:
        plt.figure(figsize=(10, 8))
        sns.scatterplot(
            data=dataset,
            x="Longitude",
            y="Latitude",
            hue=dataset.select_dtypes(include=["number"]).columns[0],
        )
        plt.title("Geographic Analysis")
        save_visualisation(plt, "geographic_analysis.png")
    else:
        print("Latitude and Longitude columns are missing.")


# Function to visualise categorical data
def visualise_categorical_data(dataset):
    non_numeric_df = dataset.select_dtypes(exclude=["number"])
    for col in non_numeric_df.columns:
        # Count the unique values in the column
        value_counts = dataset[col].value_counts()
        num_unique_values = len(value_counts)

        def adjust_labels(ax, labels, max_chars_per_line=10, rotate=False):
            """
            Helper function to adjust labels by splitting long ones into multiple lines
            and optionally rotating them.
            """
            new_labels = []
            for label in labels:
                split_label = "\n".join(
                    [
                        label[i : i + max_chars_per_line]
                        for i in range(0, len(label), max_chars_per_line)
                    ]
                )
                new_labels.append(split_label)
            ax.set_xticks(range(len(new_labels)))
            ax.set_xticklabels(
                new_labels,
                rotation=90 if rotate else 0,
                ha="center" if rotate else "right",
            )

        if num_unique_values <= 15:
            # Case 1: Bars <= 15, enhance readability
            plt.figure(figsize=(12, 8))
            ax = sns.countplot(x=col, data=dataset, order=value_counts.index)
            plt.title(f"Distribution of {col}")
            adjust_labels(ax, value_counts.index, max_chars_per_line=10, rotate=False)
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.subplots_adjust(bottom=0.25)
            save_visualisation(plt, f"{col}_distribution.png")

        elif 15 < num_unique_values <= 30:
            # Case 2: 15 < bars <=30, enhance readability
            plt.figure(figsize=(12, 8))
            ax = sns.countplot(x=col, data=dataset, order=value_counts.index)
            plt.title(f"Distribution of {col}")
            adjust_labels(ax, value_counts.index, max_chars_per_line=15, rotate=True)
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.subplots_adjust(bottom=0.35)
            save_visualisation(plt, f"{col}_distribution.png")

        else:
            # Case 3: Bars > 30, two graphs (top 15 and bottom 15 value-wise)
            top_15 = value_counts.head(15)
            bottom_15 = value_counts.tail(15)

            # Top 15 graph
            plt.figure(figsize=(12, 8))
            ax = sns.barplot(x=top_15.index, y=top_15.values)
            plt.title(f"Top 15 Distribution of {col}")
            adjust_labels(ax, top_15.index, max_chars_per_line=15, rotate=True)
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.subplots_adjust(bottom=0.35)
            save_visualisation(plt, f"{col}_top_15_distribution.png")

            # Bottom 15 graph
            plt.figure(figsize=(12, 8))
            ax = sns.barplot(x=bottom_15.index, y=bottom_15.values)
            plt.title(f"Bottom 15 Distribution of {col}")
            adjust_labels(ax, bottom_15.index, max_chars_per_line=15, rotate=True)
            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.subplots_adjust(bottom=0.35)
            save_visualisation(plt, f"{col}_bottom_15_distribution.png")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Filename required")
        sys.exit()

    filename = sys.argv[1]
    dataset = open_file(filename)
    summary = summarize(dataset)

    insights = question_llm(
        "Analyse and provide insights from the dataset.",
        context=f"dataset summary: {summary} \n Missing values: {dataset.isnull().sum()}",
    )
    print(insights)

    visualise_outliers(dataset)
    correlation_matrix = visualise_correlation(dataset)
    visualise_time_series(dataset)
    visualise_geographic_analysis(dataset)
    visualise_categorical_data(dataset)

    # Numeric analysis
    numeric_insights = question_llm(
        "Provide me insights about the following numeric columns.",
        context=f"Numeric columns summary:\n{dataset.select_dtypes(include=['number']).describe()}",
    )

    # Generating the story
    story = question_llm(
        "Generate a nice and creative story from the analysis",
        context=f"Dataset Analysis:\nSummary: {summary}\nMissing Values: {dataset.isnull().sum()}\nInsights: {insights}\nNumeric Column Insights: {numeric_insights}",
    )

    try:
        with open(os.path.join(outputDir, "README.md"), "w") as f:
            f.write("# Data Analysis Report\n\n")
            f.write("## Overview\n")
            f.write(f"File: {filename}\n\n")
            f.write("## Summary Statistics\n")
            f.write(f"{summary}\n\n")
            f.write("## Missing Values\n")
            f.write(f"{dataset.isnull().sum()}\n\n")
            f.write("## Insights\n")
            f.write(f"{insights}\n\n")
            f.write("## Numeric Insights\n")
            f.write(f"{numeric_insights}\n\n")
            f.write("## Story\n")
            f.write(f"{story}\n")
    except Exception as e:
        print(f"Error writing to README.md: {e}")

    print("Analysis complete! Results saved to README.md.")

    # question_llm("Are you ready?")
