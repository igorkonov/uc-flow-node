from typing import List
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, DisplayOptions, OptionValue

from node.schemas.enums import AuthParameters, Method, Parameters, Resource



class NodeType(flow.NodeType):
    id: str = '3aa5720b-0a02-4f8c-8397-872378a23200'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'AlfaCRM'
    is_public: bool = False
    displayName: str = 'AlfaCRM'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    group: List[str] = ["integration"]
    description: str = 'AlfaCRM_integration'
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='Действие',
            name='action',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            description='Выберите действие кубика',
            options=[
                OptionValue(
                    name='Авторизация',
                    value=AuthParameters.auth,
                    description='Авторизация пользователя',
                ),
                OptionValue(
                    name='Запрос',
                    value=AuthParameters.get_data,
                    description='Получить данные',
                ),
            ],
        ),
        Property(
            displayName='Адрес CRM',
            name='hostname',
            type=Property.Type.STRING,
            description='Введите адрес CRM',
            noDataExpression=True,
            default='uiscom.s20.online',
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.auth,
                    ],
                },
            ),
        ),
        Property(
            displayName='ID филиала',
            name='branch_id',
            type=Property.Type.NUMBER,
            description='Введите ID филиала',
            default=1,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.auth,
                    ],
                },
            ),
        ),
        Property(
            displayName='E-mail',
            name='email',
            type=Property.Type.EMAIL,
            description='Введите email',
            default='vehemop789@weirby.com',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.auth,
                    ],
                },
            ),
        ),
        Property(
            displayName='Ключ API (v2api)',
            name='api_key',
            type=Property.Type.STRING,
            description='Введите ваш API ключ (v2api)',
            default='7acaf091-77b5-11ee-8640-3cecef7ebd64',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.auth,
                    ],
                },
            ),
        ),
        Property(
            displayName='auth_data',
            name='auth_data',
            type=Property.Type.JSON,
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                },
            ),
        ),
        Property(
            displayName='Сущность',
            name='resource',
            type=Property.Type.OPTIONS,
            description='Выберите сущность',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Customer',
                    value=Resource.customer,
                    description='Пользователь',
                ),
            ],
        ),
        Property(
            displayName='Операция',
            name='operation',
            type=Property.Type.OPTIONS,
            description='Выберите операцию',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Index',
                    value=Method.index_,
                    description='Получить клиента',
                ),
                OptionValue(
                    name='Create',
                    value=Method.create,
                    description='Создать клиента',
                ),
                OptionValue(
                    name='Update',
                    value=Method.update,
                    description='Изменить клиента',
                ),
                OptionValue(
                    name='Delete',
                    value=Method.delete,
                    description='Удалить клиента',
                ),
            ],
        ),
        Property(
            displayName='Параметры',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Method.index_,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='ID клиента',
                    name=Parameters.id,
                    description='id клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default='',
                            name=Parameters.id,
                        ),
                    ],
                ),
                Property(
                    displayName='is_study',
                    name=Parameters.is_study,
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.is_study,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='имя клиента',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='',
                            name=Parameters.name,
                        ),
                    ],
                ),
                Property(
                    displayName='date_from',
                    name=Parameters.date_from,
                    description='дата добавления от, date',
                    values=[
                        Property(
                            type=Property.Type.DATETIME,
                            name=Parameters.date_from,
                        ),
                    ],
                ),
                Property(
                    displayName='date_to',
                    name=Parameters.date_to,
                    description='дата добавления до, date',
                    values=[
                        Property(
                            type=Property.Type.DATETIME,
                            name=Parameters.date_to,
                        ),
                    ],
                ),
                Property(
                    displayName='phone',
                    name=Parameters.phone,
                    description='контакты клиента',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='',
                            name=Parameters.phone,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Параметры',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Method.create,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='is_study',
                    name=Parameters.is_study,
                    description='состояние клиента ( 0 - лид, 1 - клиент)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.is_study,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='полное имя',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='Igor Konov',
                            name=Parameters.name,
                        ),
                    ],
                ),
                Property(
                    displayName='branch_ids',
                    name=Parameters.branch_ids,
                    description='массив идентификаторов филиалов (Branch)',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=Parameters.branch_ids,
                        ),
                    ],
                ),
                Property(
                    displayName='legal_type',
                    name=Parameters.legal_type,
                    description='тип клиента (1 - физ. лицо, 2 - юр. лицо)',
                    values=[
                        Property(
                            type=Property.Type.BOOLEAN,
                            default=True,
                            name=Parameters.legal_type,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Параметры',
            name='parameters',
            type=Property.Type.COLLECTION,
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Method.update,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='ID клиента',
                    name=Parameters.id,
                    description='id клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default=1,
                            name=Parameters.id,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='полное имя',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='New Test',
                            name=Parameters.name,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Параметры',
            name='parameters',
            type=Property.Type.COLLECTION,
            placeholder='Add',
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'action': [
                        AuthParameters.get_data,
                    ],
                    'resource': [
                        Resource.customer,
                    ],
                    'operation': [
                        Method.delete,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='ID клиента',
                    name=Parameters.id,
                    description='id клиента',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default=1,
                            name=Parameters.id,
                        ),
                    ],
                ),
                Property(
                    displayName='name',
                    name=Parameters.name,
                    description='полное имя',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='New Test',
                            name=Parameters.name,
                        ),
                    ],
                ),
            ],
        ),
    ]
