FROM python:3.9

# test credentials and endpoint - override in deployment
ENV SWIMLANE_URL 'https://10.152.183.244'
ENV ACCESS_TOKEN 'XwbvFV0nSSTeS4NJQcUL2NUlRcZjgxKp'
ENV APPLICATION 'Detections'

# outer framework requirements
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# here is our entry point
COPY wrapper.py .

# here is the user's module that we will call
# we *should* create a non-root user to own & execute user files...
WORKDIR /usr/src/app/userspace
COPY userspace .
RUN pip install --no-cache-dir -r requirements.txt

# execute
WORKDIR /usr/src/app
CMD [ "python", "./wrapper.py" ]
