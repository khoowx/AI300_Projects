def format_model_inputs(input_dict):
    age = int(input_dict['age'])
    gender = int(input_dict['gender'])
    senior_citizen = int(input_dict['senior_citizen'])
    num_dependents = int(input_dict['num_dependents'])
    zip_code = int(input_dict['num_dependents'])
    tenure_months = int(input_dict['tenure_months'])
    num_referrals = int(input_dict['num_referrals'])
    total_monthly_fee = float(input_dict['total_monthly_fee'])
    total_charges_quarter = float(input_dict['total_charges_quarter'])
    contract_type = input_dict['contract_type']

    return [gender, age, senior_citizen, num_dependents, tenure_months, num_referrals, total_monthly_fee, total_charges_quarter, contract_type, zip_code]

def validate(input_dict):
    errors = []

    required_fields = ['gender','age','senior_citizen','num_dependents','tenure_months','num_referrals','total_monthly_fee','total_charges_quarter','contract_type','zip_code']

    for field in required_fields:

        if field not in input_dict:
            errors.append(f'{field} not found in request.')

        if field in ['gender','age','senior_citizen','num_dependents','tenure_months','num_referrals','zip_code'] and type(input_dict[field]) != int \
                and not input_dict[field].isnumeric():
            errors.append(f'Age and children fields must be int type.')

        elif field == 'total_charges_quarter' and type(input_dict[field]) != float:
            try:
                float(input_dict['total_charges_quarter'])
            except ValueError:
                errors.append(f'Total charges per quarter - field must be numeric.')

        elif field == 'total_monthly_fee' and type(input_dict[field]) != float:
            try:
                float(input_dict['total_monthly_fee'])
            except ValueError:
                errors.append(f'Total monthly fee - field must be numeric.')

    return errors