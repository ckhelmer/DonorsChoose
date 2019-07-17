import pandas as pd
print('pandas')

projects = pd.read_csv('Data/opendata_projects000.gz', escapechar='\\', names=['_projectid', '_teacher_acctid', '_schoolid', 'school_ncesid', 'school_latitude', 'school_longitude', 'school_city', 'school_state', 'school_zip', 'school_metro', 'school_district', 'school_county', 'school_charter', 'school_magnet', 'school_year_round', 'school_nlns', 'school_kipp', 'school_charter_ready_promise', 'teacher_prefix', 'teacher_teach_for_america', 'teacher_ny_teaching_fellow', 'primary_focus_subject', 'primary_focus_area' ,'secondary_focus_subject', 'secondary_focus_area', 'resource_type', 'poverty_level', 'grade_level', 'vendor_shipping_charges', 'sales_tax', 'payment_processing_charges', 'fulfillment_labor_materials', 'total_price_excluding_optional_support', 'total_price_including_optional_support', 'students_reached', 'total_donations', 'num_donors', 'eligible_double_your_impact_match', 'eligible_almost_home_match', 'funding_status', 'date_posted', 'date_completed', 'date_thank_you_packet_mailed', 'date_expiration'])

X = projects.drop('funding_status', axis=1)
y = projects['funding_status']

print('part 1')
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

#To transform y
label_encoder.fit(y)
encoded_y = label_encoder.transform(y)

#To print y
#for label, original_class in zip(encoded_y, y):
#    print('Original Class: ' + str(original_class))
#    print('Encoded Label: ' + str(label))
#    print('-' * 12)
print('part 2')

from keras.utils import to_categorical

one_hot_y = to_categorical(encoded_y)

#Drop columns with small amounts of nan
X = projects.dropna(subset = ['teacher_prefix', 'primary_focus_subject', 'primary_focus_area', 'resource_type', 'grade_level'])
print('part 3')
#One Hot Encode X Data
from sklearn.preprocessing import OneHotEncoder

encoded_df = projects[['school_charter', 'school_magnet', 'school_year_round', 'school_nlns', 'school_kipp', 'school_charter_ready_promise', 'teacher_teach_for_america', 'teacher_ny_teaching_fellow', 'eligible_double_your_impact_match', 'eligible_almost_home_match', 'teacher_prefix', 'primary_focus_subject', 'primary_focus_area', 'resource_type', 'poverty_level', 'grade_level']]

one_hot_X = OneHotEncoder().fit_transform(encoded_df)
print('part 4')
one_hot_X.to_csv('projects-metro-excluded-outcome.csv', index = False)
one_hot_y.to_csv('projects-metro-excluded-prepped-data.csv', index = False)

print('done')