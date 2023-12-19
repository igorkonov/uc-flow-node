from enum import Enum

URL_API_GENERAL = 'https://api.hubapi.com'
CRM_V3 = '/crm/v3/objects/'
CRM_V4 = '/crm/v4/objects/'


class Resource(str, Enum):
    contacts = 'contacts'
    deals = 'deals'
    associations = 'associations'


class Method(str, Enum):
    create = 'create'
    list = 'list'
    retrieve = 'retrieve'
    update = 'update'
    destroy = 'destroy'


class ContactsParameters(str, Enum):
    email = 'email'
    firstname = 'firstname'
    lastname = 'lastname'
    phone = 'phone'
    company = 'company'
    website = 'website'


class DealsParameters(str, Enum):
    amount = 'amount'
    closedate = 'closedate'
    dealname = 'dealname'
    pipeline = 'pipeline'
    dealstage = 'dealstage'
    hubspot_owner_id = 'hubspot_owner_id'


class AssociationsParameters(str, Enum):
    from_object_type = 'fromObjectType'
    from_object_id = 'fromObjectId'
    to_object_type = 'toObjectType'
    to_object_id = 'toObjectId'
