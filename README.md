# IFPRI_IMPACT
Ingest IFPRI IMPACT to BigQuery for easy QA of Aqueduct Food

## Source:

The data was shared as URL in an email Cenacchi, Nicola (IFPRI) <N.Cenacchi@cgiar.org>. 

https://www.dropbox.com/sh/ezpnhn1773rscfk/AACVLyAKAPFY_eaAyI2JQRfGa?dl=0

## Data downloaded to 
`s3://wri-projects/Aqueduct30/rawData/IFRPI/Y2019M09D16_RH_IFPRI_IMPACT_2015_Raw_V01`


## Extra Info

For Aqueduct Food, only the MIROC (MIRO) scenario has been used. This is because the scenarios of Aqueduct and IMPACT were different and this scneario is shared between the two tools. 

| impactparameter        | scenario  | commodity | region               | productiontype | year |
|------------------------|-----------|-----------|----------------------|----------------|------|
| World price            | SSP2-MIRO | Soybean   | -                    | -              | 2005 |
| Food Demand            | SSP2-NoCC | Maize     | Afghanistan          | air            | 2010 |
| Production             | SSP2-IPSL | Rice      | Albania              | arf            | 2011 |
| Net trade              | SSP2-GFDL | Wheat     | Algeria              |                | 2012 |
| Area                   | SSP2-HGEM | -         | Angola               |                | 2013 |
| Yield                  |           |           | Argentina            |                | 2014 |
| Kcal per capita        |           |           | Armenia              |                | 2015 |
| Pop. at risk of hunger |           |           | Australia            |                | 2016 |
|                        |           |           | Austria              |                | 2017 |
|                        |           |           | Azerbaijan           |                | 2018 |
|                        |           |           | Baltic States        |                | 2019 |
|                        |           |           | Bangladesh           |                | 2020 |
|                        |           |           | Belarus              |                | 2021 |
|                        |           |           | Belgium-Luxembourg   |                | 2022 |
|                        |           |           | Belize               |                | 2023 |
|                        |           |           | Benin                |                | 2024 |
|                        |           |           | Bhutan               |                | 2025 |
|                        |           |           | Bolivia              |                | 2026 |
|                        |           |           | Botswana             |                | 2027 |
|                        |           |           | Brazil               |                | 2028 |
|                        |           |           | Bulgaria             |                | 2029 |
|                        |           |           | Burkina Faso         |                | 2030 |
|                        |           |           | Burundi              |                | 2031 |
|                        |           |           | Cambodia             |                | 2032 |
|                        |           |           | Cameroon             |                | 2033 |
|                        |           |           | Canada               |                | 2034 |
|                        |           |           | Central African Rep. |                | 2035 |
|                        |           |           | Chad                 |                | 2036 |
|                        |           |           | Chile                |                | 2037 |
|                        |           |           | China                |                | 2038 |
|                        |           |           | Colombia             |                | 2039 |
|                        |           |           | Congo                |                | 2040 |
|                        |           |           | Costa Rica           |                | 2041 |
|                        |           |           | Croatia              |                | 2042 |
|                        |           |           | Cuba                 |                | 2043 |
|                        |           |           | Cyprus               |                | 2044 |
|                        |           |           | Czech Republic       |                | 2045 |
|                        |           |           | DRC                  |                | 2046 |
|                        |           |           | Denmark              |                | 2047 |
|                        |           |           | Djibouti             |                | 2048 |
|                        |           |           | Dominican Republic   |                | 2049 |
|                        |           |           | Ecuador              |                | 2050 |
|                        |           |           | Egypt                |                |      |
|                        |           |           | El Salvador          |                |      |
|                        |           |           | Equatorial Guinea    |                |      |
|                        |           |           | Eritrea              |                |      |
|                        |           |           | Ethiopia             |                |      |
|                        |           |           | Fiji                 |                |      |
|                        |           |           | Finland              |                |      |
|                        |           |           | France               |                |      |
|                        |           |           | Gabon                |                |      |
|                        |           |           | Gambia               |                |      |
|                        |           |           | Georgia              |                |      |
|                        |           |           | Germany              |                |      |
|                        |           |           | Ghana                |                |      |
|                        |           |           | Greece               |                |      |
|                        |           |           | Greenland            |                |      |
|                        |           |           | Guatemala            |                |      |
|                        |           |           | Guinea               |                |      |
|                        |           |           | Guinea-Bissau        |                |      |
|                        |           |           | Guyanas              |                |      |
|                        |           |           | Haiti                |                |      |
|                        |           |           | Honduras             |                |      |
|                        |           |           | Hungary              |                |      |
|                        |           |           | Iceland              |                |      |
|                        |           |           | India                |                |      |
|                        |           |           | Indonesia            |                |      |
|                        |           |           | Iran                 |                |      |
|                        |           |           | Iraq                 |                |      |
|                        |           |           | Ireland              |                |      |
|                        |           |           | Israel               |                |      |
|                        |           |           | Italy                |                |      |
|                        |           |           | Ivory Coast          |                |      |
|                        |           |           | Jamaica              |                |      |
|                        |           |           | Japan                |                |      |
|                        |           |           | Jordan               |                |      |
|                        |           |           | Kazakhstan           |                |      |
|                        |           |           | Kenya                |                |      |
|                        |           |           | Kyrgyzstan           |                |      |
|                        |           |           | Laos                 |                |      |
|                        |           |           | Lebanon              |                |      |
|                        |           |           | Lesotho              |                |      |
|                        |           |           | Liberia              |                |      |
|                        |           |           | Libya                |                |      |
|                        |           |           | Madagascar           |                |      |
|                        |           |           | Malawi               |                |      |
|                        |           |           | Malaysia             |                |      |
|                        |           |           | Mali                 |                |      |
|                        |           |           | Mauritania           |                |      |
|                        |           |           | Mexico               |                |      |
|                        |           |           | Moldova              |                |      |
|                        |           |           | Mongolia             |                |      |
|                        |           |           | Morocco              |                |      |
|                        |           |           | Mozambique           |                |      |
|                        |           |           | Myanmar              |                |      |
|                        |           |           | Namibia              |                |      |
|                        |           |           | Nepal                |                |      |
|                        |           |           | Netherlands          |                |      |
|                        |           |           | New Zealand          |                |      |
|                        |           |           | Nicaragua            |                |      |
|                        |           |           | Niger                |                |      |
|                        |           |           | Nigeria              |                |      |
|                        |           |           | North Korea          |                |      |
|                        |           |           | Norway               |                |      |
|                        |           |           | Other Atlantic       |                |      |
|                        |           |           | Other Balkans        |                |      |
|                        |           |           | Other Caribbean      |                |      |
|                        |           |           | Other Indian Ocean   |                |      |
|                        |           |           | Other Pacific Ocean  |                |      |
|                        |           |           | Other Southeast Asia |                |      |
|                        |           |           | Pakistan             |                |      |
|                        |           |           | Palestine            |                |      |
|                        |           |           | Panama               |                |      |
|                        |           |           | Papua New Guinea     |                |      |
|                        |           |           | Paraguay             |                |      |
|                        |           |           | Peru                 |                |      |
|                        |           |           | Philippines          |                |      |
|                        |           |           | Poland               |                |      |
|                        |           |           | Portugal             |                |      |
|                        |           |           | Rest of Arabia       |                |      |
|                        |           |           | Romania              |                |      |
|                        |           |           | Russia               |                |      |
|                        |           |           | Rwanda               |                |      |
|                        |           |           | Saudi Arabia         |                |      |
|                        |           |           | Senegal              |                |      |
|                        |           |           | Sierra Leon          |                |      |
|                        |           |           | Slovakia             |                |      |
|                        |           |           | Slovenia             |                |      |
|                        |           |           | Solomon Islands      |                |      |
|                        |           |           | Somalia              |                |      |
|                        |           |           | South Africa         |                |      |
|                        |           |           | South Korea          |                |      |
|                        |           |           | Spain                |                |      |
|                        |           |           | Sri Lanka            |                |      |
|                        |           |           | Sudan                |                |      |
|                        |           |           | Swaziland            |                |      |
|                        |           |           | Sweden               |                |      |
|                        |           |           | Switzerland          |                |      |
|                        |           |           | Syria                |                |      |
|                        |           |           | Tajikistan           |                |      |
|                        |           |           | Tanzania             |                |      |
|                        |           |           | Thailand             |                |      |
|                        |           |           | Timor L'Este         |                |      |
|                        |           |           | Togo                 |                |      |
|                        |           |           | Tunisia              |                |      |
|                        |           |           | Turkey               |                |      |
|                        |           |           | Turkmenistan         |                |      |
|                        |           |           | UK                   |                |      |
|                        |           |           | USA                  |                |      |
|                        |           |           | Uganda               |                |      |
|                        |           |           | Ukraine              |                |      |
|                        |           |           | Uruguay              |                |      |
|                        |           |           | Uzbekistan           |                |      |
|                        |           |           | Vanuatu              |                |      |
|                        |           |           | Venezuela            |                |      |
|                        |           |           | Vietnam              |                |      |
|                        |           |           | Yemen                |                |      |
|                        |           |           | Zambia               |                |      |
|                        |           |           | Zimbabwe             |                |      |

