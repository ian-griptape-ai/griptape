# Tools

Tools can be used to execute arbitrary actions in a request/response format. They can be given to an LLM so the LLM can take appropriate action based on the input, Tool description, and the description of each Tool activity.

## Create a Tool

1. [Connect Your GitHub Account in your Griptape Cloud account](https://cloud.griptape.ai/account)
1. Install the [Griptape Cloud GitHub app to your GitHub account or organization](https://github.com/apps/griptape-cloud/installations/new/)
   - Be sure to allow the app access to `All Repositories` or select the specific repositories you need
1. Ensure your repository has a Tool Config YAML file
   - To learn more see [Tool Config YAML](tool-config.md)

You can now [create a Tool in the Griptape Cloud console](https://cloud.griptape.ai/tools/create) by providing your GitHub repository information.

### Quickstart With Samples and Templates

To get started with Structures in the Cloud, check out the [managed-tool-template on GitHub](https://github.com/griptape-ai/managed-tool-template) or deploy one of the [griptape-sample-tools from GitHub](https://github.com/griptape-ai/griptape-sample-tools/tree/main).
