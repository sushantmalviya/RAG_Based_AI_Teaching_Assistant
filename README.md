# RAG-Based AI Teaching Assistant

## Overview

RAG-Based AI Teaching Assistant is a project that helps users ask questions about educational video content.

The system processes lecture videos, converts them into audio, transcribes the audio using OpenAI Whisper, stores the transcript in JSON format, creates embeddings, retrieves relevant content using cosine similarity, and generates answers using a local LLM through Ollama.

# How to use this RAG AI Teaching assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning video_to_mp3

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning mp3_to_json

## Step 4 - Convert the json files to Vectors
Use the file preprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM


# Status 
Currently trying to improve the system. Suggestions are welcomed.