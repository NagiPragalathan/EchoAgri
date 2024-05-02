#!/bin/bash
#!/bin/bash


# Install dependencies
python -m pip install -r requirements.txt

# Run Django collectstatic command
python manage.py collectstatic --noinput