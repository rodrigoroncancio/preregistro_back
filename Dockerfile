FROM python:3.12.7-slim-bookworm
ENV PYTHONBUFFERED 1
RUN cp /usr/share/zoneinfo/America/Bogota /etc/localtime && \
  echo "America/Bogota" > /etc/timezone && \
  apt-get update && apt-get install -y curl gnupg unixodbc unixodbc-dev && \
  curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg && \
  chmod a+r /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
  apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

WORKDIR /code
COPY requirements.txt /code
RUN pip install --upgrade pip && \
  pip install --trusted-host pypy.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . /code/

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0", "-w", "4", "pnis.wsgi:application"]
