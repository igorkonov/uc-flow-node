from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from node.provider.alfacrm import Action
from node.schemas.node import NodeRunContext


EMPTY_CONTENT = {'Result': 'Empty content'}

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            action: Action = json.node.data.properties
            request = action.get_request()
            base_response = await request.execute()
            response = action.validate_response(base_response)

            if response:
                results = action.process_content(response)

                await self.request_json.save_result(results)
            else:
                await json.save_result(EMPTY_CONTENT)
            json.state = RunState.complete


        except Exception as exp:
            self.log.warning(f'Error: {exp}')
            await json.save_error({'error': f'{exp}'})
            json.state = RunState.error

        return json
