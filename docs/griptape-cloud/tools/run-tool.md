# Running a Tool

Once your Tool is created and deployed, you can run your Tool one of three ways outlined below. You may view the details of any of your runs, no matter how you created them, in the `Runs` tab of your Tool.

## From the Cloud Console

Go to the `Test` tab of your Tool to open the generated OpenAPI spec. From there, the Swagger UI can be used to create test requests.

## From the API

The API route for Tool activities is in the form of `https://cloud.griptape.ai/api/tools/{tool_id}/activities/{activity_name}`, where `tool_id` is the resource UUID of your created Tool, and `activity_name` is the name of the activity as defined in your `BaseTool` class. The activity routes will only accept an http POST method.

To fetch the OpenAPI schema, the route is `https://cloud.griptape.ai/api/tools/{tool_id}/openapi`.

```bash
--8<-- "docs/griptape-cloud/tools/src/griptape_cloud_tool.sh"
```

## Using the Griptape Framework

The Griptape framework provides a [`GriptapeCloudToolTool`](../../griptape-tools/official-tools/griptape-cloud-tool-tool.md) for interacting with your deployed Tools. Simply pass your Tool resource UUID as the `tool_id` kwarg, and the schema and activity methods will be dynamically set on the Tool.
