# Smart Query Assistant - LangFlow Workflow

An intelligent AI assistant workflow built with LangFlow that provides contextual, categorized responses to different types of user queries with integrated tool support.

## 🎯 Overview

This LangFlow workflow creates a sophisticated query understanding system that can:

- **Classify Questions Intelligently**: Automatically categorizes user input into factual, analytical, comparison, or definition queries
- **Maintain Conversation Context**: Remembers previous interactions for natural, flowing conversations
- **Perform Calculations**: Handles mathematical queries with an integrated calculator tool
- **Provide Time Information**: Responds to date and time-related questions
- **Format Responses Professionally**: Tailors response structure based on query type

## 🏗️ Architecture

The workflow consists of three main components:

### 1. Query Classification Engine
- **Purpose**: Analyzes incoming questions and categorizes them
- **Categories**:
  - 📋 **Factual Questions**: Direct information requests ("What is...?", "Who invented...?")
  - 🔍 **Analytical Questions**: Complex reasoning queries ("How does...?", "Why do...?")
  - ⚖️ **Comparison Questions**: Side-by-side analysis ("What's the difference between...?")
  - 📚 **Definition Requests**: Explanation-focused queries ("Define...", "Explain...")

### 2. Dynamic Response Templates
- **Factual Responses**: Concise, direct answers with key facts
- **Analytical Responses**: Step-by-step reasoning with logical flow
- **Comparison Responses**: Structured formats (tables, bullet points)
- **Definition Responses**: Comprehensive explanations with examples and use cases

### 3. Integrated Tool System
- **Calculator Tool**: Handles mathematical computations and calculations
- **DateTime Tool**: Provides current date, time, and time-related information
- **Smart Router**: Intelligently determines when to use tools vs. direct LLM responses

## 🚀 Getting Started

### Prerequisites
- LangFlow installed and running
- OpenAI API key (or compatible LLM provider)
- Python environment with required packages

### Installation

1. **Clone or Download** this workflow file
2. **Import into LangFlow**:
   - Open LangFlow interface
   - Click "Import" or "Load Flow"
   - Select the `smart-query-assistant.json` file
3. **Configure API Keys**:
   - Set your OpenAI API key in the LLM components
   - Configure any additional service credentials

### Setup Instructions

1. **Import the Workflow**:
   ```bash
   # In LangFlow interface
   File > Import > Select smart-query-assistant.json
   ```

2. **Configure Components**:
   - Update LLM model settings (GPT-4 recommended)
   - Set temperature to 0.3 for consistent responses
   - Configure memory component for conversation context

3. **Test the Flow**:
   - Start with simple queries: "What is artificial intelligence?"
   - Try calculations: "What is 15% of 250?"
   - Test time queries: "What is today's date?"
   - Ask analytical questions: "How does machine learning work?"

## 💡 Usage Examples

### Factual Queries
```
User: "Who invented the telephone?"
Assistant: Alexander Graham Bell invented the telephone in 1876...
```

### Analytical Queries
```
User: "How does photosynthesis work?"
Assistant: Photosynthesis is a complex process that occurs in several stages:
1. Light absorption...
2. Water splitting...
3. Carbon dioxide fixation...
```

### Calculation Queries
```
User: "What's 15% of 1,250?"
Assistant: 15% of 1,250 is 187.5
```

### Comparison Queries
```
User: "What's the difference between machine learning and deep learning?"
Assistant: Here's a comparison:

| Aspect | Machine Learning | Deep Learning |
|--------|------------------|---------------|
| Definition | ... | ... |
```

## 🔧 Customization

### Adding New Query Types
1. Modify the Query Classifier prompt template
2. Add corresponding response templates
3. Update the routing logic

### Integrating Additional Tools
1. Add new tool components in LangFlow
2. Update the Smart Router logic
3. Create tool-specific prompt templates

### Adjusting Response Formats
- Edit prompt templates in each response component
- Modify formatting instructions
- Adjust tone and style parameters

## 📊 Flow Components

| Component | Purpose | Configuration |
|-----------|---------|---------------|
| Input Handler | Receives user queries | Text input processing |
| Query Classifier | Categorizes question types | Custom prompt template |
| Memory Component | Maintains conversation context | Conversation buffer |
| Response Templates | Formats answers by type | Multiple prompt variants |
| Calculator Tool | Handles math operations | Python calculator |
| DateTime Tool | Provides time information | System datetime |
| Smart Router | Directs to appropriate handler | Conditional logic |
| Output Formatter | Final response processing | Text formatting |

## 🛠️ Troubleshooting

### Common Issues

**Flow doesn't start**:
- Check API key configuration
- Verify all components are connected
- Ensure required packages are installed

**Incorrect categorization**:
- Review Query Classifier prompt
- Add more examples to training data
- Adjust classification logic

**Tool integration fails**:
- Verify tool components are properly configured
- Check routing conditions
- Test tools individually

## 📈 Performance Tips

- Use GPT-4 for better query classification accuracy
- Set appropriate memory limits for conversation context
- Monitor token usage for cost optimization
- Implement caching for frequently asked questions

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Issues**: Found a bug or have a suggestion? Open an issue
2. **Add Query Types**: Extend the classification system
3. **Integrate New Tools**: Add functionality with additional tools
4. **Improve Templates**: Enhance response formatting
5. **Documentation**: Help improve this README or add examples

## 📝 License

This workflow is provided under the MIT License. Feel free to modify and distribute.

## 🙋‍♂️ Support

- **Issues**: Report problems via GitHub issues
- **Questions**: Ask in LangFlow community forums
- **Feature Requests**: Suggest improvements through issues

## 🔄 Version History

- **v1.0**: Initial release with basic query classification
- **v1.1**: Added calculator and datetime tools
- **v1.2**: Enhanced conversation memory
- **v1.3**: Improved response templates and formatting

---

**Ready to deploy?** Import the workflow into LangFlow and start building smarter conversational AI experiences!