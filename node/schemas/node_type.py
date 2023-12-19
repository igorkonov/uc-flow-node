from typing import List
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, DisplayOptions, OptionValue

from node.schemas.enums import Resource, Method, ContactsParameters, DealsParameters, AssociationsParameters



class NodeType(flow.NodeType):
    id: str = '3aa5720b-0a02-4f8c-8397-872378a23200'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'HubSpot'
    is_public: bool = False
    displayName: str = 'HubSpot'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    group: List[str] = ["integration"]
    description: str = 'Hubspot_integration'
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            description='Выберите объект',
            options=[
                OptionValue(
                    name='contacts',
                    value=Resource.contacts,
                    description='',
                ),
                OptionValue(
                    name='deals',
                    value=Resource.deals,
                    description='',
                ),
                OptionValue(
                    name='associations',
                    value=Resource.associations,
                    description='',
                ),
            ],
        ),
        Property(
            displayName='Access token',
            name='token',
            type=Property.Type.STRING,
            required=True,
        ),
        Property(
            displayName='Method',
            name='method',
            type=Property.Type.OPTIONS,
            description='Выберите метод',
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.contacts,
                        Resource.deals
                    ],
                },
            ),
            options=[
                OptionValue(
                    name='Create',
                    value=Method.create,
                    description='Создать',
                ),
                OptionValue(
                    name='List',
                    value=Method.list,
                    description='Получить весь список',
                ),
                OptionValue(
                    name='Retrieve',
                    value=Method.retrieve,
                    description='Получить по id',
                ),
                OptionValue(
                    name='Update',
                    value=Method.update,
                    description='Изменить',
                ),
                OptionValue(
                    name='Destroy',
                    value=Method.destroy,
                    description='Удалить',
                ),
            ],
        ),
        Property(
            displayName='Object id',
            name='object_id',
            type=Property.Type.NUMBER,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.deals,
                        Resource.contacts,
                        ],
                    'method': [
                        Method.retrieve,
                        Method.update,
                        Method.destroy,
                        ],
                }
            )
        ),
        Property(
            displayName='Limit',
            name='limit',
            type=Property.Type.NUMBER,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.deals,
                        Resource.contacts,
                        ],
                    'method': [Method.list],
                },
            ),
        ),
        Property(
            displayName='After',
            name='after',
            type=Property.Type.STRING,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.deals,
                        Resource.contacts,
                        ],
                    'method': [Method.list],
                },
            ),
        ),
        Property(
            displayName='Параметры',
            name='deal_parameters',
            type=Property.Type.COLLECTION,
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.deals,
                        ],
                    'method': [
                        Method.create,
                        Method.list,
                        Method.update,
                        ],
                }
            ),
            options=[
                Property(
                    displayName='Amount',
                    name=DealsParameters.amount,
                    description='сумма сделки',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            default=1500.00,
                            name=DealsParameters.amount,
                        ),
                    ],
                ),
                Property(
                    displayName='Close Date',
                    name=DealsParameters.closedate,
                    description='Дата закрытия сделки',
                    values=[
                        Property(
                            type=Property.Type.DATETIME,
                            name=DealsParameters.closedate,
                        ),
                    ],
                ),
                Property(
                    displayName='Deal name',
                    name=DealsParameters.dealname,
                    description='название сделки',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='New deal',
                            name=DealsParameters.dealname,
                        ),
                    ],
                ),
                Property(
                    displayName='Pipeline',
                    name=DealsParameters.pipeline,
                    description='паплайн сделки',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='default',
                            name=DealsParameters.pipeline,
                        ),
                    ],
                ),
                Property(
                    displayName='Deal stage',
                    name=DealsParameters.dealstage,
                    description='этап сделки',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='contractsent',
                            name=DealsParameters.dealstage,
                        ),
                    ],
                ),
                Property(
                    displayName='Hubspot owner id',
                    name=DealsParameters.hubspot_owner_id,
                    description='id владельца hubspot',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=DealsParameters.hubspot_owner_id,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Параметры',
            name='contacts_parameters',
            type=Property.Type.COLLECTION,
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.contacts,
                    ],
                    'method': [
                        Method.create,
                        Method.list,
                        Method.update
                    ],
                },
            ),
            options=[
                Property(
                    displayName='Email',
                    name=ContactsParameters.email,
                    description='email контакта',
                    values=[
                        Property(
                            type=Property.Type.EMAIL,
                            default='super@gmail.com',
                            name=ContactsParameters.email,
                        ),
                    ],
                ),
                Property(
                    displayName='Firstname',
                    name=ContactsParameters.firstname,
                    description='имя контакта',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='Ja',
                            name=ContactsParameters.firstname,
                        ),
                    ],
                ),
                Property(
                    displayName='Lastname',
                    name=ContactsParameters.lastname,
                    description='фамилия контакта',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='Do',
                            name=ContactsParameters.lastname,
                        ),
                    ],
                ),
                Property(
                    displayName='Phone',
                    name=ContactsParameters.phone,
                    description='телефон контакта',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='(555) 555-5555',
                            name=ContactsParameters.phone,
                        ),
                    ],
                ),
                Property(
                    displayName='Company',
                    name=ContactsParameters.company,
                    description='компания',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            default='HubSpot',
                            name=ContactsParameters.company,
                        ),
                    ],
                ),
                Property(
                    displayName='Website',
                    name=ContactsParameters.website,
                    description='вебсайт',
                    values=[
                        Property(
                            type=Property.Type.URL,
                            name=ContactsParameters.website,
                        ),
                    ],
                ),
            ],
        ),
        Property(
            displayName='Association type id',
            name='association_type_id',
            type=Property.Type.NUMBER,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.associations,
                        ],
                }
            ),
        ),
        Property(
            displayName='Параметры',
            name='associations_parameters',
            type=Property.Type.COLLECTION,
            default={},
            noDataExpression=True,
            displayOptions=DisplayOptions(
                show={
                    'resource': [
                        Resource.associations,
                    ],
                },
            ),
            options=[
                Property(
                    displayName='From object type',
                    name=AssociationsParameters.from_object_type,
                    description='идентификатор объекта, с которым вы связываетесь',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            name=AssociationsParameters.from_object_type,
                        ),
                    ],
                ),
                Property(
                    displayName='From object id',
                    name=AssociationsParameters.from_object_id,
                    description='идентификатор записи, которую нужно связать',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=AssociationsParameters.from_object_id,
                        ),
                    ],
                ),
                Property(
                    displayName='To object type',
                    name=AssociationsParameters.to_object_type,
                    description='идентификатор объекта, с которым вы связываете запись',
                    values=[
                        Property(
                            type=Property.Type.STRING,
                            name=AssociationsParameters.to_object_type,
                        ),
                    ],
                ),
                Property(
                    displayName='To object id',
                    name=AssociationsParameters.to_object_id,
                    description='идентификатор записи, с которой нужно связать запись.',
                    values=[
                        Property(
                            type=Property.Type.NUMBER,
                            name=AssociationsParameters.to_object_id,
                        ),
                    ],
                ),
            ],
        ),
    ]
