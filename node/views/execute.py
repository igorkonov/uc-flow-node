from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            text_value = json.node.data.properties['text_field']
            number_value = json.node.data.properties['number_field']
            email = ''
            datetime = ''

            result_sum = int(text_value) + number_value

            if json.node.data.properties['switch_field']:
                result_sum = str(result_sum)

            if json.node.data.properties['toggle_field']:
                email = json.node.data.properties['email_field']
                datetime = json.node.data.properties['datetime_field']


            await json.save_result({
                "result_sum": result_sum,
                "email": email,
                "datetime": datetime
            })
            json.state = RunState.complete
        except ValueError as e:
            self.log.warning(f'Error {e}')
            await json.save_error("Неправильное значение в текстовом поле, должно быть число")
            json.state = RunState.error
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
