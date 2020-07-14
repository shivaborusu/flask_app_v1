import config
import logging as log
import match_gls_xml as mx
import standard_augment_xml as stanug
import standardize_xml as stan
import soap_response_processsing as srp
import pandas as pd

import requests

log.basicConfig(filename='api.log', level=log.DEBUG)


def get_url(env, service, key):
    log.info("Inside get URL")
    # considering default as REST
    return config.env_dict[f"{env}"]+"/soap/"+service


# commented as REST API is not working
'''def get_query_params(service):
    if service == 'StandardizeAndAugmentGlobalLocationService':
        return queryparams1
    elif service == 'MatchGlobalLocationService':
        return queryparams2
    else:
        return queryparams3'''


def process_data(df, env, service, key):
    log.info(df.columns)
    df = df.fillna(value=0)
    passed_df = pd.DataFrame()
    failed_df = pd.DataFrame()
    url = get_url(env, service, key)
    print(url)
    for ix, row in df.iterrows():
        row_id = ix
        DIM_LOC_ID = row['DIM_LOC_ID']
        SRC_KY = row['SRC_KY']
        LOC_NUM = row['LOC_NUM']
        LOC_NM = row['LOC_NM']
        TIV_RC = row['TIV_RC']
        STREET_ADDRESS = row['STREET_ADDRESS']
        POSTAL_CD = row['POSTAL_CD']
        CITY_NM = row['CITY_NM']
        COUNTY = row['COUNTY']
        STATECODE = row['STATECODE']
        ISO_CNTRY_CD = row['ISO_CNTRY_CD']
        ISO_CNTRY_NM = row['ISO_CNTRY_NM']
        GEO_CDNG_PRCSN_NM = row['GEO_CDNG_PRCSN_NM']
        GEO_CDNG_PRCSN_SCHEME = row['GEO_CDNG_PRCSN_SCHEME']
        GEO_CDNG_PRCSN_CD = row['GEO_CDNG_PRCSN_CD']
        LOC_LATTD_IN_DEGRS = row['LOC_LATTD_IN_DEGRS']
        LOC_LNGTD_IN_DEGRS = row['LOC_LNGTD_IN_DEGRS']

        headers = {'content-type': 'text/xml', 'apikey': "xxxxxxxxxxxx"}
        soap_data = ""

        if service == 'MatchGlobalLocationService':
            soap_data = mx.match_xml.format(STREET_ADDRESS=STREET_ADDRESS, CITY_NM=CITY_NM,
                                            ISO_CNTRY_NM=ISO_CNTRY_NM, DIM_LOC_ID=DIM_LOC_ID, LOC_NM=LOC_NM)

        elif service == 'StandardizeAndAugmentGlobalLocationServiceRequest':
            soap_data = stanug.stan_aug_xml.format(CITY_NM=CITY_NM, STATECODE=STATECODE, POSTAL_CD=POSTAL_CD,
                                                   ISO_CNTRY_NM=ISO_CNTRY_NM, STREET_ADDRESS=STREET_ADDRESS)

        elif service == 'StandardizeGlobalLocationServiceRequest':
            soap_data = stan.stand_xml.format(CITY_NM=CITY_NM, POSTAL_CD=POSTAL_CD,
                                              ISO_CNTRY_NM=ISO_CNTRY_NM, STREET_ADDRESS=STREET_ADDRESS)

        try:
            response = requests.post(url, data=soap_data, headers=headers)
            if response.status_code in (200, 201):
                output_series = srp.response_process(response.content)
                passed_df = passed_df.append(output_series)
            else:
                raise Exception()

        except (requests.exceptions.RequestException, requests.exceptions.ConnectTimeout,
                requests.exceptions.RequestException, Exception):

            failed_df = failed_df.append(row)
            log.info("Row with issues", row_id, row)
            pass

    return passed_df, failed_df
