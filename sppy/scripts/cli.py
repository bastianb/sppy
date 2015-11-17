import click
from sppy.field import fields


@click.command()
def cli():
    click.echo('#TODO')
    for key, val in data.iteritems():
        if key not in fields:
            print key
    click.echo(20 * '#')

    for key in fields:
        if key not in data:
            print key

if __name__ == '__main__':
    cli()

data ={'vads_amount':'8800',
'vads_auth_mode':'FULL',
'vads_auth_number':'3fee8b',
'vads_auth_result':'00',
'vads_capture_delay':'0',
'vads_card_brand':'MASTERCARD',
'vads_card_number':'597010XXXXXX0001',
'vads_payment_certificate':'222db22d387fa03a5f00276d8d609b5395a67cac',
'vads_ctx_mode':'TEST',
'vads_currency':'978',
'vads_effective_amount':'8800',
'vads_site_id':'67402503',
'vads_trans_date':'20151111182032',
'vads_trans_id':'000011',
'vads_trans_uuid':'3a6a482e5dd4490e9e9e94ca7c510b44',
'vads_validation_mode':'0',
'vads_version':'V2',
'vads_warranty_result':'YES',
'vads_payment_src':'EC',
'vads_order_id':'000011',
'vads_cust_email':'test@test.test',
'vads_cust_id':'14',
'vads_cust_title':'M.',
'vads_cust_status':'PRIVATE',
'vads_cust_name':'we twe',
'vads_cust_zip':'23423',
'vads_cust_city':'wfwefw',
'vads_cust_country':'FR',
'vads_cust_phone':'123123123',
'vads_cust_cell_phone':'123123123',
'vads_ship_to_status':'PRIVATE',
'vads_ship_to_name':'we twe',
'vads_ship_to_street':'wefwef',
'vads_ship_to_city':'wfwefw',
'vads_ship_to_zip':'23423',
'vads_ship_to_country':'FR',
'vads_ship_to_phone_num':'123123123',
'vads_sequence_number':'1',
'vads_contract_used':'8773709',
'vads_trans_status':'AUTHORISED',
'vads_expiry_month':'6',
'vads_expiry_year':'2016',
'vads_bank_product':'MCW',
'vads_pays_ip':'PL',
'vads_presentation_date':'20151111182052',
'vads_effective_creation_date':'20151111182052',
'vads_operation_type':'DEBIT',
'vads_threeds_enrolled':'N',
'vads_threeds_cavv':'',
'vads_threeds_eci':'',
'vads_threeds_xid':'',
'vads_threeds_cavvAlgorithm':'',
'vads_threeds_status':'',
'vads_threeds_sign_valid':'',
'vads_threeds_error_code':'7',
'vads_threeds_exit_status':'7',
'vads_result':'00',
'vads_extra_result':'',
'vads_card_country':'FR',
'vads_language':'fr',
'vads_hash':'10c9199c7dd06a470a0491cacc46633e37089630353e9ff5f2a44e925a24d186',
'vads_url_check_src':'PAY',
'vads_action_mode':'INTERACTIVE',
'vads_cust_address':' ',
'vads_payment_config':'SINGLE',
'vads_page_action':'PAYMENT',
'vads_shop_name':'ADN-COLOR.com',
'vads_shop_url':'http://adn-color.com/',}