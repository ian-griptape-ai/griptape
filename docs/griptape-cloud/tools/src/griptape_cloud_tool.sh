export GT_CLOUD_API_KEY="<your API key here>"
export GT_CLOUD_TOOL_ID="<your tool ID here>"
export TOOL_ACTIVITY_URL="https://api.griptape.com/v1/tools/${GT_CLOUD_TOOL_ID}/activities/my_activity"

response=$(curl -X POST -H "Authorization: Bearer ${GT_CLOUD_API_KEY}" --json '{"my_key": "my_value"}' ${TOOL_ACTIVITY_URL})
echo "my_activity response: ${response}"
