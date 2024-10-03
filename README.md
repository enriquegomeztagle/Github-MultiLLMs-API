# Github Multi LLMs API

A unified API for accessing multiple language models from various providers

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-Proprietary-red.svg)

## Description

This project provides a unified API for accessing a variety of language models from different providers, including OpenAI, Mistral, Meta, Cohere, AI21, and Microsoft.

## Table of Contents

- [Available Models](#available-models)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Available Models

### OpenAI

#### Text

- `/openai/text/{model}`

  - gpt-4o-mini
  - gpt-4o
- **OpenAI o1-mini**

  > **_COMING SOON..._**
  >
- **OpenAI o1-preview**

  > **_COMING SOON..._**
  >

#### Embeddings

- `/openai/embeddings/{model}`
  - text-embedding-3-small
  - text-embedding-3-large

### Mistral

- `/mistral/text/{model}`
  - Mistral-Nemo
  - Mistral-small
  - Mistral-large
  - Mistral-large-2407

### Meta

- `/meta/text/{model}`
  - Meta-Llama-3-8B-Instruct
  - Meta-Llama-3-70B-Instruct
  - Meta-Llama-3.1-8B-Instruct
  - Meta-Llama-3.1-70B-Instruct
  - Meta-Llama-3.1-405B-Instruct

### Cohere

- `/cohere/text/{model}`
  - Cohere-command-r
  - Cohere-command-r-plus

### AI21

- `/ai21/text/{model}`
  - AI21-Jamba-1.5-Large
  - AI21-Jamba-1.5-Mini
  - AI21-Jamba-Instruct

### Microsoft Phi

#### Text

- `/microsoft-phi/text/{model}`
  - Phi-3.5-MoE-instruct
  - Phi-3.5-mini-instruct
  - Phi-3-medium-128k-instruct
  - Phi-3-medium-4k-instruct
  - Phi-3-mini-128k-instruct
  - Phi-3-mini-4k-instruct
  - Phi-3-small-128k-instruct
  - Phi-3-small-8k-instruct

#### Vision

- `/microsoft-phi/vision/{model}`
  - Phi-3.5-vision-instruct

## Prerequisites

To use this API, ensure you have the following:

- Python 3.10 or higher.
- A virtual environment (optional but recommended).
- A GITHUB_TOKEN with access to Beta Github Models.
- Dependencies installed (see installation section).

## Installation

Follow these steps to install and configure the API:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/enriquegomeztagle/Github-MultiLLMs-API
   cd Github-MultiLLMs-API
   ```
2. **Create a virtual environment (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   Make sure to set the `GITHUB_TOKEN` environment variable with your GitHub token.

   ```
   export GITHUB_TOKEN="your_token_here"
   ```

   Or create a .env with

   ```
   GITHUB_TOKEN= "your_token_here"
   ```

   And then: 

   ```
   export GITHUB_TOKEN=$(grep 'GITHUB_TOKEN' .env | cut -d'=' -f2)
   ```
5. **Start the API:**

   ```bash
   uvicorn api:app --reload
   ```

## Usage

To use the API, make HTTP requests to the provided endpoints. Below is an example of how to make a request to the API:

### Example Request to OpenAI

**Endpoint:**
POST /openai/text/gpt-4o

**Request Body:**

```json
{
    "question": "What is the capital of France?"
}
```

**Expected Response:**

```json
{
    "response": "The capital of France is Paris.",
    "success": true,
    "duration": 0.123,
    "model": "gpt-4o"
}
```

<!-- 
## Examples

(Provide concrete examples of usage for different models and use cases)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us. -->

## License

This project is licensed under a proprietary license. See the [LICENSE.md](LICENSE.md) file for details.

## Author & Contact

- [@EnriqueGomezTagle](https://github.com/enriquegomeztagle) / [@kikinacademy](https://github.com/kikinacademy)

## Acknowledgements

Thank all language model providers for innovating with this LLMs.
