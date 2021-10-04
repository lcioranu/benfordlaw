# build stage
FROM python:3.9.7-slim-bullseye AS builder

ARG BUILD_NUMBER="0.dev"

RUN mkdir "benford"
WORKDIR /benford
RUN mkdir "static"
RUN mkdir "templates"
COPY static /benford/static
COPY templates /benford/templates
COPY *.py /benford

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install wheel

RUN python setup.py bdist_wheel

RUN pip3 install dist/*.whl  --no-cache-dir

# final stage
FROM python:3.9.7-slim-bullseye AS final

ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /opt/venv /opt/venv
WORKDIR /benford

COPY service.sh ./
COPY static ./static
COPY templates ./templates
COPY *.py ./
RUN chmod +x service.sh

RUN useradd -u 1101 servicerunner
RUN chown servicerunner /benford
USER servicerunner

CMD ./service.sh