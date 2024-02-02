# Takshila

This project is a RAG application which can query gita

## Installation

To install the necessary dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

Make sure Docker is running.

Install Ollama
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
ollama pull llama2
ollama serve llama2

```
To run the application, execute the following command:

```
streamlit run app.py
```

This command will start the application and you can access it through your web browser at [URL or localhost address].

## Requirements

All requirements for this project are listed in the `requirements.txt` file. Use the command mentioned in the Installation section to install them.

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Mention any acknowledgements or credits for libraries, frameworks, or inspiration.

Feel free to modify this template to better fit your project's specific details and requirements!
