import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = '3aa5720b-0a02-4f8c-8397-872378a23200'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'sum_field'
    is_public: bool = False
    displayName: str = 'Sum_field'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'Сервис возвращает сумму двух полей'
    properties: List[Property] = [
        Property(
            displayName='Текстовое поле',
            name='text_field',
            type=Property.Type.STRING,
            placeholder='Введите число',
            description='Текстовое поле',
            required=True,
            default='0',
        ),
        Property(
            displayName='Числовое поле',
            name='number_field',
            type=Property.Type.NUMBER,
            placeholder='Введите любое число',
            description='Числовое поле',
            required=True,
            default=0,
        ),
        Property(
            displayName='Переключатель',
            name='switch_field',
            type=Property.Type.BOOLEAN,
            placeholder='Переключить',
            description='Переключатель влияет на тип возвращаемых данных. Число/текст',
            required=True,
            default=True,
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            text_value = json.node.data.properties['text_field']
            number_value = json.node.data.properties['number_field']

            result = int(text_value) + number_value

            if json.node.data.properties['switch_field']:
                result = str(result)

            await json.save_result({
                "result": result
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


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
