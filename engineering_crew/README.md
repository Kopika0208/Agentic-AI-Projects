# Engineering Crew 

EngineeringCrew is a modular, agentic engineering system built with CrewAI, designed to collaboratively design, develop, and test software solutions in an autonomous, production-like environment. It leverages a crew of specialized agents—Engineering Lead, Backend Engineer, Frontend Engineer, and Test Engineer—each assigned well-defined tasks in a sequential pipeline to simulate an agile development workflow.

These agents are configured using YAML files for both roles and responsibilities (agents.yaml) and project deliverables (tasks.yaml), enabling flexibility and easy scaling. The backend and test engineers are equipped with secure code execution capabilities (Docker sandboxed) for safe and automated code generation and testing.

The crew executes a series of tasks—Design Task, Code Task, Frontend Task, and Test Task—to move from planning to implementation and validation. Orchestrated through CrewAI’s @CrewBase framework, this system exemplifies structured collaboration among autonomous agents, supporting reproducible and auditable software engineering pipelines ideal for AI-driven development projects.


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

- Modify `src/engineering_crew/config/agents.yaml` to define your agents
- Modify `src/engineering_crew/config/tasks.yaml` to define your tasks
- Modify `src/engineering_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/engineering_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Engineering_Crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Engineering_Crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the EngineeringCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
