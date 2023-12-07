from json import JSONDecodeError
from typing import Literal, List, Optional
from urllib.parse import urljoin

import ujson
from pydantic import BaseModel, AnyHttpUrl, parse_obj_as
from uc_http_requester.requester import Request

from node.schemas.enums import URL_API_GENERAL, HEADER_TOKEN, AuthParameters, Method, Operation, Resource, Parameters
from node.schemas.models import (
    CustomerId,
    CustomerName,
    BranchIds,
    DateFrom,
    DateTo,
    IsStudy,
    LegalType,
    Phone,
)


class Config:
    arbitrary_types_allowed = True


class BaseParameters(BaseModel):
    ...

class Action(BaseModel):
    resource: Optional[str]
    operation: Optional[str]
    method: Optional[str]
    api_key: str
    email: str


    @staticmethod
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

    @staticmethod
    def get_attr(params, attr):
        obj = params.__getattribute__(attr)
        return obj[0].__getattribute__(attr) if obj else None

    @staticmethod
    def params_delete_none_object(params) -> dict:
        return {key: value for key, value in params.items() if value is not None}


    def process_content(self, response: dict) -> [dict, List[dict]]:
        return response


class Authorization(Action):
    action: Literal[AuthParameters.auth]
    hostname: str
    branch_id: int
    email: str
    api_key: str

    def get_request_params(self) -> dict:
        auth_data = {
            "email": self.email,
            "api_key": self.api_key,
        }
        return auth_data

    def get_request_url(self) -> str:
        path = f"https://{self.hostname}{URL_API_GENERAL}{Operation.auth_login}"
        return path

    def get_request(self) -> Request:

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            }
        return Request(
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=Request.Method.post,
            json=self.get_request_params(),
            headers=headers,
        )

    def process_content(self, response: dict) -> [dict, List[dict]]:
        response.update(
            {
                'branch_id': self.branch_id,
                'hostname': self.hostname,
                "email": self.email,
                "api_key": self.api_key,
            }
        )
        return response

    def validate_response(self, response) -> [dict, List[dict]]:
        result = super().validate_response(response)
        result.update(
            {
                'branch_id': self.branch_id,
                'hostname': self.hostname,
                "email": self.email,
                "api_key": self.api_key,
            }
        )
        return result

class GetCustomers(Action):
    class Parameters(BaseParameters):
        id: Optional[List[CustomerId]]
        is_study: Optional[List[IsStudy]]
        name: Optional[List[CustomerName]]
        date_from: Optional[List[DateFrom]]
        date_to: Optional[List[DateTo]]
        phone: Optional[List[Phone]]

    action: Literal[AuthParameters.get_data]
    resource: Literal[Resource.customer]
    operation: Literal[Method.index_]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            params['id'] = self.get_attr(f, Parameters.id)
            is_study = self.get_attr(f, Parameters.is_study)
            params['is_study'] = None if not is_study else is_study
            params['name'] = self.get_attr(f, Parameters.name)
            params['date_from'] = self.get_attr(f, Parameters.date_from)
            params['date_to'] = self.get_attr(f, Parameters.date_to)
            params['phone'] = self.get_attr(f, Parameters.phone)
        params = self.params_delete_none_object(params)
        return params

    def get_request_url(self) -> str:
        path = f"https://{self.auth_data['hostname']}{URL_API_GENERAL}{self.auth_data['branch_id']}/{Operation.get_customer}"
        return path

    def get_request(self) -> Request:

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            HEADER_TOKEN: self.auth_data['token'],
            }
        return Request(
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=Request.Method.post,
            headers=headers,
            json=self.get_request_params()
        )

class CreateCustomer(Action):
    class Parameters(BaseParameters):
        id: Optional[List[CustomerId]]
        is_study: Optional[List[IsStudy]]
        name: Optional[List[CustomerName]]
        branch_ids: Optional[List[BranchIds]]
        legal_type: Optional[List[LegalType]]

    action: Literal[AuthParameters.get_data]
    resource: Literal[Resource.customer]
    operation: Literal[Method.create]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            is_study = self.get_attr(f, Parameters.is_study)
            params['is_study'] = None if not is_study else int(is_study)
            params['name'] = self.get_attr(f, Parameters.name)
            params['branch_ids'] = self.get_attr(f, Parameters.branch_ids)
            params['legal_type'] = self.get_attr(f, Parameters.legal_type)
        params = self.params_delete_none_object(params)
        return params

    def get_request_url(self) -> str:
        path = f"https://{self.auth_data['hostname']}{URL_API_GENERAL}{self.auth_data['branch_id']}/{Operation.create_customer}"
        return path

    def get_request(self) -> Request:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            HEADER_TOKEN: self.auth_data['token']
            }
        return Request(
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=Request.Method.post,
            headers=headers,
            json=self.get_request_params()
        )


class UpdateCustomer(Action):
    class Parameters(BaseParameters):
        id: Optional[List[CustomerId]]
        name: Optional[List[CustomerName]]

    action: Literal[AuthParameters.get_data]
    resource: Literal[Resource.customer]
    operation: Literal[Method.update]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            params['id'] = self.get_attr(f, Parameters.id)
            params['name'] = self.get_attr(f, Parameters.name)
        params = self.params_delete_none_object(params)
        return params

    def get_request_url(self) -> str:
        path = f"https://{self.auth_data['hostname']}{URL_API_GENERAL}{self.auth_data['branch_id']}/{Operation.update_customer}?id={Parameters.id}"
        return path

    def get_request(self) -> Request:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            HEADER_TOKEN: self.auth_data['token']
            }
        params = self.get_request_params()
        query_params = {'id': params.pop('id')}
        return Request(
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=Request.Method.post,
            headers=headers,
            json=params,
            params=query_params,
        )


class DeleteCustomer(Action):
    class Parameters(BaseParameters):
        id: Optional[List[CustomerId]]
        name: Optional[List[CustomerName]]

    action: Literal[AuthParameters.get_data]
    resource: Literal[Resource.customer]
    operation: Literal[Method.delete]
    auth_data: dict
    parameters: Optional[Parameters]

    def get_request_params(self) -> dict:
        params = dict()
        f = self.parameters
        if f:
            params['id'] = self.get_attr(f, Parameters.id)
            params['name'] = self.get_attr(f, Parameters.name)
        params = self.params_delete_none_object(params)
        return params

    def get_request_url(self) -> str:
        path = f"https://{self.auth_data['hostname']}{URL_API_GENERAL}{self.auth_data['branch_id']}/{Operation.delete_customer}/?id={Parameters.id}"
        return path

    def get_request(self) -> Request:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            HEADER_TOKEN: self.auth_data['token']
            }
        return Request(
            url=self.get_request_url(),
            method=Request.Method.post,
            headers=headers,
            json=self.get_request_params(),
        )
