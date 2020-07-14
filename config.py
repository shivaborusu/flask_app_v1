# environments config
env_dict = {
"DEV" : "https://dev.cloud.api.aig.net/corp/pitney/bowes/v1",
"QA" : "https://uat.cloud.api.aig.net/corp/pitney/bowes/qa/v1",
"UAT" : "https://uat.cloud.api.aig.net/corp/pitney/bowes/v1",
"PROD" : "https://live.cloud.api.aig.net/corp/pitney/bowes/v1"
}

# for REST api implementation, not using as of now, because we are implementing SOAP
# service config
StandardizeAndAugmentGlobalLocationService = "/StandardizeAndAugmentGlobalLocationService"
queryparams1 = "Data.City='Fremont'&Data.StateProvince='KY'&Data.PostalCode=''&" \
               "Data.Country='USA'&Data.AddressLine1='La%C2%A0Avalancha Frente a Fundacion Cubano Sec '&" \
               "Data.StandardizeFlag=Y&Data.SourceLocationId=100"


MatchGlobalLocationService = "/MatchGlobalLocationService"
queryparams2 = "Data.AddressLine1=100 Connel Dr&Data.City=Berkeley&Data.Country=USA&" \
               "Data.MatchKey=C540B624USA&Data.Identifier=s&Data.SourceLocationId=1&" \
               "Data.LocationName=AIG&Data.IsSiteName_Match=Y"


StandardizeGlobalLocationService = "/StandardizeGlobalLocationService"
queryparams3 = "Data.City=INDIANAPOLIS&Data.StateProvince=KY&Data.PostalCode=46259&" \
               "Data.Country=USA&Data.AddressLine1='7837 OAK GROVE CT'&Data.SourceLocationId=100"