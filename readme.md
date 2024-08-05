# Description

This script benchmarks the performance of different Large Language Models (LLMs) in summarizing and analyzing information from bank current account pages. It compares how well each LLM can process the data and answer a specific question.

# Prerequisites

Python 3.6 or later
Ollama installed and running locally (refer to Ollama documentation for installation instructions)
Required libraries: pandas, ollama
A CSV file named current_accounts.csv with two columns:
accounts: Contains the names of the bank accounts
content: Contains the textual content of the corresponding account page
# Installation

Ensure you have Python and pip installed. Install the required libraries using pip:

Bash
```pip install ollama```
Use code with caution.

# Usage

Prepare a CSV file named current_accounts.csv with the specified format.
Run the Python script (testing_llm_models.ipynb).
# Script Functionality

The script reads the current_accounts.csv file.
It iterates through each account page and uses different LLMs (llama3.1, gemma2, mistral, phi3:14b, qwen2) to generate summaries of the content.
It then constructs a prompt asking "which is best for kids account" based on the summarized information for each account offers.
Finally, the script uses the same LLM to answer the prompt, effectively comparing their performance on the specific question.
# Customization

You can modify the accounts offering list in the script to include different accounts offerings.
The generate_text function can be adjusted to explore different prompt engineering techniques or LLM parameters for potentially improved results.
The script can be further expanded to include additional metrics for a more comprehensive comparison.
# Limitations

The script's performance relies on the quality and structure of the provided bank account pages.
LLM performance can vary significantly based on prompt construction and model-specific parameters.
# Future Work

Explore and compare additional LLMs with different capabilities.
Incorporate sentiment analysis or other Natural Language Processing (NLP) techniques for deeper insights.
Develop a more robust evaluation framework for a holistic comparison.
