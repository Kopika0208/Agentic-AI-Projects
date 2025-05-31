# AutomatedStockSelector Crew

Automated Stock Selector is an intelligent agentic system built with CrewAI [crewAI](https://crewai.com, designed to autonomously identify and evaluate trending companies for investment. It uses a modular crew of specialized agents—Trending Company Finder, Financial Researcher, and Stock Picker—that collaborate in a hierarchical process. The agents rely on tools like SerperDevTool (Serper API) for web searching for real-time search insights and generate structured analysis using pydantic models. The workflow includes identifying trending stocks, conducting market and financial research, and ultimately recommending the most promising investment opportunity for a given sector—all orchestrated through YAML-based configurations for flexibility and scalability.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/automated_stock_selector/config/agents.yaml` to define your agents
- Modify `src/automated_stock_selector/config/tasks.yaml` to define your tasks
- Modify `src/automated_stock_selector/crew.py` to add your own logic, tools and specific args
- Modify `src/automated_stock_selector/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Automated_Stock_Selector Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Automated_Stock_Selector Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the AutomatedStockSelector Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
