from typing import Union

from uc_flow_nodes.schemas import NodeRunContext as BaseNodeRunContext
from uc_flow_schemas.flow import Node as BaseNode

from node.provider.alfacrm import Authorization, CreateCustomer, DeleteCustomer, GetCustomers, UpdateCustomer


class NodeRunContext(BaseNodeRunContext):
    class Node(BaseNode):
        class Data(BaseNode.Data):
            properties: Union[
                Authorization,
                GetCustomers,
                CreateCustomer,
                UpdateCustomer,
                DeleteCustomer,
            ]

        data: Data

    node: Node
