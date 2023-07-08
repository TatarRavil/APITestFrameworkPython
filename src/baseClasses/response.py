# from jsonschema import validate
# from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response, json_key=None):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate_json(self, schema):
        if isinstance(self.response_json, list):
            if len(self.response_json) == 0:
                assert False, f"json body is empty: {self}"
            else:
                for item in self.response_json:
                    schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)

        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self

        return self

    def __str__(self):
        return \
            f"\nstatus code: {self.response.status_code} \n" \
            f"body: {self.response_json} \n" \
            f"url: {self.response.url}"





