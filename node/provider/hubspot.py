from json import JSONDecodeError
from typing import List, Optional
import ujson
from uc_http_requester.requester import Request, Response

from node.schemas.enums import (
    URL_API_GENERAL,
    CRM_V3,
)


class Config:
    arbitrary_types_allowed = True


def validate_response(response: dict) -> [dict, List[dict]]:
    try:
        if response.status_code != 200:
            raise Exception(
                f'{response.get("status_code") =} {response.get("content") = }')
        if response.content:
            content = ujson.loads(response.content)
            if content.get('errors'):
                raise Exception(f'content errors: {content = }')
        else:
            content = dict()
    except JSONDecodeError:
        raise Exception(JSONDecodeError)
    return content


def get_attr(params, attr):
    obj = params.__getattribute__(attr)
    return obj[0].__getattribute__(attr) if obj else None


def params_delete_none_object(params) -> dict:
    return {key: value for key, value in params.items() if value is not None}


def process_content(response: dict) -> [dict, List[dict]]:
    return response

class HubspotCRUD:
    def __init__(self, token: str, object_type: str):
        self.object_type = object_type
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }

    async def get_request(self, method: str, url: str, json_data: Optional[dict] = None) -> Response:

        response = await Request(
            url=url,
            method=method,
            headers=self.headers,
            json=json_data
        ).execute()
        return response

    async def create(self, params) -> Response:
        url = f'{URL_API_GENERAL}{CRM_V3}{self.object_type}'
        return await self.get_request(Request.Method.post, url, json_data=params)

    async def list(self, limit: int, after: str) -> Response:
        url = f'{URL_API_GENERAL}{CRM_V3}{self.object_type}'
        if limit:
            url += f'?limit={limit}'
        if after:
            url += f'&after={after}'
        return await self.get_request(Request.Method.get, url)

    async def retrieve(self, object_id: int) -> Response:
        url = f'{URL_API_GENERAL}{CRM_V3}{self.object_type}/{object_id}'
        return await self.get_request(Request.Method.get, url)

    async def update(self, object_id: int, params) -> Response:
        url = f'{URL_API_GENERAL}{CRM_V3}{self.object_type}/{object_id}'
        return await self.get_request(Request.Method.patch, url, json_data=params)

    async def destroy(self, object_id: int) -> Response:
        url = f'{URL_API_GENERAL}{CRM_V3}{self.object_type}/{object_id}'
        return await self.get_request(Request.Method.delete, url)


def parameters_object(params, properties_flag=True):
    properties = {param: params[param][0][param] for param in params if params[param]}

    if properties_flag:
        return {'properties': properties}
    else:
        return properties
