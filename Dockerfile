FROM python:3.10.8-slim

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip==22.3 && \
    pip install --no-cache-dir -r requirements.txt && \
    ansible-galaxy collection install netbox.netbox && \
    ansible-galaxy collection install cisco.nxos && \
    ansible-galaxy collection install cisco.ios


## fix permissions
#RUN chown -R 1000:1000 /opt/app
#
## lastly
#USER 1000
