FROM node:22-bookworm-slim

ENV USERNAME=node
ENV WORKPATH=/opt/workdir
ENV USER_ID=1000
ENV GROUP_ID=1000

RUN usermod -u ${USER_ID} ${USERNAME}
RUN usermod -g ${GROUP_ID} ${USERNAME}

WORKDIR ${WORKPATH}
RUN chown -R ${USER_ID}:${GROUP_ID} ${WORKPATH}
USER ${USERNAME}
COPY --chown=${USERNAME}:${USERNAME} package*.json ./

RUN npm install

COPY --chown=${USERNAME}:${USERNAME} . ${WORKPATH}

CMD ["npm", "run", "dev"]