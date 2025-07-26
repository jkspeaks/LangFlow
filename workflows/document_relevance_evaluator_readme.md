# Document Relevance Evaluator - LangFlow Workflow

A document relevance scoring system built with LangFlow that evaluates and filters documents for Retrieval-Augmented Generation (RAG) systems based on query relevance, ensuring only the most pertinent information is used for response generation. Helpful when you have several documents - as this will reduce the tokens used by the LLM and also prevent hallucinations and running out of context length. 

## 🎯 Overview

This LangFlow workflow creates a simpel document evaluation system that:

- **Evaluates Document Relevance**: Scores documents on a 1-5 scale based on user query entered
- **Multi-Criteria Assessment**: Analyzes directness, specificity, accuracy, and completeness
- **Intelligent Filtering**: Only passes documents meeting minimum relevance thresholds
- **Structured Output**: Returns sorted JSON arrays with detailed scoring rationale
- **Quality Control**: Prevents irrelevant information from contaminating RAG responses
- **Customizable Thresholds**: Allows users to set minimum relevance scores for processing

## 🏗️ Architecture

### Core Evaluation Components

#### 1. Document Relevance Analyzer
- **Purpose**: Evaluates each document against the user query

#### 2. Multi-Dimensional Scoring Engine
- **Scale**: 1-5 point scoring system
  - **5**: Highly relevant: Directly answers the query with specific information
  - **4**: Relevant: Contains important information related to the query
  - **3**: Somewhat relevant: Has some information related to the query but not comprehensive
  - **2**: Barely relevant: Only mentions concepts from the query but lacks useful information
  - **1**: Not relevant: Unrelated to the query

#### 3. Threshold Filter & Output Controller
- **Function**: Filters documents based on user-defined minimum scores
- **Smart Routing**: Passes qualifying documents or returns "no relevant documents" message
- **JSON Formatting**: Structures output for downstream RAG processing

## 🚀 Getting Started

### Prerequisites
- LangFlow installed and running
- OpenAI API key (or compatible LLM provider)
- Document collection for evaluation

### Installation

1. **Import the Workflow**:
   ```bash
   # In LangFlow interface
   File > Import > Select document-relevance-evaluator.json
   ```

2. **Configure Components**:
   - Set up LLM with appropriate model (GPT-4 recommended for accuracy)
   - Configure input components for queries and documents
   - Set default relevance threshold (recommended: 3.0)

## 📋 Configuration Guide

**Components**:
1. OpenAI Ranker
- Modify the json structure and criteria for ranking using the prompt here

2. Ranking Threshold
- Update the score in System Message in this component based on the number of documents and performance needs. 

## 🛠️ Troubleshooting

### Common Issues

**Inconsistent Scoring**:
- Use more detailed evaluation prompts
- Implement scoring calibration examples

**Too Few Documents Pass Threshold**:
- Lower relevance threshold
- Review document collection quality
- Analyze score distribution patterns

**Evaluation Takes Too Long**:
- Implement batch processing
- Use lighter LLM models for preliminary screening
- Cache evaluations for repeated documents

**JSON Format Errors**:
- Add output validation and formatting
- Include error handling for malformed responses
- Use structured output models when available

## 🎯 Use Cases

### RAG System Enhancement
- **Quality Filtering**: Ensure only relevant documents inform responses
- **Cost Optimization**: Reduce token usage by filtering irrelevant content
- **Response Accuracy**: Improve answer quality through better document selection

### Content Curation
- **Document Libraries**: Automatically tag and organize documents by relevance
- **Search Optimization**: Improve search result ranking
- **Knowledge Base Management**: Maintain high-quality information repositories

### Research Applications
- **Literature Reviews**: Identify most relevant papers for research topics
- **Citation Analysis**: Evaluate source relevance for academic writing
- **Expert Systems**: Build domain-specific knowledge filtering


## 📝 License

This workflow is provided under MIT License for research and commercial use.

## 🆘 Support

- **Technical Issues**: LangFlow community forums
- **Feature Requests**: GitHub issues and discussions
- **Integration Help**: Documentation and example implementations

---

**Ready to enhance your RAG system?** Import this workflow and start building more intelligent document filtering for higher quality AI responses!
