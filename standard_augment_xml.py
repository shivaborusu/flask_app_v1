'''
DIM_LOC_ID                                                  123
SRC_KY                                                      123
LOC_NUM                                                     123
LOC_NM                                                      NaN
TIV_RC                                                   200000
STREET_ADDRESS           AV RUMIPAMBA OE3-19 Y ANTONIO DE ULLOA
POSTAL_CD                                                   NaN
CITY_NM                                                   Quito
COUNTY                                                    Quito
STATECODE                                             Pichincha
ISO_CNTRY_CD                                                 EC
ISO_CNTRY_NM                                                 EC
GEO_CDNG_PRCSN_NM                                T-ABC--0-0-0-0
GEO_CDNG_PRCSN_SCHEME                                       RMS
GEO_CDNG_PRCSN_CD                                             7
LOC_LATTD_IN_DEGRS                                      -0.2295
LOC_LNGTD_IN_DEGRS                                     -78.5243
'''

stan_aug_xml = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:stan="http://www.pb.com/spectrum/services/StandardizeAndAugmentGlobalLocationService">
   <soapenv:Header/>
   <soapenv:Body>
      <stan:StandardizeAndAugmentGlobalLocationServiceRequest>
         <!--Optional:-->
         <stan:options/>
         <!--Optional:-->
         <stan:StandardizeAndAugmentGlobalLocationInput>
            <!--Zero or more repetitions:-->
            <stan:StandardizeAndAugmentGlobalLocationInputRow>
               <!--You may enter the following 39 items in any order-->
               <!--Optional:-->
               <stan:City>{CITY_NM}</stan:City>
               <!--Optional:-->
               <stan:StateProvince>{STATECODE}</stan:StateProvince>
               <!--Optional:-->
               <stan:PostalCode>{POSTAL_CD}</stan:PostalCode>
               <!--Optional:-->
               <stan:Country>{ISO_CNTRY_NM}</stan:Country>
               <!--Optional:-->
               <stan:AddressLine1>{STREET_ADDRESS}</stan:AddressLine1>
               <!--Optional:-->
               <stan:AddressLine2>?</stan:AddressLine2>
               <!--Optional:-->
               <stan:FirmName>?</stan:FirmName>
               <!--Optional:-->
               <stan:AddressLine3>?</stan:AddressLine3>
               <!--Optional:-->
               <stan:StandardizeFlag>y</stan:StandardizeFlag>
               <!--Optional:-->
               <stan:SourceLocationId>1</stan:SourceLocationId>
               <!--Optional:-->
               <stan:AddressLine4>?</stan:AddressLine4>
               <!--Optional:-->
               <stan:LongitudeInput>?</stan:LongitudeInput>
               <!--Optional:-->
               <stan:LatitudeInput>?</stan:LatitudeInput>
               <!--Optional:-->
               <stan:AddressLine5>?</stan:AddressLine5>
               <!--Optional:-->
               <stan:AddressLine6>?</stan:AddressLine6>
               <!--Optional:-->
               <stan:SubBuilding>?</stan:SubBuilding>
               <!--Optional:-->
               <stan:Street>?</stan:Street>
               <!--Optional:-->
               <stan:OccupancyType>?</stan:OccupancyType>
               <!--Optional:-->
               <stan:ConstructionClass>?</stan:ConstructionClass>
               <!--Optional:-->
               <stan:County>?</stan:County>
               <!--Optional:-->
               <stan:District>?</stan:District>
               <!--Optional:-->
               <stan:USUrbanName>?</stan:USUrbanName>
               <!--Optional:-->
               <stan:UnformattedLine1>?</stan:UnformattedLine1>
               <!--Optional:-->
               <stan:UnformattedLine2>?</stan:UnformattedLine2>
               <!--Optional:-->
               <stan:UnformattedLine3>?</stan:UnformattedLine3>
               <!--Optional:-->
               <stan:UnformattedLine4>?</stan:UnformattedLine4>
               <!--Optional:-->
               <stan:UnformattedLine5>?</stan:UnformattedLine5>
               <!--Optional:-->
               <stan:UnformattedLine6>?</stan:UnformattedLine6>
               <!--Optional:-->
               <stan:UnformattedLine7>?</stan:UnformattedLine7>
               <!--Optional:-->
               <stan:UnformattedLine8>?</stan:UnformattedLine8>
               <!--Optional:-->
               <stan:UnformattedLine9>?</stan:UnformattedLine9>
               <!--Optional:-->
               <stan:UnformattedLine10>?</stan:UnformattedLine10>
               <!--Optional:-->
               <stan:LocationName>?</stan:LocationName>
               <!--Optional:-->
               <stan:SiteName>?</stan:SiteName>
               <!--Optional:-->
               <stan:CustomErrorCode>?</stan:CustomErrorCode>
               <!--Optional:-->
               <stan:IsCRESTA>?</stan:IsCRESTA>
               <!--Optional:-->
               <stan:Building>?</stan:Building>
               <!--Optional:-->
               <stan:Number>?</stan:Number>
               <!--Optional:-->
               <stan:user_fields>
                  <!--Zero or more repetitions:-->
                  <stan:user_field>
                     <stan:name>?</stan:name>
                     <stan:value>?</stan:value>
                  </stan:user_field>
               </stan:user_fields>
            </stan:StandardizeAndAugmentGlobalLocationInputRow>
         </stan:StandardizeAndAugmentGlobalLocationInput>
      </stan:StandardizeAndAugmentGlobalLocationServiceRequest>
   </soapenv:Body>
</soapenv:Envelope>'''
