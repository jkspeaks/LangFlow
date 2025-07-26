# LangFlow Workflows

A collection of production-ready LangFlow workflows for various AI applications, from simple assistants to document processing and research automation. These are meant for learning purposes and can be customized or enhanced as required. Refer to the respective, flow specific readme.md files for details on how to customize and enhance the flows.

## 🚀 Quick Start

1. **Install LangFlow**:
   ```bash
   uv pip install langflow
   uv run langflow run
   ```

2. **Import a Workflow**:
   - Open LangFlow interface
   - Click "Import" → Select workflow JSON file
   - Configure API keys and settings
   - Run the workflow

## 📁 Sample Workflows

### [Smart Query Assistant](./workflows/smart-query-assistant.json)
An AI assistant that understands different question types, maintains conversation context, and performs calculations.
- **Use Case**: Intelligent Q&A systems
- **Tools**: Calculator, DateTime
- **Features**: Query classification, contextual responses

### [OPM Performance Reports RAG](./workflows/RAG-ingestion-flow.json)
RAG system for analyzing OPM annual performance reports with document processing and source attribution. Can be used for any set of files. 
- **Use Case**: Government document analysis
- **Tools**: PDF processing, vector search
- **Features**: Document chunking, citation tracking

### [Document Relevance Evaluator](./workflows/Document Relevance Evaluator.json)
Evaluates and scores documents for RAG systems on a 1-5 relevance scale with intelligent filtering.
- **Use Case**: RAG quality improvement
- **Tools**: LLM evaluation, JSON processing
- **Features**: Multi-criteria scoring, threshold filtering

### [Research Agent](./workflows/Research-Agent-Workflow.json)
Multi-agent research system that transforms topics into comprehensive reports with collaborative AI agents.
- **Use Case**: Automated research and reporting
- **Tools**: Wikipedia, Tavily, Yahoo Finance, Wolfram Alpha
- **Features**: Multi-agent coordination, structured reporting

## 📖 Usage

Each workflow directory contains:
- `workflow.json` - The complete LangFlow workflow file
- `README.md` - Detailed setup and usage instructions
- Additional configuration files as needed

## 📄 License

MIT License - Feel free to use and modify these workflows for your projects.

## 🆘 Support

- **Issues**: Report bugs or request features via GitHub issues
- **Discussions**: Ask questions in GitHub Discussions
- **Community**: Join the LangFlow community for tips and examples

---

**Happy building!** 🚀
