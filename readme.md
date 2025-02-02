
# Installation steps

### step 1
Install ollama to your computer:

```curl -fsSL https://ollama.com/install.sh | sh```

### step 2

```https://github.com/ollama/ollama```

select your model from github list. Large models need more system RAM

```ollama run <model_name>``` 

I used "llama2" model in my testing.

### step 3

Run opems cli interface where you can interact with the model.
```/bye``` to exit from cli interface.

```ollama help``` to see all available commands.

### step 4
install ollama python package.
```pip install ollama```

Now you can try to main.py file to see how to interact with the model.

```python main.py```

### Advanced example
See the ModelFile example to create your own model.
Creates a new model with the given name and file.
```ollama create mymodel -f ModelFile```