FROM public.ecr.aws/lambda/python:3.10
WORKDIR /code

# open port
EXPOSE 8000

# root context
COPY . ${LAMBDA_TASK_ROOT}
# add requirements
COPY requirements.txt . 

RUN yum update -y && \
    yum install -y git && \
    yum install -y gcc python27 python27-devel && \
    rm -Rf /var/cache/yum

# Instalación de Mangum
RUN pip install mangum
# install requirements
RUN pip3 install  --no-cache-dir -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Init command
CMD ["app.main.handler"]