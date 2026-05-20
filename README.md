# RAG-Based AI Teaching Assistant

## Overview

RAG-Based AI Teaching Assistant is a project that helps users ask questions about educational video content.

The system processes lecture videos, converts them into audio, transcribes the audio using OpenAI Whisper, stores the transcript in JSON format, creates embeddings, retrieves relevant content using cosine similarity, and generates answers using a local LLM through Ollama.

## Current Progress

- Added video preprocessing script (`process_videos.py`)
- Supports converting video content into audio
- Added audio transcription and JSON export script (`create_chunks.py`)

## Planned Pipeline

```text
Video
→ Audio using ffmpeg
→ Transcript using Whisper
→ JSON transcript
→ Embeddings
→ Query embedding
→ Cosine similarity retrieval
→ Ollama response
→ Answer with evaluation metrics