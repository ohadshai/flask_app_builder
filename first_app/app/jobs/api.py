from flask import request


from flask_appbuilder.api import BaseApi, expose

class JobsApi(BaseApi):

    resource_name = "jobs"
    openapi_spec_tag = "Jobs"

    # def add_apispec_components(self, api_spec):
    #     super(SecurityApi, self).add_apispec_components(api_spec)
    #     jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    #     api_spec.components.security_scheme("jwt", jwt_scheme)
    #     api_spec.components.security_scheme("jwt_refresh", jwt_scheme)

    @expose("/get_summary/", methods=["GET"])
    def get_jobs_summary(self):
        """Get all job's results from SQL DB according to job_id (if exists) and filter json in body
        ---
        get:
          description: >-
            Get all job's results from SQL DB according to job_id (if exists) and filter json in body
          requestBody:
            description: filter jobs json
            required: false
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    job_id:
                      description: Id of Job
                      example: 6e4fd45a93e0
                      type: string
                    page:
                      description: number of page (for pagination)
                      example: 2
                      type: integer
                    page_block:
                      description: number of rows per page (for pagination)
                      example: 20
                      type: integer
                    job_type:
                      description: job type
                      example: PE
                      type: string
                      enum:
                      - PE
                      - RCE
                      - DEV
                      - QA
                    status:
                      description: status of job
                      example: running
                      type: string
                      enum:
                      - pending
                      - running
                      - passed
                      - failed
                      - cancelled
                      - internal_error
                    user:
                      description: name of job's submitter
                      example: john
                      type: string
                    date:
                      description: datetime job was launched
                      example: "2021-01-07 15:06:46"
                      type: Datetime
          responses:
            200:
              description: jobs summary
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      job_type:
                        description: job type
                        example: running
                        type: string
                      job_id:
                        type: Id of job
                        example: 6e4fd45a93e0
                        type: string
                      user:
                        description: name of job's submitter
                        example: john
                        type: string
                      status:
                        description: status of job
                        example: running
                        type: string
                      date:
                        description: datetime job was launched
                        example: "2021-01-07 15:06:46"
                        type: Datetime
                      total_tests:
                        description: number tests to run
                        example: 500
                        type: integer
                      success_tests:
                        description: number successful tests
                        example: 100
                        type: integer
                      failed_tests:
                        description: number failed tests
                        example: 20
                        type: integer
                      pending_tests:
                        description: number pending tests
                        example: 370
                        type: integer
                      crashed_tests:
                        description: number tests with crash
                        example: 10
                        type: integer
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
            Run job with config json using Jenkins
        ---
        post:
          description: >-
            Run job with config json using Jenkins. Create random job id
          requestBody:
            description: job config - config of all subjobs
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    device_filter:
                      description: filter of devices with number of devices
                      type: object
                      properties:
                        hardware:
                          description: hardware unit/range of devices
                          type: string
                          example: "> XS Max"
                        software:
                          description: software unit/range of devices
                          type: string
                          example: "> 14.1"
                        user:
                          description: user name (to get user's host devices)
                          type: string
                          example: "john"
                        pac:
                          description: if device is under/above 'X' hardware
                          type: boolean
                          example: true
                    test_params:
                        description: tests parameters for each filter
                        type: object
                        properties:
                          test_repo_info:
                            description: test repository information
                            type: object
                            properties:
                                test_repo_path:
                                  description: test repository path
                                  type: string
                                  example: "http://gitlab/pe/tests"
                                branch:
                                  description: test repository branch
                                  type: string
                                  example: "master"
                                commit:
                                  description: test repository commit
                                  type: string
                                  example: "a30c49a033d625aabbb3e26025fd"
                          url:
                            description: host
                            type: string
                            example: "2.2.2.2"
                          tool_type:
                            description: tool type to run
                            type: string
                            example: "Persistent"


          responses:
            200:
              description: Submittion Success
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        description: result of run job
                        type: string
                        example: "failed"
                      reason:
                        description: reason in case of failure
                        type: string
                        example: "Jenkins is Down"
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
          security:
            - jwt_refresh: []
        """
        resp = {}
        return self.response(200, **resp)
