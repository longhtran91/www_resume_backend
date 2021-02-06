import unittest
import boto3
import requests

class TestApiGateway(unittest.TestCase):
    def setUp(self):
        self.stack_name = "wwwResumeApp"
        self.api_name = "wwwResumeApi"
        client = boto3.client("cloudformation")

        try:
            response = client.describe_stacks(StackName=self.stack_name)
        except Exception as e:
            raise Exception(
                f"Cannot find stack {self.stack_name}. \n" f'Please make sure stack with the name "{self.stack_name}" exists.'
            ) from e
        stacks = response["Stacks"]

        stack_outputs = stacks[0]["Outputs"]
        api_outputs = [output for output in stack_outputs if output["OutputKey"] == self.api_name]

        self.assertTrue(api_outputs, f"Cannot find output " + self.api_name +  "in stack {stack_name}")
        self.api_endpoint = api_outputs[0]["OutputValue"]

    def test_api_gateway(self):
        with requests.Session() as s:
            response = s.get(self.api_endpoint, headers={'Connection':'close'})
        self.assertEqual(200, response.status_code)
        self.assertTrue("view_count" in response.json())

if __name__ == '__main__':
    unittest.main()
