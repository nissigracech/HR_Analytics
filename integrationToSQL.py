import pandas as pd
from sqlalchemy import create_engine

# Database Configuration
database_user = 'root'
database_password = 'Nissigrace%4014'
database_host = '127.0.0.1'
database_name = 'hr_analytics'

# Create the database engine
engine = create_engine(f"mysql+mysqlconnector://{database_user}:{database_password}@{database_host}/{database_name}")
print("Database engine created successfully!")

#--------------------------------------------------------------------------------------------------------------------------
#Employee dataset
employee_file_path = 'Employee.csv'
try:
    employee_df = pd.read_csv(employee_file_path)  
except Exception as e:
    print(f"Error loading Employee dataset: {e}")
# Manual Data Processing for Employee Dataset
try:
    # Convert 'Hire Date' to datetime
    employee_df['HireDate'] = pd.to_datetime(employee_df['HireDate'], errors='coerce').dt.date

except Exception as e:
    print(f"Error processing Employee dataset: {e}")

# Upload Employee dataset to SQL
employee_table_name = 'employee'
try:
    employee_df.to_sql(employee_table_name, con=engine, if_exists='replace', index=False) 
    print(f"{employee_table_name} is uploaded into sql in {database_name} database")
except Exception as e:
    print(f"Error uploading Employee dataset: {e}")
 
#----------------------------------------------------------------------------------------------------------
#Performance Level dataset
performance_file_path = 'PerformanceRating.csv'
try:
    performance_df = pd.read_csv(performance_file_path) 
except Exception as e:
    print(f"Error loading Performance Rating dataset: {e}")

# Manual Data Processing for Performance Level Dataset
try:
    # Convert 'Review Date' to datetime
    performance_df['ReviewDate'] = pd.to_datetime(performance_df['ReviewDate'], errors='coerce').dt.date
except Exception as e:
    print(f"Error processing Performance Level dataset: {e}")

# Upload Performance Level dataset to SQL
performance_table_name = 'performance_rating'
try:
    performance_df.to_sql(performance_table_name, con=engine, if_exists='replace', index=False) 
    print(f"{performance_table_name} is uploaded into sql in {database_name} database")
except Exception as e:
    print(f"Error uploading Performance Rating dataset: {e}")

#--------------------------------------------------------------------------------------------------------------------------
# SatisfactionLevel
# Handling SatisfactionLevel dataset
satisfaction_file_path = 'SatisfiedLevel.csv'

try:
    # Load the SatisfactionLevel dataset
    satisfaction_df = pd.read_csv(satisfaction_file_path)
except Exception as e:
    print(f"Error loading SatisfactionLevel dataset: {e}")

try:
    satisfaction_table_name = 'satisfaction_level'
    # Upload SatisfactionLevel DataFrame to the SQL database
    satisfaction_df.to_sql(satisfaction_table_name, con=engine, if_exists='replace', index=False)
    print(f"{satisfaction_table_name} is uploaded into SQL in {database_name} database")
except Exception as e:
    print(f"Error uploading SatisfactionLevel dataset: {e}")


#--------------------------------------------------------------------------------------------------------------------------
# RatinLevel
# Handling RatingLevel dataset
rating_file_path = 'RatingLevel.csv' 
try:
    # Load the RatingLevel dataset
    rating_df = pd.read_csv(rating_file_path)
except Exception as e:
    print(f"Error loading RatingLevel dataset: {e}")
    
# Upload RatingLevel DataFrame to the SQL database
try:
    rating_table_name = 'rating_level'
    rating_df.to_sql(rating_table_name, con=engine, if_exists='replace', index=False)
    print(f"{rating_table_name} is uploaded into SQL in {database_name} database")
except Exception as e:
    print(f"Error uploading RatingLevel dataset: {e}")

