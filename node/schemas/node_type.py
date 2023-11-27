from typing import List
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, DisplayOptions, OptionValue

from node.schemas.enums import Values


class NodeType(flow.NodeType):
    id: str = '3aa5720b-0a02-4f8c-8397-872378a23200'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'test_cube'
    is_public: bool = False
    displayName: str = 'Test cube'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'Кубик для практики'
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
            displayName='Число/текст',
            name='switch_field',
            type=Property.Type.BOOLEAN,
            description='Переключатель влияет на тип возвращаемых данных. int/str',
            required=True,
            default=True,
        ),
        Property(
            displayName='Переключатель',
            name='toggle_field',
            type=Property.Type.BOOLEAN,
            description='Отображает дополнительные поля',
            required=True,
            default=False,
        ),
        Property(
            displayName="Значение 1",
            name="value_1",
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name="Значение 1",
                    value=Values.value_1,
                    description="",
                ),
                OptionValue(
                    name="Значение 2",
                    value=Values.value_2,
                    description="",
                ),
            ],
            displayOptions=DisplayOptions(
                show={"toggle_field": [True]},
            ),
        ),
        Property(
            displayName="Значение 2",
            name="value_2",
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name="Значение 1",
                    value=Values.value_1,
                    description="",
                ),
                OptionValue(
                    name="Значение 2",
                    value=Values.value_2,
                    description="",
                ),
            ],
            displayOptions=DisplayOptions(
                show={"toggle_field": [True]},
            ),
        ),
        Property(
            displayName="Почта",
            name="email_field",
            type=Property.Type.EMAIL,
            placeholder="Введите почту",
            description="Поле для ввода почты",
            required=True,
            displayOptions=DisplayOptions(
                show={
                    "toggle_field": [True],
                    "value_1": [Values.value_1],
                    "value_2": [Values.value_2],
                },
            ),
        ),
        Property(
            displayName="Дата и время",
            name="datetime_field",
            type=Property.Type.DATETIME,
            placeholder="Введите дату и время",
            description="Поле для ввода даты и время",
            required=True,
            displayOptions=DisplayOptions(
                show={
                    "toggle_field": [True],
                    "value_1": [Values.value_1],
                    "value_2": [Values.value_2],
                },
            ),
        ),
    ]
