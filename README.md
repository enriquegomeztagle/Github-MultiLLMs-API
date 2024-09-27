# Github Multi LLMs API

### A unified API for accessing multiple language models from various providers

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
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Available Models

### OpenAI

#### Text

- `/openai/text/{model}`
  - gpt-4o-mini
  - gpt-4o
  - ***OpenAI o1-mini (COMING SOON...)***
  - ***OpenAI o1-preview (COMING SOON...)***

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
  - Meta-Llama-3-8-Instruct
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

(Add information about the prerequisites needed to use the API)

## Installation

(Provide detailed instructions on how to install and configure the API)

## Usage

(Explain how to use the API, including examples of API calls and responses)

## Examples

(Provide concrete examples of usage for different models and use cases)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under a proprietary license. See the [LICENSE.md](LICENSE.md) file for details.

## Author & Contact

- [@EnriqueGomezTagle](https://github.com/enriquegomeztagle) / [@kikinacademy](https://github.com/kikinacademy)

## Acknowledgements

Thank all language model providers for innovating with this LLMs.
