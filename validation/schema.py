schema_name = {
    'required': 'Name cannot be null or empty',
    'min': {
        'len': 3,
        'message': 'Name should be at least 3 characters.'
    },
    'max': {
        'len': 20,
        'message': 'Name should be max 20 characters'
    },
}
