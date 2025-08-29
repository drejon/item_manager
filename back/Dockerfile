FROM node:22-bookworm-slim AS base

ENV USERNAME=node
ENV WORKPATH=/opt/workdir
ENV USER_ID=1000
ENV GROUP_ID=1000

RUN usermod -u ${USER_ID} ${USERNAME}
RUN usermod -g ${GROUP_ID} ${USERNAME}

RUN mkdir -p ${WORKPATH}/node_modules && chown -R ${USERNAME}:${USERNAME} ${WORKPATH}

WORKDIR ${WORKPATH}

CMD ["npm", "run", "dev"]

COPY --chown=${USERNAME}:${USERNAME} . $WORKPATH

FROM base AS ci
RUN npm install