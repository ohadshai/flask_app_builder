from flask import request


from flask_appbuilder.api import BaseApi, expose

class SecurityApi(BaseApi):

    # resource_name = "jobs"
    openapi_spec_tag = "Jobs"

    # def add_apispec_components(self, api_spec):
    #     super(SecurityApi, self).add_apispec_components(api_spec)
    #     jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    #     api_spec.components.security_scheme("jwt", jwt_scheme)
    #     api_spec.components.security_scheme("jwt_refresh", jwt_scheme)

    @expose("/get_job_results/<job_id>", methods=["GET", "POST"])
    def get_job_results(self, job_id=None):
        """Get all job's results from ELK according to job_id (if exists) and filter jsob in body
        ---
        post:
          description: >-
            Get all job's results from ELK according to job_id (if exists) and filter jsob in body
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    job_type:
                      description: job type
                      example: PE
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

    @expose("/run_job", methods=["POST"])
    def run_job(self):
        """
            Security endpoint for the refresh token, so we can obtain a new
            token without forcing the user to login again
        ---
        post:
          description: >-
            Use the refresh token to get a new JWT access token
          responses:
            200:
              description: Refresh Successful
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      access_token:
                        description: A new refreshed access token
                        type: string
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
          security:
            - jwt_refresh: []
        """
        resp = {
            API_SECURITY_ACCESS_TOKEN_KEY: create_access_token(
                identity=get_jwt_identity(), fresh=False
            )
        }
        return self.response(200, **resp)
