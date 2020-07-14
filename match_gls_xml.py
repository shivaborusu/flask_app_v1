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


match_xml = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:mat="http://www.pb.com/spectrum/services/MatchGlobalLocationService">
   <soapenv:Header/>
   <soapenv:Body>
      <mat:MatchGlobalLocationServiceRequest>
         <mat:options/>
         <mat:MatchGlobalLocationInput>
            <mat:MatchGlobalLocationInputRow>
               <mat:AddressLine1>{STREET_ADDRESS}</mat:AddressLine1>
               <mat:City>{CITY_NM}</mat:City>
               <mat:Country>{ISO_CNTRY_NM}</mat:Country>
               <mat:MatchKey>C540B624USA</mat:MatchKey>
               <mat:Identifier>s</mat:Identifier>
               <mat:SourceLocationId>{DIM_LOC_ID}</mat:SourceLocationId>
               <mat:LocationName>{LOC_NM}</mat:LocationName>
               <mat:IsSiteName_Match>Y</mat:IsSiteName_Match>
            </mat:MatchGlobalLocationInputRow>
         </mat:MatchGlobalLocationInput>
      </mat:MatchGlobalLocationServiceRequest>
   </soapenv:Body>
</soapenv:Envelope>'''