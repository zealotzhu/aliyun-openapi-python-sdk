# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkopenanalytics_open.endpoint import endpoint_data

class SetAllowIPRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'openanalytics-open', '2018-06-19', 'SetAllowIP','openanalytics')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NetworkType(self):
		return self.get_body_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_body_params('NetworkType', NetworkType)

	def get_Product(self):
		return self.get_body_params().get('Product')

	def set_Product(self,Product):
		self.add_body_params('Product', Product)

	def get_AllowIP(self):
		return self.get_body_params().get('AllowIP')

	def set_AllowIP(self,AllowIP):
		self.add_body_params('AllowIP', AllowIP)

	def get_Append(self):
		return self.get_body_params().get('Append')

	def set_Append(self,Append):
		self.add_body_params('Append', Append)