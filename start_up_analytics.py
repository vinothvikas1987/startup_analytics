!pip install shapefile

import pandas as pd
import numpy as np
import regex as re
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
sns.set_style('whitegrid')

df = pd.read_csv("/content/startup_funding.csv")

df.columns

df['Amount in USD'] = df['Amount in USD'].str.replace(',','')
df['Amount in USD'] = pd.to_numeric(df['Amount in USD'], errors='coerce')

df.info()

df.dropna(subset = ['Industry Vertical','City  Location','Amount in USD'],axis = 0 ,  inplace=True)

df.drop('Remarks',axis = 1 ,  inplace=True)

df['Amount in USD'].head(50)

df.info()

df = df.reset_index()

df.loc[df['SubVertical'].isna()]

df.iloc[1426:,5] = df.iloc[1426:,4]

df.dropna(subset = ['SubVertical'],axis = 0 ,  inplace=True)

df['SubVertical'].isna().sum()

df['SubVertical'].nunique()

df['Sector'] = df['SubVertical'].astype(str)

df.info()

df['Amount in USD']

df = df.sort_values(by=['Amount in USD'],ascending= False)

df['Amount in USD']

df['Sector'].isna().sum()

# E_commerce =  ['eCommerce','ECommerce','ETailer','Used Car Marketplace','Ridesharing','aggregator','Aggregator','Aggregation','Used Vehicles Marketplace','Used Bikes Marketplace','E-Commerce','Used Vehicle Marketplace','rental','M-Commerce','Pooling','Aggregator','E-Commerce','Ecommerce','B2B','Delivery','Grocer','eTailer','etailer','Etailer','e-tailer','Shopping','Online Pharmacy','Online Furnishing\\\\neCommerce','store','Grocery','Online Pharmacy & Drug DB','Auto Rickshaw Based Services','Commerce','Taxi','Online Kitchen Furniture','Online Fashion Video Portal','eCommece','Online Home D\\\\xc3\\\\xa9cor','delivery','Online Table Reservation','Online Car Rental Affiliates']
# Logistics =  ['Transportation,Mile','logistics','Transport','Movers','Logistics','Logistic','Logistics']
# Healthcare =  ['Healthcare','Doctors','pharmaceutical','Therapeutics','DNA','Genetics','Online Homeopathy Clinic','Doctor','healthcare','Cancer','Dental','Probiotic','Clinical','Medical','Fitness','Health','health','wellness','Wellness']
# Finance =  ['FinTech','Finance','Investing','expense','cash','bfanking','VC','Fund','loan','loans','funds','Investment','Financing','Fin-Tech','Money','Financial','NBFC','payment','Wallet','Payment','funding','Lending','Accounting','Fiinance','finance','Financial']
# BigData =  ['ai','Artificial','Intelligence','Analytics','Analytics ','User Engagment & Analytics platform','Data',]
# Ed_Tech =  ['E-Tech','Education','Test','classes','students','hindi','Parents','tutor','Tutor','vocational','training','Training','Kids','E-learning','exam','Ed-tech','Online Certification Courses','Ed-Tech','Exam','athletes','Skill Training Startup','Coaching','Edtech','Learning','learning','Sports','E-Learning']
# Energy =  ['Energy','grid','Solar','Clean','power',"Power"]
# Food_and_Beverages =  ['QSR','chain','Beverage','burger','juice','Tea','Dining','Restaurant','restaurant','beverages','Beverages','food','Food']
# Hospitality =  ['Hotel Booking','Homes','Hotel','rooms','disease','Disease','hotel','Wedding','Accommodation','Hospitality']
# Retail =  ['Retail','Retailer','Clothes','wine','beauty','Tools','marketplace','service','services','Ethnic','fashion','home','furnishing']
# Automobile =  ['automotive','Automobile','automobile','scooter','Electric']
# Ag_Tech =  ['Agtech','Agriculture','agriculture','water','Water','agri','farmer','farmers']
# Gaming =  ['Games','Gaming','gaming','games','game']
# Marketing =  ['Marketing','marketing','Advertisment','advertising','Advertising','adcertisment','ad','Ad','AD']
# Consumer_Internet =  ['Software','SaaS','SAAS','mobile social network','Social Network for Artists','Nightlife Discovery Mobile App','Video Streaming','Car Maintenance & Management mobile app','Cab Sharing service Mobile app','On Demand Mobile app developer','Picture based Social App','Location based Nightlife recommendation\\\\xc2\\\\xa0 Platform',
# 'Personalized Wish List creator app','OS','comparison','video','erp','Consumer internet','operating','review','Platform','platform','Cloud','Reviews','Real Estate','Real Estate Rating & Analysis','Social Media','App','Music Streaming App','Online','Messaging','Mobile based PoS solution','Cab Booking app platform','Personal Diagnostic Mobile App','Mobile Growth Hacking\\\\nPlatform','Reward Points','virtual reality','Professional Service Appointment booking service','usiness expense management','Video Intelligence Platform','Wealth Management Platform','Mobile App Development','Saas','IT','software','Services Platform','Customer Service Platform']
# Others =  ['Realty Tech Startup solving real life Interior Designing problems',
#        'Tech based investor firm', 'Designer-led consumer products',
#        'Fresh Produce SCM company', 'Buying Club for Small Businesses',
#        'Smart Parking Enabler',
#        'women focussed customer-to-customer reseller network',
#        'Defense Tech & Aerospace startup', 'mPOS solutions provider',
#        'Genomics Research and Diagnostics Solutions', 'co-working spaces',
#        'Buying portal for SMEs', 'Truck Network company',
#        'Project Management tool', 'Interactive Tech-Support Guides',
#        'Collaborative co-Working Spaces', 'SDN Solutions',
#        'Solution provider for pet needs', 'Photo Sharing for Groups',
#        'Parenting Info & Social Network', 'Holiday Packages provider',
#        'Bot Protection Solutions', '3D Printing Solutions for Edu space',
#        'LiFi based wireless communication provider',
#        'Gamified Consumer Insights Portal',
#        'Car Tracking & Safety System', 'Post merger Integration Partners',
#        'e-Book Publisher', 'Student focussed Content Discovery portal','Auto Insurance',
#        'Consulting', 'Cabs', 'Optimization', 'Energy', 'E-Books',
#        'Travel', 'Anti-Pollution', 'Hyperlocal Content',
#        'Regional Flavours', 'On-Demand Drivers', 'Car Wash', 'Art',
#        'Co-Working', 'Media', 'Products For Shoolgoing Children',
#        'Hyperlocal Discovery', 'E-Publishing', 'Personal Assistant',
#        'Social', 'Hygiene', 'Residential Project', 'Others',
#        'on-demand chauffeur provider', 'Medicine Intake Reminder System',
#        'Auto Classifieds Portal', 'Mobile Point of Sale solutions',
#        'Job Board', 'Gesture based Mobile Development',
#        'Automated Storage & Warehousing Solution',
#        '\\\\xc2\\\\xa0Premium Loyalty Rewards Point Management',
#        'Physical Storage warehouses', 'Travel information portal',
#        'Travel Tech', 'Career Development', 'Web Content Publishing',
#        'Interactive\\\\xc2\\\\xa0 How-To Guides',
#        'Material Collection & Recycling', 'Grey collar Job Board','Wealth Management','Business development']


# def replace(x):
#   for e,h,l,f,b,ed,en,fo,ho,r,a,ag,ga,ma,co,o in zip(E_commerce,Healthcare,Logistics,Finance,BigData,Ed_Tech,Energy,Food_and_Beverages,Hospitality,Retail,Automobile,Ag_Tech,Gaming,Marketing,Consumer_Internet,Others):

#     if e.lower() in x.lower():
#       return 'E-commerce and Aggregator'

#     elif h.lower() in x.lower():
#       return 'Healthcare'

#     elif l.lower() in x.lower():
#       return 'Logistics'

#     elif f.lower() in x.lower():
#       return 'Finance'

#     elif b.lower() in x.lower():
#       return 'BigData & AI'

#     elif ed.lower() in x.lower():
#       return 'Ed-Tech'
#     elif en.lower() in x.lower():
#       return 'Energy'

#     elif fo.lower() in x.lower():
#       return 'Food and Beverages'

#     elif ho.lower() in x.lower():
#       return 'Hospitality'

#     elif r.lower() in x.lower():
#       return 'Retail'

#     elif a.lower() in x.lower():
#       return 'Automobile'

#     elif ag.lower() in x.lower():
#       return 'Agtech'

#     elif ga.lower() in x.lower():
#       return 'Gaming'

#     elif ma.lower() in x.lower():
#       return 'Marketing'

#     elif co.lower() in x.lower():
#       return 'Consumer Internet'

#     elif o.lower() in x.lower():
#       return 'Others'


# df['Sector'] = df['Sector'].apply(replace)

df['Sector'].isna().sum()

E_commerce =  ['eCommerce','ECommerce','ETailer','Used Car Marketplace','Ridesharing','aggregator','Aggregator','Aggregation','Used Vehicles Marketplace','Used Bikes Marketplace','E-Commerce','Used Vehicle Marketplace','rental','M-Commerce','Pooling','Aggregator','E-Commerce','Ecommerce','B2B','Delivery','Grocer','eTailer','etailer','Etailer','e-tailer','Shopping','Online Pharmacy','Online Furnishing\\\\neCommerce','store','Grocery','Online Pharmacy & Drug DB','Auto Rickshaw Based Services','Commerce','Taxi','Online Kitchen Furniture','Online Fashion Video Portal','eCommece','Online Home D\\\\xc3\\\\xa9cor','delivery','Online Table Reservation','Online Car Rental Affiliates']

def replace(x):
    for s in E_commerce:
        if s.lower() in x.lower():
            return 'E-commerce and Aggregator'
    return x

df['Sector'] = df['Sector'].apply(replace)

Healthcare =  ['Healthcare','Doctors','pharmaceutical','Therapeutics','DNA','Genetics','Online Homeopathy Clinic','Doctor','healthcare','Cancer','Dental','Probiotic','Clinical','Medical','Fitness','Health','health','wellness','Wellness']

def replace(x):
    for s in Healthcare:
        if s.lower() in x.lower():
            return 'Healthcare'
    return x

df['Sector'] = df['Sector'].apply(replace)

Logistics =  ['Transportation,Mile','logistics','Transport','Movers','Logistics','Logistic','Logistics']

def replace(x):
    for s in Logistics:
        if s.lower() in x.lower():
            return 'Logistics'
    return x

df['Sector'] = df['Sector'].apply(replace)

Finance =  ['FinTech','Finance','Investing','expense','cash','banking','VC','Fund','loan','loans','funds','Investment','Financing','Fin-Tech','Money','Financial','NBFC','payment','Wallet','Payment','funding','Lending','Accounting','Fiinance','finance','Financial']

def replace(x):
    for s in Finance:
        if s.lower() in x.lower():
            return 'Finance'
    return x

df['Sector'] = df['Sector'].apply(replace)

Ed_Tech =  ['E-Tech','Education','Test','classes','students','hindi','Parents','tutor','Tutor','vocational','training','Training','Kids','E-learning','exam','Ed-tech','Online Certification Courses','Ed-Tech','Exam','athletes','Skill Training Startup','Coaching','Edtech','Learning','learning','Sports','E-Learning']

def replace(x):
    for s in Ed_Tech:
        if s.lower() in x.lower():
            return 'Ed-Tech'
    return x

df['Sector'] = df['Sector'].apply(replace)

Energy =  ['Energy','grid','Solar','Clean','power',"Power"]

def replace(x):
    for s in Energy:
        if s.lower() in x.lower():
            return 'Energy'
    return x

df['Sector'] = df['Sector'].apply(replace)

BigData =  ['ai','Artificial','Intelligence','Analytics','Analytics ','User Engagment & Analytics platform','Data',]

def replace(x):
    for s in BigData:
        if s.lower() in x.lower():
            return 'BigData & AI'
    return x

df['Sector'] = df['Sector'].apply(replace)

Food_and_Beverages =  ['QSR','chain','Beverage','burger','juice','Tea','Dining','Restaurant','restaurant','beverages','Beverages','food','Food']

def replace(x):
    for s in Food_and_Beverages:
        if s.lower() in x.lower():
            return 'Food and Beverages'
    return x

df['Sector'] = df['Sector'].apply(replace)

Hospitality =  ['Hotel Booking','Homes','Hotel','rooms','disease','Disease','hotel','Wedding','Accommodation','Hospitality']

def replace(x):
    for s in Hospitality:
        if s.lower() in x.lower():
            return 'Hospitality'
    return x

df['Sector'] = df['Sector'].apply(replace)

Retail =  ['Retail','Retailer','Clothes','wine','beauty','Tools','marketplace','service','services','Ethnic','fashion','home','furnishing']

def replace(x):
    for s in Retail:
        if s.lower() in x.lower():
            return 'Retail & Service'
    return x

df['Sector'] = df['Sector'].apply(replace)

Automobile =  ['automotive','Automobile','automobile','scooter','Electric']

def replace(x):
    for s in Automobile:
        if s.lower() in x.lower():
            return 'Automobile'
    return x

df['Sector'] = df['Sector'].apply(replace)

Ag_Tech =  ['Agtech','Agriculture','agriculture','water','Water','agri','farmer','farmers']

def replace(x):
    for s in Ag_Tech:
        if s.lower() in x.lower():
            return 'Ag-Tech'
    return x

df['Sector'] = df['Sector'].apply(replace)

pattern = r"(?i).*gam.*"

df['Sector'] = df['Sector'].str.replace(pattern,"Gaming")

pattern = r"(?i).*ad.*"

df['Sector'] = df['Sector'].str.replace(pattern,"Marketing")

df['Sector'].unique()

Gaming =  ['Games','Gaming','gaming','games','game']

def replace(x):
    for s in Gaming:
        if s.lower() in x.lower():
            return 'Gaming'
    return x

df['Sector'] = df['Sector'].apply(replace)

Media = ['News','news']

def replace(x):
    for s in Media:
        if s.lower() in x.lower():
            return 'Media'
    return x

df['Sector'] = df['Sector'].apply(replace)

Marketing =  ['Marketing','marketing','Advertisment','advertising','Advertising','adcertisment','ad','Ad','AD']

def replace(x):
    for s in Marketing:
        if s.lower() in x.lower():
            return 'Marketing'
    return x

df['Sector'] = df['Sector'].apply(replace)

M_T =  ['Manufacturing','manufacturing','brewery','smart','manufacturer','waste','prosthetics','robotics','robot','biodigestor','micro','Automation','automation','IOT','IoT','Technology']

def replace(x):
    for s in M_T:
        if s.lower() in x.lower():
            return 'Manufacturing & Technology'
    return x

df['Sector'] = df['Sector'].apply(replace)

Consumer_Internet =  ['Software','SaaS','SAAS','mobile social network','Social Network for Artists','Nightlife Discovery Mobile App','Video Streaming','Car Maintenance & Management mobile app','Cab Sharing service Mobile app','On Demand Mobile app developer','Picture based Social App','Location based Nightlife recommendation\\\\xc2\\\\xa0 Platform',
'Personalized Wish List creator app','OS','comparison','video','erp','Consumer internet','operating','review','Platform','platform','Cloud','Reviews','Real Estate','Real Estate Rating & Analysis','Social Media','App','Music Streaming App','Online','Messaging','Mobile based PoS solution','Cab Booking app platform','Personal Diagnostic Mobile App','Mobile Growth Hacking\\\\nPlatform','Reward Points','virtual reality','Professional Service Appointment booking service','usiness expense management','Video Intelligence Platform','Wealth Management Platform','Mobile App Development','Saas','IT','software','Services Platform','Customer Service Platform']

def replace(x):
    for s in Consumer_Internet:
        if s.lower() in x.lower():
            return 'Software'
    return x

df['Sector'] = df['Sector'].apply(replace)

Others =  ['Realty Tech Startup solving real life Interior Designing problems',
       'Tech based investor firm', 'Designer-led consumer products',
       'Fresh Produce SCM company', 'Buying Club for Small Businesses',
       'Smart Parking Enabler',
       'women focussed customer-to-customer reseller network',
       'Defense Tech & Aerospace startup', 'mPOS solutions provider',
       'Genomics Research and Diagnostics Solutions', 'co-working spaces',
       'Buying portal for SMEs', 'Truck Network company',
       'Project Management tool', 'Interactive Tech-Support Guides',
       'Collaborative co-Working Spaces', 'SDN Solutions',
       'Solution provider for pet needs', 'Photo Sharing for Groups',
       'Parenting Info & Social Network', 'Holiday Packages provider',
       'Bot Protection Solutions', '3D Printing Solutions for Edu space',
       'LiFi based wireless communication provider',
       'Gamified Consumer Insights Portal',
       'Car Tracking & Safety System', 'Post merger Integration Partners',
       'e-Book Publisher', 'Student focussed Content Discovery portal','Auto Insurance',
       'Consulting', 'Cabs', 'Optimization', 'Energy', 'E-Books',
       'Travel', 'Anti-Pollution', 'Hyperlocal Content',
       'Regional Flavours', 'On-Demand Drivers', 'Car Wash', 'Art',
       'Co-Working', 'Media', 'Products For Shoolgoing Children',
       'Hyperlocal Discovery', 'E-Publishing', 'Personal Assistant',
       'Social', 'Hygiene', 'Residential Project', 'Others',
       'on-demand chauffeur provider', 'Medicine Intake Reminder System',
       'Auto Classifieds Portal', 'Mobile Point of Sale solutions',
       'Job Board', 'Gesture based Mobile Development',
       'Automated Storage & Warehousing Solution',
       '\\\\xc2\\\\xa0Premium Loyalty Rewards Point Management',
       'Physical Storage warehouses', 'Travel information portal',
       'Travel Tech', 'Career Development', 'Web Content Publishing',
       'Interactive\\\\xc2\\\\xa0 How-To Guides',
       'Material Collection & Recycling', 'Grey collar Job Board','Wealth Management','Business development']

def replace(x):
    for s in Others:
        if s.lower() in x.lower():
            return 'Others'
    return x

df['Sector'] = df['Sector'].apply(replace)

df['City  Location'] = df['City  Location'].replace(['New York, Bengaluru','Kormangala','\\\\xc2\\\\xa0Bangalore','Bangalore / San Mateo','Karnataka','Bangalore','Bangalore / Palo Alto','Bangalore / USA','Bengaluru and Gurugram','Bangalore / SFO','Bangalore/ Bangkok','India/Singapore','SFO / Bangalore'],"Bengaluru").replace(['New York/ India','India / US','USA/India','\\\\xc2\\\\xa0New Delhi','India/US','US/India'],"India")
df['City  Location'] = df['City  Location'].replace("Tulangan","Indonesia").replace(['Gurugram','Gurgaon / SFO','Haryana','\\\\xc2\\\\xa0Gurgaon'],"Gurgaon")
df['City  Location'] = df['City  Location'].replace("Palo Alto","San Francisco").replace(['Noida / Singapore','\\\\xc2\\\\xa0Noida'],"Noida")
df['City  Location'] = df['City  Location'].replace(['Andheri','\\\\xc2\\\\xa0Mumbai','Mumbai / Global','Chembur','Mumbai / UK','Mumbai / NY','Mumbai/Bengaluru'],"Mumbai")
df['City  Location'] = df['City  Location'].replace("Taramani","Chennai").replace(['Pune / US','Pune/Seattle','Pune / Dubai'],"Pune")
df['City  Location'] = df['City  Location'].replace("Ahemadabad","Ahmedabad").replace("San Jose,","San Jose")
df['City  Location'] = df['City  Location'].replace("Nairobi","Kenya").replace("California","San Francisco")
df['City  Location'] = df['City  Location'].replace(['Delhi','Delhi & Cambridge','New Delhi / US'],"New Delhi").replace("Goa","Panaji").replace("Kerala","Trivandrum")
df['City  Location'] = df['City  Location'].replace(['Dallas / Hyderabad','Hyderabad/USA'],"Hyderabad").replace(['Singapore','Kenya'],'Outside India & USA')
df['City  Location'] = df['City  Location'].fillna("Others in India",axis = 0)

df['City  Location'].unique()

df['City  Location'].nunique()

df['State'] = df['City  Location']

df['State'] = df['State'].replace(['Bengaluru','Belgaum','Udupi'],"Karnataka").replace(['Chennai','Coimbatore'],"Tamil Nadu").replace(['Mumbai','Nagpur','Pune'],'Maharastra').replace(['Faridabad','Gurgaon'],'Haryana')
df['State'] = df['State'].replace(['Hyderabad'],'Telangana').replace(['Amritsar','Chandigarh'],'Punjab').replace(['Mumbai','Pune'],'Maharastra').replace(['Bhopal','Gwalior','Indore'],'Madhya Pradesh')
df['State'] = df['State'].replace(['Jaipur','Udaipur','Jodhpur'],'Rajasthan').replace(['Ahmedabad','Vadodara','Surat'],'Gujarat').replace(['Rourkela','Bhubneswar'],'Odisha').replace(['Panaji'],'Goa')
df['State'] = df['State'].replace(['Gaya'],'Bihar').replace(['Lucknow','Varanasi','Kanpur','Noida'],'Uttar Pradesh').replace(['Rourkela','Bhubneswar'],'Odisha').replace(['Kolkata'],'West Bengal').replace(['Trivandrum'],'Kerala')
df['State'] = df['State'].replace(['San Francisco','Santa Monica','Menlo Park','San Jose'],'California').replace(['Burnsville'],'Minnesota').replace(['Boston'],'Massachusetts')

df['State'].nunique()

df['Sector'].nunique()

df

df_Amount_Name_Verical_Location = df.iloc[:,[1,2,3,5,8]]

df.info()

df_sector_USD = df.iloc[ : , [9,10]]
df_sector_Type = df.iloc[ : , [8,10]]
df_state_Sector = df.iloc[: , [10,11]]
df_location_USD = df.iloc[: , [9,11]]
df_investor_USD_sector = df.iloc[:,[7,9,10]]
df_investor_location = df.iloc[:,[6,7]]

myexplode = [0.2, 0.1, 0.4, 0.7,0,0,0,0.4,0,0,0,0.4,0,0,0]

df_sector_USD.groupby(['Sector']).sum().plot(
    kind='pie', y='Amount in USD', autopct='%0.2f%%',label='', radius = 6,textprops = {"fontsize":15,'fontweight':'bold'},startangle=0,explode = myexplode,labeldistance = 1.1)
plt.legend( bbox_to_anchor=(2,3), loc="upper left").remove()

df_state_Sector

s = df_state_Sector.groupby("State").count().reset_index()

s.columns

s = s.rename(columns={'State': 'st_nm'})

merged1 = pd.merge(map_df, s, how="left", on=['st_nm'])
merged1['Sector'] = merged1['Sector'].replace(np.nan, 0)

g = df_location_USD.groupby("State").sum().reset_index()
g['Amount in USD'] = np.log10(g['Amount in USD'])

g = g.rename(columns={'State': 'st_nm'})

g.columns

merged = pd.merge(map_df, g, how="left", on=['st_nm'])
merged['Amount in USD'] = merged['Amount in USD'].replace(np.nan, 0)

fp = r'/content/india-polygon.shp'
map_df = gpd.read_file(fp)
map_df_copy = gpd.read_file(fp)
map_df.head()

map_df['st_nm'].unique()

map_df.plot(color = 'red',edgecolor = 'black',cmap='flag',column='st_nm')

merged1

fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('on')
ax.set_title('Start Up Investments', fontdict={'fontsize': '20', 'fontweight' : '10'})
merged.plot(column='Amount in USD', vmin = 0, linewidth=0.5,cmap='Pastel2', ax=ax, edgecolor='0',legend=True,markersize=[39.739192, -104.990337], legend_kwds={'label': "Start Up Investments"})

fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('on')
ax.set_title('Number of funded StartUp', fontdict={'fontsize': '20', 'fontweight' : '10'})
merged1.plot(column='Sector', vmin = 1,vmax =150, linewidth=0.5,cmap='Pastel2', ax=ax, edgecolor='0',legend=True,markersize=[39.739192, -104.990337], legend_kwds={'label': "Start Up Investments"})
