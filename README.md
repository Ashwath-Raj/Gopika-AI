# GOPIKA

Offline Multilingual Voice Intelligence Stack

## Overview

GOPIKA is a fully offline voice intelligence system built under strict hardware constraints (RTX 3050 6GB).

Phase 1 implements a modular push-to-talk voice pipeline:

Speech-to-Text → LLM → Text-to-Speech

The system is designed for:
- Full offline execution
- GPU-aware model orchestration
- Dockerized deployment
- Clean extensibility for future RAG and agent layers

## Phase 1 Scope

- Push-to-talk web interface
- Multilingual STT (Indian languages → English)
- LLM reasoning (English)
- Target-language speech output
- Stateless execution
- Sequential GPU model usage

## Architecture (Phase 1)

Browser UI  
→ API Gateway  
→ STT (faster-whisper)  
→ LLM (Llama 3 8B Q4 via Ollama)  
→ TTS (Coqui XTTS)  
→ Audio Output  

## Hardware Target

- NVIDIA RTX 3050 (6GB VRAM)
- Linux environment
- Docker runtime

## Status

Phase 1 — Voice Core (In Development)
