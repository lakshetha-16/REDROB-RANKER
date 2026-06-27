# 🧠 Intelligent Candidate Ranking System

## 📌 Overview
This project builds an AI-powered candidate ranking system that intelligently evaluates and ranks job applicants using a hybrid approach combining semantic similarity, skill signals, and profile-based scoring.

---

## 🚀 Problem Statement
Recruiters struggle to manually evaluate large volumes of candidates efficiently. This system automates candidate discovery and ranking based on relevance, experience, and behavioral signals.

---

## 🏗️ System Architecture

The pipeline consists of:

1. **Data Loading**
   - Loads 100,000+ candidate profiles

2. **Preprocessing**
   - Extracts structured features from raw profiles
   - Cleans and normalizes skills & signals

3. **Semantic Embedding**
   - Uses SentenceTransformer (MiniLM)
   - Encodes job titles + skills

4. **Hybrid Scoring Engine**
   - Semantic similarity score
   - Experience weighting
   - Skill depth scoring
   - Behavioral signals (GitHub, response rate, etc.)

5. **Ranking System**
   - Final weighted score computation
   - Sorted ranking with tie-breaking rules

6. **Submission Generator**
   - Outputs top 100 candidates in required format

---

## ⚙️ Tech Stack
- Python
- Pandas
- NumPy
- SentenceTransformers
- Scikit-learn (utility logic)

---

## 🧠 Scoring Logic

Final score =  
- Semantic relevance (45%)  
- Experience score (20%)  
- Skill score (20%)  
- Behavioral signals (15%)

---

## 📊 Output Format

The system generates:

| candidate_id | rank | score | reasoning |
|--------------|------|-------|----------|

---

## 📈 Results

- Processes 100,000 candidates
- Generates ranked list of top 100
- Passes full validation checks
- Optimized for fast inference (5–10 min runtime)

---

## 📁 Project Structure
