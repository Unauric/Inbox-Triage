# Inbox Triage

A machine learning–based text classification system designed to automatically categorize and prioritize inbox messages such as emails.

## Overview

Inbox Triage applies supervised learning techniques to analyze incoming text and classify messages based on their content. The project demonstrates a complete NLP pipeline, from data preprocessing and model training to evaluation and prediction.

It is ideal for learning and showcasing practical machine learning applied to real-world text data.

## Features

- Automatic message classification using Naive Bayes
- Preprocessing and tokenization of text data
- Model training and evaluation workflow
- Saved model persistence using JSON
- Command-line driven execution

## Project Structure

- `Models/` — Stored trained models
- `data/` — Training and testing datasets
- `nb_model.py` — Naive Bayes classifier implementation
- `evaluate.py` — Model evaluation and accuracy reporting
- `IO_Utils.py` — Input/output and preprocessing utilities

## Dataset

- `train.tsv` — Labeled training data
- `test.tsv` — Labeled testing data

The datasets are tab-separated files containing message text and corresponding labels.

## How It Works

1. Load and preprocess text data
2. Train a Naive Bayes classifier
3. Save the trained model
4. Evaluate predictions on unseen data
5. Output performance metrics

## Requirements

- Python 3.x
- scikit-learn
- numpy

Install dependencies with:

```bash
pip install -r requirements.txt
