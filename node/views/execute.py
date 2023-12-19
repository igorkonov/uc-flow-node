from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
from node.provider.hubspot import  HubspotCRUD, parameters_object
from uc_http_requester.requester import Request, Response
from uc_flow_nodes.schemas import NodeRunContext

from node.schemas.enums import CRM_V4, URL_API_GENERAL, Method, Resource

EMPTY_CONTENT = {'Result': 'Empty content'}

async def crud_object(json: NodeRunContext, token, method, object_type):
    auth_object = HubspotCRUD(token=token, object_type=object_type)

    object_params = (
        'deal_parameters' if object_type == Resource.deals else 'contacts_parameters'
    )

    try:
        if method == Method.list:
            limit = json.node.data.properties.get('limit', None)
            after = json.node.data.properties.get('after', None)
            properties = {'limit': limit, 'after': after}
            response: Response = await getattr(auth_object, method)(**properties)
        elif method in ('create', 'update', 'destroy', 'retrieve'):
            object_id = json.node.data.properties.get('object_id')
            properties = parameters_object(json.node.data.properties[object_params])
            if method == Method.create:
                response: Response = await auth_object.create(properties)
            elif method == Method.update:
                response: Response = await auth_object.update(object_id, properties)
            elif method == Method.destroy:
                response: Response = await auth_object.destroy(object_id)
            elif method == Method.retrieve:
                response: Response = await auth_object.retrieve(object_id)
        else:
            raise Exception(f'Неизвестный метод {method}')

        await json.save_result({'result': response.json()})

    except Exception as e:
        await json.save_result({'result': f'status code: {response.status_code}'})

async def association(json: NodeRunContext, token):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    parameters = parameters_object(json.node.data.properties['associations_parameters'], False)

    url = f"{URL_API_GENERAL}{CRM_V4}{parameters['fromObjectType']}/{parameters['fromObjectId']}" \
          f"/associations/default/{parameters['toObjectType']}/{parameters['toObjectId']}"

    response = await Request(
        url=url,
        method=Request.Method.put,
        headers=headers,
    ).execute()

    await json.save_result({'Result': response.json()})


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            resource = json.node.data.properties['resource']
            token = json.node.data.properties['token']
            method = json.node.data.properties['method']

            if resource in {Resource.deals, Resource.contacts}:
                await crud_object(json, token, method, resource)

            elif resource == Resource.associations:
                await association(json, token)
            else:
                await json.save_result(EMPTY_CONTENT)
            json.state = RunState.complete

        except Exception as exp:
            self.log.warning(f'Error: {exp}')
            await json.save_error({'error': f'{exp}'})
            json.state = RunState.error

        return json
