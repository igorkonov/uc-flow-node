from typing import List, Optional

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    CredentialProtocol,
)


class CredentialType(flow.CredentialType):
    id: str = 'alfacrm_api_auth'
    is_public: bool = True
    displayName: str = 'AlfaCRM API Auth'
    protocol: CredentialProtocol = CredentialProtocol.ApiKey
    protected_properties: List[Property] = []
    properties: List[Property] = [
        Property(
            displayName='CRM Address',
            name='crm_address',
            type=Property.Type.STRING,
            default='',
        ),
        Property(
            displayName='Branch ID',
            name='branch_id',
            type=Property.Type.NUMBER,
            default='',
        ),
        Property(
            displayName='Email',
            name='email',
            type=Property.Type.EMAIL,
            default='',
        ),
        Property(
            displayName='API key',
            name='api_key',
            type=Property.Type.STRING,
            default='',
        ),
    ]
    extends: Optional[List[str]] = []
