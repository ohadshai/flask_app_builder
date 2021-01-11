from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required,
)

from flask_appbuilder.api import BaseApi, expose
# from ..const import (
#     API_SECURITY_ACCESS_TOKEN_KEY,
#     API_SECURITY_PASSWORD_KEY,
#     API_SECURITY_PROVIDER_DB,
#     API_SECURITY_PROVIDER_KEY,
#     API_SECURITY_PROVIDER_LDAP,
#     API_SECURITY_REFRESH_KEY,
#     API_SECURITY_REFRESH_TOKEN_KEY,
#     API_SECURITY_USERNAME_KEY,
#     API_SECURITY_VERSION,
# )


class DevicesApi(BaseApi):

    resource_name = "devices"
    openapi_spec_tag = "Devices"

    # def add_apispec_components(self, api_spec):
    #     super(SecurityApi, self).add_apispec_components(api_spec)
    #     jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    #     api_spec.components.security_scheme("jwt", jwt_scheme)
    #     api_spec.components.security_scheme("jwt_refresh", jwt_scheme)

    @expose("/", methods=["POST"])
    # @safe
    def devices(self):
        """Get all devices from DSM according to filter
        ---
        post:
          description: >-
            Get all devices from DSM according to filter
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    hardware:
                      description: Hardware of device
                      example: 11 Pro
                      type: string
                    software:
                      description: Software of device
                      example: 14.1
                      type: string
                    udid:
                      description: Udid of device
                      example: 03b2e7e071054cf1a82e03aaa8b141b7
                      type: string
                    pac:
                      description: device hardware preference - X and above
                      example: true
                      type: boolean
                    "[device_info]":
                      description: device attributes
                      example: DeviceName=IPhone
                      type: string
          responses:
            200:
              description: all devices that qualify the filter the user sent
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      udid/hardware-software:
                        type: json

            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
        """
        if not request.is_json:
            return self.response_400(message="Request payload is not JSON")
        resp = dict()
        return self.response(200, **resp)

