from client import OpenapiSpecMockServerContractValidatorClient

def main():
    client = OpenapiSpecMockServerContractValidatorClient()
    res = client.validate_and_spawn_mock_server('https://petstore.swagger.io/v2/swagger.json')
    print('OpenAPI Mock Validator: ' + res['mock_server_id'] + ' (' + str(res['endpoints_mocked_count']) + ' endpoints)')
    print('Compliance: ' + str(res['schema_contract_compliance_pct']) + '% | Mock URL: ' + res['ephemeral_mock_base_url'])
    print('Fuzz Harness: ' + res['fuzz_testing_harness_url'])

if __name__ == '__main__':
    main()
