"""
HalluciNO Questions Database
Contains 50+ GenAI/ML-related statements - mix of truths and hallucinations

Each question has:
- id: unique identifier
- question: the statement to evaluate
- category: topic category
- is_hallucination: True if the statement is false/hallucination, False if true
- explanation: why this is true or false
- difficulty: beginner, intermediate, or expert
"""

from app.models import Question, DifficultyLevel as Difficulty

# Complete questions database with 50+ questions
QUESTIONS = [
    # Machine Learning Questions
    Question(
        id=1,
        question="Neural networks with more layers always perform better than shallow networks.",
        category="Neural Networks",
        is_hallucination=True,
        explanation="While deep networks can learn complex patterns, they don't always perform better. More layers can lead to vanishing gradients, overfitting, and increased computational cost. Shallow networks often outperform deep ones for simple tasks.",
        difficulty=Difficulty.BEGINNER,
        hints=["Think about overfitting and computational cost", "Consider simple vs complex tasks"]
    ),
    Question(
        id=2,
        question="Machine learning models require labeled data to learn patterns from data.",
        category="Machine Learning",
        is_hallucination=False,
        explanation="This is correct. Supervised learning requires labeled data. However, unsupervised and semi-supervised learning can work with unlabeled data. The statement is true for supervised learning.",
        difficulty=Difficulty.BEGINNER,
        hints=["Think of different types of learning", "Unsupervised learning exists"]
    ),
    Question(
        id=3,
        question="Overfitting occurs when a model learns noise in the training data instead of the underlying pattern.",
        category="Machine Learning",
        is_hallucination=False,
        explanation="This is accurate. Overfitting happens when a model fits too closely to training data, including its noise, resulting in poor generalization to new data.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Think about test performance vs training performance", "Consider using validation data"]
    ),
    Question(
        id=4,
        question="The learning rate in neural networks can be any positive number without affecting training.",
        category="Neural Networks",
        is_hallucination=True,
        explanation="False! Learning rate is critical. Too high causes divergence, too low causes slow convergence. It's one of the most important hyperparameters to tune.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Think about training stability", "Consider what happens with very large values"]
    ),
    
    # Generative AI Questions
    Question(
        id=5,
        question="ChatGPT was trained on data only up to January 2022.",
        category="Generative AI",
        is_hallucination=True,
        explanation="This is outdated. ChatGPT-4 has knowledge up to April 2024, and newer versions have more recent data. The original GPT-3 had a knowledge cutoff, but this has evolved.",
        difficulty=Difficulty.BEGINNER,
        hints=["ChatGPT keeps getting updated versions", "Check the current year - is this info recent?"]
    ),
    Question(
        id=6,
        question="Large Language Models generate text by predicting one token at a time.",
        category="Generative AI",
        is_hallucination=False,
        explanation="Correct! LLMs use autoregressive generation - they predict the next token in a sequence, one token at a time, using previously generated tokens.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Think about how you type one character at a time", "LLMs use 'autoregressive' generation"]
    ),
    Question(
        id=7,
        question="GPT stands for 'Generative Pre-training Transformer'.",
        category="Generative AI",
        is_hallucination=False,
        explanation="This is correct! GPT architecture uses transformer blocks and is pre-trained on large text corpora before fine-tuning.",
        difficulty=Difficulty.BEGINNER,
        hints=["G = Generative, P = Pre-training", "T = Transformer"]
    ),
    Question(
        id=8,
        question="Transformers were invented by Google and OpenAI together.",
        category="Neural Networks",
        is_hallucination=True,
        explanation="Transformers were introduced by Google researchers in the 2017 paper 'Attention Is All You Need'. While OpenAI used them, they didn't invent them.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Look up 'Attention Is All You Need' paper", "Consider who published it first"]
    ),
    
    # AI Agents Questions
    Question(
        id=9,
        question="An AI agent can perceive its environment and take actions to achieve goals.",
        category="AI Agents",
        is_hallucination=False,
        explanation="This is the definition of an AI agent! Agents perceive environments through sensors and take actions through actuators to maximize some performance metric.",
        difficulty=Difficulty.BEGINNER,
        hints=["Agents have sensors (perceive) and actuators (act)", "This is core to agent theory"]
    ),
    Question(
        id=10,
        question="All AI agents have consciousness and self-awareness.",
        category="AI Agents",
        is_hallucination=True,
        explanation="False! Most AI agents are task-oriented systems without consciousness. Current AI agents are reactive or deliberative systems, not sentient beings.",
        difficulty=Difficulty.BEGINNER,
        hints=["Consider current AI capabilities", "Is consciousness a requirement for AI agents?"]
    ),
    Question(
        id=11,
        question="Multi-agent systems can lead to emergent behaviors not predicted by individual agent design.",
        category="AI Agents",
        is_hallucination=False,
        explanation="True! When multiple agents interact, complex emergent behaviors can arise from simple individual rules, leading to system properties not explicitly programmed.",
        difficulty=Difficulty.EXPERT,
        hints=["Think of swarms or flocking behavior", "Simple rules + many agents = complex behavior"]
    ),
    
    # Prompt Engineering Questions
    Question(
        id=12,
        question="Prompt engineering is just about writing polite questions to AI models.",
        category="Prompt Engineering",
        is_hallucination=True,
        explanation="Prompt engineering involves techniques like few-shot learning, chain-of-thought, role assignment, and careful phrasing. It's much more complex than just being polite!",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Think of advanced techniques like chain-of-thought", "More than just politeness - it's a science"]
    ),
    Question(
        id=13,
        question="Chain-of-thought prompting makes LLMs show their reasoning step-by-step.",
        category="Prompt Engineering",
        is_hallucination=False,
        explanation="Correct! Chain-of-thought prompting encourages models to explain their reasoning step-by-step, often improving accuracy on complex tasks.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["It's a prompting technique that helps LLMs think", "'Let's think step by step' is an example"]
    ),
    Question(
        id=14,
        question="Temperature in LLM prompts controls how creative vs. deterministic the output is.",
        category="Prompt Engineering",
        is_hallucination=False,
        explanation="True! Temperature ranges from 0 (deterministic) to 1+ (creative). Higher temperature makes responses more random and creative.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Temperature = 0 means always pick the best token", "Higher temperature = more randomness"]
    ),
    
    # LangChain Questions
    Question(
        id=15,
        question="LangChain is a framework for building applications with Large Language Models.",
        category="LangChain",
        is_hallucination=False,
        explanation="Correct! LangChain is an open-source framework that simplifies building LLM applications with chains, agents, and memory management.",
        difficulty=Difficulty.BEGINNER,
        hints=["LangChain is open-source", "It helps build LLM applications"]
    ),
    Question(
        id=16,
        question="LangChain was created by OpenAI as an official framework.",
        category="LangChain",
        is_hallucination=True,
        explanation="False! LangChain was created by Harrison Chase and the open-source community. It's not an official OpenAI project, though it integrates with OpenAI APIs.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Created by Harrison Chase", "Not an official OpenAI product"]
    ),
    Question(
        id=17,
        question="Memory in LangChain is used to maintain conversation history and context.",
        category="LangChain",
        is_hallucination=False,
        explanation="True! LangChain's memory modules store conversation history, allowing chains and agents to maintain context across multiple interactions.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Memory maintains conversation state", "Helps LLMs remember previous messages"]
    ),
    
    # LangGraph Questions
    Question(
        id=18,
        question="LangGraph is used for building directed acyclic graphs of LLM operations.",
        category="LangGraph",
        is_hallucination=False,
        explanation="Correct! LangGraph (part of LangChain) allows you to define stateful, multi-actor workflows using graph-based structures.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["LangGraph builds workflows", "It uses graph structures"]
    ),
    Question(
        id=19,
        question="LangGraph cannot handle loops or cycles in its computation graphs.",
        category="LangGraph",
        is_hallucination=True,
        explanation="False! LangGraph is specifically designed to handle stateful processing with cycles and loops, unlike traditional DAG-based systems.",
        difficulty=Difficulty.EXPERT,
        hints=["LangGraph is more flexible than DAGs", "It handles stateful processes with cycles"]
    ),
    Question(
        id=20,
        question="Nodes in LangGraph represent functions and edges represent data flow.",
        category="LangGraph",
        is_hallucination=False,
        explanation="True! In LangGraph, nodes are computational units (functions) and edges represent how data flows between them.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Nodes = functions, Edges = connections", "Think like a flowchart"]
    ),
    
    # RAG (Retrieval-Augmented Generation) Questions
    Question(
        id=21,
        question="RAG stands for Retrieval-Augmented Generation.",
        category="RAG",
        is_hallucination=False,
        explanation="Correct! RAG is a technique that retrieves relevant documents from a knowledge base and uses them to augment LLM generation.",
        difficulty=Difficulty.BEGINNER,
        hints=["R = Retrieval, A = Augmented", "G = Generation"]
    ),
    Question(
        id=22,
        question="RAG allows LLMs to access real-time information and external knowledge bases.",
        category="RAG",
        is_hallucination=False,
        explanation="True! RAG retrieves current information from databases or documents, helping LLMs provide more accurate and up-to-date responses.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["RAG uses external databases", "Helps with current information"]
    ),
    Question(
        id=23,
        question="Vector embeddings are used in RAG to store knowledge as simple text files.",
        category="RAG",
        is_hallucination=True,
        explanation="False! Vector embeddings convert text into high-dimensional vectors stored in vector databases (like Pinecone, Weaviate). This enables semantic similarity search.",
        difficulty=Difficulty.EXPERT,
        hints=["Embeddings are vectors, not text", "Think of vector databases"]
    ),
    Question(
        id=24,
        question="RAG can reduce LLM hallucinations by grounding responses in retrieved documents.",
        category="RAG",
        is_hallucination=False,
        explanation="True! By retrieving relevant documents, RAG gives LLMs factual information to base responses on, significantly reducing hallucinations.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["RAG uses real documents as reference", "Reduces hallucinations with facts"]
    ),
    
    # Hallucinations Questions
    Question(
        id=25,
        question="AI hallucinations occur when language models generate plausible-sounding but false information.",
        category="Hallucinations",
        is_hallucination=False,
        explanation="Correct! Hallucinations are when AI generates confident but factually incorrect information that sounds reasonable.",
        difficulty=Difficulty.BEGINNER,
        hints=["LLMs can sound confident but be wrong", "This is a real problem in AI"]
    ),
    Question(
        id=26,
        question="Hallucinations are completely eliminated in modern Large Language Models.",
        category="Hallucinations",
        is_hallucination=True,
        explanation="False! Hallucinations remain a significant challenge in LLMs. Techniques like RAG and fine-tuning help reduce them but don't eliminate them.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Even modern LLMs still hallucinate", "It's an ongoing challenge"]
    ),
    Question(
        id=27,
        question="Training data quality directly affects the likelihood of AI hallucinations.",
        category="Hallucinations",
        is_hallucination=False,
        explanation="True! Poor quality, biased, or incorrect training data increases hallucination likelihood. Data quality is crucial for reliable models.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Good data = better models", "Bad data = more hallucinations"]
    ),
    
    # Open Source LLMs Questions
    Question(
        id=28,
        question="LLaMA is an open-source large language model released by Meta.",
        category="Open Source LLMs",
        is_hallucination=False,
        explanation="Correct! LLaMA is Meta's open-source LLM family, comparable in performance to GPT models but more efficient.",
        difficulty=Difficulty.BEGINNER,
        hints=["LLaMA is from Meta (Facebook)", "It's open-source"]
    ),
    Question(
        id=29,
        question="Mistral 7B is a smaller open-source model that outperforms LLaMA 13B on most benchmarks.",
        category="Open Source LLMs",
        is_hallucination=False,
        explanation="True! Mistral 7B achieves impressive performance with only 7 billion parameters through clever architecture and training techniques.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Mistral is very efficient", "7B parameters are impressive"]
    ),
    Question(
        id=30,
        question="Open-source LLMs are always completely free to use commercially.",
        category="Open Source LLMs",
        is_hallucination=True,
        explanation="False! While many are free, their usage depends on the license. Some require attribution, others have commercial restrictions.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Check the license before using commercially", "Open-source doesn't always mean free for business"]
    ),
    
    # Advanced ML Questions
    Question(
        id=31,
        question="Attention mechanism allows neural networks to focus on important parts of input data.",
        category="Neural Networks",
        is_hallucination=False,
        explanation="Correct! Attention computes weighted sums of input values, allowing the model to focus on relevant information.",
        difficulty=Difficulty.EXPERT,
        hints=["Attention = weighted focus", "Allows selective concentration on input"]
    ),
    Question(
        id=32,
        question="Backpropagation can only work with acyclic computational graphs.",
        category="Machine Learning",
        is_hallucination=False,
        explanation="Technically correct - backpropagation computes gradients through DAGs. RNNs use modified backpropagation (BPTT) for sequential data.",
        difficulty=Difficulty.EXPERT,
        hints=["Think about DAGs and gradient flow", "RNNs need special handling"]
    ),
    Question(
        id=33,
        question="Batch normalization helps prevent internal covariate shift in deep networks.",
        category="Neural Networks",
        is_hallucination=False,
        explanation="True! Batch normalization normalizes layer inputs to have zero mean and unit variance, stabilizing training.",
        difficulty=Difficulty.EXPERT,
        hints=["Batch norm normalizes inputs", "Stabilizes deep network training"]
    ),
    
    # Additional Generative AI Questions
    Question(
        id=34,
        question="Diffusion models work by gradually removing noise from random data to generate images.",
        category="Generative AI",
        is_hallucination=False,
        explanation="Correct! Diffusion models like DALL-E 3 work by reversing a noising process, iteratively denoising to create images.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Start with noise, remove it iteratively", "Used in DALL-E, Stable Diffusion"]
    ),
    Question(
        id=35,
        question="VAE stands for 'Variational AutoEncoder' and is used for generative modeling.",
        category="Generative AI",
        is_hallucination=False,
        explanation="True! VAEs learn a latent space distribution for generating new data samples similar to training data.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["VAE = Variational + AutoEncoder", "Used for generative tasks"]
    ),
    
    # More Prompt Engineering
    Question(
        id=36,
        question="Few-shot learning in prompts means showing the model a few examples of the task.",
        category="Prompt Engineering",
        is_hallucination=False,
        explanation="Correct! Few-shot prompting provides example input-output pairs to guide the model's behavior without retraining.",
        difficulty=Difficulty.BEGINNER,
        hints=["Few examples in prompt", "Teaches the model by example"]
    ),
    Question(
        id=37,
        question="System prompts directly control LLM behavior by setting initial context and instructions.",
        category="Prompt Engineering",
        is_hallucination=False,
        explanation="True! System messages establish the model's role, tone, and behavioral guidelines for the conversation.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["System prompt = initial instructions", "Controls model behavior"]
    ),
    
    # More AI Agent Questions
    Question(
        id=38,
        question="Reinforcement Learning is commonly used to train AI agents to maximize rewards.",
        category="AI Agents",
        is_hallucination=False,
        explanation="Correct! RL agents learn policies that maximize cumulative rewards through interaction with their environment.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["RL = learn from rewards", "Used to train game-playing AI"]
    ),
    Question(
        id=39,
        question="Autonomous agents can make independent decisions without any human intervention.",
        category="AI Agents",
        is_hallucination=True,
        explanation="While some agents operate independently, most have safety checks and human oversight mechanisms. Full autonomy without safeguards is risky.",
        difficulty=Difficulty.EXPERT,
        hints=["Safety is important", "Most agents have human oversight"]
    ),
    
    # MLOps and Deployment
    Question(
        id=40,
        question="MLOps includes versioning models, data, and experiments for reproducibility.",
        category="Machine Learning",
        is_hallucination=False,
        explanation="True! MLOps (ML Operations) emphasizes versioning, monitoring, and reproducibility throughout the ML lifecycle.",
        difficulty=Difficulty.EXPERT,
        hints=["MLOps = ML Operations", "Focus on reproducibility"]
    ),
    
    # Fine-tuning Questions
    Question(
        id=41,
        question="Fine-tuning an LLM means training it further on task-specific data.",
        category="Generative AI",
        is_hallucination=False,
        explanation="Correct! Fine-tuning continues training a pre-trained model on domain-specific data to adapt it for specific tasks.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Fine-tuning = additional training", "Uses task-specific data"]
    ),
    Question(
        id=42,
        question="LoRA (Low-Rank Adaptation) reduces fine-tuning costs by modifying only certain model weights.",
        category="Generative AI",
        is_hallucination=False,
        explanation="True! LoRA reduces memory and computational costs by fine-tuning only low-rank weight updates instead of all parameters.",
        difficulty=Difficulty.EXPERT,
        hints=["LoRA = Low-Rank Adaptation", "Reduces computational cost"]
    ),
    
    # Embeddings
    Question(
        id=43,
        question="Word embeddings capture semantic meaning of words in vector form.",
        category="Machine Learning",
        is_hallucination=False,
        explanation="Correct! Embeddings like Word2Vec, GloVe represent words in dense vectors where similar words are close together.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Embeddings = vectors", "Similar words are close in space"]
    ),
    Question(
        id=44,
        question="BERT embeddings are context-independent and the same for each word appearance.",
        category="Machine Learning",
        is_hallucination=True,
        explanation="False! BERT provides contextual embeddings - the same word gets different embeddings based on context in the sentence.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["BERT is contextual", "Words change meaning with context"]
    ),
    
    # Vision Transformers
    Question(
        id=45,
        question="Vision Transformers (ViT) apply transformer architecture to image classification tasks.",
        category="Neural Networks",
        is_hallucination=False,
        explanation="True! Vision Transformers divide images into patches and apply transformer self-attention, achieving excellent results.",
        difficulty=Difficulty.EXPERT,
        hints=["ViT = transformers for images", "Images are divided into patches"]
    ),
    
    # More RAG
    Question(
        id=46,
        question="Semantic search in RAG finds documents by calculating similarity between embeddings.",
        category="RAG",
        is_hallucination=False,
        explanation="Correct! Semantic search uses embeddings to find contextually relevant documents, not just keyword matches.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Semantic = meaning-based", "Uses embeddings for similarity"]
    ),
    
    # Quantization
    Question(
        id=47,
        question="Model quantization reduces model size by representing weights with lower precision.",
        category="Machine Learning",
        is_hallucination=False,
        explanation="True! Quantization converts float32 to int8 or similar, reducing size and computation while maintaining reasonable accuracy.",
        difficulty=Difficulty.EXPERT,
        hints=["Quantization = lower precision", "Reduces model size"]
    ),
    
    # More Open Source
    Question(
        id=48,
        question="Hugging Face Hub hosts pre-trained models and datasets for the ML community.",
        category="Open Source LLMs",
        is_hallucination=False,
        explanation="Correct! Hugging Face is a major platform for sharing transformers, LLMs, and datasets.",
        difficulty=Difficulty.BEGINNER,
        hints=["Hugging Face = model hub", "Hosts pre-trained models"]
    ),
    
    # Tokenization
    Question(
        id=49,
        question="Tokenization breaks text into smaller units that models can process.",
        category="Generative AI",
        is_hallucination=False,
        explanation="True! Tokenization converts text into tokens (words, subwords, characters) that are converted to numerical IDs.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Tokens = smaller text units", "Models work with token IDs"]
    ),
    
    # Context Window
    Question(
        id=50,
        question="The context window of an LLM limits the total input and output tokens it can process.",
        category="Generative AI",
        is_hallucination=False,
        explanation="Correct! Context window size (like 4K, 128K for GPT-4) determines how much information an LLM can process at once.",
        difficulty=Difficulty.INTERMEDIATE,
        hints=["Context window = max tokens", "Determines input/output limits"]
    ),
]

# Function to get random questions by difficulty
def get_questions_by_difficulty(difficulty: str, count: int = 10):
    """Get random questions of a specific difficulty level"""
    import random
    filtered = [q for q in QUESTIONS if q.difficulty == difficulty]
    return random.sample(filtered, min(count, len(filtered)))

# Function to get all categories
def get_categories():
    """Get unique categories"""
    return sorted(list(set(q.category for q in QUESTIONS)))

# Function to get questions by category
def get_questions_by_category(category: str):
    """Get all questions from a specific category"""
    return [q for q in QUESTIONS if q.category == category]
