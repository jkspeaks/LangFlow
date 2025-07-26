# Learn RAG Concept - LangFlow Workflow

A comprehensive Retrieval-Augmented Generation (RAG) system built with LangFlow for analyzing and querying any set of documents. In this workflow, I have used OPM (Office of Personnel Management) annual performance reports with intelligent document processing and source attribution. This is a freely available dataset for download. You can use any set of files with this workflow. 

## 🎯 Overview

This LangFlow workflow creates a simple document analysis system that can:

- **Process OPM PDF Reports**: Automatically ingests and processes OPM annual performance reports
- **Intelligent Document Chunking**: Splits documents into optimal chunks for retrieval
- **Vector-Based Search**: Uses embeddings and vector storage for semantic document retrieval  
- **Source Attribution**: Provides citations with specific OPM report names for all responses
- **Natural Language Querying**: Enables conversational queries about OPM performance data
- **Context-Aware Responses**: Combines retrieved document chunks with user queries for accurate answers

## 🏗️ Architecture

The workflow is divided into two main components:

### 1. Ingestion Flow (Document Processing Pipeline)
- **Document Loading**: Processes OPM annual performance reports (PDF format) from a directory
- **Text Chunking**: Splits documents into manageable, searchable sections
- **Embedding Generation**: Creates vector representations using OpenAI Embeddings
- **Vector Storage**: Stores embeddings in Chroma DB for efficient retrieval

### 2. Query Flow (Question Answering System)
- **User Input Processing**: Handles natural language queries via Chat Input
- **Query Embedding**: Converts user questions to vector format
- **Semantic Retrieval**: Finds relevant document chunks from vector store
- **Context Integration**: Combines retrieved information with user queries
- **Response Generation**: Provides comprehensive answers with proper source citations

## 🚀 Getting Started

### Prerequisites
- LangFlow installed and running
- OpenAI API key for embeddings and language model [OR] Ollama embeddings and Llama model running locally
- OPM annual performance reports (PDF files)

### Required Components
- File component (for PDF loading)
- Split Text component (for document chunking)
- OpenAI Embeddings component
- Chroma DB component (vector store)
- Prompt component (for RAG prompts)
- Chat Input/Output components

### Installation

1. **Download OPM Reports**:
   - Obtain OPM annual performance reports in PDF format
   - Organize files in a dedicated directory

2. **Import the Workflow**:
   ```bash
   # In LangFlow interface
   File > Import > Select opm-rag-system.json
   ```

3. **Configure API Keys**:
   - Set OpenAI API key in embedding and LLM components (if Ollama embeddings are not used)
   - Ensure proper authentication for all services

## 📋 Setup Instructions

### Ingestion Flow Configuration

1. **File Component Setup**:
   - Configure to load OPM PDF documents
   - Set file path to your OPM reports directory
   - Enable batch processing for multiple files

2. **Split Text Configuration**:
   - **Recommended chunk size**: 1000-1500 characters
   - **Overlap percentage**: 10-20% for context continuity
   - Experiment with different sizes for optimal performance

3. **OpenAI Embeddings Setup**:
   - Model: `text-embedding-ada-002` (recommended)
   - Configure API key and rate limits

4. **Chroma DB Configuration**:
   - **Collection name**: `opm_reports` (must match in both flows)
   - **Persistence**: Enable for data retention
   - **Distance metric**: Cosine similarity

### Query Flow Configuration

1. **Chat Input Component**:
   - Enable user query input
   - Configure input validation

2. **Query Embedding**:
   - Use same OpenAI Embeddings model as ingestion
   - Ensure consistent embedding space

3. **Vector Retrieval**:
   - **Collection name**: `opm_reports` (match ingestion flow)
   - **Top-k results**: 3-5 relevant chunks
   - **Similarity threshold**: 0.7-0.8

4. **RAG Prompt Template**:
   ```
   Based on the following context from OPM performance reports, answer the user's question. 
   Always cite the specific OPM report name(s) that provided the information.

   Context: {context}
   
   Question: {question}
   
   Answer: Provide a comprehensive response with proper citations to the OPM report(s).
   ```

## 💡 Usage Examples

### Sample Queries

**Performance Metrics Query**:
```
User: "What were the key performance indicators for federal agencies in 2023?"
System: Based on the OPM Annual Performance Report 2023, the key performance indicators included...
[Source: OPM Annual Performance Report 2023]
```

**Trend Analysis Query**:
```
User: "How has employee satisfaction changed over the past three years?"
System: According to the OPM Annual Performance Reports from 2021-2023, employee satisfaction showed...
[Sources: OPM Annual Performance Report 2021, 2022, 2023]
```

**Specific Program Query**:
```
User: "What initiatives were implemented to improve diversity and inclusion?"
System: The OPM Annual Performance Report 2023 outlines several D&I initiatives...
[Source: OPM Annual Performance Report 2023]
```

## 🔧 Optimization Tips

### Chunk Size Optimization
- **Small chunks (500-800 chars)**: Better precision, may miss context
- **Medium chunks (1000-1500 chars)**: Balanced approach (recommended)
- **Large chunks (2000+ chars)**: More context, may include irrelevant information

### Overlap Configuration
- **10% overlap**: Minimal redundancy, faster processing
- **15-20% overlap**: Good balance of context and efficiency
- **25%+ overlap**: Maximum context preservation, slower processing

### Retrieval Tuning
- Adjust similarity thresholds based on query complexity
- Fine-tune top-k results for response quality
- Monitor embedding costs and optimize batch processing

## 📊 Flow Components Detail

| Component | Purpose | Configuration Notes |
|-----------|---------|-------------------|
| File | PDF document loading | Supports batch processing |
| Split Text | Document chunking | Experiment with chunk size/overlap |
| OpenAI Embeddings | Vector generation | Use consistent model across flows |
| Chroma DB | Vector storage | Same collection name required |
| Chat Input | User query interface | Enable query validation |
| Prompt | RAG response formatting | Include citation requirements |
| Chat Output | Response display | Format with proper citations |

## 🛠️ Troubleshooting

### Common Issues

**Documents not loading**:
- Verify PDF file paths and permissions
- Check file format compatibility
- Ensure sufficient disk space

**Poor retrieval quality**:
- Adjust chunk size and overlap parameters
- Fine-tune similarity thresholds
- Review document preprocessing

**Missing citations**:
- Verify prompt template includes citation instructions
- Check document metadata preservation
- Ensure source tracking through pipeline

**Collection errors**:
- Confirm same collection name in both flows
- Clear and reinitialize Chroma DB if needed
- Check database permissions and storage

## 📈 Performance Monitoring

### Key Metrics to Track
- **Query response time**: Aim for <5 seconds
- **Retrieval accuracy**: Monitor relevance of retrieved chunks
- **Citation coverage**: Ensure all responses include proper sources
- **Token usage**: Optimize for cost efficiency

### Optimization Strategies
- Implement caching for frequently asked questions
- Use batch processing for document ingestion
- Monitor and optimize embedding API usage
- Regular vector store maintenance and updates

## 🔄 Maintenance

### Regular Tasks
- **Document Updates**: Re-run ingestion flow when new OPM reports are available
- **Vector Store Cleanup**: Periodically clean outdated embeddings
- **Performance Review**: Monitor query quality and response accuracy
- **Citation Verification**: Ensure source attribution remains accurate

### Updating Workflow
1. Stop existing flows
2. Update document sources
3. Re-run ingestion flow
4. Test query flow with sample questions
5. Verify citation accuracy

## 📝 License

This workflow is provided for educational and research purposes. Ensure compliance with OPM data usage policies. 

## 🆘 Support

- **Technical Issues**: Check LangFlow community forums
- **OPM Data Questions**: Refer to official OPM documentation
- **API Problems**: Consult OpenAI and Chroma DB support resources

---

**Ready to analyze OPM performance data?** Import the workflow and start exploring federal performance insights with intelligent document retrieval!